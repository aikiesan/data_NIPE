"""Gera um CSV por figura a partir de data/nipe.json e empacota os dados num ZIP.

Uso: python scripts/export_figuras.py   (depois de prepare_data.py)

Escreve data/figuras/*.csv e data/nipe_dados.zip.
Prefixos: hojeNN_ (aba NIPE hoje), figNN_ (Histórico), compX_ (NIPE entre os centros).
"""
import csv
import json
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / 'data'
SAIDA = DADOS / 'figuras'


def grava(nome, cabecalho, linhas):
    with open(SAIDA / nome, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(cabecalho)
        w.writerows(linhas)
    print(f'{nome}: {len(linhas)} linhas')


def v(x):
    return '' if x is None else (int(x) if isinstance(x, float) and x.is_integer() else x)


def main():
    d = json.loads((DADOS / 'nipe.json').read_text(encoding='utf-8'))
    SAIDA.mkdir(exist_ok=True)
    for f in SAIDA.glob('*.csv'):
        f.unlink()
    s = {r['ano']: r for r in d['serie_nipe']}
    t = d['textos']

    # ---------------- NIPE hoje
    u = s[2025]
    grava('hoje01_indicadores.csv', ['indicador', 'valor', 'unidade', 'ano_base', 'fonte'], [
        ['Docentes (carreira MS) com atividade no NIPE', v(u['docentes']), 'pessoas', 2025, 'AEPLAN Tab. 7.1 [1]'],
        ['Pesquisadores', v(u['pesquisadores']), 'pessoas', 2025, 'AEPLAN Tab. 7.1 [1]'],
        ['Bolsistas', v(u['bolsistas']), 'pessoas', 2025, 'AEPLAN Tab. 7.1 [1]'],
        ['Projetos em execução', v(u['projetos_em_execucao']), 'projetos', 2025, 'AEPLAN Tab. 7.1 [1]'],
        ['Projetos com financiamento', v(u['projetos_com_financiamento']), 'projetos', 2025, 'AEPLAN Tab. 8.3 [1]'],
        ['Artigos em periódicos', v(u['artigos']), 'artigos', 2025, 'AEPLAN Tab. 8.3 [1]'],
        ['FAPESP, valores contratados', v(u['fapesp_contratados']), 'R$ nominais', 2025, 'AEPLAN Tab. 10.8 [1]'],
        ['FAPESP, valores liberados', v(u['fapesp_liberados']), 'R$ nominais', 2025, 'AEPLAN Tab. 10.8 [1]'],
        ['Área construída cadastrada', 4703, 'm²', 2025, 'AEPLAN, cadastro de áreas (NIPE-F0798) [1][3]'],
        ['Vínculos no portal EDAT', 80, 'vínculos', 2026, 'EDAT/UNICAMP, consulta de 2026-11-10 (NIPE-F0784) [5]'],
    ])
    grava('hoje02_serie_recente.csv', ['ano_base', 'docentes', 'pesquisadores', 'bolsistas', 'projetos_com_financiamento', 'artigos'],
          [[a, v(s[a]['docentes']), v(s[a]['pesquisadores']), v(s[a]['bolsistas']), v(s[a]['projetos_com_financiamento']), v(s[a]['artigos'])]
           for a in range(2015, 2026)])
    rot = {'CP2B': 'CP2b'}
    grava('hoje03_projetos_por_centro.csv', ['centro', 'registros_de_projeto', 'fonte'],
          [[rot.get(r['centro'], r['centro']), r['registros'], 'NIPE_projetos_v2026-11-01 [3]'] for r in d['arquivo']['projetos_por_centro']])
    grava('hoje04_vinculos_edat.csv', ['papel', 'vinculos', 'fonte'], [
        ['Pesquisadores visitantes', 51, 'EDAT [5]; NIPE-F0221, F0784'],
        ['Pós-doutorandos', 23, 'EDAT [5]; NIPE-F0784'],
        ['Pesquisadores de carreira', 4, 'EDAT [5]; NIPE-F0221'],
        ['Pesquisadores colaboradores', 2, 'EDAT [5]; NIPE-F0221'],
    ])
    grava('hoje05_cp2b_publicacoes.csv', ['ano', 'tipo', 'publicacoes'],
          [[r['ano'], r['tipo'], r['publicacoes']] for r in d['arquivo']['cp2b']['publicacoes_ano_tipo']])
    grava('hoje06_numeros_em_disputa.csv', ['numero', 'leitura_a', 'leitura_b', 'conflito_registro', 'tratamento_no_site'],
          [[r['numero'], r['leitura_a'], r['leitura_b'], r['conflito'], r['tratamento']] for r in d['disputa']])

    # ---------------- Histórico
    grava('fig01_marcos.csv', ['data', 'marco', 'descricao', 'id_fato'], [[m['data'], m['titulo'], m['texto'], m['ids']] for m in d['marcos']])
    grava('fig02_coordenadores.csv', ['nome', 'cargo', 'ano_inicio', 'ano_fim', 'inicio_registrado', 'fim_registrado', 'selo', 'id_fato', 'fonte_url',
                                      'lattes_periodo', 'conferencia_lattes', 'lattes_atualizado', 'lattes_url'],
          [[c['nome'], c['cargo'], c['inicio'], c['fim'], c['inicio_texto'], c['fim_texto'], c['selo'], c['id_fato'], c['fonte_url'],
            c['lattes_periodo'], c['conferencia_lattes'], c['lattes_atualizado'], c['lattes_url']]
           for c in d['arquivo']['coordenadores']])
    grava('fig03_equipe_tab7_1.csv', ['ano_base', 'edicao', 'docentes', 'pesquisadores', 'pos_doutorandos', 'bolsistas'],
          [[a, s[a]['edicao'], v(s[a]['docentes']), v(s[a]['pesquisadores']), v(s[a]['pos_doutorandos']), v(s[a]['bolsistas'])] for a in sorted(s)])
    linhas = [[r['ano'], 'Anuário web (www2) [2]', r['projetos_com_financiamento']] for r in d['projetos_www2']]
    linhas += [[a, 'AEPLAN PDF, Tab. 8.3 [1]', v(s[a]['projetos_com_financiamento'])] for a in sorted(s) if s[a]['projetos_com_financiamento'] is not None]
    grava('fig04_projetos_com_financiamento.csv', ['ano_base', 'fonte', 'projetos_com_financiamento'], sorted(linhas))
    grava('fig05_fapesp_valores.csv', ['ano_base', 'criterio', 'fapesp_concedidos_ou_contratados_rs', 'fapesp_liberados_rs'],
          [[a, s[a]['fapesp_criterio'] or '', v(s[a]['fapesp_contratados']), v(s[a]['fapesp_liberados'])]
           for a in sorted(s) if s[a]['fapesp_liberados'] is not None])
    grava('fig06_producao_artigos.csv', ['ano_base', 'artigos_circulacao_internacional', 'artigos_circulacao_nacional', 'artigos_total', 'producoes_total'],
          [[a, v(s[a]['artigos_intl']), v(s[a]['artigos_nac']), v(s[a]['artigos']), v(s[a]['producoes'])] for a in range(2015, 2026)])

    # ---------------- Comparação
    c = d['cocen']
    nomes = c['nomes']
    grava('compA_series_indicadores.csv', ['ano_base', 'sigla', 'centro_ou_nucleo', 'indicador', 'valor'],
          [[r['ano'], r['sigla'], nomes.get(r['sigla'], ''), r['indicador'], r['valor']] for r in c['serie']])
    grava('compB_slope_2015_2025.csv', ['sigla', 'indicador', 'valor_2015', 'valor_2025', 'diferenca', 'razao_2025_2015'],
          [[r['sigla'], r['indicador'], r['valor_2015'], r['valor_2025'], r['diferenca'], '' if r['razao'] is None else r['razao']] for r in c['slope']])
    grava('compC_ranking_nipe.csv', ['ano_base', 'indicador', 'posicao_nipe', 'centros_com_dado', 'valor_nipe', 'mediana_cocen'],
          [[r['ano'], r['indicador'], r['posicao'], r['centros'], r['valor_nipe'], r['mediana_cocen']] for r in c['ranking']])
    grava('compD_participacao_nipe.csv', ['ano_base', 'indicador', 'nipe', 'total_cocen', 'participacao'],
          [[r['ano'], r['indicador'], v(r['nipe']), v(r['total_cocen']), r['participacao']] for r in c['participacao']])

    with zipfile.ZipFile(DADOS / 'nipe_dados.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(DADOS.rglob('*')):
            if f.is_file() and f.suffix in ('.csv', '.md', '.json'):
                z.write(f, f.relative_to(DADOS))
    print('nipe_dados.zip:', round((DADOS / 'nipe_dados.zip').stat().st_size / 1024), 'KB')


if __name__ == '__main__':
    main()
