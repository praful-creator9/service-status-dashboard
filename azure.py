import requests

def fetch_azure_status():
    url = "https://status.azure.com/en-us/status"
    try:
        # Scraping logic or API calls here
        # Example:
        response = requests.get(url)
        if response.status_code == 200:
            return "Operational", "green"
        else:
            return "Failed to fetch", "red"
    except Exception as e:
        return f"Error: {str(e)}", "red"
