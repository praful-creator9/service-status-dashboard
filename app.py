import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch Snowflake status
def fetch_snowflake_status():
    url = "https://status.snowflake.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the status element on the page
    status = soup.find("div", {"class": "status"}).get_text().strip()
    
    if "operational" in status.lower():
        return "✅ Operational", "green"
    elif "degraded" in status.lower():
        return "⚠️ Degraded Performance", "yellow"
    else:
        return "❌ Outage", "red"

# Set page title and layout
st.set_page_config(page_title="Service Status Dashboard", layout="wide")

# Custom CSS for page styling
st.markdown("<style> .stApp {background-color: #f4f4f9; font-family: 'Arial';} </style>", unsafe_allow_html=True)

# Title and intro
st.title('🔧 Service Status Dashboard')
st.markdown("**Check the operational status of Snowflake.**")

# Fetch status for Snowflake
snowflake_status, snowflake_indicator = fetch_snowflake_status()

# Display status in a table
status_data = {
    "Service": ["Snowflake"],
    "Status": [snowflake_status],
    "Indicator": [snowflake_indicator],
}

# Create DataFrame
import pandas as pd
status_df = pd.DataFrame(status_data)

# Create a color map for status indicators
color_map = {
    "green": "✅ Operational",
    "yellow": "⚠️ Degraded Performance",
    "red": "❌ Outage"
}

status_df['Status'] = status_df['Indicator'].map(color_map)

# Display status table with conditional formatting
st.subheader("Service Status Overview")
st.dataframe(status_df.style.applymap(lambda v: 'background-color: green' if v == '✅ Operational' else
                                             'background-color: red' if v == '❌ Outage' else
                                             'background-color: yellow', subset=['Status']))

# Visualize the status in a pie chart
import plotly.express as px
fig = px.pie(status_df, names='Service', color='Status', title="Service Status Distribution")
st.plotly_chart(fig)

# Display individual status details
st.subheader("Service Details")
for service, status, indicator in zip(status_df["Service"], status_df["Status"], status_df["Indicator"]):
    st.markdown(f"**{service}**: {status}")
