# GitHubUserActivity
A command-line script to fetch the recent activity of a GitHub user and display it in the terminal, built as a solution for the assignment: https://roadmap.sh/projects/github-user-activity

## 📌 Features

* Fetches activity from the GitHub Events API
* Uses no external libraries — only Python’s standard modules
* Displays events in a clean, human-readable format
* Handles common GitHub event types:
Push events
Create events
Issues
Stars (WatchEvent)
Forks
Pull requests

### Shows descriptive output like:
```bash

- Pushed 3 commits to octocat/Hello-World
- Created a new branch 'main' in octocat/Hello-World
- Starred octocat/Hello-World
```

## 🚀 How to Use
Run the script:
```bash
python fetch_user_github_activity.py
````

or

```bash
python3 fetch_user_github_activity.py
```

## 📝 Command
```bash
github-activity <username>
```

## 📌 Example
```bash
github-activity asmamousa
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Created branch 'main' in asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/TaskTrackerCLI
```
