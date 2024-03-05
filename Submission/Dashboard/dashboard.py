import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("https://raw.githubusercontent.com/Sisilia14/dicoding/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/Sisilia14/dicoding/main/hour.csv")

# Combine data
all_df = pd.concat([day_df, hour_df], axis=0)

# Function to plot bikeshare rides by weather
def plot_weatherly_users():
    weatherly_users_df = day_df.groupby("weathersit").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index()

    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x="weathersit", y="cnt", data=weatherly_users_df, ax=ax)
    ax.set_xlabel("Weather")
    ax.set_ylabel("Total Rides")
    ax.set_title("Count of bikeshare rides by Weather")
    return fig, ax

def plot_hourly_users():
    hourly_users_df = hour_df.groupby("hr").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index()

    fig, ax = plt.subplots(figsize=(16,6))
    sns.lineplot(x="hr", y="casual", data=hourly_users_df, label='Casual', ax=ax)
    sns.lineplot(x="hr", y="registered", data=hourly_users_df, label='Registered', ax=ax)
    x = range(24)
    ax.set_xticks(x)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Total Rides")
    ax.set_title("Count of bikeshare rides by hour")
    ax.axvline(x=8, color='gray', linestyle='--')
    ax.axvline(x=17, color='gray', linestyle='--')
    ax.legend(loc='upper right', fontsize=14)
    return fig, ax


# Sidebar
st.sidebar.title('Dashboard Navigation')
page = st.sidebar.radio('Select a page:', ['Weatherly Users', 'Hourly Users'])

# Main content
st.title('Bikeshare Data Dashboard')

if page == 'Weatherly Users':
    st.header('Count of bikeshare rides by Weather')
    fig, _ = plot_weatherly_users()
    st.pyplot(fig)

elif page == 'Hourly Users':
    st.header('Count of bikeshare rides by Hour')
    fig, _ = plot_hourly_users()
    st.pyplot(fig)
