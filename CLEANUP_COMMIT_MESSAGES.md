Suggested human-friendly commit messages for the HRMS Lite repository

If you would like to rewrite local commit messages to remove AI-sounding language, use the suggestions below. Only rewrite history on branches that are not shared (or after coordinating with collaborators).

Examples (replace <area> and <detail> as appropriate):

- "Initial commit: HRMS Lite"
- "Add Employee and Attendance models"
- "Add API endpoints for employees and attendance"
- "Implement serializers and validation for Employee and Attendance"
- "Add React frontend with Employee and Attendance UI"
- "Seed database with sample data"
- "Add CORS and DRF settings"
- "Add deployment configuration (Procfile, requirements)"
- "Fix employee unique validation and serializer checks"
- "Polish UI and error handling"
- "Update documentation and quick start guide"
- "Minor UI/UX improvements"

How to rewrite last N commit messages interactively:

```bash
# Edit last 3 commits messages
git rebase -i HEAD~3
# In the editor, change 'pick' to 'reword' for commits you want to rename
# Save and follow prompts to enter new commit messages
```

How to change a single commit message (most recent):

```bash
git commit --amend -m "New commit message"
```

CAUTION: Do not use `git push --force` to rewrite commits on a remote branch without coordination. If the repository is already pushed and you must rewrite history, inform teammates and use:

```bash
git push --force-with-lease origin your-branch
```

If you want, I can prepare a short script to rewrite local commit messages in bulk (for your review) — tell me how many commits you want to rewrite and whether the branch is pushed to a remote.
