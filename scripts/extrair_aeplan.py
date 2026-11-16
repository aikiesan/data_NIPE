"""Extrai dos Anuários Estatísticos da UNICAMP (AEPLAN) as tabelas por centro/núcleo da COCEN.

Uso: python scripts/extrair_aeplan.py PASTA_DOS_PDFS

Lê os PDFs das edições 2005–2026 (anos-base 2004–2025) e grava em data/fontes/aeplan/:
  COCEN_AEPLAN_tab7_1_2004-2025.csv   Tabela 7.1 (composição e atividades), todos os centros e núcleos
  COCEN_AEPLAN_tab8_3_2015-2025.csv   Tabela 8.3 (produção científica por centro/núcleo), edições 2016–2026
  COCEN_AEPLAN_conferencia.csv        testes de consistência de cada tabela extraída

Cada valor guarda edição, ano-base, página do PDF e a linha literal, como no
NIPE_AEPLAN_extracao_PDF_2004-2025.csv. A leitura usa as coordenadas das palavras
(pdfplumber): na 7.1, uma linha por sigla, com os números da mesma altura (ou da linha
seguinte, quando o nome ocupa duas linhas); na 8.3, as colunas vêm do cabeçalho de siglas
e os valores são atribuídos pela ordem da esquerda para a direita, quando a contagem bate,
ou pela coluna mais próxima, quando não bate (marcado em `atribuicao`).

Os PDFs não ficam no repositório (≈300 MB). Os nomes esperados estão em ARQUIVOS.
"""
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import pdfplumber

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / 'data' / 'fontes' / 'aeplan'
NIPE_CSV = SAIDA / 'NIPE_AEPLAN_extracao_PDF_2004-2025.csv'

ARQUIVOS = {e: f'anuario{e}.pdf' for e in range(2005, 2024)}
ARQUIVOS.update({2009: 'anuario2009-1.pdf', 2018: 'anuario2018-1.pdf', 2024: 'anuario-2024.pdf',
                 2025: 'anuario-2025.pdf', 2026: 'Anuario_2026.pdf'})

COLS_71 = ['docentes', 'pesquisadores', 'doutorandos', 'pos_doutorandos', 'pos_graduandos',
           'bolsistas', 'projetos_em_execucao', 'projetos_concluidos', 'producao_cientifica']
NUM = re.compile(r'^(?:-|\d{1,3}(?:\.\d{3})+|\d+)$')
SIGLA = re.compile(r'^[A-Z][A-Z0-9]{1,8}$')
CONHECIDAS = ['CBMEG', 'CCS', 'CCSNano', 'CEB', 'CEMIB', 'CEPAGRI', 'CEPETRO', 'CESOP', 'CIDDIC', 'CLE', 'CMU', 'CPQBA',
              'LUME', 'NEAB', 'NEPA', 'NEPAM', 'NEPO', 'NEPP', 'NICS', 'NIED', 'NIPE', 'NUDECRI', 'PAGU', 'CEIBC']
NAO_SIGLAS = {'CENTROS', 'NÚCLEOS', 'TOTAL', 'DENOMINAÇÃO', 'COMPOSIÇÃO', 'PROJETOS', 'E', 'DE', 'EM'}


def num(t):
    return 0 if t == '-' else int(t.replace('.', ''))


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def linhas(page, passo=3.2):
    """Agrupa as palavras da página em linhas pela altura (top)."""
    palavras = sorted(page.extract_words(), key=lambda w: (w['top'], w['x0']))
    grupos = []
    for w in palavras:
        if grupos and abs(w['top'] - grupos[-1][0]) <= passo:
            grupos[-1][1].append(w)
        else:
            grupos.append([w['top'], [w]])
    return [(t, sorted(ws, key=lambda w: w['x0'])) for t, ws in grupos]


def literal(ws):
    return ' '.join(w['text'] for w in ws)


def pagina(arq, pdf, n, chave):
    """Devolve a página n; se a tabela estiver girada (edições 2017–2019), gira 90° antes de ler."""
    page = pdf.pages[n - 1]
    if chave in (page.extract_text() or ''):
        return page
    import io
    import pypdf
    leitor = pypdf.PdfReader(str(arq))
    for rot in (90, 270):
        w = pypdf.PdfWriter()
        w.add_page(leitor.pages[n - 1])
        w.pages[0].rotate(rot)
        buf = io.BytesIO()
        w.write(buf)
        buf.seek(0)
        p = pdfplumber.open(buf).pages[0]
        if chave in (p.extract_text() or ''):
            return p
    return page


def paginas_dica():
    """Páginas das tabelas 7.1 e 8.3 já localizadas na extração do NIPE (uma por edição)."""
    dica = defaultdict(dict)
    with open(NIPE_CSV, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            tab = {'7.x': '7.1', '7.1': '7.1', '8.3': '8.3'}.get(r['tabela'])
            if tab and r['indicador'].startswith(('7.1_', '8.3_')):
                dica[int(r['edicao'])][tab] = int(r['pagina_pdf'])
    return dica


def oraculo_nipe():
    """Valores do NIPE na extração anterior, usados para conferir a nova leitura."""
    o = {}
    with open(NIPE_CSV, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            o[(int(r['edicao']), r['indicador'])] = r['valor']
    return o


# ---------------------------------------------------------------- Tabela 7.1
def tab71(page):
    rows = linhas(page)
    entidades, secao, total = [], 'centro', None
    for i, (top, ws) in enumerate(rows):
        ws = [w for w in ws if w['x0'] > 60]  # descarta o texto vertical da margem
        if not ws:
            continue
        t0 = ws[0]['text']
        if t0 in ('NÚCLEOS', 'NUCLEOS') or literal(ws).startswith('DENOMINAÇÃO NÚCLEOS'):
            secao = 'nucleo'
        nums = [w for w in ws if NUM.match(w['text']) and w['x0'] > 330]
        if t0.upper() == 'TOTAL':
            total = (nums, literal(ws))
            continue
        if t0 == 'CCSNano':
            t0 = 'CCS Nano'
        if (SIGLA.match(t0) or t0 == 'CCS Nano') and t0 not in NAO_SIGLAS and ws[0]['x0'] < 110:
            sigla = t0
            nome_ws = [w for w in ws[1:] if w not in nums]
            if nome_ws and nome_ws[0]['text'] in ('Nano',):
                sigla += ' ' + nome_ws[0]['text']
                nome_ws = nome_ws[1:]
            nome_ws = [w for w in nome_ws if not re.match(r'^\(\d+\)$', w['text'])]
            entidades.append({'sigla': sigla, 'nome': literal(nome_ws), 'nums': nums, 'lit': literal(ws),
                              'secao': secao, 'top': top})
        elif entidades and nums and not entidades[-1]['nums']:
            entidades[-1]['nums'] = nums  # nome em duas linhas: números na linha de baixo ou de cima
            entidades[-1]['lit'] += ' | ' + literal(ws)
        elif entidades and not nums and not SIGLA.match(t0) and abs(top - entidades[-1]['top']) < 14:
            entidades[-1]['nome'] += ' ' + literal(ws)
    # números que ficaram uma linha acima do nome (CEMIB em 2026): procura linha só de números logo antes
    for e in entidades:
        if not e['nums']:
            for top, ws in rows:
                nums = [w for w in ws if NUM.match(w['text']) and w['x0'] > 330]
                if nums and len(nums) == len(ws) and 0 < e['top'] - top < 8:
                    e['nums'], e['lit'] = nums, e['lit'] + ' | ' + literal(ws)
    return entidades, total


def colunas71(page_text, ncol):
    cols = COLS_71[:8]
    if ncol == 9:
        cols = COLS_71
    return cols


# ---------------------------------------------------------------- Tabela 8.3
def tab83(page):
    rows = linhas(page)
    cab = None
    for top, ws in rows:
        if ws and ws[0]['text'] in ('DESCRIÇÃO', 'DESCRICAO'):
            cab = ws[1:]
            break
    if cab is None:
        return None, []
    colunas = []
    cab2 = []
    for w in cab:  # siglas coladas no cabeçalho girado (ex.: "CBMEGCCS") e notas "(4)"
        if re.match(r'^\(\d+\)$', w['text']):
            continue
        partes = decompoe(w['text']) or [w['text']]
        larg = (w['x1'] - w['x0']) / len(w['text'])
        x = w['x0']
        for pt in partes:
            cab2.append(dict(w, text='CCS Nano' if pt == 'CCSNano' else pt, x0=x, x1=x + larg * len(pt)))
            x += larg * len(pt)
    cab = cab2
    for w in cab:
        if w['text'] == 'Nano' and colunas:
            colunas[-1]['sigla'] += ' Nano'
            colunas[-1]['x1'] = w['x1']
        else:
            colunas.append({'sigla': w['text'], 'x0': w['x0'], 'x1': w['x1']})
    for c in colunas:
        c['xc'] = (c['x0'] + c['x1']) / 2
    saida, ultimo = [], None
    for ordem, (top, ws) in enumerate(rows):
        ws = [w for w in ws if w['x0'] > 60]
        if not ws or ws[0]['text'] in ('DESCRIÇÃO', 'Tabela') or top < cab[0]['top'] + 2:
            continue
        nums = [w for w in ws if NUM.match(w['text']) and w['x0'] > colunas[0]['x0'] - 14]
        rot = [w for w in ws if w not in nums and w['x0'] < colunas[0]['x0'] - 4]
        if not nums:
            if rot and ultimo is not None and ultimo['n_nums'] == 0:
                ultimo['rotulo'] += ' ' + literal(rot)
            elif rot:
                ultimo = {'rotulo': literal(rot), 'nums': [], 'n_nums': 0, 'lit': literal(ws)}
                saida.append(ultimo)
            continue
        if rot:
            ultimo = {'rotulo': literal(rot), 'n_nums': len(nums), 'lit': literal(ws)}
            saida.append(ultimo)
        elif ultimo is not None and ultimo['n_nums'] == 0:
            ultimo.update(n_nums=len(nums), lit=ultimo['lit'] + ' | ' + literal(ws))
        else:
            continue
        if len(nums) == len(colunas):
            ultimo['valores'] = {c['sigla']: (w['text'], 'ordem') for c, w in zip(colunas, nums)}
        else:
            vals = {}
            for w in nums:
                xc = (w['x0'] + w['x1']) / 2
                c = min(colunas, key=lambda c: abs(c['xc'] - xc))
                vals[c['sigla']] = (w['text'], 'proximidade' if c['sigla'] not in vals else 'conflito')
            ultimo['valores'] = vals
    return [c['sigla'] for c in colunas], [s for s in saida if s.get('valores')]


def decompoe(t):
    """Divide um token em siglas conhecidas, se possível (ex.: CBMEGCCS → CBMEG, CCS)."""
    if t in CONHECIDAS:
        return [t]
    for k in sorted(CONHECIDAS, key=len, reverse=True):
        if t.startswith(k):
            resto = decompoe(t[len(k):])
            if resto:
                return [k] + resto
    return None


def chave83(rotulo):
    r = sem_acento(rotulo).upper()
    r = re.sub(r'\s*\(\d\)\s*', ' ', r)
    r = re.sub(r'\s+', ' ', r).strip()
    return r


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pasta = Path(sys.argv[1])
    dica, oraculo = paginas_dica(), oraculo_nipe()
    out71, out83, conf = [], [], []
    for edicao in sorted(ARQUIVOS):
        arq = pasta / ARQUIVOS[edicao]
        if not arq.exists():
            conf.append([edicao, edicao - 1, '-', 'arquivo', 'FALTA', f'{arq.name} não encontrado'])
            continue
        base = edicao - 1
        with pdfplumber.open(arq) as pdf:
            # ---- 7.1
            p71 = dica[edicao].get('7.1')
            ents, total = tab71(pagina(arq, pdf, p71, 'DENOMINA'))
            ncol = len(total[0]) if total else 0
            cols = COLS_71[:ncol]
            somas = [0] * ncol
            for e in ents:
                vals = [w['text'] for w in e['nums']]
                if len(vals) != ncol:
                    conf.append([edicao, base, p71, '7.1', 'AVISO', f"{e['sigla']}: {len(vals)} números para {ncol} colunas"])
                atr = 'ordem' if len(vals) == ncol else 'incompleta'
                for j, (c, v) in enumerate(zip(cols, vals)):
                    somas[j] += num(v)
                    out71.append([edicao, base, '7.1', p71, e['secao'], e['sigla'], e['nome'], c, num(v), v, atr, e['lit']])
            if total:
                tot = [num(w['text']) for w in total[0]]
                ok = somas == tot
                conf.append([edicao, base, p71, '7.1', 'OK' if ok else 'DIVERGE',
                             f'{len(ents)} centros/núcleos; soma das linhas {somas} × TOTAL impresso {tot}'])
                for c, v in zip(cols, tot):
                    out71.append([edicao, base, '7.1', p71, 'total', 'TOTAL', 'Total COCEN', c, v, str(v), 'ordem', total[1]])
            nipe = {r[7]: r[8] for r in out71 if r[0] == edicao and r[5] == 'NIPE'}
            for c in ('docentes', 'pesquisadores', 'bolsistas', 'projetos_em_execucao'):
                esperado = oraculo.get((edicao, '7.1_' + c))
                if esperado is not None and nipe.get(c) is not None:
                    conf.append([edicao, base, p71, '7.1', 'OK' if float(esperado) == nipe[c] else 'DIVERGE',
                                 f'NIPE {c}: {nipe[c]} × extração anterior {esperado}'])
            # ---- 8.3
            p83 = dica[edicao].get('8.3')
            if p83:
                siglas, linhas83 = tab83(pagina(arq, pdf, p83, 'DESCRI'))
                if siglas is None:
                    conf.append([edicao, base, p83, '8.3', 'FALTA', 'cabeçalho de siglas não encontrado'])
                    continue
                atribs = defaultdict(int)
                for ordem, l in enumerate(linhas83):
                    for s, (v, atr) in l['valores'].items():
                        atribs[atr] += 1
                        out83.append([edicao, base, '8.3', p83, ordem, l['rotulo'], chave83(l['rotulo']), s, num(v), v, atr, l['lit']])
                conf.append([edicao, base, p83, '8.3', 'OK' if not atribs.get('conflito') else 'AVISO',
                             f'{len(siglas)} colunas ({" ".join(siglas)}); {len(linhas83)} linhas; atribuição {dict(atribs)}'])
                nipe83 = {}
                for r in out83:
                    if r[0] == edicao and r[7] == 'NIPE':
                        nipe83.setdefault(r[6], r[8])
                for rot, ind in (('PROJETOS COM FINANCIAMENTO', '8.3_PROJETOS COM FINANCIAMENTO'),
                                 ('CONVENIOS', '8.3_CONVÊNIOS'), ('PROMOCAO DE EVENTOS', '8.3_PROMOÇÃO DE EVENTOS'),
                                 ('LINHAS DE PESQUISA', '8.3_LINHAS DE PESQUISA')):
                    esperado = oraculo.get((edicao, ind))
                    if esperado is not None:
                        conf.append([edicao, base, p83, '8.3', 'OK' if float(esperado) == nipe83.get(rot) else 'DIVERGE',
                                     f'NIPE {rot}: {nipe83.get(rot)} × extração anterior {esperado}'])
        print(edicao, 'ok')
    SAIDA.mkdir(parents=True, exist_ok=True)
    grava(SAIDA / 'COCEN_AEPLAN_tab7_1_2004-2025.csv',
          ['edicao', 'ano_base', 'tabela', 'pagina_pdf', 'secao', 'sigla', 'nome', 'indicador', 'valor', 'valor_impresso', 'atribuicao', 'linha_literal'], out71)
    grava(SAIDA / 'COCEN_AEPLAN_tab8_3_2015-2025.csv',
          ['edicao', 'ano_base', 'tabela', 'pagina_pdf', 'ordem_linha', 'rotulo', 'rotulo_normalizado', 'sigla', 'valor', 'valor_impresso', 'atribuicao', 'linha_literal'], out83)
    grava(SAIDA / 'COCEN_AEPLAN_conferencia.csv', ['edicao', 'ano_base', 'pagina_pdf', 'tabela', 'resultado', 'detalhe'], conf)
    print('\n'.join(' · '.join(map(str, c)) for c in conf if c[4] != 'OK'))


def grava(caminho, cab, linhas_):
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(cab)
        w.writerows(linhas_)
    print(caminho.name, len(linhas_), 'linhas')


if __name__ == '__main__':
    main()
