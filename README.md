# 🏠 CasaVista Housing Intelligence

🌐 **Live Demo:** https://casavista-housing-intelligence.streamlit.app/

## 📌 Project Overview

**CasaVista Housing Intelligence** is an interactive statistical modeling dashboard developed for analyzing the California Housing Prices dataset.

The project combines **data exploration, statistical hypothesis testing, multiple linear regression, live prediction, and model diagnostics** into a single interactive Streamlit web application.

The dashboard is designed to make statistical analysis easier to understand through interactive filters, visualizations, statistical results, and real-time predictions.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To explore and understand California housing data.
- To perform statistical hypothesis testing.
- To analyze differences in housing values across different locations.
- To build a Multiple Linear Regression model using OLS.
- To interpret regression coefficients, p-values, confidence intervals, and R².
- To evaluate regression assumptions using diagnostic tests.
- To provide an interactive web dashboard using Streamlit.
- To generate live house-value predictions based on user-provided property characteristics.

---

## ✨ Dashboard Features

### 📊 1. Data Exploration

The Data Exploration section provides an interactive overview of the dataset.

It includes:

- 🔎 Interactive filters for housing age and median income.
- 🌊 Filtering by ocean-proximity categories.
- 📋 Dataset preview.
- 💰 Median house value distribution.
- 📈 Median income vs house value visualization.
- 📦 House value comparison across locations.
- 📊 Descriptive statistical summary.
- Mean, standard deviation, median, quartiles, IQR, skewness, and kurtosis.

---

### 🧪 2. Statistical Laboratory

The Statistical Lab is used to investigate whether differences between housing groups are statistically significant.

#### Hypothesis Test 1 — Two-Group Comparison

The dashboard compares a selected numerical variable between two selected ocean-proximity groups.

The default comparison is:

**`<1H OCEAN` vs `INLAND`**

The hypotheses are:

**H₀:** There is no significant difference between the two groups.

**H₁:** There is a significant difference between the two groups.

The dashboard performs assumption checks and automatically selects an appropriate two-group test.

#### Hypothesis Test 2 — One-Way ANOVA

One-Way ANOVA is used to determine whether mean house values differ across the different ocean-proximity categories.

The hypotheses are:

**H₀:** All groups have the same mean.

**H₁:** At least one group has a different mean.

### Significance Level

The hypothesis tests use:

**α = 0.20**

Decision display:

- 🔴 **Reject H₀**
- 🟢 **Fail to Reject H₀**

Very small p-values are displayed as **< 0.001** for easier interpretation.

> Note: The hypothesis-test significance level is α = 0.20. The live prediction model separately uses a 95% prediction interval.

---

## 📈 3. Multiple Linear Regression

An Ordinary Least Squares (OLS) regression model is used to estimate the median house value.

### 🎯 Target Variable

`median_house_value`

### 🔢 Predictor Variables

The model uses the following predictors:

- `median_income`
- `housing_median_age`
- `total_rooms`
- `total_bedrooms`
- `population`
- `households`
- `latitude`
- `longitude`

The regression model provides:

- 📊 R²
- 📐 Adjusted R²
- 🔢 Regression coefficients
- 🧪 Coefficient p-values
- 📏 95% confidence intervals
- 📋 Model observations and predictor information

---

## 🏠 4. Live Property Prediction

The Property Predictor allows users to enter housing characteristics and receive a real-time estimate of the median house value.

Users can enter:

- 💰 Median Income
- 🏚️ Housing Median Age
- 🚪 Total Rooms
- 🛏️ Total Bedrooms
- 👥 Population
- 🏘️ Households
- 📍 Latitude
- 📍 Longitude

The dashboard then provides:

**🏠 Estimated Median House Value**

along with a:

**📊 95% Prediction Interval**

---

## 🔍 5. Model Diagnostics

The dashboard includes several diagnostic tools for evaluating the OLS model.

### 📉 Residuals vs Fitted Values

Used to visually inspect the relationship between residuals and fitted values and identify possible patterns or unequal variance.

### 📐 Q-Q Plot

Used to examine whether the residuals approximately follow a normal distribution.

### 🧪 Jarque-Bera Normality Test

Used to statistically test the normality of the residuals.

### 🔍 Variance Inflation Factor (VIF)

Used to check for possible multicollinearity among the predictor variables.

### 📋 OLS Coefficient Table

Displays:

- Coefficients
- P-values
- 95% confidence interval lower bound
- 95% confidence interval upper bound

---

## 📌 Dataset

**Dataset:** California Housing Prices

The dataset contains information about housing characteristics and location in California.

### Important Variables

| Variable | Description |
|---|---|
| `median_house_value` | Median value of houses |
| `median_income` | Median income of the area |
| `housing_median_age` | Median age of houses |
| `total_rooms` | Total number of rooms |
| `total_bedrooms` | Total number of bedrooms |
| `population` | Population of the area |
| `households` | Number of households |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `ocean_proximity` | Location category relative to the ocean |

### Target Variable

`median_house_value`

### Categorical Variable

`ocean_proximity`

---

## 📊 Statistical Findings

The hypothesis-testing analysis indicates statistically significant differences in house values for selected ocean-proximity group comparisons.

The One-Way ANOVA is used to evaluate differences across multiple ocean-proximity categories.

The OLS regression model explains a substantial portion of the variation in median house values using the selected housing and geographic predictors.

Model diagnostics are included to evaluate residual behavior, normality, and multicollinearity.

---

## 📂 Project Structure

```text
CasaVista Housing Project/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── housing.csv
