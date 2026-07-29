# Reproducibility Notes

All analyses are designed to be reproducible.

The repository separates:

- raw data
- processed data
- source code
- analytical outputs

Restricted healthcare datasets are intentionally excluded.

External resources should be downloaded directly from their official providers.

Random seeds, software versions, and computational parameters are documented in:

- configs/
- Supplementary Table S19

Machine-learning analyses use internally validated models.

BioBERT is used exclusively for biomedical text processing and is not part of the predictive ensemble.
