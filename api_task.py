import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Current User URL:", data["current_user_url"])
print("Repository URL:", data["repository_url"])