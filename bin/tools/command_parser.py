import argparse


class Parser:

    def __init__(self):
        self.__parser = argparse.ArgumentParser()

    def get_args(self):
        self.__parser.add_argument('-t', action='store', dest='theme',
                                   help='Change the Zsh theme')
        self.__parser.add_argument("--alias", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   help="Create an alias.")
        self.__parser.add_argument("--path", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   help="Create path.")
        self.__parser.add_argument("--default", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   help="Restores the zshrc to its default state.")
        self.__parser.add_argument("-a", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   action='store', dest='alias',
                                   help="Create an alias.")
        self.__parser.add_argument("-d", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   action='store', dest='delete',
                                   help="delete an alias.")
        self.__parser.add_argument("-c", type=self.__bool_parameter, nargs='?',
                                   const=True, default=False,
                                   action='store', dest='clear',
                                   help="clears all aliases.")
        self.__parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        return self.__parser.parse_args()

    def __bool_parameter(self, value):
        if isinstance(value, bool):
            return value
        if value.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif value.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
