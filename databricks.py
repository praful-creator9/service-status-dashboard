import requests

def fetch_databricks_status():
    url = "https://status.databricks.com/api/v2/status.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['status']['description'], data['status']['indicator']
        else:
            return "Failed to fetch", "red"
    except Exception as e:
        return f"Error: {str(e)}", "red"
