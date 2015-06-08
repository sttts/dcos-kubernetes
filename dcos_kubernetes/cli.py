"""DCOS Kubernetes Subcommand

Usage:
    dcos kubernetes --info

Options:
    --help           Show this screen
    --version        Show version
"""
import docopt
from dcos_kubernetes import constants


def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-kubernetes version {}'.format(constants.version))

    if args['kubernetes'] and args['--info']:
        print('DCOS Kubernetes subcommand')
    else:
        print(__doc__)
        return 1

    return 0
