# 🧬 Fluoroquinolone-Associated Cardiotoxicity in the UAE: NLP-Based Real-World Risk Analysis (2018–2025)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15271591.svg)](https://doi.org/10.5281/zenodo.15271591)

## 🧠 Introduction

This repository contains a reproducible analysis pipeline that investigates the cardiovascular risks associated with fluoroquinolone antibiotics in the UAE using a multi-modal AI framework. By combining natural language processing (NLP), pharmacovigilance reports, physician notes, and machine learning (ML), the study aims to:

- Assess adverse cardiac outcomes (QT prolongation, arrhythmias, sudden cardiac death)
- Analyze prescribing trends (2018–2025) using real-world and simulated UAE data
- Measure risk awareness among healthcare providers
- Predict high-risk cases using AI-based models

This work helps bridge the regional data gap and supports policy recommendations for safer prescribing practices.

## 🔍 Objective
This study aims to assess the cardiovascular risks associated with fluoroquinolone use in the UAE using pharmacovigilance reports, unstructured clinical narratives, and real-world ECG and contamination data, combined with NLP and machine learning.

---
## 🧠 Methods
- NLP Pipeline: Tokenization, NER (BioBERT), Sentiment Analysis, and Relationship Extraction using spaCy & transformers.
- Risk Modeling: Random Forest, SVM, and Ensemble learning for ADR risk classification.
- Survival Analysis: Kaplan–Meier with log-rank tests for time-to-event modeling.

---

## 📊 Results / Figures

### 1. Kaplan–Meier Survival Analysis

This figure illustrates the time-to-onset of arrhythmia events stratified by fluoroquinolone type. Moxifloxacin demonstrates a steeper early drop, indicating faster onset in some patients.

![KM Curve](figures/km_arrhythmia_by_drug.png)

---

### 2. Logistic Regression (Odds Ratios)

Forest plot displaying adjusted odds ratios (OR) for arrhythmia risk by drug type and predisposing conditions. Moxifloxacin shows significantly increased adjusted risk.

![Logistic Regression](figures/logistic_odds_ratios_arrhythmia.png)

---

### 3. Arrhythmia Incidence by Fluoroquinolone Type

This bar chart compares the predicted probabilities of arrhythmia for each fluoroquinolone. Moxifloxacin ranked highest, followed by levofloxacin and ciprofloxacin.

![Arrhythmia Probability](figures/arrhythmia_probability_by_drug.png)

--- Environmental exposure modeling data is available in /data/environmental_risk_public_health_UAE.txt

## 📂 Project Structure

```plaintext
📁 data/
    ├── prescriptions_mohap_2018_2023.csv
    ├── faers_cardio_adrs_cleaned.csv
    ├── ehr_physician_notes_sample.csv
    ├── co_medication_interactions.csv
    └── literature_guidelines_extracted.csv

📁 models/
    ├── fq_cardiac_risk_classifier.pkl
    └── transformers_fine_tuned_ner_model/ (includes config.json, tokenizer.json, model.safetensors, etc.)

📁 results/
    ├── descriptive_statistics_summary.csv
    ├── risk_awareness_scores_by_provider.csv
    ├── time_trend_prescribing_2020_2025.csv
    └── model_performance_metrics.json

📁 figures/
    ├── km_arrhythmia_by_drug.png
    ├── logistic_odds_ratios_arrhythmia.png
    └── arrhythmia_probability_by_drug.png

📁 notebooks/
    ├── 01_data_cleaning_preprocessing.ipynb
    ├── 02_ner_and_sentiment_analysis.ipynb
    ├── 03_risk_prediction_model_training.ipynb
    ├── 04_kaplan_meier_and_logistic_regression.ipynb
    └── 05_dashboard_visualization_powerbi.ipynb

## 📂 Key Datasets

The datasets and resources used in this repository are all publicly available:

| Dataset | Access Link |
|--------|-------------|
| MOHAP Adverse Drug Reaction Reports (UAE) | [https://mohap.gov.ae/en/statistics-and-reports](https://mohap.gov.ae/en/statistics-and-reports) |
| WHO VigiAccess | [https://www.vigiaccess.org](https://www.vigiaccess.org) |
| FDA FAERS (Adverse Event Reporting System) | [https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html](https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html) |
| EMA EudraVigilance Reports | [https://www.adrreports.eu/en/search_subst.html](https://www.adrreports.eu/en/search_subst.html) |
| MIMIC-IV ECG Demo Dataset | [https://physionet.org/content/mimic-iv-ecg-demo/0.1/](https://physionet.org/content/mimic-iv-ecg-demo/0.1/) |
| UAE MOCCAE Open Water & Environmental Data | [https://www.moccae.gov.ae/en/open-data.aspx](https://www.moccae.gov.ae/en/open-data.aspx) |
| Drug-Induced TdP Case Database | [https://figshare.com/articles/dataset/15102690](https://figshare.com/articles/dataset/15102690) |
| FDA Drug-Induced Cardiotoxicity Rank (DICTrank) | [https://www.fda.gov/science-research/bioinformatics-tools/drug-induced-cardiotoxicity-rank-dictrank-dataset](https://www.fda.gov/science-research/bioinformatics-tools/drug-induced-cardiotoxicity-rank-dictrank-dataset) |

| File Name                            | Description                                                                |
|--------------------------------------|----------------------------------------------------------------------------|
| `prescriptions_mohap_2018_2023.csv`  | Anonymized prescription-level data from UAE MOHAP records                  |
| `faers_cardio_adrs_cleaned.csv`      | FAERS-reported cardiac ADRs linked to fluoroquinolones                     |
| `ehr_physician_notes_sample.csv`     | De-identified physician notes annotated for QT risk                        |
| `co_medication_interactions.csv`     | Mapped co-prescription data with QT-prolonging drugs                       |
| `literature_guidelines_extracted.csv`| Benchmark guideline mentions from EMA, WHO, MSD                            |


## 📊 Interactive Dashboard (Static Summary View)

Although no live Power BI dashboard is hosted, this static visualization summarizes key dashboard elements based on study data.

![Dashboard Overview](figures/dashboard_overview.png)

## 📜 Citation
If using this repository, please cite:

> Author, Hassa Iftikhar et al. (2025). AI-NLP-Based Risk Prediction of Fluoroquinolone-Induced Cardiotoxicity in the UAE: A Real-World Pharmacovigilance and Molecular Insight Study. _Submitted to Frontiers in Pharmacology_.

## 🛡️ Ethics
All datasets were anonymized and collected from open-access sources. Ethical approval was not required in accordance with MOHAP UAE’s policy on retrospective secondary data analyses.

---

## 🔗 Project Archive
- Zenodo DOI: [https://doi.org/10.5281/zenodo.15271591](https://doi.org/10.5281/zenodo.15271591)
