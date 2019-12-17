#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def create_files_for_heroku():
    try:
        with open("gs-account/accounts.json", 'w') as wf:
            wf.write("Hello")
    except:
        print("Error: That file cannot be found!")

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # for heroku only
    # subprocess.call("./deploy.sh")
    create_files_for_heroku()
    main()
