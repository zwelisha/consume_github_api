import os
import requests
from requests.auth import HTTPBasicAuth

GITHUB_NAME = os.environ.get("GITHUB_NAME")
GITHUB_PASS = os.environ.get("GITHUB_PASS")
API_BASE_URL = "https://api.github.com"


def get_pr_time_to_first_review(repo_owner: str, repo_name: str, pull_number: int):
    url = f"{API_BASE_URL}/repos/{repo_owner}/{repo_name}/pulls/{pull_number}/reviews"
    response = requests.get(url, auth=HTTPBasicAuth(GITHUB_NAME, GITHUB_PASS))
    status = response.status_code
    if status == 404:
        raise Exception("Pull request reviews not found!")
    if status == 401:
        raise Exception("Access denied!")
    if status == 200:
        try:
            reviews = response.json()
            if len(reviews) == 0:
                return None
            first_review_time = reviews[0]["submitted_at"]
        except:
            raise Exception("unknown error occured!")
        else:
            return first_review_time
    return None


if __name__ == "__main__":
    print(get_pr_time_to_first_review("Umuzi-org", "utilities", 32))
# def get_pull_requests(repo_name, start_date, end_date):
#     '''
#     The function should output a list or array of pull requests on the repo
#     such that the PRs were created, updated, merged or closed between the given two dates.
#     '''
