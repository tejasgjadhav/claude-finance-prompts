import re, json, pathlib, html

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "PROMPTS.md").read_text()
OUT = HERE / "index.html"

KEYS = ["CONTEXT", "ROLE", "ACTION", "FORMAT", "TONE"]

def parse():
    parts = re.split(r'^## (Chapter \d+ — .+)$', SRC, flags=re.M)
    chapters = []
    for i in range(1, len(parts), 2):
        m = re.match(r'Chapter (\d+) — (.+)', parts[i].strip())
        ch, title, body = int(m.group(1)), m.group(2), parts[i+1]
        prompts = []
        for pm in re.finditer(r'^### PROMPT (\d+) — (.+?)\n+```\n(.*?)\n```', body, flags=re.M | re.S):
            raw = pm.group(3)
            pos = []
            for k in KEYS:
                mm = re.search(r'^%s:' % k, raw, flags=re.M)
                pos.append((k, mm.start()))
            layers = []
            for j, (k, s) in enumerate(pos):
                nxt = pos[j+1][1] if j+1 < len(pos) else None
                seg = (raw[s+len(k)+1:nxt] if nxt else raw[s+len(k)+1:]).rstrip()
                sep = "\n" if seg.startswith("\n") else " "
                layers.append({"k": k, "sep": sep,
                               "t": seg[1:] if sep == " " else seg.lstrip("\n")})
            prompts.append({"n": int(pm.group(1)), "title": pm.group(2).strip(), "layers": layers})
        chapters.append({"ch": ch, "title": title, "prompts": prompts})
    return chapters

SHORT = {
    2: "Equity Research", 3: "M&A Valuation", 4: "Macro Risk", 5: "Earnings Intel",
    6: "Portfolio Strategy", 7: "Quant Trading", 8: "Strategy Consulting",
    9: "Endowment", 10: "Sovereign Wealth", 11: "ESG & Climate",
    12: "Fixed Income", 13: "Claude Models", 14: "Claude.ai", 15: "Claude Code",
    16: "Cowork & MCP",
}

e = html.escape
chapters = parse()
total = sum(len(c["prompts"]) for c in chapters)
assert total == 122, total
assert len(chapters) == 15

# ---------- nav chips ----------
chips = "".join(
    '<a class="chip" href="#ch{ch}" data-ch="{ch}"><b>{ch:02d}</b> {s}</a>'.format(
        ch=c["ch"], s=e(SHORT[c["ch"]]))
    for c in chapters)

# ---------- prompt sections ----------
secs = []
for c in chapters:
    ns = [p["n"] for p in c["prompts"]]
    cards = []
    for p in c["prompts"]:
        rows = []
        for L in p["layers"]:
            rows.append(
                '<b class="gl" aria-hidden="true">{i}</b>'
                '<div class="ly"><span class="lk">{k}</span>'
                '<div class="lt" data-k="{k}" data-sep="{sp}">{t}</div></div>'.format(
                    i=L["k"][0], k=L["k"],
                    sp="n" if L["sep"] == "\n" else "s",
                    t=e(L["t"])))
        cards.append(
            '<article class="card" id="p{n}">'
            '<div class="chd">'
            '<div class="cid"><a class="pn" href="#p{n}">Prompt {n}</a>'
            '<h3>{title}</h3></div>'
            '<button class="copy" type="button">Copy prompt</button>'
            '</div>'
            '<div class="craft">{rows}</div>'
            '</article>'.format(n=p["n"], title=e(p["title"]), rows="".join(rows)))
    secs.append(
        '<section class="desk" id="ch{ch}" data-ch="{ch}">'
        '<header class="dh">'
        '<p class="eyebrow">Chapter {ch}</p>'
        '<h2>{title}</h2>'
        '<p class="drange">Prompts {a}&ndash;{b} <span>&middot;</span> {cnt} prompts</p>'
        '</header>{cards}</section>'.format(
            ch=c["ch"], title=e(c["title"]), a=ns[0], b=ns[-1],
            cnt=len(ns), cards="".join(cards)))

BAD = '"What’s our portfolio risk? Be detailed."'
GOOD = """Portfolio attached (32 positions, weights in column C). Run a 2022-style
rate-shock stress test: +300bps parallel shift, equity-bond correlation
+0.6. Output: loss in dollars by position, top 5 contributors, one hedge
recommendation with cost. Format: one table + 5 lines. BCE language only."""

FAILURES = [
    ("Too long, or carrying sections you never asked for.",
     "Format was vague. You wrote an adjective where a noun belonged."),
    ("Hedges everything, commits to nothing.",
     "The Role was too junior, or Tone never said who reads this."),
    ("Confident and wrong on a number.",
     "Action ran a multi-step calculation with no validation step under it."),
    ("Ignores a constraint you definitely stated.",
     "The constraint sat in Action, where it reads as one instruction among nine. "
     "Move it to Context, where it reads as a fact of the workspace."),
    ("Answers a different question.",
     "Context was missing the thing you assumed was obvious."),
]
frows = "".join('<tr><td>{a}</td><td>{b}</td></tr>'.format(a=e(a), b=e(b)) for a, b in FAILURES)

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
:root{
  --paper:#E5EAE0; --card:#F4F7F0; --well:#EBEFE6;
  --ink:#1A211C; --ink2:#36423A; --muted:#5D6A5B;
  --rule:#C9D1C4; --rule2:#D8DFD3;
  --accent:#8E2F3A; --accent-bg:rgba(142,47,58,.09);
  --rail:#DEE4D8; --rail-ink:#7C8A79;
  --term-bg:#18201B; --term-fg:#D8E1D4; --term-dim:#8DA089;
  --ok:#2E6B45;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  --serif:"Iowan Old Style",Charter,Georgia,"Times New Roman",serif;
  --shadow:0 1px 0 rgba(26,33,28,.04);
  --maxw:960px;
}
@media (prefers-color-scheme:dark){
  :root{
    --paper:#151813; --card:#1C211A; --well:#191E17;
    --ink:#E4E9DE; --ink2:#C3CCBC; --muted:#8E9A8A;
    --rule:#2C3427; --rule2:#242B20;
    --accent:#D2868D; --accent-bg:rgba(210,134,141,.12);
    --rail:#232A21; --rail-ink:#93A08E;
    --term-bg:#080A07; --term-fg:#D8E1D4; --term-dim:#8DA089;
    --ok:#7FBF97;
    --shadow:none;
  }
  .good pre{border-color:var(--rule)}
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font:400 17px/1.62 var(--serif);
  -webkit-font-smoothing:antialiased;
  overflow-wrap:break-word;
}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}

/* ---------- masthead ---------- */
.mast{padding:56px 0 34px;border-bottom:1px solid var(--rule)}
.kicker{
  font:600 11.5px/1 var(--mono);letter-spacing:.19em;text-transform:uppercase;
  color:var(--muted);margin:0 0 22px;
}
.kicker b{color:var(--accent);font-weight:600}
h1{
  font:600 clamp(30px,7vw,52px)/1.04 var(--mono);
  letter-spacing:-.035em;margin:0 0 18px;
}
.lede{font-size:clamp(17px,2.3vw,19px);color:var(--ink2);margin:0 0 12px;max-width:54ch}
.lede-2{font-size:16px;color:var(--muted);margin:0;max-width:62ch}
.flag{
  margin:26px 0 0;padding:14px 17px;background:var(--card);
  border:1px solid var(--rule);border-left:2px solid var(--accent);
  font:400 14px/1.6 var(--mono);color:var(--ink2);max-width:62ch;
}
.mast-grid{display:grid;gap:34px;align-items:start}
@media (min-width:940px){
  .mast-grid{grid-template-columns:minmax(0,1.15fr) minmax(300px,.85fr);gap:52px}
  .flag{margin-top:22px}
}
.legend{min-width:0}
.legend-h{
  font:600 11px/1 var(--mono);letter-spacing:.19em;text-transform:uppercase;
  color:var(--muted);margin:0 0 12px;
}
.legend .craft{
  border:1px solid var(--rule);border-radius:3px;background:var(--card);
  overflow:hidden;
}
.legend .lt{font:400 13px/1.55 var(--serif);white-space:normal}
.legend .ly{padding:11px 15px 12px}
.legend .gl{padding-top:13px}

/* ---------- contrast block ---------- */
.contrast{padding:46px 0 40px;border-bottom:1px solid var(--rule)}
.eyebrow{
  font:600 11.5px/1 var(--mono);letter-spacing:.19em;text-transform:uppercase;
  color:var(--accent);margin:0 0 12px;
}
h2{font:600 clamp(21px,3.6vw,29px)/1.18 var(--mono);letter-spacing:-.025em;margin:0 0 10px}
.pair{display:grid;gap:20px;margin:26px 0 0}
@media (min-width:800px){.pair{grid-template-columns:1fr 1fr;gap:24px}}
.spec{display:flex;flex-direction:column;min-width:0}
.spec-h{
  font:600 11.5px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;
  margin:0 0 10px;display:flex;align-items:baseline;gap:9px;
}
.spec-h .tag{
  font-size:10.5px;letter-spacing:.1em;padding:3px 7px;border-radius:2px;
  background:var(--rule2);color:var(--muted);
}
.bad .spec-h{color:var(--muted)}
.good .spec-h{color:var(--accent)}
.good .spec-h .tag{background:var(--accent-bg);color:var(--accent)}
pre{
  margin:0;font:400 13.5px/1.62 var(--mono);
  white-space:pre-wrap;overflow-wrap:anywhere;
}
.bad pre{
  background:var(--well);border:1px solid var(--rule);border-left:2px solid var(--rule);
  padding:16px 17px;color:var(--muted);
}
.good pre{
  background:var(--term-bg);color:var(--term-fg);border:1px solid var(--term-bg);
  border-left:2px solid var(--accent);padding:16px 17px;
}
.spec figcaption{
  font-size:15px;color:var(--muted);margin:11px 0 0;line-height:1.5;
}
.changed{margin:30px 0 0;padding:0;list-style:none;display:grid;gap:0;max-width:74ch}
.changed li{
  padding:11px 0 11px 0;border-top:1px solid var(--rule2);
  font-size:16px;color:var(--ink2);
  display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:baseline;
}
.changed li:last-child{border-bottom:1px solid var(--rule2)}
.changed .ck{
  font:600 10.5px/1.6 var(--mono);letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);min-width:66px;
}
details.diag{margin:28px 0 0;border-top:1px solid var(--rule2);padding-top:16px}
details.diag summary{
  cursor:pointer;font:600 12px/1 var(--mono);letter-spacing:.13em;
  text-transform:uppercase;color:var(--muted);list-style:none;
  display:flex;align-items:center;gap:9px;
}
details.diag summary::-webkit-details-marker{display:none}
details.diag summary::before{content:"+";color:var(--accent);font-size:15px;line-height:1}
details.diag[open] summary::before{content:"\2212"}
details.diag summary:hover{color:var(--ink)}
.tw{overflow-x:auto;margin:16px 0 0;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;min-width:420px;font-size:15px}
td{border-top:1px solid var(--rule2);padding:11px 14px 11px 0;vertical-align:top;color:var(--ink2)}
td:first-child{width:42%;color:var(--ink);padding-right:22px}

/* ---------- sticky nav ---------- */
.bar{
  position:sticky;top:0;z-index:40;background:var(--paper);
  border-bottom:1px solid var(--rule);
}
.bar-in{max-width:var(--maxw);margin:0 auto;padding:12px 20px 0}
.search{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.sfield{position:relative;flex:1 1 240px;min-width:0}
.sfield::before{
  content:"";position:absolute;left:12px;top:50%;width:11px;height:11px;
  margin-top:-7px;border:1.5px solid var(--muted);border-radius:50%;
}
.sfield::after{
  content:"";position:absolute;left:21px;top:50%;width:6px;height:1.5px;
  margin-top:3px;background:var(--muted);transform:rotate(45deg);
}
#q{
  width:100%;padding:10px 13px 10px 33px;background:var(--card);
  border:1px solid var(--rule);color:var(--ink);border-radius:3px;
  font:400 14.5px/1.4 var(--mono);
}
#q::placeholder{color:var(--muted)}
.tally{
  font:600 11.5px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);white-space:nowrap;
}
.tally b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums}
.chips{
  display:flex;gap:6px;overflow-x:auto;padding:11px 0 12px;
  scrollbar-width:none;-webkit-overflow-scrolling:touch;
  -webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 34px),transparent 100%);
  mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 34px),transparent 100%);
}
.chips::-webkit-scrollbar{display:none}
.chip{
  flex:none;text-decoration:none;color:var(--muted);
  font:500 12px/1 var(--mono);letter-spacing:.04em;
  padding:7px 11px;border:1px solid var(--rule);border-radius:2px;
  background:var(--card);white-space:nowrap;
}
.chip b{color:var(--rail-ink);font-weight:600;margin-right:5px;font-variant-numeric:tabular-nums}
.chip:hover{color:var(--ink);border-color:var(--rail-ink)}
.chip.on{color:var(--accent);border-color:var(--accent);background:var(--accent-bg)}
.chip.on b{color:var(--accent)}

/* ---------- desks ---------- */
.desk{padding:52px 0 4px;scroll-margin-top:118px}
.dh{margin:0 0 26px;padding-bottom:14px;border-bottom:2px solid var(--ink)}
.dh h2{margin:0 0 8px}
.drange{
  font:500 12px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);margin:0;font-variant-numeric:tabular-nums;
}
.drange span{color:var(--rule)}

/* ---------- prompt card ---------- */
.card{
  background:var(--card);border:1px solid var(--rule);border-radius:3px;
  margin:0 0 18px;box-shadow:var(--shadow);overflow:hidden;scroll-margin-top:118px;
}
.chd{
  display:flex;gap:14px;align-items:flex-start;justify-content:space-between;
  padding:15px 17px 14px;
}
.cid{min-width:0}
.pn{
  display:inline-block;text-decoration:none;
  font:600 11px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);margin:0 0 7px;font-variant-numeric:tabular-nums;
}
.pn:hover{text-decoration:underline}
.card h3{
  font:600 15.5px/1.35 var(--mono);letter-spacing:-.015em;
  margin:0;color:var(--ink);
}
.copy{
  flex:none;font:600 11.5px/1 var(--mono);letter-spacing:.11em;text-transform:uppercase;
  padding:9px 13px;border:1px solid var(--rule);background:var(--paper);
  color:var(--ink2);border-radius:2px;cursor:pointer;
}
.copy:hover{border-color:var(--accent);color:var(--accent)}
.copy[data-state="ok"]{border-color:var(--ok);color:var(--ok)}
.copy[data-state="fail"]{border-color:var(--accent);color:var(--accent)}

/* the CRAFT rail — the signature */
.craft{display:grid;grid-template-columns:38px 1fr;border-top:1px solid var(--rule)}
.gl{
  grid-column:1;background:var(--rail);border-right:1px solid var(--rule);
  border-top:1px solid var(--rule2);
  font:700 13.5px/1 var(--mono);color:var(--rail-ink);letter-spacing:.02em;
  display:flex;justify-content:center;padding:15px 0 0;
}
.ly{
  grid-column:2;border-top:1px solid var(--rule2);
  padding:13px 17px 15px;min-width:0;background:var(--card);
}
.craft > .gl:first-child,.craft > .gl:first-child + .ly{border-top:0}
.lk{
  display:block;font:600 10.5px/1 var(--mono);letter-spacing:.19em;
  text-transform:uppercase;color:var(--muted);margin:0 0 8px;
}
.lt{
  font:400 13.5px/1.66 var(--mono);color:var(--ink2);
  white-space:pre-wrap;overflow-wrap:anywhere;
}

/* ---------- misc ---------- */
.empty{padding:60px 0;text-align:center;color:var(--muted);font-size:17px;display:none}
.empty.on{display:block}
.book{
  margin:56px 0 0;padding:26px 0 0;border-top:2px solid var(--ink);
  display:grid;gap:18px;
}
@media (min-width:720px){.book{grid-template-columns:1fr auto;align-items:center;gap:30px}}
.book h2{margin:0 0 8px;font-size:clamp(19px,3vw,24px)}
.book p{margin:0;color:var(--muted);font-size:16px;max-width:52ch}
.btn{
  display:inline-block;text-decoration:none;white-space:nowrap;
  font:600 12px/1 var(--mono);letter-spacing:.13em;text-transform:uppercase;
  padding:14px 20px;background:var(--ink);color:var(--paper);border-radius:2px;
}
.btn:hover{background:var(--accent);color:#fff}
footer{
  margin:44px 0 0;padding:22px 0 60px;border-top:1px solid var(--rule);
  color:var(--muted);font-size:15px;
}
footer p{margin:0 0 8px}
.top{
  position:fixed;right:16px;bottom:16px;z-index:30;text-decoration:none;
  font:600 11px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;
  padding:11px 13px;background:var(--ink);color:var(--paper);border-radius:2px;
  opacity:0;pointer-events:none;transition:opacity .18s ease;
}
.top.on{opacity:.94;pointer-events:auto}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

@media (max-width:520px){
  .wrap,.bar-in{padding-left:16px;padding-right:16px}
  .mast{padding-top:36px}
  .craft{grid-template-columns:28px 1fr}
  .gl{font-size:11.5px;padding-top:13px}
  .ly{padding:11px 13px 13px}
  .lt{font-size:12.5px;line-height:1.62}
  .chd{padding:13px 13px 12px;gap:10px}
  .copy{padding:8px 10px;font-size:10.5px;letter-spacing:.08em}
  .card h3{font-size:14px}
  .bad pre,.good pre{padding:13px 14px;font-size:12.5px}
  .changed li{grid-template-columns:1fr;gap:3px}
  .desk{scroll-margin-top:104px}
  .card{scroll-margin-top:104px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{transition-duration:.01ms !important;animation-duration:.01ms !important}
}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
"""

JS = r"""
(function(){
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var desks = Array.prototype.slice.call(document.querySelectorAll('.desk'));
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var q = document.getElementById('q');
  var tally = document.getElementById('tally');
  var empty = document.getElementById('empty');
  var live = document.getElementById('live');
  var TOTAL = cards.length;

  /* ---- raw text for copy, haystack for search ---- */
  cards.forEach(function(c){
    var parts = [];
    Array.prototype.forEach.call(c.querySelectorAll('.lt'), function(el){
      parts.push(el.dataset.k + ':' + (el.dataset.sep === 'n' ? '\n' : ' ') + el.textContent);
    });
    c._raw = parts.join('\n\n');
    c._hay = (c.querySelector('h3').textContent + ' ' +
              c.querySelector('.pn').textContent + ' ' + c._raw).toLowerCase();
  });

  /* ---- search ---- */
  function run(){
    var t = q.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function(c){
      var hit = !t || c._hay.indexOf(t) !== -1;
      c.hidden = !hit;
      if (hit) shown++;
    });
    desks.forEach(function(d){
      var any = d.querySelector('.card:not([hidden])');
      d.hidden = !any;
    });
    tally.innerHTML = '<b>' + shown + '</b> of <b>' + TOTAL + '</b> prompts';
    empty.classList.toggle('on', shown === 0);
    live.textContent = shown + ' of ' + TOTAL + ' prompts shown';
  }
  var timer;
  q.addEventListener('input', function(){
    clearTimeout(timer); timer = setTimeout(run, 110);
  });
  q.addEventListener('keydown', function(ev){
    if (ev.key === 'Escape') { q.value = ''; run(); }
  });
  run();

  /* ---- copy with fallback ---- */
  function legacy(text){
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly','');
    ta.style.cssText = 'position:fixed;top:0;left:-9999px;opacity:0';
    document.body.appendChild(ta);
    var sel = document.getSelection();
    var prev = sel.rangeCount ? sel.getRangeAt(0) : null;
    ta.select();
    ta.setSelectionRange(0, ta.value.length);
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    if (prev) { sel.removeAllRanges(); sel.addRange(prev); }
    return ok;
  }
  function settle(btn, ok){
    btn.dataset.state = ok ? 'ok' : 'fail';
    btn.textContent = ok ? 'Copied' : 'Press ⌘C';
    if (!ok) {
      var c = btn.closest('.card');
      var r = document.createRange();
      r.selectNodeContents(c.querySelector('.craft'));
      var s = document.getSelection();
      s.removeAllRanges(); s.addRange(r);
    }
    live.textContent = ok ? 'Prompt copied to clipboard'
                          : 'Copy blocked by the browser. Prompt text selected — press Command or Control C.';
    clearTimeout(btn._t);
    btn._t = setTimeout(function(){
      btn.removeAttribute('data-state');
      btn.textContent = 'Copy prompt';
    }, 2400);
  }
  document.addEventListener('click', function(ev){
    var btn = ev.target.closest('.copy');
    if (!btn) return;
    var text = btn.closest('.card')._raw;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function(){ settle(btn, true); },
                                               function(){ settle(btn, legacy(text)); });
    } else {
      settle(btn, legacy(text));
    }
  });

  /* ---- active chip ---- */
  var byCh = {};
  chips.forEach(function(c){ byCh[c.dataset.ch] = c; });
  if ('IntersectionObserver' in window) {
    var seen = {};
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ seen[en.target.dataset.ch] = en.isIntersecting ? en.intersectionRect.top : null; });
      var best = null;
      desks.forEach(function(d){
        var v = seen[d.dataset.ch];
        if (v === null || v === undefined) return;
        if (best === null || v < seen[best]) best = d.dataset.ch;
      });
      chips.forEach(function(c){ c.classList.toggle('on', c.dataset.ch === best); });
    }, { rootMargin: '-118px 0px -55% 0px', threshold: 0 });
    desks.forEach(function(d){ io.observe(d); });
  }

  /* ---- back to top ---- */
  var top = document.getElementById('top');
  window.addEventListener('scroll', function(){
    top.classList.toggle('on', window.scrollY > 1400);
  }, { passive: true });
})();
"""

changed = [
    ("Context", "The portfolio state, its size and where the weights live — none of which the model could infer."),
    ("Role", "Not stated in the bad prompt at all, so the model picked its own seniority."),
    ("Action", "The vague noun “risk” became one named scenario with two parameters."),
    ("Format", "“Detailed” became an exact deliverable: one table plus five lines."),
    ("Tone", "“BCE language only” — Base Case Estimate, not advice."),
]
clist = "".join('<li><span class="ck">{k}</span><span>{v}</span></li>'.format(k=e(k), v=e(v))
                for k, v in changed)

legend_rows = [
    ("Context", "What is already on the desk, and where the answer goes afterwards."),
    ("Role", "Who the model answers as, and at what seniority."),
    ("Action", "The work itself, written as numbered steps."),
    ("Format", "The exact deliverable. Named sheets, named columns, a line count."),
    ("Tone", "The register, and what the answer is not allowed to claim."),
]
legend = "".join(
    '<b class="gl" aria-hidden="true">{i}</b>'
    '<div class="ly"><span class="lk">{k}</span><div class="lt">{v}</div></div>'.format(
        i=k[0].upper(), k=e(k.upper()), v=e(v))
    for k, v in legend_rows)

page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Prompt Repository &mdash; 122 finance prompts in full CRAFT</title>
<meta name="description" content="All 122 prompts from Claude AI for Finance Professionals, free and in full. Every prompt shows its five CRAFT layers: Context, Role, Action, Format, Tone.">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="The Prompt Repository — 122 finance prompts in full CRAFT">
<meta property="og:description" content="All 122 prompts from Claude AI for Finance Professionals, free and in full.">
<meta property="og:type" content="website">
<style>%(css)s</style>
</head>
<body>
<div class="sr" id="live" role="status" aria-live="polite"></div>

<div class="wrap">
  <header class="mast">
    <p class="kicker">Companion to the book &nbsp;<b>/</b>&nbsp; free &nbsp;<b>/</b>&nbsp; no sign-up</p>
    <div class="mast-grid">
      <div>
        <h1>The Prompt<br>Repository</h1>
        <p class="lede">All %(total)d prompts from <em>Claude AI for Finance Professionals</em>, in full, across %(nch)d desks. Every one is printed with its five layers intact.</p>
        <p class="lede-2">Numbering matches the book exactly. Prompt 47 here is Prompt 47 there.</p>
        <p class="flag">CRAFT is this book&rsquo;s framework. It is not Anthropic&rsquo;s, and it is not in the model documentation, so there is no point looking for it there.</p>
      </div>
      <aside class="legend">
        <p class="legend-h">The five layers, every time</p>
        <div class="craft">%(legend)s</div>
      </aside>
    </div>
  </header>

  <section class="contrast">
    <p class="eyebrow">Why the layers are there</p>
    <h2>A bad prompt, then a good one</h2>
    <p class="lede">Same analyst, same portfolio, same afternoon. The difference is how many decisions the model was left to make on its own.</p>

    <div class="pair">
      <figure class="spec bad">
        <figcaption class="spec-h">Before <span class="tag">11 words</span></figcaption>
        <pre>%(bad)s</pre>
        <figcaption>It does not say which risk: rate, credit, currency or concentration. It does not say detailed relative to what. It does not give the portfolio state or the date. It does not say whether the answer should be prose, a table or a number. The model answers anyway, guessing each of those silently.</figcaption>
      </figure>
      <figure class="spec good">
        <figcaption class="spec-h">After <span class="tag">every layer answered</span></figcaption>
        <pre>%(good)s</pre>
        <figcaption>Adjectives like detailed, thorough and professional ask the model to decide for you. Nouns and numbers are decisions already made.</figcaption>
      </figure>
    </div>

    <ul class="changed">%(clist)s</ul>

    <details class="diag">
      <summary>When a prompt fails, read the failure first</summary>
      <div class="tw">
        <table>
          <caption class="sr">What came back, and which CRAFT layer caused it</caption>
          <tbody>%(frows)s</tbody>
        </table>
      </div>
      <p class="lede-2" style="margin-top:16px">Then change one layer. Change three at once and you learn nothing about which one mattered.</p>
    </details>
  </section>
</div>

<nav class="bar" aria-label="Desks and search">
  <div class="bar-in">
    <div class="search">
      <div class="sfield">
        <label class="sr" for="q">Search prompts</label>
        <input id="q" type="search" autocomplete="off" spellcheck="false"
               placeholder="Search titles and prompt text — try &quot;stress test&quot;">
      </div>
      <p class="tally" id="tally"><b>%(total)d</b> of <b>%(total)d</b> prompts</p>
    </div>
    <div class="chips">%(chips)s</div>
  </div>
</nav>

<main class="wrap">
%(secs)s
  <p class="empty" id="empty">No prompt matches that. Try a desk name, a method, or a single word like <em>hedge</em>.</p>

  <section class="book">
    <div>
      <h2>Where these came from</h2>
      <p>Every prompt here is reproduced in full from <em>Claude AI for Finance Professionals</em>. The book is the part this page is not: the reasoning behind each layer, the walkthroughs, and what to do when the output is wrong.</p>
    </div>
    <a class="btn" href="https://www.amazon.com/dp/B0GSX73KF6" rel="noopener">The book on Amazon</a>
  </section>

  <footer>
    <p>Free to use, adapt and paste into your own workflow. Nothing here is investment advice, and every bracketed placeholder is yours to fill.</p>
    <p>%(total)d prompts &middot; %(nch)d desks &middot; five layers each.</p>
  </footer>
</main>

<a class="top" id="top" href="#">Top</a>
<script>%(js)s</script>
</body>
</html>
""" % {"css": CSS, "js": JS, "total": total, "nch": len(chapters),
       "bad": e(BAD), "good": e(GOOD), "clist": clist, "frows": frows, "legend": legend,
       "chips": chips, "secs": "\n".join(secs)}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(page)
print("wrote", OUT, len(page), "bytes;", total, "prompts,", len(chapters), "chapters")
