import sys
sys.path.append("./PyGithub");
from github import Github

import getpass
import argparse

from github import Github
from github import GithubException

# Example from Documentation
"""
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "continuous-integration/travis-ci"
    ]
  },
  "required_pull_request_reviews": {
    "dismissal_restrictions": {
      "users": [
        "octocat"
      ],
      "teams": [
        "justice-league"
      ]
    },
    "dismiss_stale_reviews": true
  },
  "enforce_admins": true,
  "restrictions": {
    "users": [
      "octocat"
    ],
    "teams": [
      "justice-league"
    ]
  }
}
"""


def protect_branch(self, branch):
    """
    :calls: `PATCH /repos/:owner/:repo/branches/:branch <https://developer.github.com/v3/repos/#enabling-and-disabling-branch-protection>`
    :param branch: string
    :rtype: None
    """
    post_parameters = {
        "protection": {
            "enabled": True,
            "required_status_checks" : {
                "enforcement_level": "everyone",
                "contexts": [
                    "required-status"
                ]
            }
		
        }
    }
    headers, data = self._requester.requestJsonAndCheck(
        "PATCH",
        self.url + "/branches/" + branch,
        input=post_parameters,
        headers={'Accept': 'application/vnd.github.loki-preview+json'}
    )

parser = argparse.ArgumentParser(description='Protect the Master branch of a Repo')
parser.add_argument('userName',help='your github username')
parser.add_argument('accessToken',help='QAuth access token')
parser.add_argument('orgName',help='github Organization name')
parser.add_argument('repoName',help='The Target Repo Name - Example: ScottNewRepo')
parser.add_argument('branchName',help='The Branch to Protect')
args = parser.parse_args()

userName=args.userName
accessToken=args.accessToken
orgName=args.orgName
repoName = args.repoName
branchName = args.branchName

#print "Input " + "*" + userName + "*" + accessToken + "*" + orgName + "*" + repoName + "*" + branchName

try:
    g = Github(userName,accessToken) 
except GithubException as ghe:
    print "***Credentials Error"
    print(ghe)
    exit()

the_user = g.get_user()

try:
    org = g.get_organization(orgName)
except GithubException as ghe:
    print(ghe)
    exit()

try:
    my_repo = org.get_repo(str(repoName))
except GithubException as ghe:
    print(ghe)
    exit()

try:
   protect_branch(my_repo,branchName)
except GithubException as ghe:
    print(ghe)
