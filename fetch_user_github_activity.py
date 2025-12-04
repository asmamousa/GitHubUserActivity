import json
import shlex
import ssl
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

def format_event(event):
    event_type = event["type"]
    repo = event.get("repo", {}).get("name", "unknown repo")

    if event_type == "PushEvent":
        commit_count = len(event["payload"].get("commits", [])) if "commits" in event["payload"] else 1
        return f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo}"

    if event_type == "IssuesEvent":
        action = event["payload"].get("action", "performed an action")
        return f"- {action.capitalize()} an issue in {repo}"

    if event_type == "CreateEvent":
        ref_type = event["payload"].get("ref_type", "")
        ref = event["payload"].get("ref", "")
        if ref_type == "repository":
            return f"- Created new repository {repo}"
        else:
            return f"- Created {ref_type} '{ref}' in {repo}"

    if event_type == "WatchEvent":
        return f"- Starred {repo}"

    if event_type == "ForkEvent":
        forked_to = event["payload"]["forkee"]["full_name"]
        return f"- Forked {repo} to {forked_to}"

    if event_type == "PullRequestEvent":
        action = event["payload"].get("action", "updated")
        return f"- {action.capitalize()} a pull request in {repo}"

    return f"- Performed {event_type} in {repo}"


def display_activity(events):
    for event in events:
        print(format_event(event))


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
        display_activity(res)

    else:
        print ('Please use github-activity <username>')