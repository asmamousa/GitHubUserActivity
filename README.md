# GitHubUserActivity
A command-line script to fetch the recent activity of a GitHub user and display it in the terminal, built as a solution for the assignment: https://roadmap.sh/projects/github-user-activity

📌 Features

* Fetches activity from the GitHub Events API
* Uses no external libraries — only Python’s standard modules
* Displays events in a clean, human-readable format
*Handles common GitHub event types:
Push events
Create events
Issues
Stars (WatchEvent)
Forks
Pull requests

Shows descriptive output like:

- Pushed 3 commits to octocat/Hello-World
- Created a new branch 'main' in octocat/Hello-World
- Starred octocat/Hello-World

🚀 How to Use
Run the script:
python handle_user_input.py
or
python3 handle_user_input.py

📝 Command
github-activity <username>

📌 Example
github-activity asmamousa
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/GitHubUserActivity
- Created branch 'main' in asmamousa/GitHubUserActivity
- Pushed 1 commit to asmamousa/TaskTrackerCLI
