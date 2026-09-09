import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CasaVista | California Housing Intelligence",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* Compact top spacing */
header[data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    background: transparent !important;
}

header[data-testid="stHeader"] * {
    display: none !important;
}

.block-container {
    padding-top: 0 !important;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #101827;
}

section[data-testid="stSidebar"] * {
    color: #e8edf5 !important;
}

section[data-testid="stSidebar"] code {
    color: #ffffff !important;
    background: #1f2a3d !important;
    border: 1px solid #334155 !important;
    border-radius: 7px;
    padding: 4px 7px;
    font-size: 12px;
}

.sidebar-data-card {
    background: #151f31;
    border: 1px solid #2a3850;
    border-radius: 12px;
    padding: 13px 14px;
    margin-top: 10px;
}

.sidebar-data-label {
    color: #93c5fd !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.sidebar-data-value {
    color: #ffffff !important;
    font-size: 13px;
    font-weight: 600;
}

.sidebar-title {
    font-size: 25px;
    font-weight: 700;
    color: white;
    margin-bottom: 2px;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #9ba8bb !important;
    margin-bottom: 25px;
}

/* HERO */

.hero {
    background: linear-gradient(
        135deg,
        #111827 0%,
        #172554 48%,
        #1e3a8a 100%
    );
    border-radius: 24px;
    padding: 42px 45px;
    margin-top: -0.15rem;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    border: 45px solid rgba(255,255,255,0.05);
    right: -80px;
    top: -80px;
}

.hero-small {
    color: #93c5fd;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-title {
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 43px;
    font-weight: 700;
    line-height: 1.15;
    margin: 0;
}

.hero-description {
    color: #cbd5e1;
    font-size: 16px;
    margin-top: 13px;
    max-width: 700px;
}

.hero-badge {
    display: inline-block;
    margin-top: 20px;
    padding: 8px 15px;
    border-radius: 30px;
    background: rgba(255,255,255,0.10);
    color: #dbeafe;
    font-size: 13px;
}

/* SECTION HEADERS */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: #111827;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 22px;
}

/* METRIC CARDS */

.metric-card {
    background: white;
    border-radius: 18px;
    padding: 22px;
    border: 1px solid #e7ebf2;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    min-height: 125px;
}

.metric-label {
    color: #64748b;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 8px;
}

.metric-value {
    color: #111827;
    font-size: 27px;
    font-weight: 700;
}

.metric-icon {
    font-size: 22px;
    margin-bottom: 7px;
}

/* CONTENT CARDS */

.content-card {
    background: white;
    border: 1px solid #e7ebf2;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.04);
}

/* INFO CARD */

.info-card {
    background: #eef5ff;
    border-left: 4px solid #2563eb;
    padding: 17px 20px;
    border-radius: 10px;
    color: #334155;
    margin: 15px 0 22px;
}

/* RESULT CARD */

.result-card {
    background: linear-gradient(135deg, #f8fafc, #eef4ff);
    border: 1px solid #dbeafe;
    border-radius: 20px;
    padding: 25px;
    margin: 18px 0;
}

.result-label {
    color: #64748b;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.result-value {
    color: #172554;
    font-size: 38px;
    font-weight: 700;
    margin-top: 5px;
}

/* PREDICTION HERO */

.prediction-card {
    background: linear-gradient(
        135deg,
        #0f172a,
        #172554,
        #1d4ed8
    );
    border-radius: 24px;
    padding: 35px;
    text-align: center;
    color: white;
    margin: 25px 0;
    box-shadow: 0 15px 40px rgba(30,64,175,0.18);
}

.prediction-label {
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #bfdbfe;
}

.prediction-value {
    font-size: 48px;
    font-weight: 700;
    margin: 8px 0;
}

.prediction-range {
    color: #dbeafe;
    font-size: 14px;
}

/* STATUS */

.success-box {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #065f46;
    padding: 17px;
    border-radius: 12px;
    font-weight: 600;
    margin-top: 15px;
}

.warning-box {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    color: #9a3412;
    padding: 17px;
    border-radius: 12px;
    font-weight: 600;
    margin-top: 15px;
}

/* REJECT RESULT */

.reject-box {
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #b91c1c;
    padding: 17px;
    border-radius: 12px;
    font-weight: 700;
    margin-top: 15px;
}

/* FAIL TO REJECT RESULT */

.fail-box {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #047857;
    padding: 17px;
    border-radius: 12px;
    font-weight: 700;
    margin-top: 15px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    padding: 35px 0 10px;
}

/* BUTTON */

.stButton > button {
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 12px;
}

/* MOBILE */

@media (max-width: 768px) {

    .hero-title {
        font-size: 32px;
    }

    .hero {
        padding: 30px;
    }

    .prediction-value {
        font-size: 36px;
    }

}

</style>
""", unsafe_allow_html=True)


# Statistical significance level requested for the hypothesis tests
ALPHA = 0.20

def format_pvalue(value):
    """Display p-values clearly using at most three decimal places."""
    if value < 0.001:
        return "< 0.001"
    return f"{value:.3f}"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("Data/housing.csv")


df = load_data()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🏠 CasaVista</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">🏡 California Housing Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "MAIN MENU",
        [
            "📊  Data Exploration",
            "🧪  Statistical Lab",
            "🏠  Property Predictor"
        ]
    )

    st.markdown("---")

    st.markdown("### 📌 Project Overview")

    st.caption(
        "An interactive statistical modeling dashboard "
        "built with Python, Statsmodels and Streamlit."
    )

    st.markdown("---")

    st.markdown("### 🗂️ Dataset")

    st.markdown(
        '<div class="sidebar-data-card">'
        '<div class="sidebar-data-label">🏠 Dataset</div>'
        '<div class="sidebar-data-value">California Housing Prices</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-data-card">'
        '<div class="sidebar-data-label">🎯 Target Variable</div>'
        '<div class="sidebar-data-value"><code>median_house_value</code></div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-data-card">'
        '<div class="sidebar-data-label">🏷️ Categorical Variable</div>'
        '<div class="sidebar-data-value"><code>ocean_proximity</code></div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-small">
📊 STATISTICAL MODELING • CALIFORNIA
</div>

<div class="hero-title">
CasaVista Housing Intelligence
</div>

<div class="hero-description">
Explore housing patterns, test statistical relationships,
and estimate California property values using an
interactive statistical modeling dashboard.
</div>

<div class="hero-badge">
📈 LIVE DATA ANALYTICS
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PAGE 1 — DATA EXPLORATION
# ============================================================

if page == "📊  Data Exploration":

    st.markdown(
        '<div class="section-title">Explore the Market</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Interactive exploration of California housing characteristics.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    st.markdown("### 🎛️ Market Filters")

    col1, col2, col3 = st.columns(3)

    with col1:

        age_range = st.slider(
            "Housing Median Age",
            float(df["housing_median_age"].min()),
            float(df["housing_median_age"].max()),
            (
                float(df["housing_median_age"].min()),
                float(df["housing_median_age"].max())
            )
        )

    with col2:

        income_range = st.slider(
            "Median Income",
            float(df["median_income"].min()),
            float(df["median_income"].max()),
            (
                float(df["median_income"].min()),
                float(df["median_income"].max())
            )
        )

    with col3:

        ocean_options = sorted(
            df["ocean_proximity"].dropna().unique()
        )

        selected_ocean = st.multiselect(
            "Ocean Proximity",
            ocean_options,
            default=ocean_options
        )

    # --------------------------------------------------------
    # FILTER DATA
    # --------------------------------------------------------

    filtered_df = df[
        (df["housing_median_age"] >= age_range[0]) &
        (df["housing_median_age"] <= age_range[1]) &
        (df["median_income"] >= income_range[0]) &
        (df["median_income"] <= income_range[1]) &
        (df["ocean_proximity"].isin(selected_ocean))
    ]

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">🏘️</div>
            <div class="metric-label">FILTERED RECORDS</div>
            <div class="metric-value">{len(filtered_df):,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        median_value = filtered_df["median_house_value"].median()

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">💰</div>
            <div class="metric-label">MEDIAN HOUSE VALUE</div>
            <div class="metric-value">${median_value:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        avg_income = filtered_df["median_income"].mean()

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">📈</div>
            <div class="metric-label">AVERAGE INCOME</div>
            <div class="metric-value">{avg_income:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">🌊</div>
            <div class="metric-label">LOCATION TYPES</div>
            <div class="metric-value">{filtered_df["ocean_proximity"].nunique()}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------------

    st.markdown("### 📋 Housing Data")

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True,
        height=330
    )

    # --------------------------------------------------------
    # CHARTS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 💰 House Value Distribution")

        fig = px.histogram(
            filtered_df,
            x="median_house_value",
            nbins=45,
            title="Distribution of Median House Value",
            marginal="box"
        )

        fig.update_layout(
            template="plotly_white",
            height=430,
            showlegend=False,
            xaxis_title="Median House Value",
            yaxis_title="Number of Houses"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.markdown("### 📈 Income vs House Value")

        sample = filtered_df.sample(
            min(3000, len(filtered_df)),
            random_state=42
        )

        fig2 = px.scatter(
            sample,
            x="median_income",
            y="median_house_value",
            color="ocean_proximity",
            title="Income vs Median House Value",
            opacity=0.65
        )

        fig2.update_layout(
            template="plotly_white",
            height=430
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # --------------------------------------------------------
    # BOX PLOT
    # --------------------------------------------------------

    st.markdown("### 🌊 House Value by Location")

    fig3 = px.box(
        filtered_df,
        x="ocean_proximity",
        y="median_house_value",
        color="ocean_proximity",
        title="House Value Across Ocean Proximity Categories"
    )

    fig3.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # --------------------------------------------------------
    # SUMMARY STATISTICS
    # --------------------------------------------------------

    st.markdown("### 📊 Statistical Summary")

    numerical_columns = filtered_df.select_dtypes(
        include=np.number
    ).columns

    summary = filtered_df[numerical_columns].describe().T

    summary["median"] = filtered_df[numerical_columns].median()

    summary["IQR"] = (
        filtered_df[numerical_columns].quantile(0.75)
        -
        filtered_df[numerical_columns].quantile(0.25)
    )

    summary["skewness"] = filtered_df[numerical_columns].skew()

    summary["kurtosis"] = filtered_df[numerical_columns].kurtosis()

    st.dataframe(
        summary,
        use_container_width=True
    )


# ============================================================
# PAGE 2 — HYPOTHESIS TESTING
# ============================================================

elif page == "🧪  Statistical Lab":

    st.markdown(
        '<div class="section-title">Statistical Laboratory</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Test whether housing values differ significantly across locations.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-card">'
        '<b>Significance level:</b> α = 0.20'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # TEST 1
    # ========================================================

    st.markdown("""
    <div class="content-card">

    <h3>🧪 Hypothesis Test 1 — Two Group Comparison</h3>

    <p>
    Compare <b>median house values</b> between two
    ocean-proximity groups.
    </p>

    </div>
    """, unsafe_allow_html=True)

    group_options = sorted(
        df["ocean_proximity"].dropna().unique()
    )

    col1, col2 = st.columns(2)

    with col1:

        group1_default = group_options.index("<1H OCEAN") if "<1H OCEAN" in group_options else 0

        group1 = st.selectbox(
            "Select Group 1",
            group_options,
            index=group1_default
        )

    with col2:

        group2_default = group_options.index("INLAND") if "INLAND" in group_options else min(1, len(group_options) - 1)

        group2 = st.selectbox(
            "Select Group 2",
            group_options,
            index=group2_default
        )

    st.markdown(
        '<div class="info-card">'
        '<b>H₀:</b> There is no significant difference in '
        'median house values between the two groups.<br><br>'
        '<b>H₁:</b> There is a significant difference in '
        'median house values between the two groups.<br><br>'
        '<b>Significance level:</b> α = 0.20'
        '</div>',
        unsafe_allow_html=True
    )

    if group1 == group2:

        st.warning(
            "Please select two different groups."
        )

    else:

        data1 = df[
            df["ocean_proximity"] == group1
        ]["median_house_value"].dropna()

        data2 = df[
            df["ocean_proximity"] == group2
        ]["median_house_value"].dropna()

        # Shapiro
        sample1 = data1.sample(
            min(len(data1), 5000),
            random_state=42
        )

        sample2 = data2.sample(
            min(len(data2), 5000),
            random_state=42
        )

        shapiro1 = stats.shapiro(sample1)
        shapiro2 = stats.shapiro(sample2)

        # Levene
        levene_result = stats.levene(
            data1,
            data2
        )

        st.markdown("### 🔍 Assumption Checks")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(f"""
            <div class="metric-card">
            <div class="metric-label">SHAPIRO — GROUP 1</div>
            <div class="metric-value">{format_pvalue(shapiro1.pvalue)}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="metric-card">
            <div class="metric-label">SHAPIRO — GROUP 2</div>
            <div class="metric-value">{format_pvalue(shapiro2.pvalue)}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:

            st.markdown(f"""
            <div class="metric-card">
            <div class="metric-label">LEVENЕ P-VALUE</div>
            <div class="metric-value">{format_pvalue(levene_result.pvalue)}</div>
            </div>
            """, unsafe_allow_html=True)

        normal = (
            shapiro1.pvalue > ALPHA
            and
            shapiro2.pvalue > ALPHA
        )

        equal_variance = (
            levene_result.pvalue > ALPHA
        )

        # Test selection
        if normal:

            test_result = stats.ttest_ind(
                data1,
                data2,
                equal_var=equal_variance
            )

            test_name = "Two-Sample t-test"

        else:

            test_result = stats.mannwhitneyu(
                data1,
                data2,
                alternative="two-sided"
            )

            test_name = "Mann-Whitney U Test"

        st.markdown("### 🔬 Statistical Result")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"""
            <div class="metric-card">
            <div class="metric-label">SELECTED TEST</div>
            <div class="metric-value" style="font-size:20px;">
            {test_name}
            </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="metric-card">
            <div class="metric-label">P-VALUE</div>
            <div class="metric-value">
            {format_pvalue(test_result.pvalue)}
            </div>
            </div>
            """, unsafe_allow_html=True)

        if test_result.pvalue < ALPHA:

            st.markdown(
                '<div class="reject-box">'
                '🔴 REJECT H₀ — There is a statistically significant '
                'difference in median house values between the '
                'selected groups.'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="fail-box">'
                '🟢 FAIL TO REJECT H₀ — There is not enough evidence '
                'to conclude that the groups have different '
                'median house values.'
                '</div>',
                unsafe_allow_html=True
            )

    # ========================================================
    # TEST 2
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="content-card">

    <h3>📊 Hypothesis Test 2 — One-Way ANOVA</h3>

    <p>
    Determine whether mean house values differ across
    the ocean-proximity categories.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="info-card">'
        '<b>H₀:</b> All ocean-proximity groups have the same mean house value.<br><br>'
        '<b>H₁:</b> At least one group has a different mean house value.<br><br>'
        '<b>Significance level:</b> α = 0.20'
        '</div>',
        unsafe_allow_html=True
    )

    anova_data = [
        df[
            df["ocean_proximity"] == group
        ]["median_house_value"].dropna()
        for group in group_options
    ]

    anova_result = stats.f_oneway(
        *anova_data
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-label">F-STATISTIC</div>
        <div class="metric-value">
        {anova_result.statistic:.3f}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-label">P-VALUE</div>
        <div class="metric-value">
        {format_pvalue(anova_result.pvalue)}
        </div>
        </div>
        """, unsafe_allow_html=True)

    if anova_result.pvalue < ALPHA:

        st.markdown(
            '<div class="reject-box">'
            '🔴 REJECT H₀ — At least one ocean-proximity group '
            'has a significantly different mean house value.'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="fail-box">'
            '🟢 FAIL TO REJECT H₀ — There is not enough evidence '
            'to conclude that the group means differ.'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# PAGE 3 — PREDICTION & DIAGNOSTICS
# ============================================================

else:

    st.markdown(
        '<div class="section-title">Property Predictor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Estimate California house values using an Ordinary Least Squares model.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MODEL
    # --------------------------------------------------------

    target = "median_house_value"

    predictors = [
        "median_income",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "latitude",
        "longitude"
    ]

    model_data = df[
        predictors + [target]
    ].dropna()

    X = model_data[predictors]

    y = model_data[target]

    X_constant = sm.add_constant(X)

    model = sm.OLS(
        y,
        X_constant
    ).fit()

    # --------------------------------------------------------
    # MODEL KPIs
    # --------------------------------------------------------

    st.markdown("### 📈 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-icon">🎯</div>
        <div class="metric-label">R²</div>
        <div class="metric-value">{model.rsquared:.3f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-icon">📐</div>
        <div class="metric-label">ADJUSTED R²</div>
        <div class="metric-value">{model.rsquared_adj:.3f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-icon">📊</div>
        <div class="metric-label">OBSERVATIONS</div>
        <div class="metric-value">{int(model.nobs):,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-icon">🔢</div>
        <div class="metric-label">PREDICTORS</div>
        <div class="metric-value">{len(predictors)}</div>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # INPUT AREA
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="content-card">

    <h3>🏠 Property Details</h3>

    <p style="color:#64748b;">
    Enter housing characteristics below to generate a live
    median house value prediction.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        median_income = st.number_input(
            "💰 Median Income",
            min_value=float(df["median_income"].min()),
            max_value=float(df["median_income"].max()),
            value=float(df["median_income"].median()),
            step=0.001,
            format="%.3f"
        )

        housing_age = st.number_input(
            "🏚️ Housing Median Age",
            min_value=int(df["housing_median_age"].min()),
            max_value=int(df["housing_median_age"].max()),
            value=int(round(df["housing_median_age"].median())),
            step=1,
            format="%d"
        )

        total_rooms = st.number_input(
            "🚪 Total Rooms",
            min_value=int(df["total_rooms"].min()),
            max_value=int(df["total_rooms"].max()),
            value=int(round(df["total_rooms"].median())),
            step=1,
            format="%d"
        )

        total_bedrooms = st.number_input(
            "🛏️ Total Bedrooms",
            min_value=int(df["total_bedrooms"].min()),
            max_value=int(df["total_bedrooms"].max()),
            value=int(round(df["total_bedrooms"].median())),
            step=1,
            format="%d"
        )

    with col2:

        population = st.number_input(
            "👥 Population",
            min_value=int(df["population"].min()),
            max_value=int(df["population"].max()),
            value=int(round(df["population"].median())),
            step=1,
            format="%d"
        )

        households = st.number_input(
            "🏘️ Households",
            min_value=int(df["households"].min()),
            max_value=int(df["households"].max()),
            value=int(round(df["households"].median())),
            step=1,
            format="%d"
        )

        latitude = st.number_input(
            "📍 Latitude",
            min_value=float(df["latitude"].min()),
            max_value=float(df["latitude"].max()),
            value=float(df["latitude"].median()),
            step=0.001,
            format="%.3f"
        )

        longitude = st.number_input(
            "📍 Longitude",
            min_value=float(df["longitude"].min()),
            max_value=float(df["longitude"].max()),
            value=float(df["longitude"].median()),
            step=0.001,
            format="%.3f"
        )

    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    input_data = pd.DataFrame({
        "median_income": [median_income],
        "housing_median_age": [housing_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "latitude": [latitude],
        "longitude": [longitude]
    })

    input_constant = sm.add_constant(
        input_data,
        has_constant="add"
    )

    prediction = model.get_prediction(
        input_constant
    )

    prediction_summary = prediction.summary_frame(
        alpha=0.05
    )

    predicted_value = prediction_summary[
        "mean"
    ].iloc[0]

    lower = prediction_summary[
        "obs_ci_lower"
    ].iloc[0]

    upper = prediction_summary[
        "obs_ci_upper"
    ].iloc[0]

    st.markdown(f"""
    <div class="prediction-card">

    <div class="prediction-label">
    ESTIMATED MEDIAN HOUSE VALUE
    </div>

    <div class="prediction-value">
    ${predicted_value:,.0f}
    </div>

    <div class="prediction-range">
    95% Prediction Interval:
    ${lower:,.0f} — ${upper:,.0f}
    </div>

    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # DIAGNOSTICS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Model Health</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Residual diagnostics used to evaluate the statistical model.'
        '</div>',
        unsafe_allow_html=True
    )

    fitted = model.fittedvalues

    residuals = model.resid

    # Residual vs Fitted

    st.markdown("### 📉 Residuals vs Fitted Values")

    fig_res = px.scatter(
        x=fitted,
        y=residuals,
        labels={
            "x": "Fitted Values",
            "y": "Residuals"
        },
        title="Residuals vs Fitted Values",
        opacity=0.45
    )

    fig_res.add_hline(
        y=0,
        line_dash="dash"
    )

    fig_res.update_layout(
        template="plotly_white",
        height=470
    )

    st.plotly_chart(
        fig_res,
        use_container_width=True
    )

    # --------------------------------------------------------
    # QQ PLOT
    # --------------------------------------------------------

    st.markdown("### 📐 Q-Q Plot")

    fig_qq = sm.qqplot(
        residuals,
        line="45",
        fit=True
    )

    fig_qq.figure.set_size_inches(
        10,
        5
    )

    st.pyplot(
        fig_qq.figure,
        use_container_width=True
    )

    # --------------------------------------------------------
    # JARQUE BERA
    # --------------------------------------------------------

    jb = stats.jarque_bera(
        residuals
    )

    st.markdown("### 🧪 Jarque-Bera Normality Test")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-label">JB STATISTIC</div>
        <div class="metric-value">
        {jb.statistic:.3f}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-label">P-VALUE</div>
        <div class="metric-value">
        {format_pvalue(jb.pvalue)}
        </div>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # VIF
    # --------------------------------------------------------

    st.markdown("### 🔍 Multicollinearity — VIF")

    vif_data = pd.DataFrame()

    vif_data["Feature"] = X.columns

    vif_data["VIF"] = [
        round(variance_inflation_factor(
            X.values,
            i
        ), 3)
        for i in range(X.shape[1])
    ]

    vif_data["VIF"] = vif_data["VIF"].round(3)

    st.dataframe(
        vif_data,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # OLS COEFFICIENTS
    # --------------------------------------------------------

    st.markdown("### 📋 OLS Coefficients")

    coefficient_table = pd.DataFrame({
        "Coefficient": model.params.round(3),
        "P-value": model.pvalues.apply(format_pvalue),
        "95% CI Lower": model.conf_int()[0].round(3),
        "95% CI Upper": model.conf_int()[1].round(3)
    })

    st.dataframe(
        coefficient_table,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🏠 CasaVista Housing Intelligence &nbsp;•&nbsp;
Statistical Modeling with Python &nbsp;•&nbsp;
M.Sc. Data Science

</div>
""", unsafe_allow_html=True)