import requests

API_URL = "https://api.github.com/users/octocat"

# Fetch the Github User


def fetch_user():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        user_data = response.json()

        print(f"Name: {user_data['name']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    except requests.RequestException as error:
        print(f"Failed to fetch Github user: {error}")


if __name__ == "__main__":
    fetch_user()
