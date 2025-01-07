import requests

def fetch_aws_status():
    url = "https://status.aws.amazon.com/rss/all.rss"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse RSS (simplified example)
            # You can implement an XML parser to extract the status
            return "Operational", "green"
        else:
            return "Failed to fetch", "red"
    except Exception as e:
        return f"Error: {str(e)}", "red"
