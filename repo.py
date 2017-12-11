from git import Repo
import difflib
from git.compat import (
    defenc,
    PY3
)
import re

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

    def commit_list_filter(self, keywords, branch_name='master'):

        commits = list(self.repo.iter_commits(branch_name))

        commits_no = len(commits)

        for counter, commit in enumerate(commits):

            matched = False
            for keyword in keywords:
                pattern = re.compile(keyword)
                match = re.search(pattern, commit.message)
                if match:
                    matched = True
                    break

            if matched:
                info(commit.message)
                # we are looping from the newest commit to the oldest
                if counter < commits_no - 1:
                    diffs = commit.diff(commits[counter+1], create_patch=True)
                    for diff in diffs:
                        ok(diff.diff.decode(defenc))

            else:
                warn(commit.message)
