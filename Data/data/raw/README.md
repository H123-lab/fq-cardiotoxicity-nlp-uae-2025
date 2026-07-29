# Raw Data Directory

## Purpose

This directory is reserved for original, unprocessed datasets obtained from their respective data providers before any cleaning, transformation, or analytical processing.

The raw data layer represents the initial input stage of the analytical workflow described in:

**"AI-Driven Pharmacovigilance and Molecular Profiling of Fluoroquinolone-Associated Cardiotoxicity in the UAE"**

The study integrates pharmacovigilance surveillance, clinical text processing, machine learning, explainable artificial intelligence, geospatial analysis, and molecular computational approaches.

---

# Data Availability

## Restricted Healthcare and Pharmacovigilance Data

Certain datasets used in this study were obtained from authorized healthcare and regulatory sources but cannot be publicly distributed due to:

- Data governance agreements
- Third-party ownership restrictions
- Privacy and confidentiality requirements
- Institutional or regulatory limitations

Examples include:

- UAE pharmacovigilance datasets
- Institution-level safety reporting datasets
- Restricted healthcare-derived records

These datasets are therefore **not included in this repository**.

---

# Expected Raw Data Inputs

The analytical framework may require the following raw input categories:

| Dataset Category | Description | Availability |
|---|---|---|
| UAE pharmacovigilance records | Regional adverse drug reaction surveillance data | Restricted |
| FAERS reports | Public adverse event reporting database | Publicly accessible |
| WHO VigiAccess data | International pharmacovigilance signals | Publicly accessible |
| EudraVigilance data | European pharmacovigilance reports | Publicly accessible |
| Clinical text resources | De-identified or publicly available biomedical text | Source dependent |
| Molecular structure data | Drug and protein structure resources | Publicly accessible |

---

# Data Handling Principles

Raw datasets should remain unchanged after acquisition.

All preprocessing steps should be performed through reproducible scripts located in:

src/data_processing.py

The raw data layer should never contain:

- Personally identifiable information
- Confidential clinical records
- Modified analytical datasets
- Intermediate processing outputs

---

# Local Usage

Researchers reproducing the analysis should place authorized raw datasets locally within this directory structure:
data/
└── raw/
├── pharmacovigilance/
├── clinical_text/
└── molecular_inputs/

Local raw data files should not be committed to version control.

---

# Version Control Policy

Large or restricted datasets are excluded from GitHub using `.gitignore`.

Only metadata, documentation, and reproducible processing scripts are maintained in this repository.

Raw data → Processing scripts → Processed datasets → Analysis outputs


---

# Contact

For questions regarding data access, analytical methods, or reproducibility procedures, contact the corresponding author.
