from dotenv import load_dotenv
import os
import csv

from GitHubRequestor import *
load_dotenv()
requestor = GitHubRequestor(os.getenv("GitHubToken"))


def getReposFromCSV(csvFile='repos.csv'):
    repoNames = []
    with open('repos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            repoNames.append(row['RepoName'])

    return repoNames


repoNames = getReposFromCSV()

for repo in repoNames:
    print("DOWNLOADING FROM REPO: " + repo)
    content = requestor.getFileContentsFromRepo(repo)
    requestor.downloadContents(repo, content)
    print("DOWNLOAD COMPLETED --> " + repo)
    print()
