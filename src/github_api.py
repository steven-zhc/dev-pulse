from src.models import Repository, session
from github import Github, Auth
import os

# Authenticate using the token
token = os.getenv('GITHUB_TOKEN')
auth = Auth.Token(token)
g = Github(auth=auth)

def get_repo_info(repo_name):
    # Check if repo info is already stored in the database
    repo = session.query(Repository).filter_by(name=repo_name).first()
    if repo:
        return repo

    # Fetch from GitHub API if not found in the database
    try:
        repo_data = g.get_repo(repo_name)
        repo = Repository(
            name=repo_name,
            description=repo_data.description,
            stars=repo_data.stargazers_count,
            forks=repo_data.forks_count,
            open_issues=repo_data.open_issues_count
        )
        session.add(repo)
        session.commit()
        return repo
    except Exception as e:
        print(f"Error fetching repo: {e}")
        session.rollback()  # Rollback on error
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
