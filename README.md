# Data NIPE

Leitura em dados do Núcleo Interdisciplinar de Planejamento Energético (NIPE) da Unicamp, de 1984 a 2026: quem atua no núcleo, o que produz, como mudou e onde fica entre os centros e núcleos da Coordenadoria de Centros e Núcleos Interdisciplinares de Pesquisa (COCEN).

**Site:** https://aikiesan.github.io/data_NIPE/

Três abas:

- **NIPE hoje** (`index.html`, a principal): o retrato de 2025 segundo o Anuário Estatístico da Assessoria de Economia e Planejamento (AEPLAN), os centros sediados no núcleo, o Centro Paulista de Estudos em Biogás e Bioprodutos (CP2b) e os números em disputa.
- **Histórico 1985–2026** (`historico.html`): marcos, coordenações, equipe, projetos, recursos da FAPESP e artigos.
- **NIPE entre os centros** (`comparacao.html`): o NIPE frente aos demais centros e núcleos da COCEN, 2015–2025.

## Fontes

1. UNICAMP, AEPLAN. Anuário estatístico, edições 2005 a 2026 (anos-base 2004 a 2025), Tab. 7.1, 8.3 e 10.6/10.8. https://aeplan.unicamp.br/
2. UNICAMP. Anuário estatístico: centros e núcleos (versão web), 2000–2021. https://www2.unicamp.br/anuario/
3. Arquivo Histórico NIPE-CP2b. Registro de 12/11/2026, exportação de 16/11/2026 (`docs/registro/`, `data/fontes/arquivo/`).
4. FAPESP, Biblioteca Virtual. https://bv.fapesp.br/
5. UNICAMP, Portal EDAT, consulta de 10/11/2026. https://portal.edat.unicamp.br/
6. UNICAMP, COCEN. https://www.cocen.unicamp.br/
7. NIPE. https://nipe.unicamp.br/
8. CP2b. https://cp2b.unicamp.br/
9. CNPq, Plataforma Lattes: currículos dos coordenadores, consulta de 16/11/2026. https://lattes.cnpq.br/

Cada figura cita a sua fonte e tem um link para o CSV com os números que desenha. O dicionário completo, as decisões de tratamento e as divergências conhecidas da fonte estão em [`data/LEIAME.md`](data/LEIAME.md).

## Estrutura

```
index.html                     aba NIPE hoje (principal)
historico.html                 aba Histórico 1985–2026
comparacao.html                aba NIPE entre os centros
assets/css/style.css           tipografia, cores, layout
assets/js/app.js               todos os gráficos (D3 v7)
data/nipe.json                 números do texto e séries usadas pelas páginas
data/paleta.json               mapeamento único de cores (site e SVGs)
data/figuras/*.csv             os números de cada figura (hoje0N, figNN, compX)
data/fontes/arquivo/           CSVs do Arquivo Histórico [3]
data/fontes/aeplan/            extração das Tab. 7.1 e 8.3 da AEPLAN, todos os centros [1]
data/nipe_dados.zip            tudo de data/ num arquivo só
data/LEIAME.md                 dicionário dos dados e fontes
docs/registro/                 registro mestre, histórico, linha do tempo e conflitos (NIPE e CP2b)
docs/varreduras/               relatórios diários de varredura do arquivo
figuras_svg/                   cada figura em SVG, para acabamento
scripts/extrair_aeplan.py      extrai as Tab. 7.1 e 8.3 dos PDFs da AEPLAN
scripts/prepare_data.py        gera data/nipe.json
scripts/export_figuras.py      gera data/figuras/*.csv e o ZIP
scripts/exportar_svg.py        gera figuras_svg/
scripts/verificar_dados.py     confere números, links e privacidade
.github/workflows/             publicação no Pages e conferência dos dados
```

Sem build: HTML, CSS e JS estáticos. D3 vem do cdnjs.

## Atualizar os dados

1. Para uma nova edição da AEPLAN, baixe o PDF, acrescente-o em `ARQUIVOS` no `scripts/extrair_aeplan.py` e rode:

   ```bash
   python scripts/extrair_aeplan.py caminho/da/pasta/dos/pdfs
   ```

   Confira `data/fontes/aeplan/COCEN_AEPLAN_conferencia.csv`: toda linha `DIVERGE` nova precisa ser explicada em `data/LEIAME.md`.
2. Para uma nova exportação do arquivo histórico, copie os CSVs para `data/fontes/arquivo/` (com a versão no nome) e os `.md` para `docs/`. Os CSVs de pessoas não entram no repositório.
3. Rode, nesta ordem:

   ```bash
   python scripts/prepare_data.py
   python scripts/export_figuras.py
   python scripts/exportar_svg.py
   python scripts/verificar_dados.py
   ```

   Se um número do texto mudar, o verificador aponta o `data-k` a corrigir no HTML.
4. Faça commit e push em `main`.

Dependências: Python 3.11 com pandas, matplotlib e (só para a extração) pdfplumber e pypdf. O verificador usa apenas a biblioteca padrão.

## Privacidade

O repositório é público. Não há CPF, e-mail, telefone, gênero nem listas nominais de pessoas; nomes aparecem apenas para cargos públicos de coordenação, com a fonte do mandato. `scripts/verificar_dados.py` falha se encontrar qualquer um desses padrões, e roda a cada push.

## Ver localmente

```bash
python -m http.server 8000
```

Depois abra http://localhost:8000.

## Publicação

O workflow `.github/workflows/pages.yml` roda o verificador e, se passar, publica a raiz do repositório a cada push em `main`. O Pages precisa estar ativado com a fonte **GitHub Actions** antes do primeiro deploy (em *Settings → Pages*, ou com `gh api repos/aikiesan/data_NIPE/pages -X POST -f build_type=workflow`).
