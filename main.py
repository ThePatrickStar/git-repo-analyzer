from utils import *
from repo import Repository as Repo

from args import ArgParser


def main():
    parser = ArgParser(description='Analyze a target git repository.')
    parser.add_argument('-kfc', help='Path to the keyword filter file to filter commit messages.')
    parser.add_argument('target_path', help='Path to the target repository.')

    args = parser.parse_args()
    print args
    # TODO: possibly check the validity of the target path here

    # repo = Repo(args.target_path)
    #
    # repo.commit_list()


if __name__ == '__main__':
    main()
