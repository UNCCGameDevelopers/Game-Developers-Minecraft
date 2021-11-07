""" simple utility to copy files into a hard coded remote server."""
import os
import sys

HOST = "GDCMinecraft"
DESTINATION_ROOT = f"{HOST}:~/minecraft"

def run(command):
    """ Run a system command and ensure that it completed. """
    print(command)

    exit_code = os.system(command)

    if exit_code != 0:
        raise RuntimeError(f"{command} completed with non-zero exit code {exit_code}")

def copy_file(file_name):
    """ Copy a file over to the destination server."""
    _, path = file_name.split("server/")

    final_destination = f"{DESTINATION_ROOT}/{path}"

    directory = os.path.dirname(final_destination.split(":")[-1])

    run(f"ssh {HOST} 'mkdir -p {directory}'")
    run(f"scp {file_name} {final_destination}")


def main():
    """ Main entrypoint for the copy utility.

    Reads a series of file names from stdin and copies them to the remote server.
    """
    for file_name in sys.stdin:
        copy_file(file_name.strip())

if __name__ == "__main__":
    main()

