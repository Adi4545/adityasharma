# When the Algorithm Meets the Absent Facility

Academic chapter on the **AI–Physical Execution Gap (AIPEG)** in India’s e-waste circular economy.

Authors: Aditya Sharma, Hossein Tabasi (corresponding), Anurag Rana, Pankaj Vaidya — Shoolini University.

This is a scholarly manuscript with a reproducible computational appendix, not a web application.

## PDF (start here)

**[manuscript/When_the_Algorithm_Meets_the_Absent_Facility.pdf](manuscript/When_the_Algorithm_Meets_the_Absent_Facility.pdf)** — complete chapter, about 27 pages.

Editable source: `manuscript/When_the_Algorithm_Meets_the_Absent_Facility_REVISED.md`

## Reproduce the theory test (Section 6.5)

```bash
python3 -m pip install -r requirements.txt
python3 analysis/run_experiment.py
python3 analysis/build_pdf.py
```

The experiment implements equations (1)–(5), reproduces the four territorial regimes, and applies the same model to 30 named Indian origins. It does **not** claim a national estimate of circularity. Cost parameters are Appendix B assumptions. Facility hubs are public-coordinate proxies, not the unpublished CPCB geocoded register.

Headline structural tests (from `results/headline_tests.csv`):

- Consolidation-cost spread ₹248 vs haulage spread ₹0.56 (ratio ~443)
- Component harvesting \(\varphi = 0\) everywhere (no licence)
- Hinterland mean refurbishment \(\varphi\): 0.011 without a node, 0.536 with a node
- Circularity Execution Ratio: 1.00 metro / state-capital; 0.00 hinterland without node; 1.00 hinterland with node (licensed, value-positive strategies only)

## Repository layout

| Path | Contents |
| --- | --- |
| `manuscript/*.pdf` | Printable chapter |
| `manuscript/*.md` | Full text |
| `analysis/` | Model, experiment, PDF builder |
| `data/` | Cited indicators + origin/hub coordinates |
| `results/` | CSV tables and figures |
| `editorial/` | Similarity/AI-writing diagnostic from the prior editing pass |
| `originals/turnitin-reports/` | Unmodified Turnitin PDFs |

## Citations

National statistics in Section 4 are tied to published sources (Baldé et al. 2024; MoEFCC/Lok Sabha 2025; PIB PRID 2102701; TRAI 2025; NITI Aayog 2026; ICEA 2024; Turaga et al. 2019). No fabricated DOIs or operator datasets.

## Licence / use

The chapter remains the authors’ intellectual work.
