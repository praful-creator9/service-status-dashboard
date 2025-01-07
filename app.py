import streamlit as st
import pandas as pd
import plotly.express as px
from service-status-dashboard.snowflake import fetch_snowflake_status
from service-status-dashboard.databricks import fetch_databricks_status
from service-status-dashboard.aws import fetch_aws_status
from service-status-dashboard.azure import fetch_azure_status
from service-status-dashboard.talend import fetch_talend_status

# Set page title and layout
st.set_page_config(page_title="Service Status Dashboard", layout="wide")

# Custom CSS (optional, to add a creative theme)
st.markdown("<style> .stApp {background-color: #f4f4f9; font-family: 'Arial';} </style>", unsafe_allow_html=True)

# Title and intro
st.title('🔧 Service Status Dashboard')
st.markdown("**Check the operational status of your cloud tools** like Snowflake, Databricks, AWS, Azure, and Talend.")

# Fetch the statuses
snowflake_status, snowflake_indicator = fetch_snowflake_status()
databricks_status, databricks_indicator = fetch_databricks_status()
aws_status, aws_indicator = fetch_aws_status()
azure_status, azure_indicator = fetch_azure_status()
talend_status, talend_indicator = fetch_talend_status()

# Display statuses with colors and indicators
status_data = {
    "Service": ["Snowflake", "Databricks", "AWS", "Azure", "Talend"],
    "Status": [snowflake_status, databricks_status, aws_status, azure_status, talend_status],
    "Indicator": [snowflake_indicator, databricks_indicator, aws_indicator, azure_indicator, talend_indicator],
}

status_df = pd.DataFrame(status_data)

# Create a color map for status indicators
color_map = {
    "green": "✅ Operational",
    "yellow": "⚠️ Degraded Performance",
    "red": "❌ Outage"
}

status_df['Status'] = status_df['Indicator'].map(color_map)

# Display status table
st.subheader("Service Status Overview")
st.dataframe(status_df.style.applymap(lambda v: 'background-color: green' if v == '✅ Operational' else
                                             'background-color: red' if v == '❌ Outage' else
                                             'background-color: yellow', subset=['Status']))

# Visualization of service statuses (e.g., pie chart)
fig = px.pie(status_df, names='Service', color='Status', title="Service Status Distribution")
st.plotly_chart(fig)

# Further enhancements: Display individual status with details
st.subheader("Service Details")
for service, status, indicator in zip(status_df["Service"], status_df["Status"], status_df["Indicator"]):
    st.markdown(f"**{service}**: {status}")
