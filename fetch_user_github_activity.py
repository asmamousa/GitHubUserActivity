import shlex
import sys
from urllib.request import Request

from helper_functions import get_user_github_activity, display_activity

while True:
    user_input = input('Enter your command:')
    command_args = shlex.split(user_input)
    if command_args[0] == 'exit':
        sys.exit(0)

    elif command_args[0] == 'github-activity':
        if len(command_args) < 2:
            print("ERROR: You must provide an argument")
            continue

        elif len(command_args) > 2:
            print("ERROR: 'github-activity' command takes only one argument")
            continue

        username = command_args[1]
        url = f"https://api.github.com/users/{username}/events"
        req = Request(url, headers={"User-Agent": "Python"})  # GitHub requires a User-Agent

        res = get_user_github_activity(req)
        display_activity(res)

    else:
        print ('Please use github-activity <username>')