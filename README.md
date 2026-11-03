# Clinical Trial Disease Category Classifier

A machine learning project that predicts a disease category from a clinical trial's brief summary.

## Project Overview

This project uses TF-IDF text features and Logistic Regression to classify clinical trial summaries into one of eight disease categories. The Streamlit app displays a predicted category and confidence score.

## Disease Categories

- Anxiety
- Breast cancer
- Chronic obstructive pulmonary disease
- COVID-19
- Glaucoma
- Rheumatoid arthritis
- Sickle cell anemia
- Type 2 diabetes

## Model Performance

On the held-out test set:

- Accuracy: 95.1%
- Macro F1-score: 0.94

These results apply to this dataset and test split. They do not represent medical advice or clinical validation.

## Project Files

- `app.py` — Streamlit prediction application
- `clinical_trials.ipynb` — Data exploration, model training, and evaluation
- `requirements.txt` — Python package dependencies
- `models/disease_classification.joblib` — Trained classification model
- `data/` — Put the dataset CSV here; dataset files are not included in this repository

## Setup and Run

1. Clone this repository:

   ```bash
   git clone https://github.com/p1170286/clinical-trial-disease-classifier.git
   cd clinical-trial-disease-classifier

2. Install the dependencies:
pip install -r requirements.txt

3. Start the app:
streamlit run app.py  
