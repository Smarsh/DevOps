# Github utilities

This repository contains python scripts to make changes to Smarshes github repos.

## Scripts 

### Installation 

- clone the repository ->  git clone https://github.com/Smarsh/DevOps
- install python version 2.7.X or higher 
	- 'brew install python'
- install pyGitHub 
	- 'brew install pyGitHub'

### ProtectMaster.py

#### Usage 

usage: ProtectMaster.py [-h] userName accessToken orgName repoName branchName

Protect the [Master|other] branch of a Repo

```
positional arguments:
  userName     your github username
  accessToken  QAuth access token
  orgName      github Organization name
  repoName     The Target Repo Name - Example: ScottNewRepo
  branchName   The Branch to Protect

optional arguments:
  -h, --help   show this help message and exit
```

##### Example:

```
  python ProtectMaster.py  sraignerSmarsh 04XXXXXXXXXXXXXXXXXXXXX9049af15db3f82704 Smarsh ScottNewRepo  master
```

### GetRepoList.py

#### Usage 

```
usage: GetRepoList.py [-h] userName accessToken orgName repoName branchName

Get List of Repos

positional arguments:
  userName     your github username
  accessToken  QAuth access token
  orgName      github Organization name
  repoName     The Target Repo Name - Example: ScottNewRepo
  branchName   The Branch to Protect

optional arguments:
  -h, --help   show this help message and exit

```

##### Example:

```
  python ProtectMaster.py  sraignerSmarsh 04XXXXXXX7xxxxx0c45XXXXXXXXXX15db3f8XXXX4 Smarsh ScottNewRepo  master
```

### CreateBlankRepo.py

#### User

```
usage: CreateBlankRepo.py [-h] userName accessToken orgName repoName

Get List of Repos

positional arguments:
  userName     your github username
  accessToken  QAuth access token
  orgName      github Organization name
  repoName     The Target Repo Name - Example: ScottNewRepo

optional arguments:
  -h, --help   show this help message and exit
```

##### Example:
```
python CreateBlankRepo.py sraignerSmarsh 046aa49276ae120c45487169049af15db3f82704 Smarsh ScottNewRepo2
```
