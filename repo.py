from git import Repo

from utils import *


class Repository:

    def __init__(self, path):
        try:
            self.repo = Repo(path)
        except Exception as e:
            danger(type(e).__name__+': '+e.message)
            danger('invalid repository path: %s' % path)

    def commit_list(self, branch_name='master'):
        commits = list(self.repo.iter_commits(branch_name))

        for commit in commits:
            info(commit.message)
