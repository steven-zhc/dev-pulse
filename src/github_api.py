from github import Github
import os

# Authenticate using the token
token = os.getenv('GITHUB_TOKEN')
g = Github(token)

def get_repo_info(repo_name):
    try:
        repo = g.get_repo(repo_name)
        return {
            "name": repo.name,
            "description": repo.description,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "open_issues": repo.open_issues_count
        }
    except Exception as e:
        print(f"Error fetching repo: {e}")
        return None

def get_commits(repo_name):
    try:
        repo = g.get_repo(repo_name)
        commits = repo.get_commits()
        return [{"sha": commit.sha, "message": commit.commit.message} for commit in commits[:5]]
    except Exception as e:
        print(f"Error fetching commits: {e}")
        return []

def get_issues(repo_name):
    try:
        repo = g.get_repo(repo_name)
        issues = repo.get_issues(state='open')
        return [{"title": issue.title, "url": issue.html_url} for issue in issues[:5]]
    except Exception as e:
        print(f"Error fetching issues: {e}")
        return []

def get_pull_requests(repo_name):
    try:
        repo = g.get_repo(repo_name)
        pulls = repo.get_pulls(state='open')
        return [{"title": pr.title, "url": pr.html_url} for pr in pulls[:5]]
    except Exception as e:
        print(f"Error fetching pull requests: {e}")
        return []
