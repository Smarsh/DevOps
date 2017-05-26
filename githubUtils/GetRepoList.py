
from github import Github

# this will need to be cleaned up a little ( use try etc. )
g = Github("sraignerSmarsh", "024b1b16c34dfa93da1e26c45e1465d9cb7f8ed0")

#print "**List of Repos**"
for repo in g.get_user().get_repos():
    print repo.name



