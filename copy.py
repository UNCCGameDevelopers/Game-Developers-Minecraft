""" simple utility to copy files into a hard coded remote server."""
import os
import sys

DESTINATION_ROOT = "GDCMinecraft:~/minecraft"

def run(command):
    """ Run a system command and ensure that it completed. """
    print(command)

    exit_code = os.system(command)

    if exit_code != 0:
        raise RuntimeError(f"{command} completed with non-zero exit code {exit_code}")

def copy_file(file_name):
    """ Copy a file over to the destination server."""
    _, path = file_name.split("server")

    run(f"scp {file_name} {DESTINATION_ROOT}/{path}")


def main():
    """ Main entrypoint for the copy utility.

    Reads a series of file names from stdin and copies them to the remote server.
    """
    for file_name in sys.stdin:
        copy_file(file_name.strip())

if __name__ == "__main__":
    main()

