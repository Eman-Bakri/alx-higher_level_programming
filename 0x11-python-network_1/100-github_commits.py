#!/usr/bin/python3
"""10 commits list"""


if __name__ == "__main__":
    import requests
    import sys

    def print_commits(i, commit_list):
        """
        List the commits, less than 10 commits
        """
        sha = commit_list[i].get('sha')
        commit = commit_list[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get('https://api.github.com/repos/' + owner +
                            '/' + repo + '/commits', headers=headers)
    commit_list = response.json()
    size = len(commit_list)
    if size < 10:
        for i in range(0, size):
            print_commits(i, commit_list)
    else:
        for i in range(0, 10):
            print_commits(i, commit_list)
