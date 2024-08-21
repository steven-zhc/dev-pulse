from src.github_api import get_repo_info

def test_get_repo_info():
    repo_info = get_repo_info('octocat/Hello-World')
    assert repo_info is not None
    assert repo_info['name'] == 'Hello-World'
    assert 'stars' in repo_info
    assert 'forks' in repo_info
