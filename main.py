from dotenv import load_dotenv
import os
from GitHubRequestor import *
load_dotenv()


requestor = GitHubRequestor(os.getenv("GitHubToken"))

repo = "PyGithub/PyGithub"


requestor.getFileContentsFromRepo(repo)
