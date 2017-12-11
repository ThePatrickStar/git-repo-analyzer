from utils import *


class KeywordCommitFilter:

    def __init__(self, path):
        self.keywords = []
        with open(path) as keyword_file:
            lines = keyword_file.readlines()

            for line in lines:
                line = line.strip()
                if line not in self.keywords:
                    self.keywords.append(line)
