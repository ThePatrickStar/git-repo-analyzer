
def ascii_print(func):

    def print_wrapper(content):
        try:
            func(content)
        except (UnicodeDecodeError, UnicodeEncodeError) as e:
            danger(e)

    return print_wrapper


@ascii_print
def warn(content):
    print '\t\033[93m'+str(content)+'\033[0m'


@ascii_print
def ok(content):
    print '\t\033[92m'+str(content)+'\033[0m'


@ascii_print
def info(content):
    print '\t\033[94m'+str(content)+'\033[0m'


@ascii_print
def danger(content):
    print '\t\033[91m'+str(content)+'\033[0m'
