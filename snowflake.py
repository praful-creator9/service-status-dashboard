import requests

def fetch_snowflake_status():
    url = "https://status.snowflake.com/api/v2/summary.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['status']['description'], data['status']['indicator']
        else:
            return "Failed to fetch", "red"
    except Exception as e:
        return f"Error: {str(e)}", "red"
