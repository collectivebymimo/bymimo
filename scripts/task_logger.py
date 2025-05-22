import datetime

def log_task(task, category="General"):
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"- [ ] {task}  \n  Category: {category}  \n  Added: {today}\n"

    with open("../notes/daily-tasks.md", "a") as f:
        f.write(entry)

    print(f"Task added: {task}")

# Example usage
log_task("Fix Google Nest stereo sound", "Personal")
