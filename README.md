# Group Name: lab04-TeamX-panda

## Who Did What

| Team Member | GitHub Username | Contribution |
|---|---|---|
| Hein Zaw Lin | 6705140038 | Deposit tests in `test_deposit.py` |
| Aye Than Tin | 6705140074 | Withdrawal tests in `test_withdraw.py` |
| Aung Myo Hlaing | 6705140040 | Teardown tests in `test_teardown.py` |
| Hein Thura Naung | IvannCoder | Shared `funded_account` fixture in `conftest.py` and README merge resolution |

## Our Merge Conflict

The conflict markers were `<<<<<<< HEAD`, `=======`, and `>>>>>>> <branch>`. Both branches edited the same contributor section in `README.md`, so Git could not determine how to combine the overlapping edits or which table entries to keep. The team kept all members' contributions in one complete table, then committed and pushed the resolved README.

## Git Contribution Summary

Output of `git shortlog -sn`:

```text
	8  6705140040
	4  Aye Than Tin
	3  6705140038
	1  Hein Thura Naung (Ivan)
	1  Your Preferred Name
```

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?** The remote branch had commits from teammates that were missing from my local branch, so Git rejected my push to prevent overwriting their work. I pulled and merged the remote changes, resolved the README conflict, committed the result, and pushed again.
2. **Why could Git not resolve the README conflict automatically?** Both branches changed overlapping lines in the same README section. Git could not infer how the team wanted those edits combined, so we chose to keep all contribution rows.
3. **What is the difference between committing and pushing?** A commit saves a snapshot in the local repository. A push uploads local commits to the remote repository so teammates can access them.
4. **How do fixtures reduce duplicated setup code in tests?** A fixture creates reusable test setup once and supplies it to each test that requests it. This avoids repeating object creation and keeps tests focused on the behavior being checked.

## Git Command Reference

| Command | Purpose |
|---|---|
| `git clone <url>` | Create a local copy of a repository |
| `git config user.name "..."` | Set the name attached to your commits |
| `git status` | View changes, staged files, and suggestions |
| `git diff` | View uncommitted changes |
| `git add <file>` | Stage a file for the next commit |
| `git commit -m "..."` | Save a snapshot in your local repository |
| `git push` | Upload commits to GitHub |
| `git pull` | Download teammates' latest changes |
| `git log --oneline --graph` | View commit history |
| `git show HEAD` | Show the latest commit in detail |
| `git restore <file>` | Discard uncommitted changes |
| `git merge --abort` | Cancel an unfinished merge |
| `git shortlog -sn` | Count commits by contributor |
| `git remote -v` | Show connected repositories |

## GitHub Repository

https://github.com/6705140040/lab04-TeamX-Panda