"""Gera data/nipe.json, com todos os agregados do site, a partir de data/fontes/.

Uso: python scripts/prepare_data.py

Entradas (imutáveis, em data/fontes/):
  arquivo/   CSVs do Arquivo Histórico NIPE-CP2b (export de 2026-11-16), sem os de pessoas
  aeplan/    série do NIPE e extração de todos os centros/núcleos da COCEN (scripts/extrair_aeplan.py)

Saída: data/nipe.json. Os textos das páginas leem os números de nipe.json["textos"], já
formatados no padrão brasileiro; scripts/verificar_dados.py confere se o número escrito no
HTML é igual ao de nipe.json.
"""
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
FONTES = RAIZ / 'data' / 'fontes'
ARQ = FONTES / 'arquivo'
AEP = FONTES / 'aeplan'
SAIDA = RAIZ / 'data' / 'nipe.json'

EXPORT = '2026-11-16'          # data do export do Arquivo Histórico
REGISTRO = '2026-11-12'        # versão do REGISTRO_MESTRE publicada em docs/registro
SIGLAS_HARMONIZADAS = {'CCS Nano': 'CCS', 'CLEHC': 'CLE'}
ANO_COMP_INI, ANO_COMP_FIM = 2015, 2025


# ---------------------------------------------------------------- formatação pt-BR
def fi(x):
    return f'{int(round(x)):,}'.replace(',', '.')


def fd(x, casas=1):
    s = f'{x:,.{casas}f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


def fp(x, casas=1):
    return fd(100 * x, casas) + '%'


def fmi(x):
    """R$ em milhões, uma casa: 8157834 -> '8,2'."""
    return fd(x / 1e6, 1)


def ordinal(n):
    return f'{n}º'


def le(caminho):
    with open(caminho, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def ano(texto):
    m = re.search(r'(19|20)\d{2}', texto or '')
    return int(m.group()) if m else None


# ---------------------------------------------------------------- NIPE: série AEPLAN
def serie_nipe():
    s = pd.read_csv(AEP / 'NIPE_AEPLAN_serie_2004-2025_PDF.csv')
    www2 = pd.read_csv(ARQ / 'NIPE_series_anuais_v2026-11-01.csv', dtype=str).fillna('')
    linhas = []
    for _, r in s.iterrows():
        a = int(r.ano_base)
        g = lambda c: (None if pd.isna(r[c]) else float(r[c]))
        linhas.append({
            'ano': a, 'edicao': int(r.edicao),
            'docentes': g('p71_docentes'), 'pesquisadores': g('p71_pesquisadores'),
            'bolsistas': g('p71_bolsistas'), 'pos_doutorandos': g('p71_pos_doutorandos'),
            'projetos_em_execucao': g('p71_projetos_em_execucao'), 'projetos_concluidos': g('p71_projetos_concluidos'),
            'projetos_com_financiamento': g('projetos_com_financiamento'),
            'convenios': g('convenios'), 'eventos': g('eventos'),
            'artigos': g('artigos'), 'artigos_intl': g('artigos_intl'), 'artigos_nac': g('artigos_nac'),
            # decisão 2: o total de produções de 2025 fica fora (K51/K57: 63 impresso × 363 soma dos itens)
            'producoes': None if a == 2025 else g('producoes_impresso'),
            'fapesp_contratados': g('fapesp_concedidos_ou_contratados'),
            'fapesp_criterio': r['fapesp_criterio'] if isinstance(r['fapesp_criterio'], str) else None,
            'fapesp_liberados': g('fapesp_liberados'),
            'nota': r['nota'] if isinstance(r['nota'], str) else '',
        })
    # série www2 (Anuário na web), só para os anos sem a Tabela 8.3 da AEPLAN por centro (2000–2014)
    proj_www2 = []
    for r in www2.to_dict('records'):
        a = int(r['ano'])
        v = r['projetos_com_financiamento']
        if v and 2000 <= a <= 2021:
            proj_www2.append({'ano': a, 'projetos_com_financiamento': int(float(v)), 'fonte': 'www2'})
    return linhas, proj_www2


# ---------------------------------------------------------------- COCEN: indicadores comparáveis
def cocen():
    t7 = pd.read_csv(AEP / 'COCEN_AEPLAN_tab7_1_2004-2025.csv')
    t8 = pd.read_csv(AEP / 'COCEN_AEPLAN_tab8_3_2015-2025.csv')
    t7 = t7[(t7.sigla != 'TOTAL') & (t7.atribuicao == 'ordem')].copy()
    t7['sigla'] = t7.sigla.replace(SIGLAS_HARMONIZADAS)
    p7 = t7.pivot_table(index=['ano_base', 'sigla'], columns='indicador', values='valor', aggfunc='first').reset_index()
    nomes = (t7.sort_values('ano_base').groupby('sigla').nome.last()).to_dict()
    secao = (t7.sort_values('ano_base').groupby('sigla').secao.last()).to_dict()

    t8 = t8.copy()
    t8['sigla'] = t8.sigla.replace(SIGLAS_HARMONIZADAS)
    # primeira ocorrência de cada rótulo na tabela (a 8.3 repete "Projetos FAPESP iniciados no ano" etc.)
    t8 = t8.sort_values(['ano_base', 'ordem_linha']).drop_duplicates(['ano_base', 'sigla', 'rotulo_normalizado'])
    rot = {'PROJETOS COM FINANCIAMENTO': 'projetos', 'ARTIGOS PUBLICADOS EM PERIODICOS': 'artigos',
           'CONVENIOS': 'convenios', 'PROMOCAO DE EVENTOS': 'eventos', 'LINHAS DE PESQUISA': 'linhas'}
    p8 = (t8[t8.rotulo_normalizado.isin(rot)].assign(ind=lambda d: d.rotulo_normalizado.map(rot))
          .pivot_table(index=['ano_base', 'sigla'], columns='ind', values='valor', aggfunc='first').reset_index())
    df = p8.merge(p7[['ano_base', 'sigla', 'docentes', 'pesquisadores', 'bolsistas']], on=['ano_base', 'sigla'], how='left')
    df['doc_pesq'] = df.docentes + df.pesquisadores
    dp = df.doc_pesq.where(df.doc_pesq > 0)
    df['projetos_por_dp'] = df.projetos / dp
    df['artigos_por_dp'] = df.artigos / dp
    df = df.rename(columns={'ano_base': 'ano'})
    return df, p7.rename(columns={'ano_base': 'ano'}), nomes, secao


INDICADORES = [
    # chave, rótulo, unidade, casas decimais
    ('projetos_por_dp', 'Projetos com financiamento por docente ou pesquisador', 'razão', 2),
    ('artigos_por_dp', 'Artigos em periódicos por docente ou pesquisador', 'razão', 2),
    ('convenios', 'Convênios', 'número', 0),
    ('eventos', 'Eventos promovidos', 'número', 0),
    ('projetos', 'Projetos com financiamento', 'número', 0),
    ('artigos', 'Artigos em periódicos', 'número', 0),
    ('doc_pesq', 'Docentes e pesquisadores', 'número', 0),
]


def comparacao(df):
    serie, ranking, participacao, slope = [], [], [], []
    for a, g in df.groupby('ano'):
        for chave, *_ in INDICADORES:
            v = g[['sigla', chave]].dropna()
            if v.empty:
                continue
            v = v.assign(pos=v[chave].rank(ascending=False, method='min').astype(int))
            n = len(v)
            for _, r in v.iterrows():
                serie.append({'ano': int(a), 'sigla': r.sigla, 'indicador': chave, 'valor': round(float(r[chave]), 4)})
            nipe = v[v.sigla == 'NIPE']
            if not nipe.empty:
                ranking.append({'ano': int(a), 'indicador': chave, 'posicao': int(nipe.pos.iloc[0]), 'centros': n,
                                'valor_nipe': round(float(nipe[chave].iloc[0]), 4),
                                'mediana_cocen': round(float(v[chave].median()), 4)})
        for chave in ('projetos', 'artigos', 'convenios', 'eventos', 'doc_pesq'):
            tot = g[chave].sum()
            nv = g.loc[g.sigla == 'NIPE', chave]
            if tot and not nv.empty and pd.notna(nv.iloc[0]):
                participacao.append({'ano': int(a), 'indicador': chave, 'nipe': float(nv.iloc[0]), 'total_cocen': float(tot),
                                     'participacao': round(float(nv.iloc[0]) / tot, 4)})
    ini = df[df.ano == ANO_COMP_INI].set_index('sigla')
    fim = df[df.ano == ANO_COMP_FIM].set_index('sigla')
    for chave, *_ in INDICADORES:
        for s in sorted(set(ini.index) & set(fim.index)):
            a, b = ini.at[s, chave], fim.at[s, chave]
            if pd.isna(a) or pd.isna(b):
                continue
            slope.append({'sigla': s, 'indicador': chave, 'valor_2015': round(float(a), 4), 'valor_2025': round(float(b), 4),
                          'diferenca': round(float(b - a), 4), 'razao': round(float(b / a), 4) if a else None})
    return serie, ranking, participacao, slope


# ---------------------------------------------------------------- registros do Arquivo Histórico
def arquivo():
    proj = le(ARQ / 'NIPE_projetos_v2026-11-01.csv')
    por_centro = Counter(r['centro'] for r in proj)
    coord = []
    for r in le(ARQ / 'NIPE_coordenadores_v2026-11-16.csv'):
        ini, fim = ano(r['inicio']), ano(r['fim'])
        if r['nome'].startswith('Marcelo'):
            fim = 2027
        if r['nome'].startswith('Bruna') and r['cargo'].lower().startswith('coordenadora associada') and not fim:
            fim = 2027
        coord.append({'nome': r['nome'], 'cargo': re.sub(r'[“”"]', '', r['cargo']).replace(' [S]', ''),
                      'inicio': ini, 'fim': fim or ini, 'selo': r['selo'].strip('[]'), 'id_fato': r['id_fato'],
                      'inicio_texto': r['inicio'], 'fim_texto': r['fim'], 'fonte_url': r['fonte_url'],
                      'lattes_periodo': r['lattes_periodo'], 'lattes_url': r['lattes_url'],
                      'lattes_atualizado': r['lattes_atualizado'], 'conferencia_lattes': r['conferencia_lattes']})
    cp2b_proj = le(ARQ / 'CP2B_projetos_v2026-10-25.csv')
    cp2b_pub = le(ARQ / 'CP2B_publicacoes_v2026-11-01.csv')
    vistos, pubs = set(), []
    for r in cp2b_pub:
        k = (r['doi'] or r['titulo']).lower()
        if k in vistos:
            continue
        vistos.add(k)
        pubs.append(r)
    cp2b_pub_ano_tipo = Counter((r['ano'], r['tipo']) for r in pubs)
    fin = Counter()
    for r in cp2b_proj:
        f = r['financiador'].split(',')[0].split('+')[0].strip()
        fin[f or 'não informado'] += 1
    return {
        'projetos_por_centro': [{'centro': c, 'registros': n} for c, n in por_centro.most_common()],
        'projetos_total': len(proj),
        'coordenadores': coord,
        'cp2b': {
            'projetos': len(cp2b_proj),
            'projetos_por_financiador': [{'financiador': f, 'projetos': n} for f, n in fin.most_common()],
            'publicacoes_distintas': len(pubs),
            'publicacoes_ano_tipo': [{'ano': int(a), 'tipo': t, 'publicacoes': n} for (a, t), n in sorted(cp2b_pub_ano_tipo.items())],
        },
    }


# ---------------------------------------------------------------- marcos e números em disputa
MARCOS = [
    ('1984-12-26', 'Criação do Núcleo de Energia (NUCLENER)', 'Portaria GR 271/84; coordenação de C. A. Mariottoni até 1993.', 'NIPE-F0001, F0070'),
    ('1987', 'Mestrado em Planejamento de Sistemas Energéticos', 'Criado na Faculdade de Engenharia Mecânica (FEM); doutorado em 1993.', 'NIPE-F0040'),
    ('1993-11-30', 'NUCLENER passa a ser NIPE', 'Deliberação CONSU-A-027/1993 aprova o regimento; decisão do Conselho Científico em dez/1992; DOE em 1993-12-15.', 'NIPE-F0431, F0002, F0003'),
    ('1998', 'Criação da COCEN', 'O NIPE passa a responder à Coordenadoria de Centros e Núcleos Interdisciplinares de Pesquisa.', 'NIPE-F0009'),
    ('2002-03-26', 'Novo regimento', 'Deliberação CONSU-A-006/2002, vigente até 2015.', 'NIPE-F0432'),
    ('2009-12-21', 'Centro Paulista de Pesquisa em Bioenergia', 'Convênio do SPBioenRC, base do futuro Laboratório de Bioenergia.', 'NIPE-F0140'),
    ('2015', 'Regimento atual e criação do LABIOEN', 'CONSU-A-003/2015 (DOE 2015-04-14); linha de pesquisa em Bioenergia e laboratório criados no mesmo ano.', 'NIPE-F0200, F0131'),
    ('2016-10-19', 'Projeto Temático FAPESP–BBSRC', 'Processo 2015/50612-8, coordenação de T. T. Franco, sede no NIPE.', 'NIPE-F0756'),
    ('2021', 'Centro de Engenharia de Plasticultura (CEP)', 'Selecionado na chamada FAPESP–Braskem; sede no NIPE (processo 21/05251-8).', 'NIPE-F0454, F0489'),
    ('2025-02-01', 'CP2b inicia as atividades', 'Centro Paulista de Estudos em Biogás e Bioprodutos (processo 24/01112-1), vigência até 2030.', 'NIPE-F0023'),
    ('2025-04-03', 'Inauguração do LABIOEN', 'Inauguração física do Laboratório de Bioenergia, criado em 2015.', 'NIPE-F0020, F0131'),
    ('2025-09-19', 'Posse da coordenação atual', 'M. P. da Cunha, mandato de 2025-07-17 a 2027-07-16; B. de S. Moraes, coordenadora associada.', 'NIPE-F0013, F0247'),
    ('2026-09-17', 'Novo Centro de Ciência para o Desenvolvimento', 'Selecionado na 5ª chamada da FAPESP (processo 2026/05010-4), com sede no NIPE.', 'NIPE-F0282, F0321'),
]

DISPUTA = [
    ('Produções em 2025 (AEPLAN, Tab. 8.3)', '63 impresso', '363 (soma dos subitens)', 'K51, K57', 'Total omitido; usam-se os subitens (artigos).'),
    ('Projetos com financiamento em 2020 e 2021', '22 e 17 (Anuário web)', '26 e 24 (Anuário em PDF)', '—', 'Adota-se o PDF da AEPLAN, mesma fonte dos demais centros.'),
    ('Área do Laboratório de Bioenergia', '4.014 m² (cadastro AEPLAN 2025)', '6.000 m² (divulgação 2024–2025)', 'K70', 'Publica-se o cadastro, com a ressalva.'),
    ('Corpo de pesquisadores (Anuário web)', 'total do quadro (ex.: 21 em 2021)', 'soma das categorias MS (6)', 'K20', 'Série da Tab. 7.1 da AEPLAN no lugar da lista nominal.'),
    ('Coordenação 2019–2021', 'titular sem ato localizado', 'B. de S. Moraes coordenadora associada', 'K27', 'Lacuna mantida na Fig. 2.'),
    ('Fim do mandato de G. M. Jannuzzi', 'até 01/2013 (currículo Lattes)', "I. M. L. D'Ottaviano no Anuário 2011; L. A. B. Cortez desde 01/2012 (currículo Lattes)", 'K11, K12', 'Mandato desenhado até 2011; divergência anotada na Fig. 2.'),
    ('Campus Sustentável (CPFL)', 'R$ 1,46 mi (P&D)', 'R$ 8,1 mi / R$ 9,5 mi (programa)', 'K52', 'Não somado à captação do NIPE.'),
]


def main():
    serie, proj_www2 = serie_nipe()
    comp_df, p7, nomes, secao = cocen()
    serie_comp, ranking, participacao, slope = comparacao(comp_df)
    arq = arquivo()
    s = {r['ano']: r for r in serie}
    u = s[2025]
    rk = {(r['ano'], r['indicador']): r for r in ranking}
    pt = {(r['ano'], r['indicador']): r for r in participacao}
    n_centros_2025 = int(comp_df[comp_df.ano == 2025].sigla.nunique())
    proj_centro = {r['centro']: r['registros'] for r in arq['projetos_por_centro']}
    pp = comp_df.set_index(['ano', 'sigla'])
    adp = lambda a, sg: float(pp.at[(a, sg), 'artigos_por_dp'])
    med = lambda a, k: rk[(a, k)]['mediana_cocen']

    textos = {
        # hoje
        'docentes_2025': fi(u['docentes']), 'pesquisadores_2025': fi(u['pesquisadores']),
        'bolsistas_2025': fi(u['bolsistas']), 'pos_doutorandos_2025': fi(u['pos_doutorandos']),
        'proj_exec_2025': fi(u['projetos_em_execucao']), 'proj_conc_2025': fi(u['projetos_concluidos']),
        'projetos_2025': fi(u['projetos_com_financiamento']), 'projetos_2024': fi(s[2024]['projetos_com_financiamento']),
        'artigos_2025': fi(u['artigos']), 'artigos_intl_2025': fi(u['artigos_intl']), 'artigos_2024': fi(s[2024]['artigos']),
        'fapesp_contr_2025': fmi(u['fapesp_contratados']), 'fapesp_lib_2025': fmi(u['fapesp_liberados']),
        'eventos_2025': fi(u['eventos']), 'convenios_2025': fi(u['convenios']),
        'area_total': '4.703', 'area_labioen': '4.014', 'area_sede': '653',
        'edat_vinculos': '80', 'edat_posdocs': '23', 'edat_visitantes': '51',
        'registros_projetos': fi(arq['projetos_total']), 'registros_nipe': fi(proj_centro['NIPE']),
        'registros_cep': fi(proj_centro['CEP']), 'registros_cp2b': fi(proj_centro['CP2B']), 'registros_cepil': fi(proj_centro['CePIL']),
        'cp2b_projetos': fi(arq['cp2b']['projetos']), 'cp2b_publicacoes': fi(arq['cp2b']['publicacoes_distintas']),
        'fatos_registro': '796', 'conflitos_registro': '66',
        # histórico
        'docentes_2004': fi(s[2004]['docentes']), 'pesquisadores_2004': fi(s[2004]['pesquisadores']),
        'docentes_2016': fi(s[2016]['docentes']), 'pesquisadores_2016': fi(s[2016]['pesquisadores']),
        'projetos_2015': fi(s[2015]['projetos_com_financiamento']), 'projetos_2021': fi(s[2021]['projetos_com_financiamento']),
        'projetos_2022': fi(s[2022]['projetos_com_financiamento']),
        'artigos_2016': fi(s[2016]['artigos']), 'artigos_2019': fi(s[2019]['artigos']), 'artigos_2022': fi(s[2022]['artigos']),
        'producoes_2016': fi(s[2016]['producoes']), 'producoes_2017': fi(s[2017]['producoes']),
        'fapesp_contr_2024': fmi(s[2024]['fapesp_contratados']),
        'n_coordenacoes': fi(len(arq['coordenadores'])), 'n_coordenadores': fi(len({c['nome'] for c in arq['coordenadores']})),
        # comparação
        'n_centros_2025': fi(n_centros_2025),
        'rank_projetos_2025': ordinal(rk[(2025, 'projetos')]['posicao']), 'rank_artigos_2025': ordinal(rk[(2025, 'artigos')]['posicao']),
        'rank_artigos_dp_2025': ordinal(rk[(2025, 'artigos_por_dp')]['posicao']),
        'rank_projetos_dp_2025': ordinal(rk[(2025, 'projetos_por_dp')]['posicao']),
        'rank_projetos_dp_2015': ordinal(rk[(2015, 'projetos_por_dp')]['posicao']),
        'rank_artigos_dp_2015': ordinal(rk[(2015, 'artigos_por_dp')]['posicao']),
        'part_projetos_2025': fp(pt[(2025, 'projetos')]['participacao']), 'part_projetos_2015': fp(pt[(2015, 'projetos')]['participacao']),
        'part_artigos_2025': fp(pt[(2025, 'artigos')]['participacao']), 'part_docpesq_2025': fp(pt[(2025, 'doc_pesq')]['participacao']),
        'artigos_dp_nipe_2025': fd(adp(2025, 'NIPE'), 2), 'artigos_dp_med_2025': fd(med(2025, 'artigos_por_dp'), 2),
        'artigos_dp_nipe_2019': fd(adp(2019, 'NIPE'), 2), 'artigos_dp_med_2019': fd(med(2019, 'artigos_por_dp'), 2),
        'projetos_dp_nipe_2025': fd(float(pp.at[(2025, 'NIPE'), 'projetos_por_dp']), 2),
        'projetos_dp_med_2025': fd(med(2025, 'projetos_por_dp'), 2),
        'n_centros_2015': fi(comp_df[comp_df.ano == 2015].sigla.nunique()),
        'artigos_dp_med_2015': fd(med(2015, 'artigos_por_dp'), 2),
        'rank_artigos_dp_2023': ordinal(rk[(2023, 'artigos_por_dp')]['posicao']),
        'n_slope_artigos_dp': fi(sum(1 for r in slope if r['indicador'] == 'artigos_por_dp')),
        'n_sub_artigos_dp': fi(sum(1 for r in slope if r['indicador'] == 'artigos_por_dp' and r['diferenca'] > 0)),
    }
    dados = {
        'meta': {'gerado_em': date.today().isoformat(), 'export_arquivo': EXPORT, 'registro': REGISTRO,
                 'aeplan_edicoes': '2005–2026', 'ano_comparacao': [ANO_COMP_INI, ANO_COMP_FIM]},
        'textos': textos,
        'paleta': json.loads((RAIZ / 'data' / 'paleta.json').read_text(encoding='utf-8')),
        'serie_nipe': serie,
        'projetos_www2': proj_www2,
        'arquivo': arq,
        'marcos': [{'data': d, 'titulo': t, 'texto': x, 'ids': i} for d, t, x, i in MARCOS],
        'disputa': [{'numero': a, 'leitura_a': b, 'leitura_b': c, 'conflito': k, 'tratamento': t} for a, b, c, k, t in DISPUTA],
        'cocen': {
            'indicadores': [{'chave': k, 'rotulo': r, 'unidade': un, 'casas': c} for k, r, un, c in INDICADORES],
            'nomes': nomes, 'secao': secao,
            'serie': serie_comp, 'ranking': ranking, 'participacao': participacao, 'slope': slope,
            'pessoal': [{'ano': int(r.ano), 'sigla': r.sigla, 'docentes': None if pd.isna(r.docentes) else int(r.docentes),
                         'pesquisadores': None if pd.isna(r.pesquisadores) else int(r.pesquisadores)}
                        for r in p7.itertuples()],
        },
    }
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print('nipe.json:', round(SAIDA.stat().st_size / 1024), 'KB')
    for k, v in textos.items():
        print(f'  {k}: {v}')


if __name__ == '__main__':
    main()
