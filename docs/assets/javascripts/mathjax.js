// Configurazione MathJax per pymdownx.arithmatex (generic), secondo la
// documentazione Zensical (authoring/math). Delimitatori: \( \) inline, \[ \] blocco.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Ricomposizione delle formule a ogni cambio di pagina e nelle annotazioni.
document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})

component$.subscribe(({ ref }) => {
  if (ref.classList.contains("md-annotation"))
    MathJax.typesetPromise([ref])
})
