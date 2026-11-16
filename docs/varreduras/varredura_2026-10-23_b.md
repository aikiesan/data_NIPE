# Varredura NIPE e CP2B — 2026-10-23 (sexta-feira, 2ª execução do dia, ~19h BRT) · Fase 1
> Execução nº 25 · Ênfase do dia: C10 Imprensa + C09 Eventos (sexta), mais C08 (NIPE) e C11/C01/C03 (CP2B), as categorias de menor cobertura · Consultas usadas: ~91 web (NIPE 54, CP2B 37) + ~45 leituras por curl em raw.githubusercontent.com (só leitura)
> Fatos novos: NIPE +29 ([V] 29/[S] 0) · CP2B +10 ([V] 10/[S] 0) · Pistas novas: 19 (P598–P607, P620–P628) · Conflitos novos: 2 (NIPE-K47, CP2B-K47)
> Links do Drive: ver a seção "Arquivos salvos" no fim deste relatório. Esta é a versão _b do dia (a execução das ~02h já gravou varredura_2026-10-23.md).

## Resumo executivo
- **Convênios do NIPE com empresas, por um caminho novo:** as pautas da CONEX/PROEC de 2013 listam contratos do NIPE com nº de processo, parceiro, objeto, valor e responsável. Saíram 4 fatos: CPFL Paulista PD 138-07, de R$ 155.010,00 (resp. Arnaldo Walter); aditivo da CHESF; contrato com a Eletropaulo; e a "AES" de 2010, agora identificada como **AES Tietê**. CHESF e Eletropaulo são parceiras novas no registro.
- **PI do NIPE:** +1 patente concedida de pesquisador do NIPE (BR102013011126-0, secagem por bomba de calor, Vivaldo Silveira Jr., B1 em 2020-09-29) e +1 software depositado (Calculadora Biomassa2Biogas, Inova PC329).
- **[CePIL]:** a fila de posts de 2026 foi fechada (P577 e P340): 6 reuniões mensais, os **4 eixos do CePIL**, a troca de "Living Lab" por "Laboratório Vivo" e a entrada de Jannuzzi no SPGET (painel científico global de transição energética, sede na USP).
- **CP2B:** os assets públicos do site trouxeram 8 dos 10 fatos: o Manual de Identidade Visual (jul/2025, feito pela GHM Solutions), os patrocinadores do I Fórum Paulista (Ouro Equinor, Prata Clean Environment Brasil, Bronze Analítica e CSUS), a faixa de 21 parceiros e apoiadores, o defeso eleitoral que ocultou os parceiros públicos até 25/10 e o **Arqueia**, sistema de gestão de equipamentos do CP2b.
- **Programa CCD:** a FAPESP fala em 83 CCDs em 4 editais e põe 20 centros no 3º edital, o do CP2B; a Agência FAPESP de 2024 dava 21 (novo CP2B-K47).
- **Saturação:** NIPE C01 e CP2B C07 entram em saturação (3 execuções sem fato novo [V]); seguem com checagem semanal.

## Grandes números que mudaram hoje (antes → depois)
- NIPE, fatos registrados: 492 → **521** (29 [V]). CP2B: 252 → **262**.
- NIPE, convênios com empresas com valor: + CPFL PD 138-07, **R$ 155.010,00** (contrato de 2009, relatório final em 2013).
- NIPE, PI: patentes de pesquisadores do NIPE +1 (BR102013011126-0); software +1 (PC329_BIOGAS, depositado).
- NIPE, parceiros: + CHESF, Eletropaulo, AES Tietê (antes só "AES"), Shandong Academy of Sciences (visita de 2026-05-29), SPGET.
- CP2B, parceiros e apoiadores: faixa da home com **21 logos** contra **15** na /api/partners. Novos no registro: Mulheres do Biogás e MCPAR Engenharia.
- CP2B, I Fórum Paulista: **4 patrocinadores** (valores não divulgados).
- Programa CCD: **83 CCDs em 4 editais** (10 + 19 + 20 + 34).
- Sem mudança: OpenAlex 6 / Crossref 5 artigos com o award 24/01112-1; valor do auxílio 24/01112-1 segue sem fonte.

## Verificação do dia
- Confirmados: NIPE-F0230, F0240, F0250; CP2B-F0070, F0100, F0140. Os 6 conferem com a fonte.
- Promovidos a [V]: 0. Os 3 fatos [S] do NIPE ficaram sem fonte primária nova; o CP2B não tem fatos [S].
- Links corrigidos: 0.
- Conflitos resolvidos: 0. Conflitos que avançaram: CP2B-K35 (parceiros; fica aberto só para UCA e LNEG), CP2B-K46/NIPE-K47 (InterCocen realizada em 19–20/09 em outro local; a nota de adiamento não foi achada), NIPE-K27 (Telma ainda coordenadora em 2016-10-20). NIPE-K46: a via das tabelas FAPESP 2023 está esgotada.
- Recontagem rápida: OpenAlex 6; Crossref 5; /api/partners 15 ativos; /api/news 6; /api/boletins 1; podcast 1 episódio.

## Frente de expansão do dia
- **NIPE E7 (atos oficiais):** normas da PG 2851 (CONSU-A-008/2007) e 3361 (CONSU-A-008/2013) lidas, sem o NIPE. Ponto de parada: faltam os ids 2695 e 2329 (P493); portarias de coordenadores (P460) sem avanço.
- **NIPE E5 [CePIL]:** P577 e P340 concluídas. Ponto de parada: posts de 2025–2026 ainda não lidos, listados na P604.
- **CP2B E3/E8:** OpenAlex 6, Crossref 5; /api/team 105–106 com erro (≥99 membros). Ponto de parada: sondar ids 107–115.

## NIPE — novidades de hoje
### Frentes exploradas
| Categoria | Fonte/estratégia | Consultas | Resultado |
|---|---|---|---|
| C09/C10/C11 [CePIL] | WP REST: search=CePIL (índice de 100 posts) + 8 × include= de 3 ids; 3 listagens por data (truncadas) | 12 | 20 (F0493–F0512) + 4 compl. — P577 e P340 concluídas; posts?after/before e _fields=title.rendered vêm truncados ou ignorados — usar search + include |
| C10 | Agência FAPESP (InterCocen) | 2 | 0 (compl. F0334; K47) — — |
| C10 | JU 2007–2019 via WebSearch unicamp.br + fetch www2 | 10 | 3 (F0513–F0515) — www2: 5 SERVER_ERROR (estatico-2023, JU 2019, notícias 2017 e 2018) e 4 acessos ok |
| C08 | Inova ?s=biogás, ?s=Jannuzzi; PC329; Anuário FEA/DETA-0034 2020; Google Patents direto | 6 | 2 (F0516, F0517) — Caminho novo: o 0034 dos Anuários das unidades dá patentes de pesquisadores do NIPE |
| C01/C03 | JU_0001; WebSearch "Núcleo de Energia"; sede (JU 339, 376, COPEI 144) | 6 | 0 (+F0514 lateral) — P204 e P536 sem avanço |
| C12 | COCEN /cai-consu/relatorio-de-atividades; FAPESP tabelas 2023 (com e sem offset) | 3 | 0 — Só formulários nos outros triênios; tabelas FAPESP extraíveis só até a Tab. 21 |
| C05 | CAMINHO NOVO: pautas da CONEX/PROEC (busca Funcamp/transparência + 4 pautas) | 6 | 4 (F0518–F0521) + compl. F0205 — 2 de 4 pautas com processos "(NIPE)"; a Funcamp não rendeu nada direto |
| C02 E7 | Base PG: normas 2851 e 3361 | 2 | 0 — Contexto do modelo de regimento, sem NIPE |
| C04 | WebSearch CPPLEI 2026/05010-4 | 1 | 0 — Ainda não indexado |
| Verificação | Anuário 2013 participa (F0230), Crossref (F0240), COCEN relatório de gestão (F0250) | 3 | 0 — Os 3 conferem |

### Fatos novos
| ID | Categoria | Fato resumido | Fonte | Selo |
|---|---|---|---|---|
| NIPE-F0493 | C09 | [CePIL] Reunião mensal de planejamento científico e estratégico do CePIL no NIPE, na sexta (27/03). Houve apresentações do Senai e da FACAMP (Faculdades de Campinas). Pauta: Laboratório Vivo, próximos projetos-piloto,… | https://www.nipe.unicamp.br/2026/03/27/cepil-realiza-reuniao-mensal-de-planejamento-com-presenca-do-senai/ | [V] |
| NIPE-F0494 | C09 | [CePIL] Reunião mensal do CePIL no NIPE (26/06). Pauta: relatório científico da FAPESP, parcerias com o Senai e projeto do Laboratório Vivo (no jardim do NIPE). Participaram Luís Henrique Mendes de Oliveira (Coordenador de… | https://www.nipe.unicamp.br/2026/06/26/cepil-realiza-reuniao-mensal-no-nipe-com-participacao-do-senai-e-pesquisador-internacional/ | [V] |
| NIPE-F0495 | C09 | [CePIL][CEP] O post do NIPE de 2026-04-01 anuncia a 2ª edição do InterCocen "nos dias 23 e 24 de maio no Espaço Cis Guanabara", das 9h às 16h, com entrada gratuita. No sábado (23/05), CePIL e Senai fariam a dinâmica "A Ciência da… | https://www.nipe.unicamp.br/2026/04/01/parceria-entre-cepil-e-senai-destaca-o-papel-da-iluminacao-publica-no-intercocen-2026/ | [V] |
| NIPE-F0496 | C11 | [CePIL] Reunião mensal do CePIL no NIPE (29/05) com pesquisadores da Shandong Academy of Sciences ("Energy Institute/Qilu University of Technology/Shandong Academy of Sciences"). A parceria é anterior: vem "desde 2025", pelo… | https://www.nipe.unicamp.br/2026/05/29/cepil-realiza-reuniao-mensal-no-nipe-com-participacao-de-pesquisadores-internacionais-da-shandong-academy-of-sciences/ | [V] |
| NIPE-F0497 | C11 | [CePIL] Gilberto De Martino Jannuzzi integra o Painel Científico para a Transição Energética Global (SPGET). O painel foi anunciado em 25/04/2026 em Santa Marta (Colômbia) pela ministra Irene Vélez Torres, na 1ª Conferência sobre… | https://www.nipe.unicamp.br/2026/05/06/diretor-do-cepil-integra-painel-cientifico-para-a-transicao-energetica-global/ | [V] |
| NIPE-F0498 | C09 | [CePIL] Apresentação do Projeto de Iluminação Pública Inteligente da Unicamp (Campus Sustentável), na noite de 08/06. Organização: Juliana Ulian (GHM Solutions/CPIIC). Graziella Demantova ("Coordenadora de Inovação e Projetos… | https://www.nipe.unicamp.br/2026/06/09/cepil-participa-de-apresentacao-do-projeto-de-iluminacao-publica-inteligente-da-unicamp/ | [V] |
| NIPE-F0499 | C09 | [CePIL] 2º Congresso Internacional e Multidisciplinar sobre o Urbano (Laboratório Social Urbano/UnB, Brasília, 9–11/06/2026). No GT 27, Sessão 01 (09/06, 08h30–10h30), foi apresentado o trabalho "Iluminação Pública e Impactos… | https://www.nipe.unicamp.br/2026/06/09/integrantes-do-cepil-participam-do-2o-congresso-internacional-e-multidisciplinar-sobre-o-urbano/ | [V] |
| NIPE-F0500 | C10 | [CePIL] Canal Solar (jornalista Caique Amorim), matéria "A geopolítica da energia em um mundo fragmentado", com entrevista de Jannuzzi ("Diretor do Centro Paulista de Inovação em Iluminação Pública"). Citação: "O Brasil precisa… | https://www.nipe.unicamp.br/2026/04/13/coordenador-do-cepil-participa-de-entrevista-para-o-canal-solar/ | [V] |
| NIPE-F0501 | C10 | [CePIL] Portal Envolverde, reportagem de Amélia Gonzales "A ética e a filosofia podem ajudar a pensar sobre o uso eficiente da energia, diz Gilberto Jannuzzi" (entrevista do diretor do CePIL). A data exata da matéria não é dada | https://www.nipe.unicamp.br/2026/06/10/diretor-do-cepil-participa-de-entrevista-para-o-portal-envolverde/ | [V] |
| NIPE-F0502 | C11 | [CePIL] Visita da Semil ao CePIL no NIPE (terça, 31/03): Marisa de Barros, subsecretária de Energia e Mineração, com assessoras. Foram apresentados o Laboratório Vivo e "novos projetos pilotos". Marcelo Pereira da Cunha… | https://www.nipe.unicamp.br/2026/03/31/cepil-recebe-semil-para-apresentacao-de-novos-projetos-e-do-laboratorio-vivo/ | [V] |
| NIPE-F0503 | C10 | [CePIL] Entrevista de Jannuzzi (diretor do CePIL) ao CPTEn/Unicamp, conduzida pela pesquisadora Lira Luz Benites Lazaro, publicada na página "fala-pesquisador-transicao-energetica-como-processo-historico" do site do CPTEn.… | https://www.nipe.unicamp.br/2026/03/30/coordenador-do-cepil-concede-entrevista-ao-cpten/ | [V] |
| NIPE-F0504 | C03 | [CePIL] O CePIL "passa a utilizar a expressão Laboratório Vivo em substituição ao termo em inglês Living Lab". Explica a mudança de nome entre os posts de 2025 ("Living Lab") e os de 2026 | https://www.nipe.unicamp.br/2026/03/24/cepil-adota-o-termo-laboratorio-vivo-e-reforca-compromisso-com-a-ciencia-acessivel/ | [V] |
| NIPE-F0505 | C09 | [CePIL] Visita técnica do PROCEL ao projeto de iluminação pública da Unicamp (quinta, 05/02, 9h–12h), com CePIL, FEEC, Campus Sustentável e CPTEn. Até então havia "17 luminárias" instaladas, em troca de vapor de sódio 250 W por… | https://www.nipe.unicamp.br/2026/02/09/projeto-de-iluminacao-publica-da-unicamp-conta-com-participacao-do-cepil-em-visita-do-procel/ | [V] |
| NIPE-F0506 | C02 | [CePIL] 1ª reunião anual de 2026 do CePIL, no NIPE (sexta, 23/01), com pesquisadores, colaboradores e novos bolsistas. Prioridades definidas: projetos com parceiros (incl. Inovação e Novos Negócios), eventos técnico-científicos,… | https://www.nipe.unicamp.br/2026/01/23/cepil-realiza-primeira-reuniao-anual-e-define-prioridades-estrategicas-para-2026/ | [V] |
| NIPE-F0507 | C02 | [CePIL] Reunião mensal (24/07) com Jannuzzi ("Diretor do CePIL"). A integração de bolsistas e pesquisadores foi organizada pelos 4 eixos do centro: "Governança e ecossistema", "Pesquisa socioambiental jurídica e normativa",… | https://www.nipe.unicamp.br/2026/07/27/cepil-realiza-reuniao-mensal-no-nipe-e-discute-integracao-entre-pesquisadores/ | [V] |
| NIPE-F0508 | C09 | [CePIL] Reunião mensal no NIPE (sexta, 28/08). Pauta: produções científicas e "modalidades de registro intelectual", reuniões com fabricantes sobre o Laboratório Vivo, demandas da Inteligência de Dados e eixos de pesquisa. Houve… | https://www.nipe.unicamp.br/2026/08/28/cepil-realiza-reuniao-mensal-no-nipe-e-discute-producoes-cientificas-internas/ | [V] |
| NIPE-F0509 | C09 | [CePIL] Reunião mensal no NIPE (sexta, 25/09). Pauta: avanço da plataforma DataLuz, resultados do UPA e do InterCocen, trabalho com consórcios, selo InovaLuz e atividades dos bolsistas. Não há nomes nem números | https://www.nipe.unicamp.br/2026/09/25/cepil-realiza-reuniao-mensal-no-nipe-e-discute-avancos-em-projetos/ | [V] |
| NIPE-F0510 | C11 | [CePIL] Jannuzzi ("Coordenador do CePIL") participou do Fórum Internacional de Energias Renováveis China (Shandong)-Brasil, em Jinan, em 11/09/2025. Eram "mais de 50 especialistas e acadêmicos", e a organização foi do Instituto… | https://www.nipe.unicamp.br/2025/09/16/coordenador-do-cepil-participa-do-forum-internacional-china-shandong-brasil-sobre-energias-renovaveis-em-jinan/ | [V] |
| NIPE-F0511 | C09 | [CePIL] Jannuzzi foi escalado para o painel "Descarbonização até 2050: Desafios e Oportunidades para a Cooperação Sul-Sul", proposto pela FAPESP e aprovado pelo MMA, na Zona Azul do Pavilhão Brasil da COP30, em 15/11/2025.… | https://www.nipe.unicamp.br/2025/09/29/coordenador-do-cepil-professor-gilberto-jannuzzi-participa-de-mesa-proposta-pela-fapesp-na-cop-30/ | [V] |
| NIPE-F0512 | C11 | [CePIL] Inauguração do Centro de Pesquisas Interdisciplinar de Estudos Brasil-China (CIEBC), no Instituto de Economia (quarta, 26/11), marcando a "transição do CIEBC de grupo de pesquisa para centro de pesquisa". O CePIL foi… | https://www.nipe.unicamp.br/2025/11/27/integrantes-do-cepil-comparecem-a-inauguracao-do-centro-interdisciplinar-de-estudos-brasil-china/ | [V] |
| NIPE-F0513 | C10 | Jornal da Unicamp nº 360, "Integração energética ganha força no setor sucroalcooleiro" (Manuel Alves Filho). Pontos: Silvia Nebra "da Faculdade de Engenharia Mecânica (FEM) e do Núcleo Interdisciplinar de Planejamento Energético… | https://www2.unicamp.br/unicamp/unicamp_hoje/ju/maio2007/ju360pag04.html | [V] |
| NIPE-F0514 | C10 | Jornal da Unicamp, seção Fapesp: "A análise foi feita pelo pesquisador do Núcleo Interdisciplinar de Planejamento Energético (Nipe) da Unicamp Isaias Macedo". A análise foi apresentada em 2007-10-02 no workshop "Tecnologia e… | https://www2.unicamp.br/unicamp/unicamp_hoje/jornalPDF/ju376pag10.pdf | [V] |
| NIPE-F0515 | C10 | Portal Unicamp (Patrícia Lauretti), "Biocombustíveis avançados são alternativa para aviação sustentável". Telma Teixeira Franco aparece como "coordenadora do Núcleo Interdisciplinar de Planejamento Estratégico (Nipe) da Unicamp"… | https://www2.unicamp.br/unicamp/noticias/2016/10/20/biocombustiveis-avancados-sao-alternativa-para-aviacao-sustentavel | [V] |
| NIPE-F0516 | C08 | Patente BR102013011126-0, "Dispositivo de secagem por bomba de calor". Inventores: Vivaldo Silveira Junior e Paula Lyra Falquetto; titular Unicamp. Publicação A2 em 2014-12-23; intenção de conceder (B09A) em 2020-08-04; B1 em… | https://patents.google.com/patent/BR102013011126B1/pt | [V] |
| NIPE-F0517 | C08 | Software no portfólio da Inova Unicamp: "Calculadora Biomassa2Biogas", código PC329_BIOGAS, status "DEPOSITADA". Autores: Tânia Forster Carneiro, Hudson Giovani Zanin (FEEC), Manoel Victor Frutuoso Barrionuevo, Larissa Castro… | https://tecnologias.inova.unicamp.br/tecnologia/pc329_biogas/ | [V] |
| NIPE-F0518 | C05 | CONEX/PROEC, 322ª Sessão Ordinária (2013-10-31). Processo 01-P-5018-09 (NIPE): contrato UNICAMP/FUNCAMP/CPFL/FUPAI/Andalusia – Assessoria em Gestão Empresarial Ltda. para P&D à CPFL Paulista, projeto "PD 138-07 – Potencial de… | https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pauta31outubro.pdf | [V] |
| NIPE-F0519 | C05 | CONEX 322ª: processo 01-P-17296-08 (NIPE), 2º termo aditivo ao contrato UNICAMP/FUNCAMP/CHESF, projeto "Desenvolvimento de sistema de aproveitamento de fontes de calor para uso em aquecimento de fluídos". O aditivo prorroga a… | https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pauta31outubro.pdf | [V] |
| NIPE-F0520 | C05 | CONEX/PROEC, 323ª Sessão Ordinária (2013-11-21): relatório final do processo 01-P-10416-09, contrato de prestação de serviços UNICAMP/FUNCAMP/Eletropaulo Metropolitana Eletricidade de São Paulo S.A. Objeto: sistema que aproveita… | https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pautaconex21nov.pdf | [V] |
| NIPE-F0521 | C05 | Súmula da 321ª reunião da CONEX (19/09/2013), transcrita na pauta da 322ª: relatórios finais aprovados dos processos 01-P-14415-06 (NIPE) e 01-P-3779-08 (NIPE). A súmula não traz parceiro, objeto nem valor (P599) | https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pauta31outubro.pdf | [V] |

### Fatos atualizados (complementos)
| ID | Acréscimo |
|---|---|
| NIPE-F0187 | Post do NIPE de 2026-04-23 sobre a mesma reunião NCEPU (manhã de 23/04). Pelo CePIL foram Maria Eduarda Brollo (aspectos legais) e Mario Ramos (gestor de projetos). Marcelo Pereira da Cunha estava… |
| NIPE-F0479 | A entrevista à CGTN América tem post próprio de 2026-06-12. O vídeo no YouTube se chama "China and Brazil team up for clean energy solutions". Jannuzzi diz "desde o ano passado nós expandimos nossa… |
| NIPE-F0057 | Cerimônia de entrega dos dispositivos de telegestão (TIM) em 2026-01-27, no auditório da Congregação da FEEC: "mais de 2.600 pontos de iluminação" e "redução de até 70%". O financiamento vem de… |
| NIPE-F0205 | A "AES" do projeto 01-P-05514-10 é a AES Tietê. Objeto: tempo de recorrência e restrição de vazão máxima, com avaliação de danos de inundação a jusante das usinas e ganhos energéticos. Responsável:… |
| NIPE-F0334 | A Agência FAPESP (2026-09-14) dá a 2ª Feira InterCocen-Unicamp no "sábado (19) e domingo (20/09)", 9h–16h, no Centro de Eventos da Secretaria Municipal de Educação de Campinas (R. Antônio Nunes dos… |
| NIPE-F0464 | O "Marcos Paulo" do LuxAmérica 2026 é Marcos Paulo Dias Leite Resende (programação do GT 27 do Congresso do Urbano/UnB, F0499). P535 resolvida quanto ao nome |
| NIPE-F0305 | O post do NIPE de 2025-09-16 (F0510) confirma a presença de Jannuzzi/CePIL no fórum de Jinan de 2025-09-11 |
| NIPE-F0476 / F0334 | Agora há 5 aparições conjuntas de CePIL+Senai em 2026: InterCocen anunciado (F0495), reuniões de 27/03 e 26/06 (F0493, F0494), UPA e InterCocen realizado |
| NIPE-K19 (variante) | Mais 2 ocorrências de "Núcleo Interdisciplinar de Planejamento Estratégico": JU nº 360 (2007, F0513) e Portal Unicamp 2016-10-20 (F0515) |

### Pistas novas na fila
- P598 (alta): CONEX/PROEC: outras pautas e súmulas (conex.proec.unicamp.br/assets/docs/conex/pautas/pautaconexDDmes.pdf) com processos "(NIPE)" — contratos, aditivos e relatórios finais com nº, parceiro, valor e…
- P599 (média): Processos 01-P-14415-06 e 01-P-3779-08 (NIPE): parceiro, objeto, valor (súmula CONEX 321ª)
- P600 (média): Contratos de Vivaldo Silveira Jr. com CHESF (01-P-17296-08) e Eletropaulo (01-P-10416-09): valor, código P&D ANEEL, ligação com as patentes (F0237, F0516)
- P601 (média): SPGET: composição, mandato, papel de Jannuzzi, sede na USP (5 anos)
- P602 (baixa): InterCocen 2026: nota de adiamento de maio para setembro (K47)
- P603 (média): Confirmar a realização do painel da COP30 (15/11/2025) pelos posts 4695 (2025-11-14) e 4741 (2025-12-02, "balanço da COP 30")
- P604 (média): Posts CePIL ainda não lidos (índice da WP search=CePIL, 100 itens). Ids de 2025: 4741, 4695, 4684, 4607, 4590, 4574, 4566, 4530, 4382, 4237, 4208, 4206, 4170, 4148, 4010, 4001, 3693 (IAAS China),…
- P605 (média): Projeto de Iluminação Pública Inteligente da Unicamp: valor do convênio ENBPar/PROCEL e data de entrega formal (jun/2026, CPIIC)
- P606 (baixa): Inova: "Otimização no tratamento de resíduos sólidos" (códigos 1542 e 542, reator em batelada; provável grupo Forster-Carneiro) e PC359/PC345 (CP2B Maps; PC345 já no CP2B). Conferir autores e status
- P607 (média): Anuários das unidades (padrão www2 …/anuario/AAAA/<UNIDADE>/<DEPTO>-0034.html; FEA/DETA, FEM, FEQ, FEAGRI) para patentes de pesquisadores do NIPE fora do Anuário NIPE (Vivaldo, Valença, Ennio,…
- P623 (média): CEPISIP no projetos-ccd2026.pdf, nome antigo do CePIL (ver NIPE-K05)

## CP2B — novidades de hoje
### Frentes exploradas
| Categoria | Fonte/estratégia | Consultas | Resultado |
|---|---|---|---|
| C01/C09/C11 | curl em raw.githubusercontent.com de public/assets (template .docx, manual .pdf, apoio-patrocinio.png, parceiros*.png), lidos com python3 -I,… | 0 web (~10 curl) | 5 (F0253–F0255, F0258, + parte de F0257) — Caminho novo e muito produtivo: os assets são legíveis inteiros, com metadados de autoria e data |
| C02/C09/C11 | curl: deploy.sh, docs/PUBLICACAO_VM.md, deployment/GO_LIVE_CHECKLIST.md, DEFESO_ELEITORAL_2026.md, src/utils/defeso.js, .htaccess, vercel.json, Home.jsx,… | 0 web (~25 curl) | 3 (F0256, F0257, F0260) — Os docs na raiz do repositório guardam decisões datadas. CronogramaEvento.jsx foi removido (404) |
| C03/C08 | WebFetch cp2b.unicamp.br/arqueia (+ agenda-publica, boas-praticas) e /abiove | 5 | 1 (F0259) — Agenda carregada por JS; /abiove dá client_error |
| C09/C10 | API do site: news, events, boletins, podcast, partners; Spotify; WebSearch "CP2b Talks" | 7 | 0 (complementos) — Nada novo em out/2026 |
| C09 (K46) | WP REST do NIPE (search CP2B, InterCocen, include=) + WebSearch ×2 + Agência FAPESP 59181 + Band + CEB | 8 | 0 (complemento F0157) — Realização confirmada (19–20/09, Centro de Eventos SME); sem fonte de adiamento |
| C01/C12 | CAMINHO NOVO: ccd.fapesp.br/sobre → projetos-ccd2026.pdf (+ 1 WebSearch sem resultado) | 3 | 1 (F0261) — 83 CCDs em 4 editais; K47 |
| C09/C06 | P552: daal.ufc.br (página de palestrante + home) + 2 WebSearch | 4 | 1 (F0262) — O WebSearch com "anaerobic digestion Latin America" achou o DAAL XV |
| pistas | P557: ADBA awards | 1 | 0 — Sem o CP2B |
| E3/E8 | OpenAlex award, Crossref award, OpenAlex fulltext "Biogas and Bioproducts", /api/team/105 e 106 | 5 | 0 — OpenAlex 6, Crossref 5, fulltext com 44 resultados sem relação, ids 105/106 com client_error |
| C11 | WebSearch UCA + Unicamp + CP2B | 1 | 0 — Sem resultado |
| verificação | fapesp.br/14897, Tribuna do Sertão, nipe.unicamp.br/oportunidades | 3 | 0 — F0070, F0100 e F0140 ok |

### Fatos novos
| ID | Categoria | Fato resumido | Fonte | Selo |
|---|---|---|---|---|
| CP2B-F0253 | C01 Identidade (identidade visual) | Manual de Identidade Visual do CP2B. São 34 páginas em 1920×1080 (InDesign 20.4, depois iLovePDF), com rodapé "JUL 2025". A última página diz "MATERIAL DESENVOLVIDO POR:" e traz o logo "ghm solutions — Assessoria de Marketing",… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/cp2b_web/public/assets/press-kit/manual-identidade-visual-cp2b.pdf | [V] |
| CP2B-F0254 | C09 Ensino/extensão | "TEMPLATE DE OFERECIMENTO DE CURSO – CP2b", lido inteiro. Metadados: criado em 2026-08-10T14:17Z, modificado em 2026-08-10T14:28Z, lastModifiedBy "Luciana C L Lenhari", 4 páginas, 620 palavras. São 13 seções: Identificação;… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/cp2b_web/public/assets/capacitacao/template-oferecimento-curso-cp2b.docx | [V] |
| CP2B-F0255 | C09 Eventos / C05 | Patrocinadores do I Fórum Paulista de Biogás e Bioprodutos. A imagem /assets/apoio-patrocinio.png aparece na página-memória do Fórum sob o rótulo "Patrocínio e apoio" (ForumPaulista.jsx). Cotas: "PATROCINADOR OURO" Equinor;… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/cp2b_web/public/assets/apoio-patrocinio.png | [V] |
| CP2B-F0256 | C09 Eventos | Mesa de abertura e Painel 2 previstos no cronograma do I Fórum Paulista. O dado vem do bloco original citado no "Registro de Conformidade com o Defeso Eleitoral 2026"; a página CronogramaEvento.jsx já foi removida. Mesa de… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/DEFESO_ELEITORAL_2026.md | [V] |
| CP2B-F0257 | C11 Colaborações / C10 | Defeso eleitoral 2026 no site do CP2B. Base citada: Lei 9.504/1997, art. 73, VI, "b", e Ofício Circular GR 01/2026. O site ocultou os parceiros públicos SAASP e SMVMADS/PMC (content.js com `public: []`). A imagem de parceiros… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/DEFESO_ELEITORAL_2026.md | [V] |
| CP2B-F0258 | C11 Colaborações | Faixa "Parceiros e Apoiadores" da home do site novo (Home.jsx, imagem /assets/parceiros.png; o original pré-defeso está em parceiros_original.png). São 21 logos: FAPESP; E-Renova (Unidade Embrapii FEQ-Unicamp); São Paulo Governo… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/cp2b_web/public/assets/parceiros_original.png | [V] |
| CP2B-F0259 | C03 Estrutura / C08 Software | Arqueia. Aplicação servida em cp2b.unicamp.br/arqueia. Título "Entrar · Arqueia"; descrição "Gestão, rastreabilidade e compartilhamento de infraestrutura laboratorial."; chamada "Compartilhar recursos. Ampliar descobertas." /… | https://cp2b.unicamp.br/arqueia | [V] |
| CP2B-F0260 | C10 Mídia (site) / C02 | Roteiro "Publicação na VM da Unicamp — segunda, 28/09/2026". Leva ao ar a versão com a página de Capacitação, "o logo do CP2b no centro dos eixos" e o "pacote de segurança e SEO preparado em 26/09". O site roda numa VM Debian da… | https://raw.githubusercontent.com/aikiesan/cp2bfun/main/cp2b_web/docs/PUBLICACAO_VM.md | [V] |
| CP2B-F0261 | C01 Identidade / C12 | PDF FAPESP "projetos-ccd2026.pdf" (Centros de Ciência para o Desenvolvimento), linkado em ccd.fapesp.br/sobre. Literal: "Já estão aprovados 83 CCDs selecionados em quatro editais". Pelo resumo, a contagem é 10 + 19 + 20 + 34. O… | https://fapesp.br/files/upload/16421/projetos-ccd2026.pdf | [V] |
| CP2B-F0262 | C09 Eventos / C06 | XV Workshop e Simpósio Latino-americano de Digestão Anaeróbia (DAAL XV), tema "Contributing to the energy transition and decarbonization", em Fortaleza-CE, no Hotel Oásis Atlântico Imperial. Presidência: A. B. dos Santos (UFC) e… | https://daal.ufc.br/?lang=en | [V] |

### Fatos atualizados (complementos)
| ID | Acréscimo |
|---|---|
| CP2B-F0157 | 2026-10-23: a 2ª InterCocen aconteceu em 19 e 20/09/2026, das 9h às 16h, no "Centro de Eventos da Secretaria Municipal de Educação" de Campinas (R. Antônio Nunes dos Santos, 121, Jardim do Vovô),… |
| CP2B-F0089 | A Clean Environment Brasil, que a Canal Solar citou no fórum de biogás de "sexta-feira (28)" na Unicamp, é "Patrocinador Prata" do I Fórum Paulista (F0255). Isso reforça que a nota da Canal Solar… |
| CP2B-F0251 | O Manual de Identidade Visual é de "JUL 2025", tem 34 páginas e foi feito pela GHM Solutions (F0253) |
| CP2B-F0245 | Template: criado e modificado em 2026-08-10 por "Luciana C L Lenhari"; Eixo 0 nomeado "E0 Planejamento e Gestão Estratégica"; hora-aula Extecamp de R$ 877,75 (F0254). A rota /capacitacao entrou no ar… |
| CP2B-F0235 | Reforça a identidade da "planilha da Luciana" com L. C. Lenhari da Silva: ela é a lastModifiedBy do template do Eixo 6 (2026-08-10). Segue inferência |
| CP2B-F0036 / F0012 | Nome do Eixo 0: "EIXO 0 – Coordenação do CP2B" no Workshop de 2025-12-02; "E0 Planejamento e Gestão Estratégica" no template de ago/2026 |
| CP2B-F0174 | Rechecado em 2026-10-23: 15 registros, todos active=true, o último updated_at em 2026-08-24T11:44:28. Os órgãos públicos seguem ativos no banco e são escondidos na vitrine pelo código do defeso… |
| CP2B-F0022 / F0023 | Facamp e UNESP seguem presentes pela equipe no content.js: Daniel F. N. Menezes (FACAMP); Hildo Guillardi Júnior (FESJBV/UNESP); Marcelo M. de Magalhães (CET/UNESP); Sarita C. Rabelo (FCA/UNESP). A… |
| CP2B-F0234 / F0250 | /api/podcast segue com 1 episódio (id 1, created 2026-09-09, published_at null). A página do episódio no Spotify não mostra outros episódios nem o link do programa. WebSearch "CP2b Talks" sem… |
| CP2B-F0169 | 2026-10-23 (19h): /api/news com as mesmas 6 notícias (a mais recente é a id 16, de 2026-05-28); /api/events = [] |
| CP2B-F0233 | /api/boletins segue só com a Edição 1 |
| CP2B-F0208 / F0144 | Recontagem de 2026-10-23: OpenAlex awards.funder_award_id:24/01112-1 = 6 (mesmos DOIs); Crossref award.number:2024/01112-1 = 5 (mesmos DOIs) |
| CP2B-F0176 / F0071 | O PDF projetos-ccd2026 repete a entrada do CP2B, sem valor. ccd.fapesp.br/sobre dá a série por chamada 32/34/20/19/10 (= 115) e liga para uma lista "CCDs financiados" na BV (bv.fapesp.br/pt/705, não… |
| CP2B-F0231 / P551 | O roteiro de 28/09/2026 numera as migrações até 052 (051 = /capacitacao; 052 = metadados de 3 publicações). As migrações 042 e 043 (08/09) ficam entre essas datas. Nomes dos arquivos ainda… |
| CP2B-F0223 / P550 | laboratories.js segue igual: 17.188 bytes, sha256 fb301e28… O prefixo "fb301e42…" anotado em 2026-10-23 (02h) parece erro de digitação, porque o tamanho é o mesmo. Sem regeneração |
| CP2B-F0073 | Pista fraca para "Barão Geraldo": as boas práticas do Arqueia citam "Laboratórios do CP2b" junto a serviços de emergência do "Campus Barão Geraldo". Não dá o endereço da sede; segue sem confirmação… |

### Pistas novas na fila
- P620 (média): App "ABIOVE" servido na mesma VM do site (/abiove; client_error no WebFetch): o que é, se tem relação com a Associação Brasileira das Indústrias de Óleos Vegetais e se é projeto do CP2B (Eixo…
- P621 (alta): Arqueia: lista de equipamentos da agenda pública (carregada por JS; procurar a rota de API do Arqueia), data de criação, equipe; pode dar os equipamentos do CP2b Lab (P472)
- P622 (média): Lista "CCDs financiados pelo programa" na BV (bv.fapesp.br/pt/705/centros-de-ciencia-para-o-desenvolvimento-ccd-sp; /pt/ costuma dar 403, tentar /en/705): ver o CP2B, o valor e K47
- P624 (média): Pós-defeso: reler parceiros.png, content.js (`partners.public`) e /api/partners a partir de 2026-10-26 e ver se a restauração traz parceiro novo
- P625 (baixa): "Analítica" (patrocinadora bronze do Fórum): identificar a empresa
- P626 (média): Programação completa do I Fórum Paulista (CronogramaEvento.jsx foi removido do main): procurar cópia (outros docs do repositório, notícias, LinkedIn) com painéis e painelistas
- P627 (baixa): "Mulheres do Biogás", "MCPAR Engenharia" e "Sesamm" na faixa de apoiadores: natureza do apoio e data
- P628 (média): Pastas cp2b_web/docs/ e deployment/ do repositório: procurar outros documentos datados (decisões, regimento, Anexo 11) lendo os nomes citados nos arquivos já baixados

## Conflitos e dúvidas
- **NIPE-K47 (novo):** o InterCocen 2026 foi anunciado para 23–24/05 no Espaço Cis Guanabara (post do NIPE de 2026-04-01) e realizado em 19–20/09 no Centro de Eventos da SME de Campinas. É provável adiamento, mas nenhuma fonte o confirma. Ligado ao CP2B-K46.
- **CP2B-K47 (novo):** número de CCDs do 3º edital, 21 (Agência FAPESP 2024) contra 20 (FAPESP 2026). Não afeta o CP2B.
- **CP2B-F0256** (mesa de abertura do Fórum) vem do cronograma previsto citado no documento do defeso. É programação, não ata, e por isso tem confiança média.
- **CP2B-F0260** (publicação do site em 28/09) é um roteiro; a execução nessa data não foi confirmada por outra fonte.

## ⚠️ Limitações de hoje
- Upload: a versão completa de NIPE_C01_C03_v2026-10-23_b.md não foi salva (envio interrompido por filtro). As 3 linhas novas estão no ADENDO; ver "Arquivos salvos".
- www2.unicamp.br deu SERVER_ERROR em 5 de 9 acessos à noite (notícias de 2017–2019 e estatico-2023).
- A página COCEN de relatórios CAI/CONSU só tem 3 relatórios com conteúdo; os números por centro não estão lá (P570, P571 e P532 encerradas na prática).
- As Tabelas 25–28 do relatório FAPESP 2023 não são extraíveis (caminho morto para o valor do CEP).
- A agenda pública do Arqueia carrega por JS e não foi legível; /abiove dá erro.
- CPPLEI (2026/05010-4) ainda não aparece na BV.

## Painel de saturação (resumo)
| Instituição | Categorias abertas | Saturadas | Em manutenção | % saturação |
|---|---|---|---|---|
| NIPE | 11 | 1 (C01) | 0 | 8% |
| CP2B | 11 | 1 (C07) | 0 | 8% |

## Ficha-resumo atualizada — NIPE
- Núcleo Interdisciplinar de Planejamento Energético (UNICAMP/COCEN). O NUCLENER foi criado em 1984 e transformado em NIPE pela CONSU-A-027/1993. Sede: Rua Cora Coralina, 330.
- Coordenação: Marcelo P. da Cunha (mandato COCEN 2025-07-17 a 2027-07-16); coordenadora associada Bruna de Souza Moraes.
- Centros abrigados: CP2B (CCD 24/01112-1), CePIL (CCD 24/01110-9; 4 eixos), CEP (CPE FAPESP/Braskem 21/05251-8), CPPLEI (CCD 2026/05010-4), LABIOEN, PPBioen e LH2.
- Registro: 521 fatos (518 [V]). FAPESP por ano nos Anuários de 2001 a 2021. Convênios com empresas: CPFL, AES Tietê, CHESF, Eletropaulo, Petrobras, TotalEnergies, Braskem e outros.
- PI: patentes 2016–2021 completas nos Anuários, mais BR102013011126-0 (2020); software PC329_BIOGAS (depositado).

## Ficha-resumo atualizada — CP2B
- Centro Paulista de Estudos em Biogás e Bioprodutos, FAPESP CCD 24/01112-1 (2025-02-01 a 2030-01-31), 3º edital CCD, sediado no NIPE.
- Direção: Bruna de Souza Moraes; vice-diretora Renata Piacentini Rodriguez. 8 eixos + Eixo 0 ("Planejamento e Gestão Estratégica").
- Registro: 262 fatos [V]. 15 bolsas vinculadas, 53 associados e 5 PIs na BV. OpenAlex 6 e Crossref 5 artigos com o award.
- Parceiros: 15 formais (API) e 21 logos na faixa da home, entre eles FAPESP, Equinor/Res2Bio, Sabesp, Comgás, UNIFAL, USP, TU Delft, UCA e LNEG.
- Marcos de 2026: I Fórum Paulista (28/05; 4 patrocinadores), sede laboratorial (29/05), Arqueia (gestão de equipamentos) e template de cursos.

## Plano para a próxima execução
Sábado 2026-10-24 (ênfase C11 + C12): CONEX/PROEC 2010–2016 (P598–P600); parceiros internacionais do NIPE; posts CePIL restantes (P604); Anuários das unidades para patentes (P607). CP2B: pós-defeso dos parceiros públicos a partir de 2026-10-26 (P624), lista de CCDs na BV (P622, K47), Arqueia (P621) e programação do Fórum (P626). Recontagem mensal em 2026-11-01; catálogos CSV no domingo, 2026-10-25.

## Fontes consultadas hoje
1. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=5700,6103,5725&_fields=id,date,title,content
2. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?after=2026-03-01T00:00:00&before=2026-07-01T00:00:00&per_page=50&_fields=id,date,title
3. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?after=2026-03-01T00:00:00&before=2026-06-20T00:00:00&per_page=40&_fields=id,date,title.rendered
4. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=6042,6011,6007&_fields=id,date,title,content
5. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?after=2026-04-15T00:00:00&before=2026-06-10T00:00:00&per_page=20&_fields=id,date,title.rendered
6. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/search?search=CePIL&per_page=100&type=post&subtype=post
7. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=5817,5778,5877&_fields=id,date,title,content
8. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=5976,5990,5737&_fields=id,date,title,content
9. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=5719,5708,5690&_fields=id,date,title,content
10. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=4868,5103,4809&_fields=id,date,title,content
11. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=4221,4356,4707&_fields=id,date,title,content
12. (NIPE) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=6670,6533,6337&_fields=id,date,title,content
13. (NIPE) WebSearch: InterCocen 2026 Unicamp adiada setembro Cis Guanabara
14. (NIPE) https://agencia.fapesp.br/2a-feira-intercocen-unicamp-celebracao-da-ciencia-interdisciplinar/59181
15. (NIPE) WebSearch: "unicamp.br/unicamp/ju" Nipe Núcleo Interdisciplinar de Planejamento Energético (unicamp.br)
16. (NIPE) WebSearch: Jornal da Unicamp "do Nipe" pesquisador bioenergia 2017 (www2.unicamp.br, unicamp.br)
17. (NIPE) https://unicamp.br/unicamp/unicamp_hoje/ju/maio2007/ju360pag04.html (redirecionamento)
18. (NIPE) https://www2.unicamp.br/unicamp/unicamp_hoje/ju/maio2007/ju360pag04.html
19. (NIPE) WebSearch: "unicamp.br/unicamp/ju" Telma Franco Nipe coordenadora
20. (NIPE) https://www2.unicamp.br/estatico-2023/eventos/2019/10/16/bioenergia-e-planejamento-energetico-ciclo-de-seminarios-do-nipe-recebe-para/ (SERVER_ERROR)
21. (NIPE) https://www2.unicamp.br/unicamp/ju/noticias/2019/08/07/projetos-internacionais-exploram-biomassas-para-producao-de-biocombustiveis/ (SERVER_ERROR ×2)
22. (NIPE) https://www.cocen.unicamp.br/cai-consu/relatorio-de-atividades
23. (NIPE) https://fapesp.br/publicacoes/relatorio2023-tabelas.pdf (sem offset e offset 60000)
24. (NIPE) WebSearch: "26/05010-4" OR "2026/05010-4" Centro Paulista de Planejamento Energético Integrado
25. (NIPE) https://tecnologias.inova.unicamp.br/?s=biog%C3%A1s
26. (NIPE) https://tecnologias.inova.unicamp.br/tecnologia/pc329_biogas/
27. (NIPE) https://tecnologias.inova.unicamp.br/?s=Jannuzzi
28. (NIPE) WebSearch: patente "Bruna de Souza Moraes" inventor Unicamp biogás vinhaça BR10
29. (NIPE) https://www2.unicamp.br/anuario/2020/FEA/DETA/DETA-0034.html
30. (NIPE) https://patents.google.com/patent/BR102013011126B1/pt
31. (NIPE) https://www2.unicamp.br/unicamp/unicamp_hoje/jornalPDF/JU_0001.pdf
32. (NIPE) WebSearch: "Núcleo de Energia" Unicamp jornalPDF JU 1987…1992
33. (NIPE) WebSearch: "sede do Nipe" OR "prédio do Nipe" Unicamp inauguração
34. (NIPE) https://www2.unicamp.br/unicamp/unicamp_hoje/jornalPDF/ju339pg02.pdf
35. (NIPE) https://www2.unicamp.br/unicamp/unicamp_hoje/jornalPDF/ju376pag10.pdf
36. (NIPE) https://cgu.unicamp.br/documento/copei-pautas-e-atas/copei_ata_2018_144_20181218
37. (NIPE) https://www.pg.unicamp.br/norma/2851/0
38. (NIPE) https://www.pg.unicamp.br/norma/3361/0
39. (NIPE) WebSearch: Funcamp transparência convênios "Núcleo Interdisciplinar de Planejamento Energético"
40. (NIPE) https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pauta31outubro.pdf
41. (NIPE) https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pautaconex21nov.pdf
42. (NIPE) WebSearch: CONEX pauta "(NIPE)" contrato Funcamp relatório final processo 01-P (conex.proec.unicamp.br) — 0 resultados
43. (NIPE) WebSearch: conex.proec.unicamp.br pauta NIPE Vivaldo Silveira contrato
44. (NIPE) https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pautaconex10abril.pdf
45. (NIPE) https://www.conex.proec.unicamp.br/assets/docs/conex/pautas/pautaconex23out.pdf
46. (NIPE) https://www2.unicamp.br/anuario/2013/centronucleo/NIPE-projetosQueParticipa.html
47. (NIPE) https://api.crossref.org/works?filter=award.number:2012/00282-3&rows=60&select=DOI,title,issued,container-title,author
48. (NIPE) https://cocen.unicamp.br/files/documents/relatoriosGestao/46cd0a04f0144b45da517373a763df2c-130924.pdf
49. (NIPE) https://www2.unicamp.br/unicamp/noticias/2016/10/20/biocombustiveis-avancados-sao-alternativa-para-aviacao-sustentavel
50. (NIPE) WebSearch: "Nipe" Unicamp notícia 2018 Gustavo Valença coordenador… (unicamp.br)
51. (NIPE) https://www2.unicamp.br/unicamp/noticias/2017/03/21/workshop-debate-utilizacao-de-biomassa-na-producao-de-produtos-quimicos/ (SERVER_ERROR)
52. (NIPE) https://www2.unicamp.br/unicamp/noticias/2018/06/11/eficiencia-energetica-e-discutida-por-especialista-em-evento-da-unicamp/ (SERVER_ERROR)
53. (CP2B) https://cp2b.unicamp.br/arqueia (×2)
54. (CP2B) https://cp2b.unicamp.br/arqueia/agenda-publica
55. (CP2B) https://cp2b.unicamp.br/arqueia/boas-praticas
56. (CP2B) https://cp2b.unicamp.br/abiove (client_error)
57. (CP2B) https://cp2b.unicamp.br/api/news
58. (CP2B) https://cp2b.unicamp.br/api/events
59. (CP2B) https://cp2b.unicamp.br/api/boletins
60. (CP2B) https://cp2b.unicamp.br/api/podcast
61. (CP2B) https://cp2b.unicamp.br/api/partners
62. (CP2B) https://cp2b.unicamp.br/api/team/105 (client_error)
63. (CP2B) https://cp2b.unicamp.br/api/team/106 (client_error)
64. (CP2B) https://open.spotify.com/episode/1DdLorkIHbFozWm6Eme1S7?si=cEoxU0CIS9upo1rjj7UD1w
65. (CP2B) WebSearch "CP2b Talks" podcast
66. (CP2B) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?search=CP2B&per_page=10&_fields=id,date,title,link
67. (CP2B) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?search=InterCocen&per_page=20&_fields=id,date,title,link
68. (CP2B) https://www.nipe.unicamp.br/wp-json/wp/v2/posts?include=6605,6680&_fields=id,date,title,content
69. (CP2B) WebSearch InterCocen 2026 feira de ciências Cocen Unicamp 19 de setembro
70. (CP2B) https://agencia.fapesp.br/2a-feira-intercocen-unicamp-celebracao-da-ciencia-interdisciplinar/59181
71. (CP2B) https://www.band.com.br/nacional/sp/feira-da-unicamp-reune-ciencias-e-artes-neste-final-de-semana-em-campinas
72. (CP2B) WebSearch InterCocen adiada maio 2026 Espaço Cis Guanabara
73. (CP2B) https://www.ceb.unicamp.br/?p=5334
74. (CP2B) https://fapesp.br/14897/centros-de-ciencia-para-o-desenvolvimento
75. (CP2B) https://www.tribunadosertao.com.br/geral/2026/05/28/910471-equinor-investe-r-172-milhoes-em-projeto-para-avaliar-producao-de-biometano
76. (CP2B) https://www.nipe.unicamp.br/oportunidades/
77. (CP2B) WebSearch ccd.fapesp.br "Biogás e Bioprodutos"
78. (CP2B) https://ccd.fapesp.br/sobre
79. (CP2B) https://fapesp.br/files/upload/16421/projetos-ccd2026.pdf
80. (CP2B) https://api.openalex.org/works?filter=awards.funder_award_id:24/01112-1&per_page=50&select=doi,title,publication_date
81. (CP2B) https://api.crossref.org/works?filter=award.number:2024/01112-1&rows=50&select=DOI,title,issued,container-title
82. (CP2B) https://api.openalex.org/works?filter=fulltext.search:%22Biogas%20and%20Bioproducts%22&select=doi,title,publication_date&per_page=50
83. (CP2B) https://awards.adbioresources.org/education-campaign-of-the-year-amplum-biogas-knowledge-and-education-initiative/
84. (CP2B) WebSearch daal.ufc.br Renata Piacentini Rodriguez speaker CP2B
85. (CP2B) https://daal.ufc.br/speaker/renata-piacentini-rodriguez-2/?lang=en
86. (CP2B) WebSearch daal.ufc.br anaerobic digestion Latin America workshop UFC Fortaleza 2026
87. (CP2B) https://daal.ufc.br/?lang=en
88. (CP2B) WebSearch Universidad de Cádiz Unicamp biogás convenio CP2B
89. (CP2B) Leituras curl em https://raw.githubusercontent.com/aikiesan/cp2bfun/main/ … :

## Arquivos salvos (Google Drive, pasta "Arquivo Histórico NIPE-CP2B")
- Pasta raiz: https://drive.google.com/drive/folders/1pJngdDR350NxbcmNu-t7LSn5NqOLaw9K
- NIPE_REGISTRO_MESTRE_v2026-10-23_b.md: https://drive.google.com/file/d/16nF4FuMmmMx4SCtHW-hGNZY85np_f04l/view
- CP2B_REGISTRO_MESTRE_v2026-10-23_b.md: https://drive.google.com/file/d/1WvU7ViWSryf_eZQzlvDQbkFe8L_nUmPP/view
- 00_PLANO_E_SATURACAO_v2026-10-23_c.md: https://drive.google.com/file/d/16L1Nt6NWJwF0k7XoY8W2kRFk9-oDv2f5/view
- 00_FILA_DE_PISTAS_NIPE_v2026-10-23_b.md: https://drive.google.com/file/d/13msMf9OamJYFBcR6YtrhXbhNRRvROggm/view
- 00_FILA_DE_PISTAS_CP2B_v2026-10-23_b.md: https://drive.google.com/file/d/1iM31AM-cJ84g2EmhlRxcBEvVMyNaTTrD/view
- Partes NIPE (_v2026-10-23_b): C04a https://drive.google.com/file/d/1HhhgGzBIaNLWMT6j3fpOrbOLkf7kl9nq/view · C05 https://drive.google.com/file/d/1NlLsLWaXCIr-wPyTWNGR0vbCHAbrAjBX/view · C08_C09 https://drive.google.com/file/d/1VOySVpdRpGgzLnIUWfARMiJFH1JzUwHo/view · C10 https://drive.google.com/file/d/1pTJiiSCWZLloF-RPsgLAw_xBwlip3bYg/view · C11_C12 https://drive.google.com/file/d/1BOpWmdLqOogeJGpOceWj6x_yVJ26an-w/view · CONFLITOS https://drive.google.com/file/d/1WbBgsUHO0f3p3f5czEMetovRh0ytAUaX/view · HISTORICO https://drive.google.com/file/d/1zOu4Q3YzBQJClOr-jyKsgO0TxWID2_Bi/view
- NIPE C01–C03: **a versão completa _b NÃO foi salva** (o envio foi interrompido por um filtro). Para não perder nada, foi criado NIPE_C01_C03_v2026-10-23_b_ADENDO.md (https://drive.google.com/file/d/1tNck5mDPXrTC2w37pj1VO2190KdHFTYA/view) com as 3 linhas novas (F0504, F0506, F0507). Estado atual: NIPE_C01_C03_v2026-10-23.md + ADENDO. A próxima execução deve aplicar o adendo.
- Partes CP2B (_v2026-10-23_b): C01_C03 https://drive.google.com/file/d/1SmnzDLp9I9azTmqYEE3YxYJn-WIGkgA7/view · C07_C09 https://drive.google.com/file/d/1nAF501XdtZkH9YF7ldPNVUBG84bZ5RC5/view · C10_C12 https://drive.google.com/file/d/1SOQgX7zepGFApPZMTsxIb3YCecCemAjA/view · CONFLITOS https://drive.google.com/file/d/1TkXks8kX12YcdU5LDZUclRPI8-pF7Xxs/view
- Sem mudança hoje (seguem _v2026-10-23): NIPE_C04b, NIPE_C06_C07, CP2B_C04_C05, CP2B_C06. Documento "NIPE in big numbers": não gerado (próximo em 2026-11-01). Catálogos CSV: não gerados (próximos no domingo, 2026-10-25).
- Verificação: os 16 arquivos completos foram baixados de volta e conferidos por sha256, todos idênticos aos locais.

---
*Rotina "Arquivo Histórico NIPE e CP2B". Selos: [V] fonte primária lida · [S] resumo/secundária — verificar. Nenhuma escrita em git foi feita (o repositório aikiesan/cp2bfun foi só lido, por curl em raw.githubusercontent.com).*
