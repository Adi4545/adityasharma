# When the Algorithm Meets the Absent Facility

**Research repository** for the academic manuscript on the **AI–Physical Execution Gap (AIPEG)** in India’s e-waste circular economy.

This repository is intentionally limited to the **manuscript**, **reproducible computational appendix**, and **reported results**, so it can be cited and showcased as the official paper artefact.

**Do not treat this repository as a general software project.** Course notes, tooling experiments, and unrelated materials are excluded.

---

## Citation

Aditya Sharma, Hossein Tabasi\*, Anurag Rana, Pankaj Vaidya (Shoolini University).  
*When the Algorithm Meets the Absent Facility: The AI–Physical Execution Gap in India’s E-Waste Circular Economy.*

Suggested BibTeX:

```bibtex
@unpublished{sharma2026aipeg,
  title  = {When the Algorithm Meets the Absent Facility: The AI--Physical Execution Gap in India's E-Waste Circular Economy},
  author = {Sharma, Aditya and Tabasi, Hossein and Rana, Anurag and Vaidya, Pankaj},
  year   = {2026},
  note   = {Manuscript and computational appendix},
  url    = {https://github.com/Adi4545/adityasharma}
}
```

Machine-readable citation metadata: [`CITATION.cff`](CITATION.cff)

---

## Start here (manuscript)

| File | Role |
| --- | --- |
| [`manuscript/AIPEG_Manuscript_Publishable_Final.pdf`](manuscript/AIPEG_Manuscript_Publishable_Final.pdf) | **Publishable PDF** (preferred for reading / sharing) |
| [`manuscript/When_the_Algorithm_Meets_the_Absent_Facility.pdf`](manuscript/When_the_Algorithm_Meets_the_Absent_Facility.pdf) | Same chapter PDF (stable filename) |
| [`manuscript/When_the_Algorithm_Meets_the_Absent_Facility_REVISED.md`](manuscript/When_the_Algorithm_Meets_the_Absent_Facility_REVISED.md) | Editable full text |

---

## Results (Section 6.5 computational test)

Headline structural tests (`results/headline_tests.csv`):

- Consolidation-cost spread ₹248 vs haulage spread ₹0.56 (ratio ~443)
- Component harvesting \(\varphi = 0\) wherever no licence exists
- Hinterland mean refurbishment \(\varphi\): 0.011 without a node, 0.536 with a node
- Circularity Execution Ratio: 1.00 metro / state-capital; 0.00 hinterland without node; 1.00 hinterland with node (licensed, value-positive strategies only)

| Path | Contents |
| --- | --- |
| `results/headline_tests.csv` | Headline structural tests |
| `results/table3_reproduction.csv` | Table 3 reproduction |
| `results/district_phi.csv` | District-level \(\varphi\) panel |
| `results/cer_without_added_nodes.csv` | CER by territorial class |
| `results/sensitivity_refurbishment.csv` | Sensitivity to refurbishment surplus |
| `results/figures/` | Figures 1–5 (PNG) |

---

## Reproduce the theory test

```bash
python3 -m pip install -r requirements.txt
python3 analysis/run_experiment.py
python3 analysis/build_pdf.py   # regenerates the chapter PDF from Markdown
```

The experiment implements equations (1)–(5), reproduces the four territorial regimes, and applies the same model to 30 named Indian origins. It does **not** claim a national estimate of circularity. Cost parameters are Appendix B assumptions. Facility hubs are public-coordinate proxies, not the unpublished CPCB geocoded register.

---

## Repository layout (research only)

```
manuscript/     # chapter PDF + Markdown source
analysis/       # AIPEG model, experiment runner, PDF builder
data/           # cited indicators + origin/hub coordinates
results/        # CSV tables + figures from Section 6.5
CITATION.cff    # citation metadata
requirements.txt
```

---

## Sources for national statistics

National figures in Section 4 are tied to published sources (Baldé et al. 2024; MoEFCC/Lok Sabha 2025; PIB PRID 2102701; TRAI 2025; NITI Aayog 2026; ICEA 2024; Turaga et al. 2019). No fabricated DOIs or operator datasets.

---

## Licence / use

The chapter remains the authors’ intellectual work. Use of code and tables for scholarly reproduction is welcome with citation.

**GitHub showcase URL:** https://github.com/Adi4545/adityasharma
