from dotenv import load_dotenv
import os
from GitHubRequestor import *
load_dotenv()


requestor = GitHubRequestor(os.getenv("GitHubToken"))

repo = "YubaNeupane/LIbarary-Management-System"


content = requestor.getFileContentsFromRepo(repo)
requestor.downloadContents(repo, content)
