from utils import *
from args import ArgParser


def main():
    parser = ArgParser(description='Analyze a target git repository.')
    parser.add_argument('target_path', help='Path to the target repository.')

    args = parser.parse_args()
    # TODO: possibly check the validity of the target path here


if __name__ == '__main__':
    main()
