import click
from src.github_api import get_repo_info, get_commits, get_issues, get_pull_requests
from src.models import session, Repository

@click.command()
@click.argument('repo_name', required=False)
def fetch_info(repo_name):
    """Fetch GitHub repository information."""
    if not repo_name:
        print("Repository name not provided. Retrieving all stored repositories.")
        repos = session.query(Repository).all()
        for repo in repos:
            print(f"Repository: {repo.name}, Stars: {repo.stars}, Forks: {repo.forks}")
        return

    info = get_repo_info(repo_name)
    if info:
        print(f"Repository: {info.name}")
        print(f"Description: {info.description}")
        print(f"Stars: {info.stars}, Forks: {info.forks}, Open Issues: {info.open_issues}")

        print("\nRecent Commits:")
        for commit in get_commits(repo_name):
            print(f"{commit['sha']}: {commit['message']}")

        print("\nOpen Issues:")
        for issue in get_issues(repo_name):
            print(f"{issue['title']} - {issue['url']}")

        print("\nOpen Pull Requests:")
        for pr in get_pull_requests(repo_name):
            print(f"{pr['title']} - {pr['url']}")
    else:
        print("Repository not found.")

if __name__ == '__main__':
    fetch_info()
