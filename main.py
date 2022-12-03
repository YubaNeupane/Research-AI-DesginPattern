from GitHubRequestor import *
githubToken = "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"
requestor = GitHubRequestor(githubToken)

repo = "PyGithub/PyGithub"


requestor.getFileContentsFromRepo(repo)
