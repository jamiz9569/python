import requests

language = input("Enter programming language: ").strip()

if not language:
    print("Please enter a programming language.")
else:
    params = {
        "q": f"language:{language}",
        "sort": "stars",
        "order": "desc"
    }
    url = "https://api.github.com/search/repositories"

    try:
        response = requests.get(url, params=params, timeout=10, headers={"Accept": "application/json"})
        response.raise_for_status()

        data = response.json()
        items = data.get("items", [])

        if not items:
            print(f"No repositories found for language: {language}")
        else:
            print("Search URL:", response.url)
            for repo in items[:5]:
                print("-" * 40)
                print("Name:", repo.get("full_name", "N/A"))
                print("Description:", repo.get("description") or "No description")
                print("Stars:", repo.get("stargazers_count", "N/A"))
                print("Repository URL:", repo.get("html_url", "N/A"))

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    except ValueError:
        print("Invalid JSON response.")