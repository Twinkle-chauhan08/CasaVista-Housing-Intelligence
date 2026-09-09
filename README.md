🏠 CasaVista Housing Intelligence

An interactive California Housing statistical modeling dashboard built with Python, Streamlit, Statsmodels, Pandas, SciPy, and Plotly.

✨ Features

📊 Data Exploration — filters, data preview, charts, and statistical summary

🧪 Statistical Lab — two-group hypothesis testing and One-Way ANOVA

📈 OLS Regression — coefficients, p-values, confidence intervals, R², and adjusted R²

🏠 Live Property Prediction — predicted median house value with a 95% prediction interval

🔍 Model Diagnostics — residual plot, Q-Q plot, Jarque-Bera test, and VIF

📂 Project Structure

CasaVista Housing Project/
├── app.py
├── requirements.txt
├── README.md
└── Data/
    └── housing.csv

📌 Dataset

Dataset: California Housing Prices

Target variable: median_house_value

Categorical variable: ocean_proximity

OLS predictors

median_income, housing_median_age, total_rooms, total_bedrooms, population, households, latitude, longitude

🧪 Hypothesis Testing

The hypothesis tests use:

Significance level: α = 0.20

Test 1 compares two selected ocean_proximity groups. The default comparison is:

<1H OCEAN vs INLAND

Test 2 uses One-Way ANOVA across the ocean-proximity categories.

Decision display:

🔴 Reject H₀

🟢 Fail to Reject H₀

Very small p-values are displayed as < 0.001.

Note: the hypothesis-test α = 0.20 is separate from the 95% prediction interval used for live predictions.

🚀 How to Run

1. Create and activate a virtual environment

python -m venv .venv

Windows:

.venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Start the Streamlit app

streamlit run app.py

The dashboard will open in your browser.

🛠️ Technologies

Python

Streamlit

Pandas

NumPy

SciPy

Statsmodels

Plotly

Matplotlib

🎓 Academic Project

M.Sc. Data Science — Semester 1
Statistical Modeling with Python

CasaVista demonstrates exploratory analysis, hypothesis testing, multiple linear regression, prediction, and residual diagnostics in an interactive web dashboard.
