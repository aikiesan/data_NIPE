# Varredura NIPE e CP2B — 2026-10-25 02:06 (domingo) · Fase 1
> Execução nº 30 · 1ª de domingo = **consolidação** · Ênfase: duplicatas, conflitos, linha do tempo, indicadores, catálogos CSV, narrativa · Expansão histórica: R3 e R4 leves · Consultas usadas: ~29 (NIPE 20, CP2B 9)
> Fatos novos: NIPE +2 ([V] 2 / [S] 0; de 2015–hoje: 2) · CP2B +1 (+ F0281 regravado) · Pistas novas: 4 (P713–P716) + 4 reconstituídas (P709–P712) · Conflitos novos: 0 (K52 parcialmente resolvido)
> Saturação: NIPE 1/12 (8%) · CP2B 1/12 (8%) · Arquivos gravados: ver "Arquivos desta execução" no fim

## Resumo executivo
- **Falhas silenciosas de upload na execução 29 (sábado 22h):** 5 arquivos citados como gravados NÃO existem no Drive — NIPE_C04a_v2026-10-24_d, NIPE_C09_v2026-10-24_d, NIPE_HISTORICO_v2026-10-24_f, CP2B_C10_C12_v2026-10-24_d e 00_FILA_DE_PISTAS_CP2B_v2026-10-24_d. Nenhum fato do NIPE se perdeu (F0001–F0588 conferidos um a um nas partes existentes); CP2B-F0281 foi reaberto e regravado; complementos do Adendo E em C09 e pistas CP2B P709–P712 foram reconstituídos; 4 complementos da frente R2 em C04a perderam-se sem texto.
- **Grande número revisto:** o projeto Campus Sustentável (CPFL, P&D + PEE ANEEL, 36 meses) tem investimento total de **R$ 9,5 mi [V]** pelo site oficial (F0590). O R$ 1,46 mi do relatório CPFL seria a parcela P&D executada pela Unicamp; o conflito K52 fica aberto só para o R$ 8,1 mi de 2018 e a data de início.
- **Série anual 1984–2026 consolidada:** a tabela "C12 por ano" passou de 68 para 48 linhas (uma por ano + 5 intervalos); novo CSV com 43 anos, coordenação por ano, FAPESP sediado/participação, outras fontes pontuais, produção dos Anuários e estimativa OpenAlex 2022–2025; erro corrigido em 2019 (23 projetos, não 1).
- **1ª versão da NIPE_HISTORIA_NARRATIVA**: 6 períodos (1984–2026), quadro-síntese e tabelas por ano geradas do CSV.
- **CP2b:** o conjunto de dados f36wp9 ("Banco de dados PILAR-2b") passou a declarar os awards FAPESP 2024/01112-1 e 2025/08745-2 — 1º dado com DOI que cita o auxílio do CP2b (CP2B-F0282). Recontagem BV sem mudança (5 PIs/53 associados/15 bolsas/1 publicação).

## Grandes números e séries que mudaram (antes → depois)
| Indicador | Antes | Depois | IDs |
|---|---|---|---|
| Total de fatos NIPE | 588 | 590 ([V] 586 · [S] 4) | F0589, F0590 |
| Total de fatos CP2B | 281 (1 perdido no Drive) | 282 ([V] 282) | CP2B-F0281, F0282 |
| Campus Sustentável — valor | R$ 1,46 mi [V] × R$ 9,5 mi [S] × R$ 8,1 mi [S] | R$ 9,5 mi [V] (projeto inteiro) + R$ 1,46 mi [V] (P&D Unicamp); R$ 8,1 mi [S] | F0577, F0590, K52 |
| Série anual (CSV) | 28 linhas, 2019 com 1 projeto | 43 linhas (1984–2026), 2019 = 23 projetos, coordenador por ano | dados/NIPE_series_anuais_v2026-10-25.csv |
| Catálogo de projetos NIPE | 62 linhas (2026-10-18) | 154 linhas (todas as linhas de C04/C05 com processo, financiador ou valor) | dados/NIPE_projetos_v2026-10-25.csv |
| Coordenadores | sem catálogo | 14 linhas com ato/fonte | dados/NIPE_coordenadores_v2026-10-25.csv |

## Expansão histórica (consolidação; R3/R4 leves)
- Série 1984–2026 completa no CSV; lacunas mantidas vazias: valores 1984–2000 e 2022–2026, pessoas 1993–1999 e 2022–2024, produção oficial 2022–2024.
- R3: Campus Sustentável (F0590). BioLoop (P702) sem confirmação independente (strings não indexadas).
- R4: ato de 2025 (Cunha) — o doflash do DOE-SP não abre 2025 (client_error até na pg_0001); vai para resgate manual.
- Ponto de parada: R3 a fundo na próxima execução (valores dos CCD e do [CEP]; Finep; CNPq; ANEEL).

## Verificação
NIPE: 3 confirmados (F0380 — programa do debate de 2014-05-28, com complemento; F0390 — CPFL Rio Uruguai R$ 644.076,40; F0400 — Crossref 9 DOIs). CP2B: F0150 confirmado em parte (DataCite mudou: fundingReferences preenchido → F0282). 0 promovidos a [V] por snippet (o R$ 9,5 mi virou fato [V] novo); 0 links corrigidos; conflito trabalhado: NIPE-K52 (parcialmente resolvido).

## NIPE — novidades
| ID | Cat. | Data | Fato | Fonte | Selo |
|---|---|---|---|---|---|
| NIPE-F0589 | C10 | 2026-10-23 | Artigo de opinião de M. D. Berni no site do NIPE: “A ONU e a Governança Multilateral da Geopolítica Energética” | https://www.nipe.unicamp.br/2026/10/23/a-onu-e-a-governanca-multilateral-da-geopolitica-energetica/ | [V] |
| NIPE-F0590 | C05 | 2017/2018 | Campus Sustentável: R$ 9,5 mi, 36 meses desde 01/2018 (outra página: 08/2017), P&D + PEE ANEEL | https://campus-sustentavel.unicamp.br/?p=1009 | [V] |
Complementos: F0577 (valor total), F0380 (verificação), F0251 e F0082 (Adendo E reaplicado). Pistas novas: P713 (R$ 8,1 mi/início do Campus Sustentável), P714 (artigos de opinião do site). Pistas trabalhadas: P699, P701, P702 (status na fila).
Consolidação: checagem de duplicatas por (data, URL) achou 14 grupos — todos projetos distintos da mesma página de Anuário ou o par intencional F0115/F0578 (K51); nenhuma fusão necessária. Linha do tempo reordenada cronologicamente (315 linhas + 2).

## CP2B — novidades
| ID | Cat. | Fato | Fonte | Selo |
|---|---|---|---|---|
| CP2B-F0281 | C10 | (regravado) Site com 20 páginas ativas; Microscópio de Ideias na 2ª edição (2026-09-09) | https://cp2b.unicamp.br/api/page-settings | [V] |
| CP2B-F0282 | C08 | DataCite f36wp9 declara FAPESP 2024/01112-1 e 2025/08745-2 | https://api.datacite.org/dois?query=%22Centro%20Paulista%20de%20Estudos%20em%20Biog%C3%A1s%22&page[size]=50 | [V] |
Sem notícias, oportunidades ou eventos novos no site desde 2026-10-20. Pistas novas: P715 (páginas metaninho/capacitacao alteradas), P716 (data da atualização do DataCite). P624: o defeso eleitoral do site acaba em 2026-10-26 00h — reabrir parceiros na próxima execução.

## Conflitos e dúvidas
- NIPE-K52: parcialmente resolvido (ver acima). Abertos sem mudança: K51 (AEPLAN 2025), K27, K53, K54, K55; CP2B-K51.

## ⚠️ Limitações e fontes para resgate manual
- 5 arquivos da execução 29 não chegaram ao Drive (ver resumo). A partir de agora a rotina confere com search_files, ao fim, se todos os arquivos existem.
- Notícia Unicamp 2018-01-31 (Campus Sustentável): SERVER_ERROR pela 4ª vez — valor R$ 8,1 mi.
- DOE-SP 2025 (portaria de Marcelo P. da Cunha): doflash não cobre; buscar em doe.sp.gov.br, termo “Planejamento Energético”, jul–set/2025.
- BioLoop (01-P-11277/2026, R$ 14.999.945,97): link downloads.sg expirado; pauta CONSU/CONEX 2026.
- AEPLAN Tab. 8.3 (2025): conferência visual da coluna do NIPE (K51).

## Painel de saturação (resumo)
NIPE 1/12 saturadas (C01). CP2B 1/12 (C03). Fase 1 mantida (período padrão até 2026-11-08).

## Plano para a próxima execução
Domingo ~06h: execução normal. NIPE: R3 a fundo (valores dos CCD/[CEP], Finep, CNPq, ANEEL), P705, P713. CP2B: pós-defeso (P624) a partir de 2026-10-26. Recontagem mensal e "NIPE in big numbers" em 2026-11-01.

## Fontes consultadas
1. https://www.nipe.unicamp.br/wp-json/wp/v2/posts?per_page=10&_fields=id,date,link,title
2. WebSearch "NIPE Unicamp outubro 2026"
3. https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=6759&_fields=id,date,link,title,content
4. WebSearch "BioLoop Unicamp Finep CEPETRO NIPE"
5. WebSearch "\"Núcleo Interdisciplinar de Planejamento Energético\" 2026"
6. WebSearch Jornal da Unicamp CPPLEI/CePIL/CEP 2026
7. https://www.nipe.unicamp.br/docs/eventos/programa-28maio.pdf
8. https://www2.unicamp.br/anuario/2019/centronucleo/NIPE-projetosQueParticipa.html
9. https://api.crossref.org/works?filter=award.number:2016/16438-3&rows=50&select=DOI,title,issued,container-title,author
10. https://www2.unicamp.br/unicamp/noticias/2018/01/31/unicamp-e-cpfl-celebram-parceria-em-eficiencia-energetica-e-reducao-de-consumo (SERVER_ERROR)
11. WebSearch "\"Campus Sustentável\" Unicamp CPFL \"9,5 milhões\""
12. https://campus-sustentavel.unicamp.br/en/home-2/
13. https://www.unicamp.br/unicamp/noticias/2018/01/31/unicamp-e-cpfl-celebram-parceria-em-eficiencia-energetica-e-reducao-de-consumo (SERVER_ERROR)
14. WebSearch Campus Sustentável milhões P&D 2018
15. https://campus-sustentavel.unicamp.br/?p=1009
16. WebSearch "\"01-P-11277/2026\" OR \"14.999.945,97\""
17. WebSearch Finep Unicamp Doubek BioLoop 15 milhões 2026
18. https://diariooficial.imprensaoficial.com.br/doflash/prototipo/2025/Julho/17/exec2/pdf/pg_0055.pdf (client_error)
19. WebSearch doe.sp.gov.br Unicamp NIPE designando 2025
20. https://diariooficial.imprensaoficial.com.br/doflash/prototipo/2025/Julho/18/exec2/pdf/pg_0001.pdf (client_error)
21. https://cp2b.unicamp.br/api/page-settings
22. https://cp2b.unicamp.br/api/content/microscopio
23. https://cp2b.unicamp.br/api/news
24. https://cp2b.unicamp.br/api/opportunities
25. https://cp2b.unicamp.br/api/events
26. WebSearch "CP2B Unicamp biogás outubro 2026"
27. https://bv.fapesp.br/en/auxilios/116427/sao-paulo-center-for-biogas-and-bioproducts-studies
28. https://api.datacite.org/dois?query=%22Centro%20Paulista%20de%20Estudos%20em%20Biog%C3%A1s%22&page[size]=50

## Arquivos desta execução (pastas do Drive)
Raiz: 00_PLANO_E_SATURACAO_v2026-10-25, 00_FILA_DE_PISTAS_NIPE_v2026-10-25, 00_FILA_DE_PISTAS_CP2B_v2026-10-25 · NIPE/: NIPE_REGISTRO_MESTRE, NIPE_LINHA_DO_TEMPO, NIPE_C05, NIPE_C09, NIPE_C10, NIPE_CONFLITOS, NIPE_HISTORICO, NIPE_HISTORIA_NARRATIVA (todos _v2026-10-25) · CP2B/: CP2B_REGISTRO_MESTRE, CP2B_C07_C08, CP2B_C10_C12 (_v2026-10-25) · dados/: NIPE_series_anuais, NIPE_projetos, NIPE_publicacoes, NIPE_parceiros, NIPE_coordenadores, CP2B_projetos, CP2B_publicacoes (_v2026-10-25.csv) · relatorios_diarios/: este arquivo.
