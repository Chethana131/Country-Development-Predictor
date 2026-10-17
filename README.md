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

## Setup (after restoring missing data/assets)

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place the CSV at `data/merged_development_data_full.csv` and the plots in `assets/`.
4. Update the file paths in `app/app.py` to use `data/merged_development_data_full.csv`, `models/model.pkl`, and the image files in `assets/`.
5. Run the app from the repository root:

   ```bash
   streamlit run app/app.py
   ```

## Model notes

The included notebook defines 16 socioeconomic input features and three targets: `gdp_per_capita`, `HDI`, and `happiness_score`. It trains a `MultiOutputRegressor` wrapping a `RandomForestRegressor`. Review the notebook for the exact preprocessing and evaluation steps before retraining.

The current app and notebook use somewhat different target-column naming conventions (for example, `GDP per capita` in the app versus `gdp_per_capita` in the notebook). Confirm that the saved model, dataset schema, and displayed units align before publishing a fully reproducible release.

## Limitations

This is an exploratory predictive model, not a causal policy simulator. Changing a slider shows how the trained model responds to changed inputs; it does not establish that a real-world policy change would cause the predicted outcome. Predictions depend on the coverage, quality, and time alignment of the underlying data.

## Report

The project report is included under `docs/project_report.pdf`.
