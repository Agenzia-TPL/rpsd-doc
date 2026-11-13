# Bozze di issue per Zensical

Problemi emersi dallo spike di `bootstrap-site` (Zensical 0.1.1, `zensical-ui` 0.0.42,
Python 3.13, 13 novembre 2026). **Non ancora aperte**: aprirle su
https://github.com/zensical/zensical/issues solo con l'approvazione di Franco, dopo aver
ricontrollato che non esistano già e che il problema sia presente nell'ultima release.

Il testo delle issue è in inglese, la lingua del progetto upstream.

| # | Titolo | Impatto per rpsd-doc | Stato |
|---|---|---|---|
| 1 | Search dialog strings are not localized | Requisito *Italian interface and search* soddisfatto solo in parte | bozza |
| 2 | Italian translation incomplete (`tabs`, `clipboard.error`) | Due stringhe minori in inglese | bozza |
| 3 | Copy of annotated code keeps trailing whitespace | Cosmetico; prima di aprirla confrontare con Material | da verificare |

---

## 1. Search dialog strings are not localized

**Environment**: zensical 0.1.1, zensical-ui 0.0.42, configuration in `mkdocs.yml`.

**Config**:

```yaml
theme:
  name: material
  variant: classic
  language: it
```

**Expected**: the search dialog uses the configured language, as the rest of the theme does
(the header button already reads "Cerca", and `search.json` has `lang: ["it"]`).

**Actual**: the search dialog opened from the header is entirely in English: input placeholder
and `aria-label` "Search", buttons "Close search" and "Filters", status line "1 result" /
"2 results". The strings are hard-coded in
`zensical_ui/templates/assets/javascripts/bundle.*.min.js`, so they cannot be overridden
through `partials/languages/*.html` or a custom translation partial.

**Request**: take these strings from the theme translations (or expose them as
translation keys) so they follow `theme.language`.

---

## 2. Italian translation incomplete

**Environment**: as above.

**Actual**: in `zensical_ui/templates/partials/languages/it.html`:

- `"tabs": "Tabs"` is not translated (used as the `aria-label` of the navigation tabs);
- `clipboard.error` is missing, so the English fallback "Could not copy to clipboard" is used.

**Proposed values**: `"tabs": "Schede"`, `"clipboard.error": "Impossibile copiare negli appunti"`.

---

## 3. Copy of annotated code keeps trailing whitespace (da verificare)

**Prima di aprirla**: controllare se Material for MkDocs si comporta allo stesso modo; se sì,
non è una regressione di Zensical e non va aperta.

**Steps**: XML code block with an annotation in a comment at the end of the line:

````markdown
``` xml
<PublicationDelivery version="1.0"> <!-- (1)! -->
```
````

**Actual**: the copy button produces `<PublicationDelivery version="1.0"> ` with a trailing
space where the annotation comment was. The annotation marker itself is correctly removed.

**Expected**: no trailing whitespace on lines whose annotation comment was stripped.
