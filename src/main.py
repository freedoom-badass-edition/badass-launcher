import os
from git import Repo

print("welcome to bad*ss launcher")
repo_url = "https://github.com/freedoom-badass-edition/freedoom-badass-edition.git"
repo = Repo.clone_from(repo_url, os.getcwd()+"/freedoom-badass-edition")
print("done")

