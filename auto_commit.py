from datetime import datetime
import os

file_path = "last_commit.txt"

# Write timestamp to file
with open(file_path, "w") as f:
    f.write(f"Last updated: {datetime.utcnow().isoformat()}Z\n")

# Git commands
os.system("git config user.name 'Your Name'")
os.system("git config user.email 'your@email.com'")
os.system("git add .")
os.system(f"git commit -m 'Auto commit on {datetime.utcnow().date()}'")
os.system("git push")
