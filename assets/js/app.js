/* Data NIPE — visualizações do Núcleo Interdisciplinar de Planejamento Energético (UNICAMP).
   Lê data/nipe.json (gerado por scripts/prepare_data.py). Cada figura tem um CSV em data/figuras/.
   Cores de dados em nipe.json.paleta (cópia de data/paleta.json): NIPE e CP2b sempre iguais. */
(() => {
  'use strict';

  const L = d3.formatLocale({ decimal: ',', thousands: '.', grouping: [3], currency: ['R$ ', ''] });
  const fN = L.format(',d');
  const fD1 = L.format(',.1f');
  const fD2 = L.format(',.2f');
  const fP1 = L.format('.1%');
  const fMi = (v) => fD1(v / 1e6);
  const docEl = document.documentElement;
  const cssv = (name) => getComputedStyle(docEl).getPropertyValue(name).trim();
  const PAGINA = document.body.dataset.page;
  let D = null;
  let COR = {};

  const el = (tag, cls, text) => {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  };

  /* ---------- tooltip ---------- */
  const tipEl = document.getElementById('tip');
  function tip(event, title, rows) {
    tipEl.replaceChildren(el('div', 'h', title));
    for (const r of rows) {
      const row = el('div', 'r');
      const left = el('span');
      if (r.color) { const i = el('i'); i.style.background = r.color; left.append(i); }
      left.append(r.label);
      row.append(left, el('b', '', r.value));
      tipEl.append(row);
    }
    tipEl.hidden = false;
    moveTip(event);
  }
  function moveTip(event) {
    const w = tipEl.offsetWidth, h = tipEl.offsetHeight;
    let x = event.clientX + 14, y = event.clientY - h - 12;
    if (x + w > innerWidth - 8) x = event.clientX - w - 14;
    if (y < 8) y = event.clientY + 16;
    tipEl.style.left = Math.max(8, x) + 'px';
    tipEl.style.top = y + 'px';
  }
  const hideTip = () => { tipEl.hidden = true; };
  addEventListener('scroll', hideTip, { passive: true });

  function segmented(container, options, current, onPick) {
    container.replaceChildren();
    for (const o of options) {
      const b = el('button', '', o.label);
      b.type = 'button';
      b.setAttribute('aria-pressed', String(o.value === current));
      b.addEventListener('click', () => {
        for (const x of container.querySelectorAll('button')) x.setAttribute('aria-pressed', String(x === b));
        onPick(o.value);
      });
      container.append(b);
    }
  }

  /* ---------- interface: cabeçalho, menu, revelações ---------- */
  const head = document.getElementById('head');
  const heroEl = document.getElementById('topo');
  const menuBtn = document.getElementById('menu-btn');
  const solidez = () => head.classList.toggle('solid', heroEl.getBoundingClientRect().bottom < 72);
  addEventListener('scroll', solidez, { passive: true });
  solidez();
  const fechaMenu = () => {
    head.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.setAttribute('aria-label', 'Abrir menu');
    document.body.style.overflow = '';
  };
  menuBtn.addEventListener('click', () => {
    const aberto = head.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', String(aberto));
    menuBtn.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    document.body.style.overflow = aberto ? 'hidden' : '';
  });
  for (const a of document.querySelectorAll('#menu a')) a.addEventListener('click', fechaMenu);
  addEventListener('keydown', (e) => { if (e.key === 'Escape') fechaMenu(); });

  const rio = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); }
  }, { rootMargin: '0px 0px -8% 0px' });
  for (const n of document.querySelectorAll('.rise')) rio.observe(n);

  const navLinks = [...document.querySelectorAll('#menu a')].filter((a) => a.getAttribute('href').startsWith('#'));
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      for (const a of navLinks) a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id);
    }
  }, { rootMargin: '-35% 0px -60% 0px' });
  for (const a of navLinks) { const s = document.querySelector(a.getAttribute('href')); if (s) io.observe(s); }

  const renders = [];
  const reg = (f) => { renders.push(f); try { f(); } catch (e) { console.error(e); } };
  let lastW = innerWidth, timer = 0;
  addEventListener('resize', () => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (Math.abs(innerWidth - lastW) > 4) { lastW = innerWidth; for (const f of renders) { try { f(); } catch (e) { console.error(e); } } }
    }, 160);
  });

  /* ---------- números no texto: sempre de nipe.json ---------- */
  function preencheTextos() {
    for (const n of document.querySelectorAll('[data-k]')) {
      const v = D.textos[n.dataset.k];
      if (v !== undefined) n.textContent = v;
      else console.warn('chave sem valor em nipe.json:', n.dataset.k);
    }
  }

  /* ---------- gráficos genéricos ---------- */
  function svgBox(box, H) {
    box.replaceChildren();
    const W = box.clientWidth || 600;
    const svg = d3.select(box).append('svg').attr('viewBox', `0 0 ${W} ${H}`).attr('width', W).attr('height', H);
    return { svg, W, H };
  }

  // linhas: series = [{key, label, color, width, dash, pts:[{x,y}], fundo}]
  function linhas(box, series, o = {}) {
    const H = o.H || Math.max(200, Math.min(320, Math.round((box.clientWidth || 600) * 0.42)));
    const { svg, W } = svgBox(box, H);
    const m = Object.assign({ t: 14, r: o.rotulos ? Math.min(96, Math.round(W * 0.28)) : 14, b: 24, l: 40 }, o.m || {});
    const todos = series.flatMap((s) => s.pts);
    const x = d3.scaleLinear(o.xDom || d3.extent(todos, (p) => p.x), [m.l, W - m.r]);
    const y = d3.scaleLinear([o.yMin ?? Math.min(0, d3.min(todos, (p) => p.y)), o.yMax ?? d3.max(todos, (p) => p.y)], [H - m.b, m.t]).nice(4);
    const yt = o.yTicks || y.ticks(4);
    svg.append('g').selectAll('line').data(yt).join('line').attr('x1', m.l).attr('x2', W - m.r).attr('y1', y).attr('y2', y)
      .attr('stroke', cssv('--rule')).attr('stroke-dasharray', (d) => (d === 0 ? null : '2 3'));
    svg.append('g').selectAll('text').data(yt).join('text').attr('x', m.l - 6).attr('y', (d) => y(d) + 4).attr('text-anchor', 'end')
      .text(o.yFmt || fN);
    const xt = o.xTicks || x.ticks(5);
    svg.append('g').selectAll('text').data(xt).join('text').attr('x', x).attr('y', H - 6).attr('text-anchor', 'middle').text((d) => d);
    const ln = d3.line().defined((p) => p.y !== null && p.y !== undefined).x((p) => x(p.x)).y((p) => y(p.y));
    const g = svg.append('g');
    const ordenadas = [...series].sort((a, b) => (a.fundo === b.fundo ? 0 : a.fundo ? -1 : 1));
    const paths = g.selectAll('path').data(ordenadas).join('path').attr('fill', 'none').attr('d', (s) => ln(s.pts))
      .attr('stroke', (s) => s.color).attr('stroke-width', (s) => s.width || 2).attr('stroke-dasharray', (s) => s.dash || null)
      .attr('stroke-linejoin', 'round').attr('stroke-linecap', 'round');
    for (const s of ordenadas.filter((s) => s.pontos)) {
      g.append('g').selectAll('circle').data(s.pts.filter((p) => p.y !== null)).join('circle')
        .attr('cx', (p) => x(p.x)).attr('cy', (p) => y(p.y)).attr('r', 3).attr('fill', s.color);
    }
    if (o.rotulos) {
      for (const s of series.filter((s) => !s.fundo && s.label)) {
        const ult = [...s.pts].reverse().find((p) => p.y !== null);
        if (ult) svg.append('text').attr('x', x(ult.x) + 6).attr('y', y(ult.y) + 4).attr('class', 'lbl-strong').attr('fill', s.color).style('fill', s.color).text(s.label);
      }
    }
    if (o.hoverLinha) {
      // passar o mouse destaca a linha mais próxima (comparação entre centros)
      const realce = svg.append('path').attr('fill', 'none').attr('stroke', cssv('--ink')).attr('stroke-width', 1.6).attr('visibility', 'hidden');
      svg.append('rect').attr('x', m.l).attr('y', m.t).attr('width', Math.max(0, W - m.l - m.r)).attr('height', H - m.t - m.b).attr('fill', 'transparent')
        .on('pointermove', (event) => {
          const [mx, my] = d3.pointer(event);
          const xv = Math.round(x.invert(mx));
          let melhor = null, dist = Infinity;
          for (const s of series) {
            const p = s.pts.find((q) => q.x === xv);
            if (!p || p.y === null) continue;
            const dd = Math.abs(y(p.y) - my);
            if (dd < dist) { dist = dd; melhor = { s, p }; }
          }
          if (!melhor) return;
          realce.attr('d', ln(melhor.s.pts)).attr('visibility', 'visible').attr('stroke', melhor.s.key === 'NIPE' ? COR.NIPE : cssv('--ink'));
          tip(event, `${melhor.s.label || melhor.s.key} · ${xv}`, [{ label: o.rotuloValor || 'valor', value: (o.tipFmt || o.yFmt || fN)(melhor.p.y) }]);
        })
        .on('pointerleave', () => { realce.attr('visibility', 'hidden'); hideTip(); });
    } else {
      const guia = svg.append('line').attr('y1', m.t).attr('y2', H - m.b).attr('stroke', cssv('--ink')).attr('visibility', 'hidden');
      svg.append('rect').attr('x', m.l).attr('y', m.t).attr('width', Math.max(0, W - m.l - m.r)).attr('height', H - m.t - m.b).attr('fill', 'transparent')
        .on('pointermove', (event) => {
          const xv = Math.round(x.invert(d3.pointer(event)[0]));
          const rows = series.filter((s) => !s.fundo).map((s) => {
            const p = s.pts.find((q) => q.x === xv);
            return p && p.y !== null ? { color: s.color, label: s.label || s.key, value: (o.tipFmt || o.yFmt || fN)(p.y) } : null;
          }).filter(Boolean);
          if (!rows.length) { hideTip(); return; }
          guia.attr('x1', x(xv)).attr('x2', x(xv)).attr('visibility', 'visible');
          tip(event, String(xv), rows);
        })
        .on('pointerleave', () => { guia.attr('visibility', 'hidden'); hideTip(); });
    }
    return { svg, x, y, W, H, m, paths };
  }

  // barras horizontais em HTML (como no Data BEPE)
  function barras(boxId, rows, fmt = fN) {
    const box = document.getElementById(boxId);
    box.replaceChildren();
    const max = d3.max(rows, (r) => r.value);
    for (const r of rows) {
      const row = el('div', 'bar-row');
      const l = el('div', 'l', r.label);
      if (r.sub) l.append(el('small', '', r.sub));
      const t = el('div', 't');
      const f = el('div', 'f');
      f.style.width = (100 * r.value / max) + '%';
      f.style.background = r.color || COR.contexto;
      t.append(f);
      row.append(l, t, el('div', 'v', fmt(r.value)));
      box.append(row);
    }
  }

  // barras verticais empilhadas
  function colunas(box, rows, keys, cores, rotulos, o = {}) {
    const H = o.H || Math.max(220, Math.min(320, Math.round((box.clientWidth || 600) * 0.4)));
    const { svg, W } = svgBox(box, H);
    const m = { t: 14, r: 8, b: 24, l: 40 };
    const x = d3.scaleBand(rows.map((r) => r.x), [m.l, W - m.r]).paddingInner(0.2);
    const tot = (r) => d3.sum(keys, (k) => r[k] || 0);
    const y = d3.scaleLinear([0, d3.max(rows, tot)], [H - m.b, m.t]).nice(4);
    svg.append('g').selectAll('line').data(y.ticks(4)).join('line').attr('x1', m.l).attr('x2', W - m.r).attr('y1', y).attr('y2', y)
      .attr('stroke', cssv('--rule')).attr('stroke-dasharray', (d) => (d === 0 ? null : '2 3'));
    svg.append('g').selectAll('text').data(y.ticks(4)).join('text').attr('x', m.l - 6).attr('y', (d) => y(d) + 4).attr('text-anchor', 'end').text(fN);
    const st = d3.stack().keys(keys).value((r, k) => r[k] || 0)(rows);
    svg.append('g').selectAll('g').data(st).join('g').attr('fill', (s, i) => cores[i])
      .selectAll('rect').data((s) => s).join('rect')
      .attr('x', (d) => x(d.data.x)).attr('width', x.bandwidth()).attr('y', (d) => y(d[1])).attr('height', (d) => Math.max(0, y(d[0]) - y(d[1])));
    svg.append('g').selectAll('text').data(rows).join('text').attr('x', (r) => x(r.x) + x.bandwidth() / 2).attr('y', H - 6)
      .attr('text-anchor', 'middle').text((r) => r.x);
    svg.append('g').selectAll('text').data(rows).join('text').attr('x', (r) => x(r.x) + x.bandwidth() / 2).attr('y', (r) => y(tot(r)) - 4)
      .attr('text-anchor', 'middle').attr('class', 'lbl-strong').text((r) => (tot(r) ? fN(tot(r)) : ''));
    svg.append('g').selectAll('rect').data(rows).join('rect').attr('x', (r) => x(r.x)).attr('width', x.bandwidth()).attr('y', m.t)
      .attr('height', H - m.t - m.b).attr('fill', 'transparent')
      .on('pointermove', (event, r) => tip(event, String(r.x), keys.map((k, i) => ({ color: cores[i], label: rotulos[i], value: fN(r[k] || 0) }))))
      .on('pointerleave', hideTip);
  }

  function legenda(boxId, itens) {
    const box = document.getElementById(boxId);
    if (!box) return;
    box.replaceChildren();
    for (const it of itens) {
      const s = el('span');
      const i = el('i');
      i.style.background = it.color;
      if (it.dash) { i.style.background = 'transparent'; i.style.border = `1.5px dashed ${it.color}`; }
      s.append(i, it.label);
      box.append(s);
    }
  }

  /* ================================================================ NIPE hoje */
  function startHoje() {
    const s = new Map(D.serie_nipe.map((r) => [r.ano, r]));
    const anos = d3.range(2015, 2026);
    const serie = (k) => anos.map((a) => ({ x: a, y: s.get(a)[k] }));
    reg(() => linhas(document.getElementById('chart-recente-proj'),
      [{ key: 'NIPE', label: 'NIPE', color: COR.NIPE, width: 2.4, pontos: true, pts: serie('projetos_com_financiamento') }],
      { H: 220, xTicks: [2015, 2020, 2025] }));
    reg(() => linhas(document.getElementById('chart-recente-art'),
      [{ key: 'NIPE', label: 'NIPE', color: COR.NIPE, width: 2.4, pontos: true, pts: serie('artigos') }],
      { H: 220, xTicks: [2015, 2020, 2025] }));
    const nomeCentro = { CP2B: 'CP2b' };
    const corCentro = (c) => (c === 'NIPE' ? COR.NIPE : c === 'CP2B' ? COR.CP2b : COR.contexto);
    const sub = { NIPE: 'projetos do próprio núcleo', CEP: 'Centro de Engenharia de Plasticultura', CP2B: 'Centro Paulista de Estudos em Biogás e Bioprodutos',
      CePIL: 'Centro Paulista de Inovação em Iluminação Pública', LH2: 'Laboratório de Hidrogênio', LABIOEN: 'Laboratório de Bioenergia' };
    barras('bars-centros', D.arquivo.projetos_por_centro.map((r) => ({
      label: nomeCentro[r.centro] || r.centro, sub: sub[r.centro], value: r.registros, color: corCentro(r.centro),
    })));
    barras('bars-edat', [
      { label: 'Pesquisadores visitantes', value: 51 }, { label: 'Pós-doutorandos', value: 23 },
      { label: 'Pesquisadores de carreira', value: 4 }, { label: 'Pesquisadores colaboradores', value: 2 },
    ]);
    const tipos = ['artigo/outro', 'livro/capítulo', 'tese/dissertação'];
    const rot = ['Artigos e outros', 'Livros e capítulos', 'Teses e dissertações'];
    const coresCp2b = [COR.CP2b, '#F2C46B', '#F7DFAE'];
    const pub = d3.rollup(D.arquivo.cp2b.publicacoes_ano_tipo, (v) => d3.sum(v, (r) => r.publicacoes), (r) => r.ano, (r) => r.tipo);
    const rows = [...pub.keys()].sort().map((a) => Object.assign({ x: a }, Object.fromEntries(tipos.map((t) => [t, pub.get(a).get(t) || 0]))));
    legenda('legend-cp2b', tipos.map((t, i) => ({ color: coresCp2b[i], label: rot[i] })));
    reg(() => colunas(document.getElementById('chart-cp2b'), rows, tipos, coresCp2b, rot, { H: 220 }));
    const tb = document.querySelector('#tab-disputa tbody');
    for (const r of D.disputa) {
      const tr = el('tr');
      for (const c of [r.numero, r.leitura_a, r.leitura_b, r.conflito, r.tratamento]) tr.append(el('td', '', c));
      tb.append(tr);
    }
  }

  /* ================================================================ Histórico */
  function startHistorico() {
    const ol = document.getElementById('marcos');
    for (const m of D.marcos) {
      const li = el('li');
      const t = el('time', '', m.data.length > 4 ? m.data.split('-').reverse().join('/') : m.data);
      li.append(t, el('h3', '', m.titulo), el('p', '', m.texto), el('p', 'dica', m.ids));
      ol.append(li);
    }
    reg(drawGantt);
    const s = D.serie_nipe;
    const pts = (k) => s.map((r) => ({ x: r.ano, y: r[k] }));
    legenda('legend-equipe', [{ color: COR.NIPE, label: 'Pesquisadores' }, { color: COR.contexto_escuro, label: 'Docentes' }]);
    reg(() => linhas(document.getElementById('chart-equipe'), [
      { key: 'pesq', label: 'Pesquisadores', color: COR.NIPE, width: 2.4, pts: pts('pesquisadores') },
      { key: 'doc', label: 'Docentes', color: COR.contexto_escuro, width: 1.6, pts: pts('docentes') },
    ], { rotulos: true, xTicks: [2004, 2010, 2015, 2020, 2025] }));
    reg(() => linhas(document.getElementById('chart-bolsistas'), [
      { key: 'bol', label: 'Bolsistas', color: COR.contexto_escuro, width: 1.6, pts: pts('bolsistas') },
    ], { H: 200, xTicks: [2004, 2025] }));
    const www2 = D.projetos_www2.map((r) => ({ x: r.ano, y: r.projetos_com_financiamento }));
    const aep = s.filter((r) => r.projetos_com_financiamento !== null).map((r) => ({ x: r.ano, y: r.projetos_com_financiamento }));
    legenda('legend-projetos', [{ color: COR.contexto_escuro, label: 'Anuário web (www2), 2000–2021' }, { color: COR.NIPE, label: 'AEPLAN, PDF, 2015–2025' }]);
    reg(() => linhas(document.getElementById('chart-projetos'), [
      { key: 'www2', label: 'Anuário web', color: COR.contexto_escuro, width: 1.6, pontos: true, pts: www2 },
      { key: 'aeplan', label: 'AEPLAN', color: COR.NIPE, width: 2.4, pontos: true, pts: aep },
    ], { xTicks: [2001, 2005, 2010, 2015, 2020, 2025] }));
    const fap = s.filter((r) => r.fapesp_liberados !== null);
    legenda('legend-fapesp', [{ color: COR.NIPE, label: 'Concedidos (até 2015) ou contratados' }, { color: COR.contexto_escuro, label: 'Liberados', dash: true }]);
    reg(() => linhas(document.getElementById('chart-fapesp'), [
      { key: 'contr', label: 'Contratados', color: COR.NIPE, width: 2.4, pontos: true, pts: fap.map((r) => ({ x: r.ano, y: r.fapesp_contratados })) },
      { key: 'lib', label: 'Liberados', color: COR.contexto_escuro, width: 1.6, dash: '4 3', pts: fap.map((r) => ({ x: r.ano, y: r.fapesp_liberados })) },
    ], { yFmt: (v) => fMi(v), tipFmt: (v) => 'R$ ' + fMi(v) + ' mi', xTicks: [2008, 2012, 2016, 2020, 2025] }));
    const art = s.filter((r) => r.ano >= 2015).map((r) => ({ x: r.ano, intl: r.artigos_intl || 0, nac: r.artigos_nac || 0 }));
    legenda('legend-artigos', [{ color: COR.NIPE, label: 'Circulação internacional' }, { color: '#9CC3E0', label: 'Circulação nacional' }]);
    reg(() => colunas(document.getElementById('chart-artigos'), art, ['intl', 'nac'], [COR.NIPE, '#9CC3E0'], ['Internacional', 'Nacional']));
  }

  function drawGantt() {
    const box = document.getElementById('chart-gantt');
    const cs = D.arquivo.coordenadores;
    const H = cs.length * 26 + 40;
    const { svg, W } = svgBox(box, H);
    const estreito = W < 640;
    const m = { t: 10, r: estreito ? 8 : 230, b: 24, l: 8 };
    const x = d3.scaleLinear([1984, 2027.6], [m.l, W - m.r]);
    const y = (i) => m.t + i * 26;
    const ticks = [1984, 1993, 2002, 2011, 2020, 2027];
    svg.append('g').selectAll('line').data(ticks).join('line').attr('x1', x).attr('x2', x).attr('y1', m.t).attr('y2', H - m.b)
      .attr('stroke', cssv('--rule')).attr('stroke-dasharray', '2 3');
    svg.append('g').selectAll('text').data(ticks).join('text').attr('x', x).attr('y', H - 6).attr('text-anchor', 'middle').text((d) => d);
    const defs = svg.append('defs');
    defs.append('pattern').attr('id', 'hach').attr('width', 6).attr('height', 6).attr('patternUnits', 'userSpaceOnUse')
      .attr('patternTransform', 'rotate(45)').append('line').attr('x1', 0).attr('y1', 0).attr('x2', 0).attr('y2', 6)
      .attr('stroke', COR.NIPE).attr('stroke-width', 2);
    cs.forEach((c, i) => {
      const assoc = /ssociad/.test(c.cargo);
      const incerto = c.selo === 'S';
      const x0 = x(c.inicio), x1 = Math.max(x(c.fim), x0 + 5);
      svg.append('rect').attr('x', x0).attr('y', y(i)).attr('width', x1 - x0).attr('height', 16).attr('rx', 3)
        .attr('fill', incerto ? 'url(#hach)' : assoc ? COR.contexto : COR.NIPE)
        .attr('stroke', incerto ? COR.NIPE : 'none')
        .on('pointermove', (event) => tip(event, c.nome, [
          { label: 'Cargo', value: c.cargo }, { label: 'Início', value: c.inicio_texto }, { label: 'Fim', value: c.fim_texto },
          { label: 'Selo', value: incerto ? '[S] só no Lattes ou em fonte secundária' : '[V] verificado' },
          { label: 'Lattes', value: c.conferencia_lattes || '—' }, { label: 'Fato', value: c.id_fato }]))
        .on('pointerleave', hideTip);
      const nome = c.nome + (assoc ? (/associado/i.test(c.cargo) ? ' (associado)' : ' (associada)') : '');
      if (estreito) {
        svg.append('text').attr('x', x1 > W / 2 ? x0 - 4 : x1 + 4).attr('y', y(i) + 12).attr('text-anchor', x1 > W / 2 ? 'end' : 'start').attr('class', 'gantt-lbl').text(nome);
      } else {
        svg.append('text').attr('x', x1 + 6).attr('y', y(i) + 12).attr('class', 'gantt-lbl').text(nome);
      }
    });
  }

  /* ================================================================ NIPE entre os centros */
  const IND = () => Object.fromEntries(D.cocen.indicadores.map((i) => [i.chave, i]));
  const fmtInd = (k) => (IND()[k].casas ? fD2 : fN);
  const PAINEIS = ['projetos_por_dp', 'artigos_por_dp', 'convenios', 'eventos', 'projetos', 'artigos'];

  function startComparacao() {
    const porInd = d3.group(D.cocen.serie, (r) => r.indicador, (r) => r.sigla);
    const nomes = D.cocen.nomes;
    const grid = document.getElementById('sm-grid');
    const caixas = {};
    for (const k of PAINEIS) {
      const cell = el('div', 'sm-cell');
      const h = el('h4', '', IND()[k].rotulo);
      h.append(el('small', '', IND()[k].unidade === 'razão' ? 'valor por docente ou pesquisador' : 'número declarado no ano'));
      const c = el('div', 'chart');
      cell.append(h, c);
      grid.append(cell);
      caixas[k] = c;
    }
    reg(() => {
      for (const k of PAINEIS) {
        const g = porInd.get(k);
        const series = [...g.entries()].map(([sg, rs]) => ({
          key: sg, label: sg === 'NIPE' ? 'NIPE' : `${sg} · ${nomes[sg] || ''}`,
          color: sg === 'NIPE' ? COR.NIPE : COR.contexto, width: sg === 'NIPE' ? 2.6 : 1, fundo: sg !== 'NIPE',
          pts: d3.range(2015, 2026).map((a) => { const r = rs.find((q) => q.ano === a); return { x: a, y: r ? r.valor : null }; }),
        }));
        linhas(caixas[k], series, { H: 190, xTicks: [2015, 2020, 2025], yFmt: IND()[k].casas ? fD1 : fN, tipFmt: fmtInd(k), hoverLinha: true, m: { l: 34 } });
      }
    });

    let indSlope = 'artigos_por_dp';
    segmented(document.getElementById('seg-slope'), PAINEIS.map((k) => ({ value: k, label: IND()[k].rotulo.replace(' com financiamento', '').replace(' em periódicos', '') })),
      indSlope, (v) => { indSlope = v; drawSlope(indSlope); });
    reg(() => drawSlope(indSlope));

    const rk = d3.group(D.cocen.ranking, (r) => r.indicador);
    const rg = document.getElementById('rank-grid');
    const rcx = {};
    for (const k of PAINEIS) {
      const cell = el('div', 'sm-cell');
      const ult = rk.get(k).find((r) => r.ano === 2025);
      const h = el('h4', '', IND()[k].rotulo);
      h.append(el('small', '', ult ? `2025: ${ult.posicao}º de ${ult.centros}` : ''));
      const c = el('div', 'chart');
      cell.append(h, c);
      rg.append(cell);
      rcx[k] = c;
    }
    reg(() => {
      for (const k of PAINEIS) drawRank(rcx[k], rk.get(k));
    });

    const part = d3.group(D.cocen.participacao, (r) => r.indicador);
    const sp = (k) => (part.get(k) || []).map((r) => ({ x: r.ano, y: r.participacao }));
    reg(() => linhas(document.getElementById('chart-part'), [
      { key: 'projetos', label: 'Projetos', color: COR.NIPE, width: 2.4, pts: sp('projetos') },
      { key: 'artigos', label: 'Artigos', color: '#9CC3E0', width: 2, pts: sp('artigos') },
      { key: 'doc_pesq', label: 'Docentes e pesq.', color: COR.contexto_escuro, width: 1.6, pts: sp('doc_pesq') },
    ], { yFmt: L.format('.0%'), tipFmt: fP1, rotulos: true, xTicks: [2015, 2020, 2025] }));
  }

  function drawSlope(k) {
    const box = document.getElementById('chart-slope');
    const rows = D.cocen.slope.filter((r) => r.indicador === k);
    const H = 420;
    const { svg, W } = svgBox(box, H);
    const m = { t: 24, b: 28, l: 70, r: 150 };
    const xa = m.l, xb = Math.max(m.l + 140, Math.min(W - m.r, m.l + 360));
    const y = d3.scaleLinear([0, d3.max(rows, (r) => Math.max(r.valor_2015, r.valor_2025))], [H - m.b, m.t]).nice();
    const f = fmtInd(k);
    svg.append('text').attr('x', xa).attr('y', 14).attr('text-anchor', 'middle').attr('class', 'lbl-strong').text('2015');
    svg.append('text').attr('x', xb).attr('y', 14).attr('text-anchor', 'middle').attr('class', 'lbl-strong').text('2025');
    for (const xx of [xa, xb]) svg.append('line').attr('x1', xx).attr('x2', xx).attr('y1', m.t).attr('y2', H - m.b).attr('stroke', cssv('--rule'));
    const ord = [...rows].sort((a, b) => (a.sigla === 'NIPE') - (b.sigla === 'NIPE'));
    const g = svg.append('g');
    for (const r of ord) {
      const nipe = r.sigla === 'NIPE';
      const cor = nipe ? COR.NIPE : COR.contexto;
      const gg = g.append('g').style('cursor', 'default');
      gg.append('line').attr('x1', xa).attr('x2', xb).attr('y1', y(r.valor_2015)).attr('y2', y(r.valor_2025)).attr('stroke', cor).attr('stroke-width', nipe ? 3 : 1.2);
      gg.append('circle').attr('cx', xa).attr('cy', y(r.valor_2015)).attr('r', nipe ? 4.5 : 3).attr('fill', cor);
      gg.append('circle').attr('cx', xb).attr('cy', y(r.valor_2025)).attr('r', nipe ? 4.5 : 3).attr('fill', cor);
      gg.on('pointermove', (event) => tip(event, `${r.sigla} · ${D.cocen.nomes[r.sigla] || ''}`, [
        { label: '2015', value: f(r.valor_2015) }, { label: '2025', value: f(r.valor_2025) }, { label: 'Diferença', value: f(r.diferenca) }]))
        .on('pointerleave', hideTip);
    }
    // rótulos: NIPE e os três maiores de 2025, sem sobreposição
    const alvo = [...rows].sort((a, b) => b.valor_2025 - a.valor_2025).slice(0, 3);
    if (!alvo.find((r) => r.sigla === 'NIPE')) alvo.push(rows.find((r) => r.sigla === 'NIPE'));
    const itens = alvo.filter(Boolean).map((r) => ({ r, y: y(r.valor_2025) }));
    itens.sort((a, b) => a.y - b.y);
    for (let i = 1; i < itens.length; i++) if (itens[i].y - itens[i - 1].y < 14) itens[i].y = itens[i - 1].y + 14;
    for (const it of itens) {
      const nipe = it.r.sigla === 'NIPE';
      svg.append('text').attr('x', xb + 10).attr('y', it.y + 4).attr('class', nipe ? 'lbl-strong' : 'lbl').style('fill', nipe ? COR.NIPE : null)
        .text(`${it.r.sigla} ${f(it.r.valor_2025)}`);
    }
    const n = rows.find((r) => r.sigla === 'NIPE');
    if (n) svg.append('text').attr('x', xa - 10).attr('y', y(n.valor_2015) + 4).attr('text-anchor', 'end').attr('class', 'lbl-strong').style('fill', COR.NIPE).text(`NIPE ${f(n.valor_2015)}`);
  }

  function drawRank(box, rows) {
    const H = 170;
    const { svg, W } = svgBox(box, H);
    const m = { t: 10, r: 14, b: 22, l: 28 };
    const x = d3.scaleLinear([2015, 2025], [m.l, W - m.r]);
    const y = d3.scaleLinear([1, 23], [m.t, H - m.b]);
    const area = d3.area().x((r) => x(r.ano)).y0(y(1)).y1((r) => y(r.centros));
    svg.append('path').attr('d', area(rows)).attr('fill', cssv('--paper-2'));
    for (const t of [1, 10, 20]) {
      svg.append('line').attr('x1', m.l).attr('x2', W - m.r).attr('y1', y(t)).attr('y2', y(t)).attr('stroke', cssv('--rule')).attr('stroke-dasharray', '2 3');
      svg.append('text').attr('x', m.l - 6).attr('y', y(t) + 4).attr('text-anchor', 'end').text(t + 'º');
    }
    for (const t of [2015, 2020, 2025]) svg.append('text').attr('x', x(t)).attr('y', H - 5).attr('text-anchor', 'middle').text(t);
    svg.append('path').attr('d', d3.line().x((r) => x(r.ano)).y((r) => y(r.posicao))(rows)).attr('fill', 'none').attr('stroke', COR.NIPE).attr('stroke-width', 2.4);
    svg.append('g').selectAll('circle').data(rows).join('circle').attr('cx', (r) => x(r.ano)).attr('cy', (r) => y(r.posicao)).attr('r', 3.5).attr('fill', COR.NIPE)
      .on('pointermove', (event, r) => tip(event, `NIPE · ${r.ano}`, [{ label: 'Posição', value: `${r.posicao}º de ${r.centros}` },
        { label: 'Valor do NIPE', value: fmtInd(r.indicador)(r.valor_nipe) }, { label: 'Mediana COCEN', value: fmtInd(r.indicador)(r.mediana_cocen) }]))
      .on('pointerleave', hideTip);
  }

  /* ---------- baixar cada figura em PNG (mesmo recurso do Data BEPE) ---------- */
  const H2I = 'https://cdn.jsdelivr.net/npm/html-to-image@1.11.11/dist/html-to-image.js';
  let h2iCarga = null;
  const carregaH2I = () => h2iCarga || (h2iCarga = new Promise((ok, erro) => {
    const sc = document.createElement('script');
    sc.src = H2I;
    sc.onload = () => ok(window.htmlToImage);
    sc.onerror = () => { h2iCarga = null; erro(new Error('html-to-image não carregou')); };
    document.head.append(sc);
  }));
  const slug = (t) => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 72).replace(/-+$/, '');
  async function baixaPNG(fig, btn) {
    const rotulo = btn.textContent;
    btn.disabled = true;
    btn.textContent = 'Gerando…';
    const assinatura = el('p', 'fig-assinatura', 'Data NIPE · aikiesan.github.io/data_NIPE');
    fig.append(assinatura);
    try {
      const h2i = await carregaH2I();
      await document.fonts.ready;
      const url = await h2i.toPng(fig, {
        pixelRatio: 2, backgroundColor: getComputedStyle(fig).backgroundColor,
        style: { transition: 'none', animation: 'none', opacity: '1', transform: 'none' },
        filter: (n) => !(n.classList && (n.classList.contains('png') || n.classList.contains('csv') || n.classList.contains('svg'))),
      });
      const cap = fig.querySelector('figcaption');
      const a = el('a');
      a.href = url;
      a.download = 'data-nipe-' + slug(cap ? cap.textContent : 'figura') + '.png';
      document.body.append(a);
      a.click();
      a.remove();
      btn.textContent = rotulo;
    } catch (e) {
      console.error(e);
      btn.textContent = 'Não foi possível gerar';
      setTimeout(() => { btn.textContent = rotulo; }, 3000);
    } finally {
      assinatura.remove();
      btn.disabled = false;
    }
  }
  for (const fig of document.querySelectorAll('figure.fig')) {
    const b = el('button', 'png', 'Figura (PNG)');
    b.type = 'button';
    b.setAttribute('aria-label', 'Baixar esta figura em PNG');
    b.addEventListener('click', () => baixaPNG(fig, b));
    (fig.querySelector('.fig-src') || fig).append(b);
  }

  d3.json('data/nipe.json').then((dados) => {
    D = dados;
    COR = D.paleta;
    preencheTextos();
    if (PAGINA === 'hoje') startHoje();
    else if (PAGINA === 'historico') startHistorico();
    else if (PAGINA === 'comparacao') startComparacao();
  }).catch((e) => {
    console.error(e);
    document.querySelector('main').prepend(el('p', 'wrap fig-note', 'Não foi possível carregar os dados. Recarregue a página.'));
  });
})();
