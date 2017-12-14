from git import Repo
import difflib
from git.compat import (
    defenc,
    PY3
)
import re

from utils import *
from report_generator import *


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

        commit_dicts = []

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
                diff_list = []
                if counter < commits_no - 1:
                    diffs = commit.diff(commits[counter+1], create_patch=True)
                    for diff in diffs:
                        added_file = ''
                        if diff.a_path is not None:
                            added_file = '+++ '+diff.a_path+'\\n'
                        deleted_file = ''
                        if diff.b_path is not None:
                            deleted_file = '--- '+diff.b_path+'\\n'
                        try:
                            content = deleted_file+added_file+diff.diff.encode('utf-8').replace("'", '"').replace('\n', '\\n')
                            diff_list.append({
                                'id': str(len(diff_list)),
                                'content': content,
                            })
                        except (UnicodeDecodeError, UnicodeEncodeError) as e:
                            danger(e)
                        # danger(diff)
                        # ok(diff.diff.decode(defenc))
                try:
                    commit_dict = {
                        'id': str(len(commit_dicts)),
                        'binsha': str(commit),
                        'committed_datetime': str(commit.committed_datetime),
                        'committer': str(commit.committer),
                        'msg': str(commit.message),
                        'diffs': diff_list,
                    }
                    # danger(commit_dict['diffs'])
                    # danger(len(commit_dict['diffs']))
                    commit_dicts.append(commit_dict)
                except (UnicodeEncodeError, UnicodeDecodeError) as e:
                    danger(e)

            else:
                warn(commit.message)

        generate_commit_list(commit_dicts)

