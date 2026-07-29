# NLP Corpus Description

## Purpose

This document describes the textual sources used for biomedical natural language processing (NLP) in this study.

The original source documents are **not redistributed** in this repository because they contain copyrighted regulatory and manufacturer material or are subject to licensing restrictions.

Instead, this document provides a transparent description of the corpus used during concept extraction.

---

# Corpus Components

The NLP workflow incorporated publicly available biomedical text from multiple complementary sources, including:

- UAE Ministry of Health and Prevention (MOHAP) pharmacovigilance safety communications
- UAE regulatory drug safety notices
- FDA Drug Safety Communications
- European Medicines Agency (EMA) safety communications
- Publicly available fluoroquinolone prescribing information and package leaflets
- Published biomedical literature describing fluoroquinolone-associated adverse drug reactions
- Public pharmacovigilance narratives and regulatory reports

These documents were used solely for biomedical concept extraction and terminology normalization.

---

# NLP Objective

The objective of the NLP component was to identify clinically relevant concepts associated with fluoroquinolone-induced cardiotoxicity, including:

- Fluoroquinolone drug names
- Cardiovascular adverse events
- QT prolongation
- Torsades de Pointes
- Ventricular arrhythmias
- Bradyarrhythmias
- Drug-drug interaction terminology
- Cardiovascular risk factors
- Clinical outcome terminology
- Medication names
- Regulatory safety terminology

---

# NLP Processing

Text preprocessing included:

- Unicode normalization
- Removal of formatting artifacts
- Sentence segmentation
- Tokenization
- Lowercase normalization where appropriate
- Abbreviation expansion
- Biomedical terminology mapping

Named entity recognition (NER) was performed using BioBERT.

Extracted entities were subsequently mapped to standardized clinical vocabularies including MedDRA terminology before downstream statistical and machine-learning analyses.

BioBERT was used exclusively for biomedical concept extraction and was **not** included in the final predictive ensemble.

---

# Availability

Many original source documents are publicly available from their respective regulatory agencies and publishers.

Because several documents remain subject to copyright, licensing, or redistribution restrictions, the original text corpus is not included in this repository.

This repository therefore provides only the analytical workflow rather than redistributing protected source material.

---

# Reproducibility

Researchers wishing to reproduce the NLP pipeline may obtain equivalent publicly available regulatory safety communications, prescribing information, and biomedical literature from their original publishers and process them using the workflow described in this repository.
