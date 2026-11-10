import requests

username = input("Enter GitHub username: ").strip()
url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url, timeout=10, headers={"Accept": "application/json"})
    print("Status code:", response.status_code)

    if response.status_code == 404:
        print(f"User '{username}' does not exist.")
    else:
        response.raise_for_status()
        data = response.json()

        print("Login:", data.get("login", "N/A"))
        print("Name:", data.get("name", "N/A"))
        print("Public Repositories:", data.get("public_repos", "N/A"))
        print("Followers:", data.get("followers", "N/A"))
        print("Following:", data.get("following", "N/A"))
        print("Created At:", data.get("created_at", "N/A"))

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.JSONDecodeError:
    print("The server did not return valid JSON.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

