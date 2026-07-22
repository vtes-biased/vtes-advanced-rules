// Rewrites the document's shorthand into krcg-wired markup, in one text-node pass:
//   {Card Name}  -> <span class="krcg-card">Card Name</span>   (krcg.js adds the image modal)
//   [pot] [ACTION] -> <span class="krcg-icon">glyph</span>     (Ankha font, via krcg.css)
// Runs before krcg.js (which binds on window `load`); text inside code/links is left alone.
(function () {
  // Ankha glyph map — copied from krcg's krcg-blogger.js (icon_map). Discipline codes are
  // case-sensitive (lower = inferior, upper = superior); card types match case-insensitively.
  var ICON = {
    "aus":"a","obe":"b","cel":"c","dom":"d","dem":"e","for":"f","san":"g","thn":"h","ani":"i",
    "pro":"j","chi":"k","val":"l","mel":"m","nec":"n","obf":"o","pot":"p","qui":"q","pre":"r",
    "ser":"s","tha":"t","vis":"u","vic":"v","abo":"w","myt":"x","dai":"y","spi":"z",
    "AUS":"A","OBE":"B","CEL":"C","DOM":"D","DEM":"E","FOR":"F","SAN":"G","THN":"H","ANI":"I",
    "PRO":"J","CHI":"K","VAL":"L","MEL":"M","NEC":"N","OBF":"O","POT":"P","QUI":"Q","PRE":"R",
    "SER":"S","THA":"T","VIS":"U","VIC":"V","ABO":"W","MYT":"X","DAI":"Y","SPI":"Z",
    "tem":"?","TEM":"!","str":"à","STR":"á","obt":"$","OBT":"£","mal":"â","MAL":"ã",
    "conviction":"¤","action":"0","political":"2","politics":"2","politic":"2","political action":"2",
    "ally":"3","recruit":"3","equipment":"5","equip":"5","retainer":"8","employ":"8","reaction":"7",
    "react":"7","action modifier":"1","modifier":"1","mod":"1","combat":"4","reflex":"6","flight":"^",
    "merged":"µ ","merge":"µ ","advanced":"|","advance":"|","adv":"|","event":"[","power":"§",
    "innocence":"#","inn":"#","defense":"@","def":"@","martyrdom":"&","mar":"&","justice":"%","jus":"%",
    "vengeance":"(","ven":"(","vision":")","vin":")","redemption":"*","red":"*"
  };
  function iconGlyph(tok) {
    if (Object.prototype.hasOwnProperty.call(ICON, tok)) return ICON[tok];        // exact: pot / POT
    var lo = tok.toLowerCase();
    return Object.prototype.hasOwnProperty.call(ICON, lo) ? ICON[lo] : null;      // ACTION -> action
  }

  var SKIP = { CODE:1, PRE:1, A:1, SCRIPT:1, STYLE:1 };
  var TOKEN = /\{([^}]+)\}|\[([^\]]+)\]/g;

  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: function (n) {
      var v = n.nodeValue;
      if (v.indexOf("{") < 0 && v.indexOf("[") < 0) return NodeFilter.FILTER_REJECT;
      for (var p = n.parentNode; p; p = p.parentNode)
        if (SKIP[p.nodeName]) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = [], n;
  while ((n = walker.nextNode())) nodes.push(n);

  for (var i = 0; i < nodes.length; i++) {
    var node = nodes[i], text = node.nodeValue, frag = document.createDocumentFragment();
    var last = 0, m, changed = false;
    TOKEN.lastIndex = 0;
    while ((m = TOKEN.exec(text))) {
      var repl = null;
      if (m[1] != null) {                                   // {Card Name}
        repl = document.createElement("span");
        repl.className = "krcg-card";
        repl.textContent = m[1];
      } else {                                              // [icon] — only if it maps
        var g = iconGlyph(m[2]);
        if (g != null) {
          repl = document.createElement("span");
          repl.className = "krcg-icon";
          repl.textContent = g;
        }
      }
      if (repl == null) continue;                           // unknown [token]: leave literal
      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      frag.appendChild(repl);
      last = TOKEN.lastIndex;
      changed = true;
    }
    if (!changed) continue;
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  }
})();
