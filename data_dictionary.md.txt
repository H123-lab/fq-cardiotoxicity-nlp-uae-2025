
# 📘 Data Dictionary

This file documents the variables and fields used across all datasets in this study on fluoroquinolone-related cardiac risks in the UAE population.

---

## 📁 prescriptions_mohap_2018_2023.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Prescription_ID          | Unique ID assigned to each prescription                     |
| Year                     | Year the drug was prescribed (2018–2023)                     |
| Facility                 | Healthcare institution where prescription was issued         |
| Patient_Age              | Age of the patient                                           |
| Patient_Gender           | Gender of the patient                                        |
| Fluoroquinolone          | Name of the drug prescribed (e.g., Ciprofloxacin)            |
| Dosage_mg_day            | Daily dosage in milligrams                                   |
| Duration_days            | Duration of prescription (in days)                           |
| Co_Medications           | Other drugs prescribed with the fluoroquinolone              |

---

## 📁 faers_cardio_adrs_cleaned.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Case_ID                  | Unique identifier for each adverse event report              |
| Fluoroquinolone_Used     | Drug involved in the reported event                          |
| Adverse_Event_Reported   | Description of the ADR (e.g., Arrhythmia, Bradycardia)       |
| Patient_Age              | Age of the affected patient                                  |
| Gender                   | Gender of the patient                                        |
| Time_to_Onset_days       | Days between drug use and ADR appearance                     |
| Outcome                  | Patient outcome (Recovered, Hospitalized, Death, etc.)       |
| Data_Source              | Source database (FAERS, WHO, etc.)                           |

---

## 📁 ehr_physician_notes_sample.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Note_ID                  | Unique ID for each clinical note                             |
| Note_Text                | Unstructured clinical note or physician comment              |
| Sentiment_Score          | Sentiment polarity score (numeric)                           |
| Sentiment_Label          | Categorized as Positive, Neutral, or Negative                |
| Risk_Term                | Risk phrase detected (e.g., QT prolongation)                 |
| Risk_Level               | Labeled risk class (Low, Moderate, High)                     |

---

## 📁 risk_awareness_scores_by_provider.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Provider                 | Name of healthcare facility                                  |
| Total_Notes              | Total clinical notes analyzed                                |
| Fluoroquinolone_Mentions| Count of drug mentions                                       |
| Cardio_Risk_Mentions     | Count of cardiovascular risk mentions                       |
| %_Risk_Aware_Notes       | Percentage of notes documenting risk                         |
| Risk_Awareness_Score     | Score from 0–100 based on sentiment + documentation          |

---

## 📁 time_trend_prescribing_2020_2025.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Year                     | Calendar year (2020–2025)                                    |
| Ciprofloxacin            | Number of prescriptions per year                             |
| Levofloxacin             | Number of prescriptions per year                             |
| Moxifloxacin             | Number of prescriptions per year                             |
| ECG-Monitored_Prescriptions | Prescriptions flagged with ECG-related note               |
| Total_Prescriptions      | Combined prescriptions that year                             |

---

## 📁 model_performance_metrics.json

| Key                      | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| accuracy                 | Classification model accuracy                                |
| precision                | Positive predictive value                                    |
| recall                   | Sensitivity of model                                         |
| f1_score                 | Harmonic mean of precision and recall                        |
| auc_roc                  | Area under the ROC curve                                     |
| Drug_encoded             | Encoded categorical values for model training                |
| Risk_Term_encoded        | Encoded categorical risk terms                               |

---

## 📁 vectorized_text.csv, tokenized_sentences.txt, tokenized_words.txt

| File                     | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| vectorized_text.csv      | Numerical embedding of each sentence for ML use              |
| tokenized_sentences.txt  | Each line = one sentence from EHR/leaflet                    |
| tokenized_words.txt      | Token-level breakdown of full text                          |

---

## 📁 refined_structural_data.csv

| Column                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| Extracted Medical Terms  | Terms extracted using keyword-based rules (not full NER)     |
| Fluoroquinolones Mentioned| All drugs detected in that note                             |
| Cardiovascular Risks     | Risk terms found in note (QT, arrhythmia, etc.)              |
| Co-Prescribed Drugs      | Other drugs mentioned alongside fluoroquinolones             |

---

📌 For any questions regarding data usage or column definitions, please refer to the `README.md` or contact the study author.

