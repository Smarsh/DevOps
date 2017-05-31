import sys
sys.path.append("./PyGithub");
from github import Github
import getpass
import argparse

parser = argparse.ArgumentParser(description='Get List of Repos')
parser.add_argument('userName',help='your github username')
parser.add_argument('accessToken',help='QAuth access token')
args = parser.parse_args()

userName=args.userName
accessToken=args.accessToken

# this will need to be cleaned up a little ( use try etc. )
g = Github(userName, accessToken)

#print "**List of Repos**"
for repo in g.get_user().get_repos():
    print repo.name




