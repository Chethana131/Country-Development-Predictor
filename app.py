import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# Load model and data
# --------------------------
model = joblib.load("model.pkl")
data = pd.read_csv("merged_development_data_full.csv")

# Clean columns
data.columns = data.columns.str.strip()

# --------------------------
# Define
# --------------------------
features = [
    'Access to electricity (% of population)',
    'R&D spending (% of GDP)',
    'Education spending (% of GDP)',
    'Health spending (% of GDP)',
    'Unemployment rate (% of labor force)',
    'Life expectancy at birth',
    'Population growth (annual %)',
    'Life expectancy',
    'Expected years of schooling',
    'Mean years of schooling',
    'GNI per capita',
    'social_support',
    'healthy_life_expectancy',
    'freedom_to_make_life_choices',
    'generosity',
    'perceptions_of_corruption'
]

countries = ['India', 'China', 'USA', 'Bangladesh', 'Belgium', 'Canada']

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Development Predictor", layout="wide")
st.title("🌍 Country Development Indicator Predictor")

selected_country = st.selectbox("Select a Country:", countries)

# Filter country data for the selected country
country_data = data[data['Country'].str.lower() == selected_country.lower()]
latest_year = country_data['Year'].max()
prev_year_data = country_data[country_data['Year'] == latest_year - 1]
latest_data = country_data[country_data['Year'] == latest_year]

st.caption(f"Using previous year values from {latest_year - 1} as baseline")

# --------------------------
# Sidebar sliders
# --------------------------
st.sidebar.header("Adjust Input Features")

input_data = {}

for feature in features:
    col_data = data[feature].dropna()
    min_val, max_val = float(col_data.min()), float(col_data.max())

    # Try to get previous year’s value
    if not prev_year_data.empty and pd.notna(prev_year_data[feature].values[0]):
        default_val = float(prev_year_data[feature].values[0])
        label = feature
    else:
        # If missing, impute with the mean and mark as (imputed)
        default_val = float(col_data.mean())
        label = f"{feature} (imputed)"

    input_data[feature] = st.sidebar.slider(
        label=label,
        min_value=round(min_val, 2),
        max_value=round(max_val, 2),
        value=round(default_val, 2),
        step=0.1
    )

# --------------------------
# Static baseline prediction (previous-year / imputed)
# --------------------------
baseline_input_df = pd.DataFrame([input_data])
baseline_pred = model.predict(baseline_input_df)[0]
baseline_gdp, baseline_hdi, baseline_happiness = baseline_pred[0], baseline_pred[1], baseline_pred[2]

# Pull actual latest-year values
if not latest_data.empty:
    actual_gdp = latest_data['GDP per capita'].values[0]
    actual_hdi = latest_data['HDI'].values[0]
    actual_happiness = latest_data['happiness_score'].values[0]
else:
    actual_gdp = actual_hdi = actual_happiness = np.nan

# Show actual vs baseline prediction
st.subheader(f"Development Indicators for {selected_country} ({latest_year})")
col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns(3)

# HDI
col1.markdown(
    f"**HDI**  \n"
    f"Actual: {round(actual_hdi,3)}  \n"
    f"Predicted: {round(baseline_hdi,3)}",
    unsafe_allow_html=True
)

# GDP per capita
col2.markdown(
    f"**GDP per capita**  \n"
    f"Actual: {round(actual_gdp,2)} USD  \n"
    f"Predicted: {round(baseline_gdp,2)} USD",
    unsafe_allow_html=True
)

# Happiness Score
col3.markdown(
    f"**Happiness Score**  \n"
    f"Actual: {round(actual_happiness,3)}  \n"
    f"Predicted: {round(baseline_happiness,3)}",
    unsafe_allow_html=True
)
# --------------------------
# Live-updating predictions from sliders
# --------------------------
updated_input_df = pd.DataFrame([input_data])
updated_pred = model.predict(updated_input_df)[0]
upd_gdp, upd_hdi, upd_happiness = updated_pred[0], updated_pred[1], updated_pred[2]

st.subheader("Predicted Development Indicators (Based on Slider Values)")
col1, col2, col3 = st.columns(3)
col1.metric("HDI", round(upd_hdi,3))
col2.metric("GDP per capita", f"{round(upd_gdp,2)} USD")
col3.metric("Happiness Score", round(upd_happiness,3))

# --------------------------
# Feature Importance Plots
# --------------------------
st.subheader("Feature Importance (Random Forest Model)")

st.image("HDI.png", caption="HDI feature importance", use_column_width=True)
st.image("GDP.png", caption="GDP feature importance", use_column_width=True)
st.image("Hscore.png", caption="Happiness score feature importance", use_column_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & RandomForestRegressor")
