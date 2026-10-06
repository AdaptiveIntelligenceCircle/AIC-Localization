# AIC-Localization

**Language packs and translation process for Adaptive Intelligence Circle orientation materials.**

Status: **pre-Covenant**, experimental, under-claim. 

This repository holds translations and localization aids for selected AIC public documents.  

It does **not** create new protocol rules, does not alter technical specifications, and does not constitute official legal interpretation in any language.

## Purpose

- Make key orientation materials accessible in languages beyond English, starting with Vietnamese.
- Keep a clear record of what has been translated and at what review level.
- Provide a shared glossary so that core terms (Third Path, Ethical Kernel, fail-closed, NeedHuman, entity ≠ immunity, …) stay consistent.
- Support Global South and multilingual contributors without diluting under-claim discipline.

## Canonical language

**English is the canonical language** for technical precision, formal models, and any text that could be read as normative.

When a translation and the English source diverge:

1. Prefer the English source for technical and policy meaning.
2. Open an issue to improve the translation.
3. Do not treat a translation as an independent authority that overrides the source.

Legal and regulatory orientation texts remain “not legal advice” in every language.

## Layout

```
AIC-Localization/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── overview.md
│   ├── process.md
│   ├── status.md
│   └── limitations.md
├── locales/
│   ├── en/                 # reference / short canonical excerpts
│   └── vi/                 # Vietnamese
├── glossary/
│   ├── en.md
│   └── vi.md
├── templates/
│   └── translation-note.md
├── scripts/                # optional helpers
└── status/                 # machine-readable or summary status
```

## Currently prioritized documents

| Document family | Priority | Notes |
|-----------------|----------|-------|
| Beginners / beginner orientation | High | First contact for new contributors |
| What AIC is / is-and-is-not | High | Boundary clarity |
| Core principles (short) | High | Third Path, fail-closed, entity ≠ immunity |
| FAQ (selected answers) | High | Status, token, mainnet, law |
| Glossary of terms | High | Consistency across languages |
| Covenant criteria (high-level summary only) | Medium | Pre-declaration; no expansion of claims |
| Whitepaper chapters | Lower | Large; do incrementally if capacity allows |

## Quick start for readers

1. Choose your language under `locales/`.
2. Read the local `README` or index in that folder.
3. When in doubt about meaning, check the English source and `docs/limitations.md`.

## Quick start for translators

1. Read `docs/process.md` and `CONTRIBUTING.md`.
2. Use `glossary/` for established term translations.
3. Keep under-claim language intact (do not “improve” caution into stronger claims).
4. Submit small, reviewable units.

## Relationship to other AIC repositories

- **AIC-Beginners**, **MyVision**, **AIC-Whitepaper**, **AIC-Legal** — sources of canonical text.
- **AIC-Policy-Tools** — policy orientation; translations must preserve “not legal advice”.
- **Website (adaptiveintelligencecircle.github.io)** — may later consume selected localized pages; no automatic pipeline is assumed.

## Principles observed

- **Under-claim** in every language.
- **Entity ≠ immunity** — no translation creates special status.
- **No token rule-power** — no language version introduces economic rule-power.
- **Pre-Covenant** — translations do not advance mainnet or Covenant declaration.
- **Fail-closed spirit** — when a term is ambiguous, prefer the more cautious rendering and note uncertainty.

## License

GPL-3.0-or-later for structure and scripts (see LICENSE).  
Translated documentation is provided so that the same freedoms and the same limitations travel with the text.  
Where upstream documents use additional terms (e.g. CC-BY), respect those terms.

## Maintenance note

During periods of reduced maintainer availability the repository remains public.  
High-quality, under-claim-preserving translations are welcome.
