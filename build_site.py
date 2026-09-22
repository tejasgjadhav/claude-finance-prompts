import re, pathlib, html

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "PROMPTS.md").read_text()
OUT = HERE / "index.html"

KEYS = ["CONTEXT", "ROLE", "ACTION", "FORMAT", "TONE"]


def parse():
    parts = re.split(r'^## (Chapter \d+ — .+)$', SRC, flags=re.M)
    chapters = []
    for i in range(1, len(parts), 2):
        m = re.match(r'Chapter (\d+) — (.+)', parts[i].strip())
        ch, title, body = int(m.group(1)), m.group(2), parts[i + 1]
        prompts = []
        for pm in re.finditer(r'^### PROMPT (\d+) — (.+?)\n+```\n(.*?)\n```',
                              body, flags=re.M | re.S):
            raw = pm.group(3)
            pos = [(k, re.search(r'^%s:' % k, raw, flags=re.M).start()) for k in KEYS]
            layers = []
            for j, (k, s) in enumerate(pos):
                nxt = pos[j + 1][1] if j + 1 < len(pos) else None
                seg = (raw[s + len(k) + 1:nxt] if nxt else raw[s + len(k) + 1:]).rstrip()
                sep = "\n" if seg.startswith("\n") else " "
                layers.append({"k": k, "sep": sep,
                               "t": seg[1:] if sep == " " else seg.lstrip("\n")})
            prompts.append({"n": int(pm.group(1)), "title": pm.group(2).strip(),
                            "layers": layers})
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
nums = sorted(p["n"] for c in chapters for p in c["prompts"])
assert total == 122, total
assert len(chapters) == 15, len(chapters)
assert nums == list(range(1, 123)), "prompt numbering has gaps or duplicates"

chips = "".join(
    '<a class="chip" href="#ch{ch}" data-ch="{ch}"><b>{a}&ndash;{b}</b> {s}</a>'.format(
        ch=c["ch"], s=e(SHORT[c["ch"]]),
        a=c["prompts"][0]["n"], b=c["prompts"][-1]["n"])
    for c in chapters)

blocks = []
for c in chapters:
    ns = [p["n"] for p in c["prompts"]]
    rows = []
    for p in c["prompts"]:
        layers = "".join(
            '<div class="ly"><span class="lk">{k}</span>'
            '<div class="lt" data-k="{k}" data-sep="{sp}">{t}</div></div>'.format(
                k=L["k"], sp="n" if L["sep"] == "\n" else "s", t=e(L["t"]))
            for L in p["layers"])
        rows.append(
            '<article class="entry" id="p{n}">'
            '<a class="num" href="#p{n}">{n}</a>'
            '<div class="head"><h2>{title}</h2>'
            '<button class="copy" type="button">Copy</button></div>'
            '<div class="layers">{layers}</div>'
            '</article>'.format(n=p["n"], title=e(p["title"]), layers=layers))
    blocks.append(
        '<section class="desk" id="ch{ch}" data-ch="{ch}">'
        '<h3 class="divider"><span>Chapter {ch} &middot; {title}</span>'
        '<span class="dnum">{a}&ndash;{b}</span></h3>'
        '{rows}</section>'.format(
            ch=c["ch"], title=e(c["title"]), a=ns[0], b=ns[-1], rows="".join(rows)))

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
:root{
  --paper:#E5EAE0; --card:#F4F7F0;
  --ink:#1A211C; --ink2:#36423A; --muted:#5D6A5B;
  --rule:#C9D1C4; --rule2:#D6DDD0;
  --accent:#8E2F3A; --accent-bg:rgba(142,47,58,.09);
  --ok:#2E6B45;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  --maxw:1000px;
}
@media (prefers-color-scheme:dark){
  :root{
    --paper:#151813; --card:#1C211A;
    --ink:#E4E9DE; --ink2:#C3CCBC; --muted:#8E9A8A;
    --rule:#2C3427; --rule2:#242B20;
    --accent:#D2868D; --accent-bg:rgba(210,134,141,.12);
    --ok:#7FBF97;
  }
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--paper);color:var(--ink);
  font:400 14px/1.6 var(--mono);-webkit-font-smoothing:antialiased;
  overflow-wrap:break-word;
}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}

/* ---------- compact head ---------- */
.mast{padding:24px 0 16px}
h1{font:600 20px/1.25 var(--mono);letter-spacing:-.02em;margin:0 0 8px}
.sub{margin:0 0 6px;color:var(--ink2);font-size:13.5px}
.note{margin:0;color:var(--muted);font-size:12.5px}
.sep{color:var(--muted);margin:0 5px}

/* ---------- sticky bar ---------- */
.bar{position:sticky;top:0;z-index:40;background:var(--paper);border-bottom:1px solid var(--rule)}
.bar-in{max-width:var(--maxw);margin:0 auto;padding:10px 20px 0}
.search{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.sfield{flex:1 1 220px;min-width:0}
#q{
  width:100%;padding:8px 11px;background:var(--card);border:1px solid var(--rule);
  color:var(--ink);border-radius:2px;font:400 13.5px/1.4 var(--mono);
}
#q::placeholder{color:var(--muted)}
.tally{font:600 11.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);white-space:nowrap}
.tally b{color:var(--ink);font-variant-numeric:tabular-nums}
.chips{display:flex;gap:5px;overflow-x:auto;padding:9px 0 10px;scrollbar-width:none;
  -webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 30px),transparent 100%);
  mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 30px),transparent 100%)}
.chips::-webkit-scrollbar{display:none}
.chip{flex:none;text-decoration:none;color:var(--muted);font:500 11.5px/1 var(--mono);
  padding:6px 9px;border:1px solid var(--rule);border-radius:2px;background:var(--card);
  white-space:nowrap}
.chip b{color:var(--ink2);font-weight:600;font-variant-numeric:tabular-nums}
.chip:hover{color:var(--ink);border-color:var(--muted)}
.chip.on{color:var(--accent);border-color:var(--accent);background:var(--accent-bg)}
.chip.on b{color:var(--accent)}

/* ---------- desk divider ---------- */
.desk{scroll-margin-top:104px}
.divider{
  display:flex;justify-content:space-between;align-items:baseline;gap:14px;
  margin:26px 0 0;padding:8px 0 7px;border-top:2px solid var(--ink);
  border-bottom:1px solid var(--rule);
  font:600 11.5px/1.4 var(--mono);letter-spacing:.13em;text-transform:uppercase;
  color:var(--ink);
}
.dnum{color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}

/* ---------- one prompt ---------- */
.entry{
  display:grid;grid-template-columns:54px minmax(0,1fr);
  column-gap:12px;padding:12px 0 14px;border-bottom:1px solid var(--rule2);
  scroll-margin-top:104px;
}
.num{
  grid-column:1;grid-row:1/span 2;text-decoration:none;
  font:700 20px/1.15 var(--mono);color:var(--accent);
  font-variant-numeric:tabular-nums;text-align:right;padding-top:1px;
}
.num:hover{text-decoration:underline}
.head{
  grid-column:2;grid-row:1;display:flex;gap:12px;align-items:baseline;
  justify-content:space-between;margin:0 0 7px;
}
.head h2{font:600 14px/1.35 var(--mono);margin:0;color:var(--ink);min-width:0}
.copy{
  flex:none;font:600 10.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  padding:6px 9px;border:1px solid var(--rule);background:var(--card);
  color:var(--muted);border-radius:2px;cursor:pointer;
}
.copy:hover{border-color:var(--accent);color:var(--accent)}
.copy[data-state="ok"]{border-color:var(--ok);color:var(--ok)}
.copy[data-state="fail"]{border-color:var(--accent);color:var(--accent)}
.layers{grid-column:2;grid-row:2;min-width:0}
.ly{display:grid;grid-template-columns:72px minmax(0,1fr);column-gap:12px;padding:1px 0}
.lk{
  font:600 10px/1.75 var(--mono);letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);padding-top:2px;
}
.lt{font:400 13px/1.6 var(--mono);color:var(--ink2);white-space:pre-wrap;overflow-wrap:anywhere}

.empty{padding:44px 0;color:var(--muted);font-size:14px;display:none}
.empty.on{display:block}
footer{margin:0;padding:22px 0 56px;color:var(--muted);font-size:12.5px}
.top{
  position:fixed;right:14px;bottom:14px;z-index:30;text-decoration:none;
  font:600 10.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  padding:9px 11px;background:var(--ink);color:var(--paper);border-radius:2px;
  opacity:0;pointer-events:none;transition:opacity .18s ease;
}
.top.on{opacity:.94;pointer-events:auto}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

@media (max-width:640px){
  .ly{grid-template-columns:minmax(0,1fr);column-gap:0}
  .lk{line-height:1.5;padding-top:5px}
}
@media (max-width:520px){
  .wrap,.bar-in{padding-left:14px;padding-right:14px}
  .entry{grid-template-columns:38px minmax(0,1fr);column-gap:9px}
  .num{font-size:17px}
  .head h2{font-size:13px}
  .lt{font-size:12.5px}
  .divider{font-size:10.5px;letter-spacing:.1em}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *{transition-duration:.01ms !important;animation-duration:.01ms !important}
}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
"""

JS = r"""
(function(){
  var entries = [].slice.call(document.querySelectorAll('.entry'));
  var desks   = [].slice.call(document.querySelectorAll('.desk'));
  var chips   = [].slice.call(document.querySelectorAll('.chip'));
  var q = document.getElementById('q');
  var tally = document.getElementById('tally');
  var empty = document.getElementById('empty');
  var live = document.getElementById('live');
  var TOTAL = entries.length;

  entries.forEach(function(en){
    var parts = [];
    [].forEach.call(en.querySelectorAll('.lt'), function(el){
      parts.push(el.dataset.k + ':' + (el.dataset.sep === 'n' ? '\n' : ' ') + el.textContent);
    });
    en._raw = parts.join('\n\n');
    en._hay = (en.querySelector('h2').textContent + ' ' +
               en.querySelector('.num').textContent + ' ' + en._raw).toLowerCase();
  });

  function run(){
    var t = q.value.trim().toLowerCase(), shown = 0;
    entries.forEach(function(en){
      var hit = !t || en._hay.indexOf(t) !== -1;
      en.hidden = !hit;
      if (hit) shown++;
    });
    desks.forEach(function(d){ d.hidden = !d.querySelector('.entry:not([hidden])'); });
    tally.innerHTML = '<b>' + shown + '</b> of <b>' + TOTAL + '</b>';
    empty.classList.toggle('on', shown === 0);
    live.textContent = shown + ' of ' + TOTAL + ' prompts shown';
  }
  var timer;
  q.addEventListener('input', function(){ clearTimeout(timer); timer = setTimeout(run, 110); });
  q.addEventListener('keydown', function(ev){ if (ev.key === 'Escape'){ q.value=''; run(); } });
  run();

  function legacy(text){
    var ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly','');
    ta.style.cssText = 'position:fixed;top:0;left:-9999px;opacity:0';
    document.body.appendChild(ta);
    var sel = document.getSelection();
    var prev = sel.rangeCount ? sel.getRangeAt(0) : null;
    ta.select(); ta.setSelectionRange(0, ta.value.length);
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    if (prev){ sel.removeAllRanges(); sel.addRange(prev); }
    return ok;
  }
  function settle(btn, ok){
    btn.dataset.state = ok ? 'ok' : 'fail';
    btn.textContent = ok ? 'Copied' : 'Press ⌘C';
    if (!ok){
      var r = document.createRange();
      r.selectNodeContents(btn.closest('.entry').querySelector('.layers'));
      var s = document.getSelection(); s.removeAllRanges(); s.addRange(r);
    }
    live.textContent = ok ? 'Prompt copied to clipboard'
      : 'Copy blocked by the browser. Prompt text selected — press Command or Control C.';
    clearTimeout(btn._t);
    btn._t = setTimeout(function(){ btn.removeAttribute('data-state'); btn.textContent = 'Copy'; }, 2200);
  }
  document.addEventListener('click', function(ev){
    var btn = ev.target.closest('.copy');
    if (!btn) return;
    var text = btn.closest('.entry')._raw;
    if (navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(function(){ settle(btn,true); },
                                               function(){ settle(btn, legacy(text)); });
    } else { settle(btn, legacy(text)); }
  });

  if ('IntersectionObserver' in window){
    var seen = {};
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){ seen[en.target.dataset.ch] = en.isIntersecting ? en.intersectionRect.top : null; });
      var best = null;
      desks.forEach(function(d){
        var v = seen[d.dataset.ch];
        if (v === null || v === undefined) return;
        if (best === null || v < seen[best]) best = d.dataset.ch;
      });
      chips.forEach(function(c){ c.classList.toggle('on', c.dataset.ch === best); });
    }, { rootMargin: '-104px 0px -55% 0px', threshold: 0 });
    desks.forEach(function(d){ io.observe(d); });
  }

  var top = document.getElementById('top');
  window.addEventListener('scroll', function(){
    top.classList.toggle('on', window.scrollY > 1200);
  }, { passive: true });
})();
"""

page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Prompt Repository &mdash; %(total)d finance prompts, 1 to %(total)d</title>
<meta name="description" content="A free repository of %(total)d finance prompts, numbered 1 to %(total)d, each in its five CRAFT layers.">
<meta name="color-scheme" content="light dark">
<style>%(css)s</style>
</head>
<body>
<div class="sr" id="live" role="status" aria-live="polite"></div>

<div class="wrap">
  <header class="mast">
    <h1>The Prompt Repository &mdash; prompts 1 to %(total)d</h1>
    <p class="sub">%(total)d finance prompts, in full. Each one is numbered, so prompt 47 stays prompt 47 wherever you reference it.</p>
    <p class="note">CRAFT is the framework used on this page. It is not Anthropic&rsquo;s and it is not in the model documentation.</p>
  </header>
</div>

<nav class="bar" aria-label="Desks and search">
  <div class="bar-in">
    <div class="search">
      <div class="sfield">
        <label class="sr" for="q">Search prompts</label>
        <input id="q" type="search" autocomplete="off" spellcheck="false"
               placeholder="Search all %(total)d prompts">
      </div>
      <p class="tally" id="tally"><b>%(total)d</b> of <b>%(total)d</b></p>
    </div>
    <div class="chips">%(chips)s</div>
  </div>
</nav>

<main class="wrap">
%(blocks)s
  <p class="empty" id="empty">No prompt matches that.</p>
  <footer>%(total)d prompts, %(nch)d desks, five layers each. Free to use and adapt. Not investment advice.</footer>
</main>

<a class="top" id="top" href="#">Top</a>
<script>%(js)s</script>
</body>
</html>
""" % {"css": CSS, "js": JS, "total": total, "nch": len(chapters),
       "chips": chips, "blocks": "\n".join(blocks)}

OUT.write_text(page)
print("wrote %s: %d prompts (1-%d), %d chapters, %d bytes"
      % (OUT.name, total, nums[-1], len(chapters), len(page)))
