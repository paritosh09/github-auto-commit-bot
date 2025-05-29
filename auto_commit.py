from datetime import datetime
import subprocess

file_path = "last_commit.txt"

# Update file with timestamp
with open(file_path, "w") as f:
    f.write(f"Last updated: {datetime.utcnow().isoformat()}Z\n")

# Configure Git
subprocess.run(["git", "config", "user.name", "paritosh09"], check=True)
subprocess.run(["git", "config", "user.email", "paritoshupreti1999@gmail.com"], check=True)

# Stage changes
subprocess.run(["git", "add", "."], check=True)

# Only commit if there are staged changes
diff_result = subprocess.run(["git", "diff", "--cached", "--quiet"])
if diff_result.returncode != 0:
    subprocess.run(["git", "commit", "-m", f"Auto commit on {datetime.utcnow().date()}"], check=True)
    subprocess.run(["git", "push"], check=True)
else:
    print("Nothing to commit.")
