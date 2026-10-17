# Country Development Indicator Predictor

An explainable machine-learning project that explores relationships between socioeconomic indicators and three country-level development outcomes: **GDP per capita, Human Development Index (HDI), and Happiness Score**. The project includes a Streamlit interface with interactive feature sliders for exploring hypothetical input scenarios and a trained multi-output Random Forest model.

**Live demo:** https://developmental-predictor.onrender.com/

## Features

- Predicts GDP per capita, HDI, and Happiness Score from socioeconomic indicators.
- Interactive Streamlit controls for changing input assumptions and comparing predictions.
- Random Forest feature-importance visualizations.
- Notebook-based data preparation and model experimentation.

## Tech stack

Python, pandas, NumPy, scikit-learn, joblib, Matplotlib, Jupyter, and Streamlit.

## Repository layout

```text
country-development-predictor/
├── app/
│   └── app.py
├── models/
│   └── model.pkl
├── notebooks/
│   ├── data_preprocessing_and_neural_network.ipynb
│   ├── random_forest_model.ipynb
│   └── random_forest_model_experiment.ipynb
├── docs/
│   └── project_report.pdf
├── data/       # Add the required dataset here; see below
├── assets/     # Add the feature-importance plots here; see below
├── requirements.txt
└── README.md
```

## Important: files needed to run the app

The uploaded source files did **not** include all runtime data/assets. The current Streamlit app expects these files:

- `merged_development_data_full.csv` — required to populate country/year values and slider defaults.
- `HDI.png`, `GDP.png`, and `Hscore.png` — feature-importance images shown by the interface.

The data-preparation notebook also expects the original source files `WDICSV.csv`, `HDI.xlsx`, and `World Hapiness.xlsx` (the spelling of the last filename is used in the notebook). These were not included in the uploaded files either. The app will not run locally until the required CSV and images are restored and the paths in `app/app.py` are updated to match this repository layout.

Do not replace the missing CSV with an unrelated or guessed dataset: the columns and preprocessing need to match the trained model and application.


## Limitations

This is an exploratory predictive model, not a causal policy simulator. Changing a slider shows how the trained model responds to changed inputs; it does not establish that a real-world policy change would cause the predicted outcome. Predictions depend on the coverage, quality, and time alignment of the underlying data.

## Report

The project report is included under `docs/project_report.pdf`.
