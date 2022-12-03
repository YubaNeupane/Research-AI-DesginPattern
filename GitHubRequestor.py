from github import Github


class GitHubRequestor:
    def __init__(self, token):
        self.githubClient = Github(token)

    def getFileContentsFromRepo(self, repo):
        repo = self.githubClient.get_repo(repo)
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                print(file_content)
