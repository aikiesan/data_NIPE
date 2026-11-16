# Dicionário dos dados — Data NIPE

Este arquivo descreve cada tabela publicada em `data/`, as fontes numeradas citadas no site e os cuidados de leitura de cada série. Os números do texto das páginas saem de `data/nipe.json`; os números de cada figura saem do CSV correspondente em `data/figuras/`. O script `scripts/verificar_dados.py` confere as duas coisas a cada push.

Siglas usadas: NIPE (Núcleo Interdisciplinar de Planejamento Energético), CP2b (Centro Paulista de Estudos em Biogás e Bioprodutos), COCEN (Coordenadoria de Centros e Núcleos Interdisciplinares de Pesquisa), AEPLAN (Assessoria de Economia e Planejamento da Unicamp), EDAT (Portal de dados de pessoal da Unicamp), FAPESP (Fundação de Amparo à Pesquisa do Estado de São Paulo), BV (Biblioteca Virtual da FAPESP).

Formato de todos os CSVs: UTF-8, separador vírgula, ponto como separador decimal, células vazias para dado ausente. Valores em reais são nominais (sem correção monetária).

## Fontes

1. UNIVERSIDADE ESTADUAL DE CAMPINAS. Assessoria de Economia e Planejamento. **Anuário estatístico**. Campinas: UNICAMP, 2005–2026. Edições 2005 a 2026 (anos-base 2004 a 2025), Tab. 7.1 (pessoal e projetos dos centros e núcleos), 8.3 (produção dos centros e núcleos) e 10.6/10.8 (recursos FAPESP). https://aeplan.unicamp.br/
2. UNIVERSIDADE ESTADUAL DE CAMPINAS. **Anuário estatístico: centros e núcleos** (versão web). Campinas: UNICAMP, 2000–2021. https://www2.unicamp.br/anuario/
3. ARQUIVO HISTÓRICO NIPE-CP2b. Registro mestre, conflitos, linha do tempo e tabelas. Estado do registro de 12/11/2026 (inclui os adendos até essa data), exportação de 16/11/2026. Publicado em `docs/registro/` e `data/fontes/arquivo/`.
4. FUNDAÇÃO DE AMPARO À PESQUISA DO ESTADO DE SÃO PAULO. **Biblioteca Virtual da FAPESP**. Processos citados no registro. https://bv.fapesp.br/
5. UNIVERSIDADE ESTADUAL DE CAMPINAS. **Portal EDAT**: vínculos da unidade NIPE. Consulta de 10/11/2026. https://portal.edat.unicamp.br/
6. UNIVERSIDADE ESTADUAL DE CAMPINAS. Coordenadoria de Centros e Núcleos Interdisciplinares de Pesquisa. **Centros e núcleos**. https://www.cocen.unicamp.br/
7. NÚCLEO INTERDISCIPLINAR DE PLANEJAMENTO ENERGÉTICO. Sítio institucional. https://nipe.unicamp.br/
8. CENTRO PAULISTA DE ESTUDOS EM BIOGÁS E BIOPRODUTOS. Sítio institucional. https://cp2b.unicamp.br/
9. CONSELHO NACIONAL DE DESENVOLVIMENTO CIENTÍFICO E TECNOLÓGICO. **Plataforma Lattes**: currículos dos coordenadores do NIPE. Consulta de 16/11/2026. https://lattes.cnpq.br/

Cada linha das tabelas do arquivo histórico traz `id_fato` (ex.: `NIPE-F0070`, `CP2B-F0012`), que remete ao fato correspondente em `docs/registro/*_REGISTRO_MESTRE_v2026-11-12.md`, e `selo`, a classificação do registro: `[V]` (verificado na fonte citada) ou `[S]` (fonte secundária, sem documento primário localizado). No registro de 12/11/2026, 792 dos 796 fatos do NIPE têm selo `[V]`.

## Decisões de tratamento

1. **Série de referência 2004–2025: AEPLAN em PDF [1].** É a mesma fonte para todos os centros e cobre o período inteiro. O Anuário web [2] entra só como complemento para 2000–2003 em projetos com financiamento; onde as duas fontes cobrem o mesmo ano e divergem (2020 e 2021), adota-se o PDF.
2. **Total de "produções" de 2025 não é publicado.** A Tab. 8.3 da edição 2026 imprime 63 para o NIPE, enquanto a soma dos subitens dá 363 (conflitos K51 e K57 do registro). O site usa os subitens (artigos), que não estão em disputa.
3. **Projetos do arquivo separados por centro.** `NIPE_projetos_v2026-11-01.csv` reúne projetos do NIPE e dos centros sediados no núcleo (CEP, CP2b, CePIL e outros). O site mostra a divisão pela coluna `centro` e não soma esse arquivo com `CP2B_projetos_v2026-10-25.csv`, porque os dois registros se sobrepõem.
4. **Estado do registro de 12/11/2026.** Os CSVs do arquivo vão até o fato F0751; os adendos posteriores entram nos documentos de `docs/registro/`.
5. **Pessoas.** Publicam-se apenas agregados. Nomes aparecem somente para cargos públicos de coordenação, com a fonte de cada mandato. Não há gênero, nem inferido nem declarado, em nenhuma tabela.

## `data/nipe.json`

Arquivo único lido pelas três páginas. Chaves principais:

| Chave | Conteúdo |
|---|---|
| `meta` | data de geração, data do registro e da exportação, edições AEPLAN, anos da comparação |
| `textos` | cada número citado no texto das páginas, já formatado em português; o HTML traz o mesmo valor em `data-k` e o verificador exige igualdade |
| `paleta` | cópia de `data/paleta.json` |
| `serie_nipe` | série anual do NIPE, 2004–2025, AEPLAN [1] |
| `projetos_www2` | projetos com financiamento 2000–2021 no Anuário web [2] |
| `arquivo` | contagens do arquivo histórico [3]: projetos por centro, coordenadores, números do CP2b |
| `marcos` | marcos institucionais 1984–2026 [3] |
| `disputa` | números em disputa e o tratamento adotado |
| `cocen` | comparação com os centros e núcleos: indicadores, nomes, séries, posição do NIPE, participação, 2015 × 2025 |

`data/paleta.json` guarda o mapeamento único de cores usado pelo site e pelos SVGs (paleta Okabe-Ito): NIPE `#0072B2`, CP2b `#E69F00`, demais centros em cinza `#B9B4AC`.

## `data/figuras/` — um CSV por figura

### Aba "NIPE hoje" (`index.html`)

| Arquivo | Colunas | Fonte |
|---|---|---|
| `hoje01_indicadores.csv` | `indicador`, `valor`, `unidade`, `ano_base`, `fonte` — os números do retrato de 2025 | [1], [3], [5] |
| `hoje02_serie_recente.csv` | `ano_base`, `docentes`, `pesquisadores`, `bolsistas`, `projetos_com_financiamento`, `artigos` — 2015–2025 | [1] |
| `hoje03_projetos_por_centro.csv` | `centro`, `registros_de_projeto`, `fonte` — registros de projeto do arquivo por centro | [3] |
| `hoje04_vinculos_edat.csv` | `papel`, `vinculos`, `fonte` — vínculos ativos na unidade NIPE | [5] |
| `hoje05_cp2b_publicacoes.csv` | `ano`, `tipo`, `publicacoes` — publicações do CP2b registradas no arquivo | [3] |
| `hoje06_numeros_em_disputa.csv` | `numero`, `leitura_a`, `leitura_b`, `conflito_registro`, `tratamento_no_site` | [1], [2], [3] |

### Aba "Histórico 1985–2026" (`historico.html`)

| Arquivo | Colunas | Fonte |
|---|---|---|
| `fig01_marcos.csv` | `data`, `marco`, `descricao`, `id_fato` | [3] |
| `fig02_coordenadores.csv` | `nome`, `cargo`, `ano_inicio`, `ano_fim` (usados no desenho), `inicio_registrado`, `fim_registrado` (texto do registro, com ressalvas), `selo`, `id_fato`, `fonte_url`, `lattes_periodo`, `conferencia_lattes`, `lattes_atualizado`, `lattes_url` | [2], [3], [6], [7], [9] |
| `fig03_equipe_tab7_1.csv` | `ano_base`, `edicao`, `docentes`, `pesquisadores`, `pos_doutorandos`, `bolsistas` | [1] Tab. 7.1 |
| `fig04_projetos_com_financiamento.csv` | `ano_base`, `fonte`, `projetos_com_financiamento` | [1] Tab. 8.3; [2] até 2003 |
| `fig05_fapesp_valores.csv` | `ano_base`, `criterio` (concedidos até o ano-base 2015, contratados a partir de 2016), `fapesp_concedidos_ou_contratados_rs`, `fapesp_liberados_rs` | [1] Tab. 10.6/10.8 |
| `fig06_producao_artigos.csv` | `ano_base`, `artigos_circulacao_internacional`, `artigos_circulacao_nacional`, `artigos_total`, `producoes_total` (vazio em 2025) | [1] Tab. 8.3 |

Os mandatos de `fig02_coordenadores.csv` se sobrepõem em alguns anos (1997, 2002, 2011, 2013, 2019): o registro guarda o que cada fonte diz e o desenho mostra as sobreposições sem resolvê-las. Mandatos sem ato localizado vêm anotados em `fim_registrado`.

**Conferência com os currículos Lattes [9] (16/11/2026).** Os 12 currículos dos coordenadores foram lidos na seção "Atuação profissional". O Lattes é declaração do próprio pesquisador: quando concorda com outra fonte (Anuário, EDAT, Diário Oficial), a data passa a seguir o currículo, que é mais preciso no mês; quando é a única fonte, o selo é `[S]`. A coluna `conferencia_lattes` diz, para cada mandato, se o currículo confirma, corrige, acrescenta, diverge ou não registra o cargo. Resultado:

- confirmam: L. A. B. Cortez (11–12/1997 a 01–03/2002 e 01/2012 a 04/2013), E. P. da Silva (fim em 12/2005), T. T. Franco (2013–2017, fecha o conflito K27), B. S. Moraes (coordenadora 2021–2025 e associada desde 2025);
- corrigem: S. V. Bajay coordenou de 08/1993 a 12/1997, e não "1994–1999" (fonte secundária; conflitos K08 e K40); L. A. Rossi coordenou de 01/2006 a 12/2009, e não até 2008; E. P. da Silva começou em 01/2002, e não em 2001;
- acrescentam: L. A. Rossi foi coordenador associado de 03/2004 a 12/2005 (só no Lattes, selo `[S]`);
- divergem: G. M. Jannuzzi declara a coordenação de 01/2010 a 01/2013, o que se sobrepõe ao registro de I. M. L. D'Ottaviano no Anuário 2011 e ao início do segundo período de L. A. B. Cortez (01/2012); o desenho encerra o mandato em 2011 e o texto registra a divergência;
- não registram o cargo: C. A. Mariottoni (currículo atualizado em 2018), I. M. L. D'Ottaviano (que coordenava a COCEN de 05/2009 a 05/2013, o que reforça a hipótese de coordenação pro tempore, K11), G. P. Valença, M. P. da Cunha e J. M. F. J. da Silveira (nenhum registro de coordenação do NIPE em 2025, K36 segue aberto).

Os currículos ficam fora do repositório; publicam-se só as datas dos cargos de coordenação, o link público de cada currículo e a data da sua última atualização. O detalhamento por conflito está em `docs/registro/NIPE_ADENDO_LATTES_v2026-11-16.md`.

### Aba "NIPE entre os centros" (`comparacao.html`)

| Arquivo | Colunas | Fonte |
|---|---|---|
| `compA_series_indicadores.csv` | `ano_base`, `sigla`, `centro_ou_nucleo`, `indicador`, `valor` — todos os centros, 2015–2025 | [1] Tab. 7.1 e 8.3 |
| `compB_slope_2015_2025.csv` | `sigla`, `indicador`, `valor_2015`, `valor_2025`, `diferenca`, `razao_2025_2015` | [1] |
| `compC_ranking_nipe.csv` | `ano_base`, `indicador`, `posicao_nipe` (1 = maior valor), `centros_com_dado`, `valor_nipe`, `mediana_cocen` | [1] |
| `compD_participacao_nipe.csv` | `ano_base`, `indicador`, `nipe`, `total_cocen`, `participacao` (fração de 0 a 1) | [1] |

Indicadores (coluna `indicador`):

| Código | Definição |
|---|---|
| `projetos` | projetos com financiamento (Tab. 8.3, "Projetos com financiamento") |
| `artigos` | artigos publicados em periódicos (Tab. 8.3) |
| `convenios` | convênios (Tab. 8.3) |
| `eventos` | promoção de eventos (Tab. 8.3) |
| `doc_pesq` | docentes + pesquisadores (Tab. 7.1) |
| `projetos_por_dp` | `projetos` ÷ `doc_pesq` |
| `artigos_por_dp` | `artigos` ÷ `doc_pesq` |

Empates recebem a mesma posição (a menor). Centros com `doc_pesq` igual a zero ficam sem valor nas razões.

## `data/fontes/` — tabelas de origem

### `data/fontes/arquivo/` — Arquivo Histórico NIPE-CP2b [3]

Cópias dos CSVs da exportação de 16/11/2026, com a versão no nome do arquivo.

| Arquivo | Linhas | Conteúdo |
|---|---|---|
| `NIPE_series_anuais_v2026-11-01.csv` | 43 | série anual consolidada pelo registro (projetos, FAPESP, produção, área), com `fonte_url`, `selo`, `id_fato`, `nota` |
| `NIPE_projetos_v2026-11-01.csv` | 225 | projetos do NIPE e dos centros sediados; coluna `centro` separa NIPE, CEP, CP2b, CePIL |
| `NIPE_publicacoes_v2026-10-25.csv` | 103 | publicações com DOI ligadas ao NIPE |
| `NIPE_parceiros_v2026-11-01.csv` | 41 | organizações parceiras |
| `NIPE_coordenadores_v2026-11-16.csv` | 15 | mandatos de coordenação, com ato, fonte e a conferência com o currículo Lattes [9] |
| `CP2B_projetos_v2026-10-25.csv` | 34 | projetos do CP2b |
| `CP2B_publicacoes_v2026-11-01.csv` | 73 | publicações do CP2b |
| `CP2B_parceiros_v2026-11-01.csv` | 16 | parceiros do CP2b |

A coluna `responsavel` de `NIPE_projetos` reproduz o pesquisador responsável tal como publicado na BV FAPESP [4]. Os CSVs de pessoas do arquivo (`*_pessoas*.csv`) e a planilha de conferência de gênero não são publicados.

### `data/fontes/aeplan/` — extração dos Anuários AEPLAN [1]

| Arquivo | Conteúdo |
|---|---|
| `COCEN_AEPLAN_tab7_1_2004-2025.csv` | Tab. 7.1, todos os centros e núcleos, anos-base 2004–2025, uma linha por centro × indicador |
| `COCEN_AEPLAN_tab8_3_2015-2025.csv` | Tab. 8.3, todos os centros e núcleos, anos-base 2015–2025, uma linha por centro × rótulo |
| `COCEN_AEPLAN_conferencia.csv` | resultado da conferência de cada edição (`OK`, `DIVERGE`, `AVISO`) |
| `NIPE_AEPLAN_extracao_PDF_2004-2025.csv` | extração anterior, só do NIPE, usada como referência de conferência |
| `NIPE_AEPLAN_serie_2004-2025_PDF.csv` | série do NIPE em formato largo, a partir da extração anterior |

Colunas das extrações COCEN: `edicao` (ano da edição do Anuário), `ano_base` (ano a que os dados se referem, em geral `edicao − 1`), `tabela`, `pagina_pdf` (página do arquivo PDF, não a numeração impressa), `secao` (centro ou núcleo), `sigla`, `nome`, `indicador` ou `rotulo`/`rotulo_normalizado`/`ordem_linha`, `valor` (numérico), `valor_impresso` (como aparece no PDF, inclusive `-`), `atribuicao` e `linha_literal` (a linha do PDF, para conferência).

`atribuicao` diz como cada número foi ligado à coluna: `ordem` (a linha tem tantos números quantas colunas e a ligação é posicional), um número de coluna (ligado pela posição horizontal, quando faltam números) ou `incompleta` (excluída da análise).

#### Método de extração

`scripts/extrair_aeplan.py` lê os PDFs com pdfplumber e agrupa as palavras em linhas pela coordenada vertical, em vez de converter a página em texto corrido (que desalinha colunas). As edições 2017 a 2019 trazem as tabelas em páginas giradas; o script gira a página antes da leitura. Cabeçalhos com siglas coladas no PDF (ex.: "CBMEGCCS") são separados por decomposição nas siglas conhecidas.

Conferências feitas a cada extração:

- a soma das linhas de cada coluna da Tab. 7.1 é comparada com o TOTAL impresso;
- os valores do NIPE são comparados com a extração anterior (`NIPE_AEPLAN_extracao_PDF_2004-2025.csv`); todos coincidem.

#### Divergências conhecidas da fonte

Nas edições abaixo a soma das linhas da Tab. 7.1 difere do TOTAL impresso no próprio PDF. A extração reproduz as linhas como impressas; a diferença é da fonte.

| Edição (ano-base) | Coluna | Soma das linhas | TOTAL impresso |
|---|---|---|---|
| 2008 (2007) | projetos concluídos | 382 | 158 |
| 2009 (2008) | projetos em execução; concluídos | 600; 480 | 513; 211 |
| 2015 (2014) | pesquisadores; projetos em execução | 538; 793 | 533; 783 |
| 2017 (2016) | pesquisadores | 411 | 441 |

Outros avisos:

- edição 2025 (ano-base 2024), Tab. 7.1: a linha do CIDDIC tem 7 números para 8 colunas; marcada como `incompleta` e excluída;
- edição 2016 (ano-base 2015), Tab. 8.3: as colunas do CLE e do NEPA são idênticas no PDF; mantidas como impressas.

#### Quebras de série

- **Início em 2015.** A Tab. 8.3 com todos os centros em colunas comparáveis começa na edição 2016 (ano-base 2015). Antes disso a comparação não é feita.
- **Mudanças de nome.** CCS passa a CCS Nano e CLEHC a CLE; as siglas foram harmonizadas (`CCS Nano` → `CCS`, `CLEHC` → `CLE`) para formar séries contínuas. CDMC e NIDIC antecedem o CIDDIC, que aparece a partir de 2010.
- **Entradas e saídas.** O NEE deixa a tabela em 2010; o NEAB entra em 2024; o CEIBC em 2025. Em 2026 a criação do CPqS extinguiu CEPAGRI, NEPA e NEPAM (efeito nas próximas edições).
- **Critério FAPESP.** Até o ano-base 2015 a AEPLAN publica recursos concedidos; a partir de 2016, contratados. Em 2017, cancelamentos deixaram o valor contratado negativo na fonte.
- **Dados declarados.** Os números da AEPLAN são declarados pelos próprios centros. Em 2015 o NIPE declarou zero artigo; os saltos entre anos podem refletir mudança de critério de declaração, não só de atividade.

## Limitações

- A comparação usa contagens declaradas; não pondera qualidade, área ou porte dos projetos.
- Não há dados bibliométricos externos. A conferência dos artigos por OpenAlex foi considerada e não foi feita nesta versão; a coluna `artigos_openalex_estimativa` de `NIPE_series_anuais` é uma estimativa do registro, não usada nas figuras.
- Os registros de projeto do arquivo [3] cobrem o que foi localizado até 12/11/2026 e não equivalem à contagem da AEPLAN.

## Privacidade

O repositório é público. `scripts/verificar_dados.py` falha se encontrar, em qualquer arquivo publicado:

- endereço de e-mail, número de CPF ou de telefone;
- CSV de pessoas nominais (`*_pessoas*`) ou de gênero;
- coluna `genero`, `gênero` ou `sexo`;
- coluna `nome` fora de `NIPE_coordenadores_v2026-11-16.csv` e `fig02_coordenadores.csv` (cargos públicos) e de `COCEN_AEPLAN_tab7_1_2004-2025.csv` (onde `nome` é o nome do centro ou núcleo).

## Arquivos derivados

- `data/nipe_dados.zip`: `nipe.json`, `paleta.json`, os CSVs de `data/figuras/` e de `data/fontes/` e este LEIAME num arquivo só.
- `figuras_svg/*.svg`: as figuras em vetor (texto editável, fonte sans-serif única, 175 mm ou 85 mm de largura), geradas por `scripts/exportar_svg.py` a partir dos mesmos CSVs.
