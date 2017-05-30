
import sys
sys.path.append("./PyGithub");
from github import Github

import getpass
import argparse

from github import Github
from github import GithubException

parser = argparse.ArgumentParser(description='Get List of Repos')
parser.add_argument('userName',help='your github username')
parser.add_argument('accessToken',help='QAuth access token')
parser.add_argument('orgName',help='github Organization name')
parser.add_argument('repoName',help='The Target Repo Name - Example: ScottNewRepo')
args = parser.parse_args()

userName=args.userName
accessToken=args.accessToken
orgName=args.orgName
repoName = args.repoName

try:
    g = Github(userName,accessToken)
except GithubException as ghe:
    print(ghe)
    exit()

try:
    org = g.get_organization(orgName)
except GithubException as ghe:
    print(ghe)

try:
    org.create_repo(
        repoName, # name -- string
        "New repo, created using PyGithub", # description -- string
        "http://www.example.org", # homepage -- string
        True, # private -- bool
        True, # has_issues -- bool
        True, # has_wiki -- bool
        True, # has_downloads -- bool
        auto_init=True,
        gitignore_template="Python")

except GithubException as ghe:
    print(ghe)


