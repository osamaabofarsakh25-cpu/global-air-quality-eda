import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


#  Load final dataset
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
st.title(" Global Air Quality Dashboard")

df = pd.read_csv("data/air_quality_final.csv")

st.subheader("Preview of Dataset (Head 10)")
st.dataframe(df.head(10))

st.markdown("## Average Pollutant Levels by Country")

# Select columns for pollutant averages
pollutant_columns = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

# Compute average pollutants per country
# Compute average pollutants per country
country_pollutants = (
    df.groupby("Country")[pollutant_columns]
      .mean()
      .reset_index()
      .sort_values("PM2.5", ascending=False)
)

# Show only the top 20 countries or entire table if smaller
country_pollutants_top = country_pollutants.head(20)

st.dataframe(country_pollutants_top, use_container_width=True)


# PM2.5 AQI CATEGORY DISTRIBUTION
st.subheader("PM2.5 AQI Category Distribution in Top 3 Polluted Countries")

# compute top 3 polluted countries
top3 = df.groupby("Country")["PM2.5"].mean().nlargest(3).index.tolist()
df_top3 = df[df["Country"].isin(top3)]

# AQI Category counts
aqi_counts_top3 = (
    df_top3.groupby(["Country", "AQI_Category"])
    .size()
    .reset_index(name="PM2.5 Count")
)

# Bar chart
fig1 = px.bar(
    aqi_counts_top3,
    x="Country",
    y="PM2.5 Count",
    color="AQI_Category",
    barmode="group",
    title="PM2.5 AQI Category Distribution in Top 3 Polluted Countries",
)
st.plotly_chart(fig1, use_container_width=True)

# AQI Category Table
st.subheader("AQI Category Summary Table")
st.dataframe(aqi_counts_top3)


# Seasonal PM2.5 Variation
st.subheader("Seasonal PM2.5 Variation in Top 3 Polluted Countries")

seasonal_df = (
    df_top3.groupby(["Season", "Country"])["PM2.5"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    seasonal_df,
    x="Season",
    y="PM2.5",
    color="Country",
    barmode="group",
    title="Seasonal PM2.5 Variation in Top 3 Polluted Countries",
)

st.plotly_chart(fig2, use_container_width=True)


# Correlation Heatmap (Pollutants + Weather)
st.subheader("Correlation Heatmap for Air Pollutants and Weather Variables")

# Select only numeric environmental columns
numeric_cols = [
    "PM2.5", "PM10", "NO2", "SO2", "CO", "O3",
    "Temperature", "Humidity", "Wind Speed"
]

corr = df[numeric_cols].corr()

# Draw heatmap
fig3, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".3f", ax=ax)
plt.title("Correlation Heatmap for Air Pollutants and Weather Variables")

st.pyplot(fig3)
