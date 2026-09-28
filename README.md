# Group Name: TeamX-Panda

## Who Did What

| Team Member | GitHub Username | Contribution |
|---|---|---|
| Hein Zaw Lin | 6705140038 | Deposit tests in `test_deposit.py` |
| Aye Than Tin | 6705140074 | Withdrawal tests in `test_withdraw.py` |
| Aung Myo Hlaing | 6705140040 | Teardown tests in `test_teardown.py` |
| Chan Myae Thaw Tar | 6705140048 | Shared tests in `test_shared.py` |
| Hein Thura Naung | IvannCoder | Shared `funded_account` fixture in `conftest.py` |

## Our Merge Conflict

The conflict markers were `<<<<<<< HEAD`, `=======`, and `>>>>>>> <branch>`. During the merge, different team members edited the same contributor-table section in `README.md`. Git could not automatically choose how to combine those overlapping edits, so the team decided to keep every member's contribution in the completed five-row table.

## Git Contribution Summary

Output of `git shortlog -sn`:

```text
	15  6705140040
	 5  Chan Myae Thaw Tar
	 4  Aye Than Tin
	 3  6705140038
	 6  Hein Thura Naung (Ivan)
```

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?** The remote branch contained teammates' commits that were missing locally, so Git rejected the push to prevent overwriting their work. I pulled their changes, resolved the README conflict by keeping all contributions, then committed and pushed the merge.
2. **Why could Git not resolve the README conflict automatically?** Both branches edited overlapping content in the same contributor-table section. Git could not infer how the competing edits should be combined, so the team retained all five rows.
3. **What is the difference between committing and pushing?** A commit saves a snapshot in the local repository. A push uploads local commits to the remote repository for teammates to access.
4. **How do fixtures reduce duplicated setup code in tests?** A fixture provides reusable setup to each test that requests it. This avoids repeating object creation and lets tests focus on the behavior being checked.

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
