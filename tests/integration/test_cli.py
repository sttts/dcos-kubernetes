from common import exec_command


def test_help():
    returncode, stdout, stderr = exec_command(
        ['dcos-kubernetes', 'kubernetes', '--help'])

    assert returncode == 0
    assert stdout == b"""DCOS Kubernetes Example Subcommand

Usage:
    dcos kubernetes info

Options:
    --help           Show this screen
    --version        Show version
"""
    assert stderr == b''
