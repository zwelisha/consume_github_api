import requests as reqs
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
import os

GITHUB_NAME = os.environ.get("GITHUB_NAME")
GITHUB_PASS = os.environ.get("GITHUB_PASSWORD")
BASE_URL = "https://api.github.com"


def list_prs_between_two_dates(
    repo_owner: str, repo_name: str, start_date: str, end_date: str
):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    response = reqs.get(url, auth=HTTPBasicAuth(GITHUB_NAME, GITHUB_PASS))
    print(response.status_code)
    last_pull = response.json()
    return last_pull
# test comment 
if __name__ == "__main__":
    print(
        list_prs_between_two_dates(
            "Umuzi-org", "utilities", "2020-03-30T08:39:32Z", "2020-04-10T08:39:32Z"
        )
    )
