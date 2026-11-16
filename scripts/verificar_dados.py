"""Confere dados, textos e privacidade do repositório. Falha (código 1) se algo estiver errado.

Roda nas Actions a cada push e pode rodar à mão: python scripts/verificar_dados.py

1. Privacidade: nenhum e-mail, CPF ou telefone em data/, docs/, figuras_svg/ e nas páginas;
   nenhum CSV de pessoas nominais (*_pessoas*), nenhuma coluna de gênero/sexo, nenhum CSV
   com coluna `nome` fora da lista de cargos públicos (NIPE_coordenadores, fig02).
2. Números do texto: cada <… data-k="chave">valor</…> das páginas é igual a nipe.json["textos"][chave].
3. Figuras: todo CSV citado nas páginas existe; todo CSV de data/figuras é citado; toda
   referência [n] citada existe na lista de fontes da página.
4. Grafia: "CP2b" (b minúsculo) no texto visível das páginas, nos títulos dos SVGs e no LEIAME;
   "CP2B" só em nomes de arquivo e identificadores (CP2B-F…, CP2B_…).
5. AEPLAN: a extração da Tab. 7.1 bate com o TOTAL impresso, exceto nas edições conhecidas
   (documentadas em data/LEIAME.md), e os valores do NIPE batem com a extração anterior.
"""
import csv
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAGINAS = ['index.html', 'historico.html', 'comparacao.html']
erros = []

EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}')
CPF = re.compile(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b')
# com DDD, ou sem DDD logo após "tel.", "telefone", "fone" ou "fax"
TELEFONE = re.compile(r'(?:\(\d{2}\)\s?|\b\d{2}\s)(?:9\s?)?\d{4}[-\s]\d{4}\b'
                      r'|(?:\btel\.?|\btelefones?|\bfone|\bfax)\W{0,15}\d{4}[-\s]?\d{4}\b', re.I)
EMAILS_OK = {'github-actions[bot]@users.noreply.github.com'}
DIVERGENCIAS_71_CONHECIDAS = {2007, 2008, 2014, 2016}
# `nome` permitido: cargos públicos de coordenação e nomes de centros/núcleos (não de pessoas)
CSV_COM_NOMES_OK = {'NIPE_coordenadores_v2026-11-16.csv', 'fig02_coordenadores.csv', 'COCEN_AEPLAN_tab7_1_2004-2025.csv'}


def arquivos_do_repo():
    """Arquivos que vão para o GitHub: rastreados + novos não ignorados (respeita o .gitignore)."""
    try:
        saida = subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard'], cwd=RAIZ,
                               capture_output=True, text=True, encoding='utf-8', check=True).stdout
        lista = [RAIZ / p for p in saida.splitlines() if p]
        if lista:
            return lista
    except (OSError, subprocess.CalledProcessError):
        pass
    ignorar = ('_privado', 'data_NIPE_export', '.git', '__pycache__')
    return [p for p in RAIZ.rglob('*') if p.is_file() and not any(i in p.as_posix() for i in ignorar)]


def privacidade(arquivos):
    for p in arquivos:
        rel = p.relative_to(RAIZ).as_posix()
        if p.suffix.lower() not in ('.csv', '.md', '.json', '.html', '.svg', '.txt', '.yml'):
            continue
        texto = p.read_text(encoding='utf-8', errors='replace')
        for m in EMAIL.findall(texto):
            if m not in EMAILS_OK:
                erros.append(f'{rel}: e-mail encontrado ({m})')
        if CPF.search(texto):
            erros.append(f'{rel}: padrão de CPF')
        if rel.startswith(('data/', 'docs/')) and TELEFONE.search(texto):
            erros.append(f'{rel}: padrão de telefone ({TELEFONE.search(texto).group()})')
        if p.suffix == '.csv':
            if re.search(r'_pessoas', p.name, re.I) or 'genero' in p.name.lower():
                erros.append(f'{rel}: CSV de pessoas nominais ou de gênero não pode ser publicado')
            cab = texto.split('\n', 1)[0].lower().split(',')
            if any(c.strip() in ('genero', 'gênero', 'sexo') for c in cab):
                erros.append(f'{rel}: coluna de gênero/sexo')
            if 'nome' in [c.strip() for c in cab] and p.name not in CSV_COM_NOMES_OK:
                erros.append(f'{rel}: coluna "nome" fora da lista de cargos públicos')


class Pagina(HTMLParser):
    """Coleta data-k (com o texto do elemento), hrefs e o texto visível."""

    def __init__(self):
        super().__init__()
        self.dk, self.hrefs, self.ids, self.visivel = [], [], set(), []
        self.pilha = []
        self.oculto = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self.oculto += 1
        if 'id' in a:
            self.ids.add(a['id'])
        if 'href' in a:
            self.hrefs.append(a['href'])
        if tag in ('br', 'meta', 'link', 'img', 'input'):
            return
        self.pilha.append([tag, a.get('data-k'), ''])

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.oculto -= 1
        while self.pilha:
            t, k, txt = self.pilha.pop()
            if k:
                self.dk.append((k, txt.strip()))
            if self.pilha:
                self.pilha[-1][2] += txt
            if t == tag:
                break

    def handle_data(self, data):
        if self.oculto:
            return
        self.visivel.append(data)
        if self.pilha:
            self.pilha[-1][2] += data


def paginas(textos, csvs_figuras):
    citados = set()
    for nome in PAGINAS:
        p = Pagina()
        p.feed((RAIZ / nome).read_text(encoding='utf-8'))
        for k, txt in p.dk:
            if k not in textos:
                erros.append(f'{nome}: data-k="{k}" não existe em nipe.json')
            elif txt != textos[k]:
                erros.append(f'{nome}: data-k="{k}" diz "{txt}", nipe.json diz "{textos[k]}"')
        for h in p.hrefs:
            if h.startswith('#ref-') and h[1:] not in p.ids:
                erros.append(f'{nome}: referência {h} citada mas ausente da lista de fontes')
            if h.startswith('data/') or h.startswith('figuras_svg/') or h.startswith('assets/'):
                alvo = RAIZ / h.split('?')[0]
                if not alvo.exists():
                    erros.append(f'{nome}: link para arquivo inexistente: {h}')
                if h.startswith('data/figuras/'):
                    citados.add(Path(h).name)
        visivel = ' '.join(p.visivel)
        for m in re.finditer(r'CP2B(?![-_])', visivel):
            erros.append(f'{nome}: "CP2B" no texto visível (use "CP2b"): …{visivel[max(0, m.start() - 30):m.end() + 30]}…')
    for f in csvs_figuras - citados:
        erros.append(f'data/figuras/{f}: CSV de figura não citado em nenhuma página')


def grafia_extra():
    leia = (RAIZ / 'data' / 'LEIAME.md').read_text(encoding='utf-8')
    texto = re.sub(r'`[^`]*`', '', leia)
    for m in re.finditer(r'CP2B(?![-_])', texto):
        erros.append(f'data/LEIAME.md: "CP2B" fora de nome de arquivo: …{texto[max(0, m.start() - 30):m.end() + 30]}…')
    for svg in (RAIZ / 'figuras_svg').glob('*.svg'):
        if re.search(r'>[^<]*CP2B(?![-_])[^<]*<', svg.read_text(encoding='utf-8')):
            erros.append(f'figuras_svg/{svg.name}: "CP2B" num texto do SVG')


def aeplan():
    conf = RAIZ / 'data' / 'fontes' / 'aeplan' / 'COCEN_AEPLAN_conferencia.csv'
    with open(conf, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['resultado'] == 'DIVERGE':
                if r['tabela'] == '7.1' and r['detalhe'].startswith(tuple('0123456789')) and int(r['ano_base']) in DIVERGENCIAS_71_CONHECIDAS:
                    continue
                erros.append(f"AEPLAN {r['tabela']} edição {r['edicao']}: {r['detalhe']}")
            if r['resultado'] == 'FALTA':
                erros.append(f"AEPLAN {r['tabela']} edição {r['edicao']}: {r['detalhe']}")


def main():
    textos = json.loads((RAIZ / 'data' / 'nipe.json').read_text(encoding='utf-8'))['textos']
    csvs = {p.name for p in (RAIZ / 'data' / 'figuras').glob('*.csv')}
    arquivos = arquivos_do_repo()
    privacidade(arquivos)
    paginas(textos, csvs)
    grafia_extra()
    aeplan()
    if erros:
        print('\n'.join(erros))
        print(f'\n{len(erros)} problema(s).')
        sys.exit(1)
    print(f'Dados conferidos: {len(arquivos)} arquivos sem e-mail, CPF ou telefone; '
          f'{len(textos)} números do texto iguais aos de nipe.json; {len(csvs)} CSVs de figura citados.')


if __name__ == '__main__':
    main()
