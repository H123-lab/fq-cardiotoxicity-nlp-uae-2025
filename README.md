# Fluoroquinolone-Associated Cardiotoxicity in the UAE: Integrated Pharmacovigilance, Explainable AI, Geospatial Analysis, and Molecular Characterization

This repository contains the computational analysis framework associated with the manuscript:

**Fluoroquinolone-Associated Cardiotoxicity in the UAE: An Integrated Pharmacovigilance, Explainable AI, Geospatial, and Molecular Analysis (2018–2023)**

The repository is being structured to provide a transparent and reproducible computational record of the analyses reported in the manuscript.

---

## Study Scope

This study investigates fluoroquinolone-associated cardiovascular adverse drug reactions (ADRs) in the United Arab Emirates (UAE) during **January 1, 2018 through December 31, 2023**.

The analytical framework integrates:

1. Pharmacovigilance signal detection
2. Clinical and pharmacological feature harmonization
3. Natural language processing (NLP)
4. Machine-learning prediction
5. Explainable artificial intelligence (XAI)
6. Drug-drug interaction (DDI) network analysis
7. Descriptive geospatial analysis
8. Molecular docking and structure-activity relationship (SAR) analysis
9. In silico ADMET and toxicity prediction

The objective is to connect population-level safety signals with interpretable clinical risk factors and hypothesis-generating molecular evidence.

---

## Analytical Framework

The analytical workflow follows the sequence:

**Data acquisition → harmonization and quality control → NLP-based concept extraction → pharmacovigilance signal detection → statistical modeling → machine-learning prediction → internal validation → SHAP-based explainability → DDI network analysis → geospatial reporting analysis → molecular docking/SAR/ADMET characterization**

The analytical components are complementary rather than a single causal model.

In particular:

- Pharmacovigilance analyses characterize reported safety signals.
- Machine-learning models estimate predictive associations within the analytical dataset.
- SHAP provides model-level feature attribution.
- Geospatial analyses characterize regional reporting patterns.
- Molecular analyses provide hypothesis-generating mechanistic information.
- Molecular structural modifications are computational candidates and are not experimentally validated in this study.

---

## Machine-Learning Models

The predictive modeling framework consists of:

- Random Forest
- XGBoost
- Logistic Regression

The final ensemble combines predictions from these three models using a weighted averaging strategy, with ensemble weights determined during internal validation.

### Important model-definition statement

**BioBERT is not part of the predictive ensemble.**

BioBERT is used exclusively for biomedical named-entity recognition and clinical concept extraction from relevant text sources. Extracted concepts are normalized and incorporated into the structured analytical dataset.

The final predictive ensemble is therefore:

**Random Forest + XGBoost + Logistic Regression**

and **not** Random Forest + XGBoost + BioBERT.

---

## Explainable AI

Model interpretability is assessed using SHapley Additive exPlanations (SHAP).

SHAP analyses are used to:

- rank influential predictors;
- quantify feature contributions to model predictions;
- examine predictor-response relationships; and
- compare machine-learning feature attribution with independent predictors identified through multivariable logistic regression.

The final SHAP feature list and ranking will be generated directly from the finalized analytical model implementation to maintain exact correspondence between code, figures, tables, and manuscript text.

---

## Pharmacovigilance Analyses

Signal detection uses complementary disproportionality methods:

- Proportional Reporting Ratio (PRR)
- Reporting Odds Ratio (ROR)
- Information Component (IC)
- Empirical Bayes Geometric Mean (EBGM)

Multivariable logistic regression is used to evaluate adjusted associations between predefined clinical/drug-related predictors and the study outcome.

---

## Natural Language Processing

Biomedical text processing uses BioBERT-based NLP methods for:

- biomedical named-entity recognition;
- clinical concept extraction;
- terminology normalization; and
- mapping of extracted concepts to standardized clinical/pharmacological terminology.

BioBERT is an NLP component only and is not used as a predictive ensemble classifier.

---

## Geospatial Analysis

Geospatial analysis evaluates the regional distribution of reported fluoroquinolone-associated cardiovascular ADRs within the UAE.

These analyses describe **reporting patterns and geographic heterogeneity**.

They do **not** estimate:

- true population incidence;
- causal geographic risk;
- environmental causation; or
- individual-level exposure-response relationships.

Potential differences in healthcare access, reporting intensity, surveillance practices, and regional population structure are therefore considered important contextual factors.

---

## Molecular Analysis

Molecular analyses include:

- molecular docking;
- protein-ligand interaction characterization;
- structure-activity relationship (SAR) analysis;
- physicochemical and drug-likeness assessment;
- ADMET prediction; and
- computational toxicity prediction.

These analyses are intended to provide **hypothesis-generating mechanistic evidence** concerning differential fluoroquinolone cardiotoxicity and predicted hERG liability.

Computational structural modifications represent candidate redesign strategies and require experimental validation before any translational or clinical interpretation.

---

## Validation and Generalizability

Machine-learning development uses stratified internal cross-validation and internal evaluation procedures.

Model performance is assessed using metrics including:

- accuracy;
- sensitivity;
- specificity;
- precision;
- recall;
- F1-score;
- ROC-AUC; and
- calibration measures.

The study does **not** claim external validation against an independent clinical cohort.

Accordingly, model performance should be interpreted as **internally validated predictive performance**, rather than externally validated clinical prediction performance.

---

## Data Sources and Data Availability

The repository contains analysis code, documentation, and reproducibility materials.

Certain UAE pharmacovigilance and prescription-level datasets used in the study were obtained from third-party sources under access conditions that do not permit public redistribution. These restricted source datasets are therefore NOT included in this repository.

In particular, the original MOHAP-derived dataset used for the primary analysis is not publicly redistributed here.

Where legally and technically appropriate, the repository provides:
- analysis scripts and notebooks;
- data dictionaries and variable specifications;
- preprocessing and harmonization procedures;
- model-development code;
- configuration files and software requirements;
- non-identifiable synthetic or demonstration data where applicable; and
- derived results that do not disclose restricted source records.

Restricted source datasets are not included in this repository.

The analysis requires authorized access to the underlying data.
Users must place locally authorized datasets in their own environment
and configure the corresponding input path before running the analysis.
Researchers seeking access to restricted source data should contact the relevant data custodian directly and obtain any required authorization before attempting to reproduce analyses involving those data.

Publicly accessible external datasets are identified separately, together with their original source and applicable access conditions.

---

## Reproducibility

The repository is being reconstructed to maintain one-to-one consistency between:

**Manuscript Methods ↔ source code ↔ analytical parameters ↔ model definitions ↔ results ↔ figures ↔ supplementary tables**

Particular attention is being given to:

- exact model composition;
- feature definitions;
- SHAP feature rankings;
- ensemble weights;
- preprocessing rules;
- data harmonization;
- statistical thresholds;
- validation procedures;
- software versions;
- molecular docking parameters; and
- provenance of derived results.

The finalized computational environment and software specifications are documented in the supplementary analytical pipeline.

---

## Software Environment

The principal computational environment includes:

- Python 3.11
- R 4.3.3
- scikit-learn
- XGBoost
- SHAP
- BioBERT
- Hugging Face Transformers
- PyTorch
- GeoPandas
- ArcGIS Pro
- Cytoscape
- Schrödinger Maestro/Glide
- PyMOL
- PLIP
- SwissADME
- pkCSM
- ProTox-II

Exact versions and analysis-specific parameters will be documented in the repository and supplementary analytical pipeline.

---

## Repository Structure

The finalized repository will be organized approximately as follows:

```text
fq-cardiotoxicity-nlp-uae-2025/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── environment/
│   ├── requirements.txt
│   └── environment.yml
│
├── config/
│   └── analysis_config.yaml
│
├── data/
│   ├── raw/
│   ├── external/
│   ├── processed/
│   └── README.md
│
├── src/
│   ├── data/
│   ├── pharmacovigilance/
│   ├── nlp/
│   ├── statistics/
│   ├── machine_learning/
│   ├── explainability/
│   ├── ddi/
│   ├── geospatial/
│   └── molecular/
│
├── scripts/
│   └── run_pipeline.py
│
├── results/
│   ├── tables/
│   ├── figures/
│   └── supplementary/
│
├── notebooks/
│
└── docs/
    ├── data_dictionary.md
    ├── analytical_pipeline.md
    └── reproducibility.md
