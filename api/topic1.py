import requests

# Public endpoint that returns a random joke in JSON format.
url = "https://v2.jokeapi.dev/joke/Any?type=twopart"

try:
    # Send the API request with a timeout and a JSON accept header.
    response = requests.get(url, timeout=10, headers={"Accept": "application/json"})
    print("Status code:", response.status_code)

    # Stop execution if the server responds with an HTTP error.
    response.raise_for_status()

    # Convert the response body into a Python dictionary.
    data = response.json()

    # If the API reports an error, show the message from the service.
    if data.get("error"):
        print("The API returned an error:", data.get("message", "Unknown error"))
    elif data.get("type") == "twopart":
        # Two-part jokes include a setup and a delivery/punchline.
        print("Joke:", data.get("setup", "Unknown setup"))
        print("Answer:", data.get("delivery") or data.get("punchline", "Unknown answer"))
    else:
        # Some jokes are returned as a single string field.
        print("Joke:", data.get("joke", "No joke available."))

except requests.exceptions.HTTPError as e:
    # Handle failed HTTP responses such as 404 or 500.
    print("HTTP Error:", e)

except requests.exceptions.JSONDecodeError:
    # The server did not return valid JSON.
    print("The server did not return valid JSON.")

except requests.exceptions.Timeout:
    # The request did not finish in time.
    print("Request timed out.")

except requests.exceptions.RequestException as e:
    # Catch any other request-related errors.
    print("Request failed:", e)