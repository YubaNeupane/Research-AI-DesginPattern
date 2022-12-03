from github import Github
import os
import requests


class GitHubRequestor:
    def __init__(self, token):
        self.githubClient = Github(token)

    def getFileContentsFromRepo(self, repo):
        repo = self.githubClient.get_repo(repo)
        contents = repo.get_contents("")
        returnData = []
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                returnData.append(file_content)

        return returnData

    def __makeProjectDirectory(self, repoName):
        if not os.path.exists("gitHubProjects"):
            os.mkdir("gitHubProjects")
            print("Directory ", "gitHubProjects",  " Created ")

        if not os.path.exists("gitHubProjects/"+repoName):
            os.makedirs("gitHubProjects/"+repoName)
            print("Directory ", "gitHubProjects/"+repoName,  " Created ")
            return True
        else:
            print("Directory ", "gitHubProjects/"+repoName,
                  " already exists, delete dictionary and try again")
            return True

    def downloadContents(self, repoName, contents):
        if (self.__makeProjectDirectory(repoName)):
            for content in contents:
                response = requests.get(content.download_url)

                os.makedirs(os.path.dirname("gitHubProjects/" +
                            repoName + "/"+content.path), exist_ok=True)
                with open("gitHubProjects/"+repoName + "/"+content.path, "wb") as f:
                    print("DOWNLOADING.....", content.path)
                    f.write(response.content)
