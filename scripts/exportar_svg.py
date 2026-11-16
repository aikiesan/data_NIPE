"""Exporta cada figura do site em SVG (figuras_svg/) para acabamento em Affinity/Illustrator.

Uso: python scripts/exportar_svg.py   (depois de export_figuras.py)

Lê só os CSVs de data/figuras/ e as cores de data/paleta.json, de modo que o SVG e o site
desenham os mesmos números com a mesma codificação de cores. Texto editável
(svg.fonttype = none), uma família sans-serif, corpo de 7–8 pt, largura final de 175 mm
(figura de página) ou 85 mm (coluna). As tabelas (hoje01, hoje06) não têm SVG.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
FIG = RAIZ / 'data' / 'figuras'
SAIDA = RAIZ / 'figuras_svg'
PAL = json.loads((RAIZ / 'data' / 'paleta.json').read_text(encoding='utf-8'))
NIPE, CP2B, CINZA, CINZA_E = PAL['NIPE'], PAL['CP2b'], PAL['contexto'], PAL['contexto_escuro']
MM = 1 / 25.4
LARGA, COLUNA = 175 * MM, 85 * MM

plt.rcParams.update({
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none',
    'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 7.5, 'axes.titlesize': 8, 'axes.labelsize': 7.5, 'xtick.labelsize': 7, 'ytick.labelsize': 7,
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.linewidth': 0.6,
    'xtick.major.width': 0.6, 'ytick.major.width': 0.6, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5,
    'axes.titlelocation': 'left', 'axes.titleweight': 'bold', 'legend.frameon': False, 'svg.hashsalt': 'data-nipe',
})
BR = FuncFormatter(lambda x, _: f'{x:,.0f}'.replace(',', '.'))
BR2 = FuncFormatter(lambda x, _: f'{x:.1f}'.replace('.', ','))


def le(nome):
    with open(FIG / nome, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def n(x):
    return float(x) if x not in ('', None) else None


GERADAS = []


def salva(fig, nome, titulo, fonte):
    GERADAS.append((nome, titulo))
    fig.text(0, 1.0, titulo, ha='left', va='bottom', fontsize=8, fontweight='bold', gid='titulo')
    fig.text(0, -0.02, fonte, ha='left', va='top', fontsize=6.5, color=CINZA_E, gid='fonte')
    fig.savefig(SAIDA / f'{nome}.svg', bbox_inches='tight', pad_inches=0.05, metadata={'Date': None})
    plt.close(fig)
    print(nome + '.svg')


def hoje02():
    r = le('hoje02_serie_recente.csv')
    anos = [int(x['ano_base']) for x in r]
    fig, axs = plt.subplots(1, 2, figsize=(LARGA, 50 * MM), gridspec_kw={'width_ratios': [1, 1]})
    for ax, col, rot in ((axs[0], 'projetos_com_financiamento', 'Projetos com financiamento'), (axs[1], 'artigos', 'Artigos em periódicos')):
        ys = [n(x[col]) for x in r]
        ax.plot(anos, ys, color=NIPE, lw=1.4, marker='o', ms=2.5, gid=f'linha-{col}')
        ax.set_title(rot)
        ax.set_yticks([0, max(ys)])
        ax.yaxis.set_major_formatter(BR)
        ax.set_xticks([2015, 2020, 2025])
        ax.annotate(f'{ys[-1]:.0f}', (anos[-1], ys[-1]), xytext=(3, 0), textcoords='offset points', va='center', color=NIPE)
    salva(fig, 'hoje02_serie_recente', 'Projetos e artigos declarados pelo NIPE atingem o maior valor da série em 2025',
          'Fonte: AEPLAN/UNICAMP, Anuário Estatístico, Tab. 8.3, edições 2016–2026 [1].')


def hoje03():
    r = le('hoje03_projetos_por_centro.csv')
    r.sort(key=lambda x: int(x['registros_de_projeto']))
    fig, ax = plt.subplots(figsize=(COLUNA, 45 * MM))
    cores = [PAL['centros_sediados'].get(x['centro'], CINZA) for x in r]
    ax.barh([x['centro'] for x in r], [int(x['registros_de_projeto']) for x in r], color=cores, height=0.65, gid='barras')
    for i, x in enumerate(r):
        ax.text(int(x['registros_de_projeto']) + 2, i, x['registros_de_projeto'], va='center', fontsize=7)
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', length=0)
    salva(fig, 'hoje03_projetos_por_centro', 'Sete em cada dez registros de projeto são do NIPE',
          'Registros de projeto no Arquivo Histórico NIPE-CP2b, por centro responsável [3].')


def hoje04():
    r = le('hoje04_vinculos_edat.csv')[::-1]
    fig, ax = plt.subplots(figsize=(COLUNA, 35 * MM))
    ax.barh([x['papel'] for x in r], [int(x['vinculos']) for x in r], color=CINZA, height=0.6, gid='barras')
    for i, x in enumerate(r):
        ax.text(int(x['vinculos']) + 1, i, x['vinculos'], va='center', fontsize=7)
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', length=0)
    salva(fig, 'hoje04_vinculos_edat', 'Visitantes são a maioria dos 80 vínculos do NIPE', 'Fonte: portal EDAT/UNICAMP, consulta de 2026-11-10 [5].')


def hoje05():
    r = le('hoje05_cp2b_publicacoes.csv')
    tipos = sorted({x['tipo'] for x in r})
    anos = sorted({x['ano'] for x in r})
    val = {(x['ano'], x['tipo']): int(x['publicacoes']) for x in r}
    fig, ax = plt.subplots(figsize=(COLUNA, 40 * MM))
    esq = [0] * len(anos)
    tons = [CP2B, '#F2C46B', '#F7DFAE']
    for t, cor in zip(tipos, tons):
        w = [val.get((a, t), 0) for a in anos]
        ax.barh(anos, w, left=esq, color=cor, height=0.55, label=t, gid=f'cp2b-{t}')
        esq = [a + b for a, b in zip(esq, w)]
    ax.legend(loc='lower right', fontsize=6.5)
    ax.xaxis.set_major_formatter(BR)
    salva(fig, 'hoje05_cp2b_publicacoes', 'A produção registrada do CP2b concentra-se em 2026',
          'Publicações distintas (DOI ou título) no Arquivo Histórico NIPE-CP2b [3].')


def fig01():
    r = le('fig01_marcos.csv')
    fig, ax = plt.subplots(figsize=(LARGA, 60 * MM))
    xs = [int(x['data'][:4]) + (int(x['data'][5:7]) - 1) / 12 if len(x['data']) >= 7 else int(x['data'][:4]) for x in r]
    ax.axhline(0, color=CINZA_E, lw=0.6)
    for i, (x, m) in enumerate(zip(xs, r)):
        y = (1 if i % 2 == 0 else -1) * (0.35 + 0.3 * ((i // 2) % 3))
        ax.plot([x, x], [0, y], color=CINZA, lw=0.5)
        ax.plot(x, 0, 'o', color=NIPE, ms=3)
        ax.text(x, y, f"{m['data'][:4]}  {m['marco']}", fontsize=6.3, ha='center', va='bottom' if y > 0 else 'top', gid=f'marco-{i}')
    ax.set_ylim(-1.4, 1.4)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xticks([1985, 1995, 2005, 2015, 2025])
    salva(fig, 'fig01_marcos', 'De núcleo de energia a sede de três centros financiados pela FAPESP (1984–2026)',
          'Fonte: Arquivo Histórico NIPE-CP2b, linha do tempo e registro mestre [3]; IDs dos fatos no CSV.')


def fig02():
    r = le('fig02_coordenadores.csv')
    fig, ax = plt.subplots(figsize=(LARGA, 70 * MM))
    for i, c in enumerate(r):
        ini, fim = int(c['ano_inicio']), int(c['ano_fim'])
        assoc = 'ssociad' in c['cargo']
        incerto = c['selo'] == 'S'
        ax.barh(i, max(fim - ini, 0.6), left=ini, height=0.6, color='none' if incerto else (CINZA if assoc else NIPE),
                edgecolor=NIPE if incerto else 'none', hatch='////' if incerto else None, lw=0.6, gid=f'mandato-{i}')
        ax.text(fim + 0.4, i, c['nome'] + ((' (associado)' if 'associado' in c['cargo'].lower() else ' (associada)') if assoc else ''), va='center', fontsize=6.5)
    ax.invert_yaxis()
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xlim(1983, 2036)
    ax.set_xticks([1984, 1993, 2002, 2011, 2020, 2027])
    salva(fig, 'fig02_coordenadores', 'Onze pessoas coordenaram o NIPE; há trechos sem ato formal (2011, 2019–2021, 2023–2025)',
          'Hachurado: período declarado só no currículo Lattes ou em fonte secundária [S]. Fonte: Arquivo Histórico NIPE-CP2b [3]; Anuários [1][2]; currículos Lattes [9].')


def fig03():
    r = le('fig03_equipe_tab7_1.csv')
    anos = [int(x['ano_base']) for x in r]
    fig, axs = plt.subplots(1, 2, figsize=(LARGA, 50 * MM), gridspec_kw={'width_ratios': [2, 1]})
    ax = axs[0]
    for col, cor, rot in (('pesquisadores', NIPE, 'Pesquisadores'), ('docentes', CINZA_E, 'Docentes')):
        ys = [n(x[col]) for x in r]
        ax.plot(anos, ys, color=cor, lw=1.3, gid=f'linha-{col}')
        ax.text(anos[-1] + 0.3, ys[-1], rot, color=cor, va='center', fontsize=7)
    ax.set_title('Docentes e pesquisadores')
    ax.set_xticks([2004, 2010, 2015, 2020, 2025])
    ax = axs[1]
    ys = [n(x['bolsistas']) for x in r]
    ax.plot(anos, ys, color=CINZA_E, lw=1.0)
    ax.set_title('Bolsistas')
    ax.set_yticks([0, max(ys)])
    ax.set_xticks([2004, 2025])
    salva(fig, 'fig03_equipe_tab7_1', 'O corpo declarado do NIPE oscila de ano para ano e atinge o maior número de pesquisadores em 2025',
          'Fonte: AEPLAN/UNICAMP, Anuário Estatístico, Tab. 7.1, edições 2005–2026 [1].')


def fig04():
    r = le('fig04_projetos_com_financiamento.csv')
    fig, ax = plt.subplots(figsize=(LARGA, 55 * MM))
    for fonte, cor, mk in (('www2', CINZA_E, 's'), ('AEPLAN', NIPE, 'o')):
        pts = [(int(x['ano_base']), int(x['projetos_com_financiamento'])) for x in r if fonte in x['fonte']]
        ax.plot(*zip(*pts), color=cor, lw=1.1, marker=mk, ms=2.6, label='Anuário web (www2)' if fonte == 'www2' else 'AEPLAN, PDF (Tab. 8.3)', gid=f'serie-{fonte}')
    ax.legend(loc='upper left')
    ax.yaxis.set_major_formatter(BR)
    ax.set_xticks([2001, 2005, 2010, 2015, 2020, 2025])
    salva(fig, 'fig04_projetos_com_financiamento', 'Até 2021, o NIPE registrava menos de 30 projetos com financiamento por ano; de 2022 a 2025, entre 39 e 175',
          'Fontes: Anuário Estatístico da UNICAMP, versão web, 2000–2021 [2]; AEPLAN, PDF, 2015–2025 [1].')


def fig05():
    r = le('fig05_fapesp_valores.csv')
    anos = [int(x['ano_base']) for x in r]
    fig, ax = plt.subplots(figsize=(LARGA, 55 * MM))
    ax.plot(anos, [n(x['fapesp_concedidos_ou_contratados_rs']) / 1e6 for x in r], color=NIPE, lw=1.3, marker='o', ms=2.5, label='Concedidos (até 2015) ou contratados', gid='contratados')
    ax.plot(anos, [n(x['fapesp_liberados_rs']) / 1e6 for x in r], color=CINZA_E, lw=1.1, ls='--', label='Liberados', gid='liberados')
    ax.axhline(0, color=CINZA, lw=0.5)
    ax.yaxis.set_major_formatter(BR2)
    ax.set_ylabel('R$ milhões (nominais)')
    ax.legend(loc='upper left')
    salva(fig, 'fig05_fapesp_valores', 'Os valores FAPESP contratados pelo NIPE chegaram a R$ 8,2 milhões em 2025',
          'Valores nominais. Critério muda de "concedidos" para "contratados" em 2016. Fonte: AEPLAN, Tab. 10.6/10.8 [1].')


def fig06():
    r = le('fig06_producao_artigos.csv')
    anos = [int(x['ano_base']) for x in r]
    fig, ax = plt.subplots(figsize=(LARGA, 55 * MM))
    i_ = [n(x['artigos_circulacao_internacional']) or 0 for x in r]
    n_ = [n(x['artigos_circulacao_nacional']) or 0 for x in r]
    ax.bar(anos, i_, color=NIPE, width=0.7, label='Circulação internacional', gid='artigos-int')
    ax.bar(anos, n_, bottom=i_, color='#9CC3E0', width=0.7, label='Circulação nacional', gid='artigos-nac')
    ax.legend(loc='upper left')
    ax.set_xticks(anos)
    ax.yaxis.set_major_formatter(BR)
    salva(fig, 'fig06_producao_artigos', 'Os artigos declarados pelo NIPE passaram de nenhum em 2015 a 180 em 2025',
          'Fonte: AEPLAN/UNICAMP, Anuário Estatístico, Tab. 8.3, edições 2016–2026 [1].')


IND = {'projetos_por_dp': 'Projetos por docente ou pesquisador', 'artigos_por_dp': 'Artigos por docente ou pesquisador',
       'convenios': 'Convênios', 'eventos': 'Eventos promovidos', 'projetos': 'Projetos com financiamento', 'artigos': 'Artigos em periódicos'}


def compA():
    r = le('compA_series_indicadores.csv')
    s = defaultdict(lambda: defaultdict(list))
    for x in r:
        s[x['indicador']][x['sigla']].append((int(x['ano_base']), float(x['valor'])))
    fig, axs = plt.subplots(2, 3, figsize=(LARGA, 95 * MM), sharex=True)
    for ax, k in zip(axs.flat, IND):
        for sg, pts in s[k].items():
            if sg != 'NIPE':
                ax.plot(*zip(*sorted(pts)), color=CINZA, lw=0.6, alpha=0.8, gid=f'{k}-{sg}')
        ax.plot(*zip(*sorted(s[k]['NIPE'])), color=NIPE, lw=1.6, gid=f'{k}-NIPE')
        ax.set_title(IND[k], fontsize=7.5)
        ax.set_xticks([2015, 2020, 2025])
    salva(fig, 'compA_series_indicadores', 'O NIPE (azul) entre os centros e núcleos da COCEN (cinza), 2015–2025',
          'Fonte: AEPLAN/UNICAMP, Anuário Estatístico, Tab. 7.1 e 8.3, edições 2016–2026 [1].')


def compB():
    r = [x for x in le('compB_slope_2015_2025.csv') if x['indicador'] == 'artigos_por_dp']
    fig, ax = plt.subplots(figsize=(COLUNA, 80 * MM))
    for x in r:
        nipe = x['sigla'] == 'NIPE'
        ax.plot([0, 1], [float(x['valor_2015']), float(x['valor_2025'])], color=NIPE if nipe else CINZA, lw=1.6 if nipe else 0.7, marker='o', ms=2, gid=f"slope-{x['sigla']}")
        if nipe or float(x['valor_2025']) > 2:
            ax.text(1.04, float(x['valor_2025']), x['sigla'], va='center', fontsize=6.5, color=NIPE if nipe else CINZA_E)
    ax.set_xticks([0, 1], ['2015', '2025'])
    ax.set_xlim(-0.1, 1.3)
    ax.yaxis.set_major_formatter(BR2)
    salva(fig, 'compB_slope_2015_2025', 'Artigos por docente ou pesquisador, 2015 e 2025',
          'Fonte: AEPLAN, Tab. 7.1 e 8.3 [1].')


def compC():
    r = le('compC_ranking_nipe.csv')
    fig, axs = plt.subplots(2, 3, figsize=(LARGA, 80 * MM), sharex=True)
    for ax, k in zip(axs.flat, IND):
        pts = sorted((int(x['ano_base']), int(x['posicao_nipe']), int(x['centros_com_dado'])) for x in r if x['indicador'] == k)
        ax.fill_between([p[0] for p in pts], [p[2] for p in pts], 1, color='#EFEDE8', lw=0)
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=NIPE, lw=1.3, marker='o', ms=2.5, gid=f'rank-{k}')
        ax.set_ylim(23, 0.5)
        ax.set_yticks([1, 10, 20])
        ax.set_title(IND[k], fontsize=7.5)
        ax.set_xticks([2015, 2020, 2025])
    salva(fig, 'compC_ranking_nipe', 'Posição do NIPE entre os centros e núcleos da COCEN (1 = maior valor)',
          'Área clara: número de centros e núcleos com dado no ano. Fonte: AEPLAN, Tab. 7.1 e 8.3 [1].')


def compD():
    r = le('compD_participacao_nipe.csv')
    fig, ax = plt.subplots(figsize=(COLUNA, 55 * MM))
    for k, cor, rot in (('projetos', NIPE, 'Projetos'), ('artigos', '#9CC3E0', 'Artigos'), ('doc_pesq', CINZA_E, 'Docentes e pesquisadores')):
        pts = sorted((int(x['ano_base']), 100 * float(x['participacao'])) for x in r if x['indicador'] == k)
        ax.plot(*zip(*pts), color=cor, lw=1.3, gid=f'part-{k}')
        ax.text(pts[-1][0] + 0.3, pts[-1][1], rot, color=cor, fontsize=6.5, va='center')
    ax.set_ylabel('% do total da COCEN')
    ax.set_xticks([2015, 2020, 2025])
    salva(fig, 'compD_participacao_nipe', 'Participação do NIPE no total da COCEN',
          'Fonte: AEPLAN, Tab. 7.1 e 8.3 [1].')


def main():
    SAIDA.mkdir(exist_ok=True)
    for f in (hoje02, hoje03, hoje04, hoje05, fig01, fig02, fig03, fig04, fig05, fig06, compA, compB, compC, compD):
        f()
    indice()


def indice():
    """figuras_svg/index.html: lista das figuras em vetor, linkada pelas páginas."""
    from html import escape
    itens = chr(10).join(
        f'    <li><a href="{n}.svg">{escape(t)}</a> <span>· <a href="../data/figuras/{n}.csv">CSV</a></span></li>'
        for n, t in GERADAS)
    (SAIDA / 'index.html').write_text(f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Figuras em SVG · Data NIPE</title>
  <style>
    :root {{ --fg: #1d1d1b; --bg: #fbfaf7; --mut: #6b665e; --link: {NIPE}; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --fg: #ece9e3; --bg: #181816; --mut: #a8a299; --link: #56B4E9; }} }}
    body {{ font: 16px/1.5 system-ui, sans-serif; color: var(--fg); background: var(--bg); max-width: 760px; margin: 0 auto; padding: 32px 16px; }}
    a {{ color: var(--link); }} span, p {{ color: var(--mut); }} li {{ margin: .4em 0; }}
  </style>
</head>
<body>
  <p><a href="../index.html">← Data NIPE</a></p>
  <h1>Figuras em SVG</h1>
  <p>Vetores com texto editável, fonte sans-serif única, 175 mm ou 85 mm de largura, gerados por
  <code>scripts/exportar_svg.py</code> a partir dos CSVs de <code>data/figuras/</code>. As tabelas do site não têm SVG.</p>
  <ul>
{itens}
  </ul>
</body>
</html>
''', encoding='utf-8')
    print('index.html')


if __name__ == '__main__':
    main()
