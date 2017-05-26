import sys
sys.path.append("./PyGithub");
from github import Github

import getpass
import argparse

from github import Github
from github import GithubException

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


parser = argparse.ArgumentParser(description='List all repos for an org')
parser.add_argument('orgName',help='github Organization name')
parser.add_argument('repoName',help='The Target Repo Name - Example: ScottNewRepo')
parser.add_argument('branchName',help='The Branch to Protect')
args = parser.parse_args()

# this will need to be cleaned up later perhaps input as arguments
try:
    g = Github("sraignerSmarsh", "024b1b16c34dfa93da1e26c45e1465d9cb7f8ed0")
except GithubException as ghe:
    print "***Credentials Error"
    print(ghe)
    exit()

the_user = g.get_user()

orgName=args.orgName
repoName = args.repoName
branchName = args.branchName


try:
    org = g.get_organization(orgName)
except GithubException as ghe:
    print(ghe)
    exit()

try:
    my_repo = org.get_repo(str(repoName))
except GithubException as ghe:
    print(ghe)
    print "Input " + "*" + orgName + "*" + repoName + "*" + branchName
    exit()

try:
   protect_branch(my_repo,branchName)
except GithubException as ghe:
    print(ghe)
