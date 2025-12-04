import json
import shlex
import ssl
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def get_user_github_activity(request):

    context = ssl._create_unverified_context()

    try:
        with urlopen(request, context=context) as response:
            if response.status == 200:
                data = response.read().decode("utf-8")
                return json.loads(data)

    except HTTPError as e:
        print("HTTP Error:", e.code, e.reason)

    except URLError as e:
        print("URL Error:", e.reason)

while True:
    full_input = input('Enter your command:')
    command_parts = shlex.split(full_input)
    if command_parts[0] == 'exit':
        sys.exit(0)

    elif command_parts[0] == 'github-activity':
        if len(command_parts) < 2:
            print("ERROR: You must provide an argument")
            continue

        elif len(command_parts) > 2:
            print("ERROR: 'github-activity' command takes only one argument")
            continue

        username = command_parts[1]
        url = f"https://api.github.com/users/{username}/events"
        req = Request(url, headers={"User-Agent": "Python"})  # GitHub requires a User-Agent

        res = get_user_github_activity(req)
        print(res)

    else:
        print ('Please use github-activity <username>')