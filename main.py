import argparse
from models.user import User
from models.project import Project
from models.task import Task

def main():
    parser = argparse.ArgumentParser(description="CLI Tool for Users, Projects, and Tasks")
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", default="")

    # Add project
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--desc", default="")
    add_project.add_argument("--due", default="")

    # Add task
    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)

    args = parser.parse_args()

    User.load()  # Load existing users

    if args.command == "add-user":
        User(args.name, args.email)
        User.save()
        print(f"User {args.name} added.")

    elif args.command == "add-project":
        user = User.find(args.user)
        if not user:
            print(f"User {args.user} not found.")
            return
        project = Project(args.title, args.desc, args.due)
        user.add_project(project)
        User.save()
        print(f"Project {args.title} added to user {args.user}.")

    elif args.command == "add-task":
        project = Project.find(args.project)
        if not project:
            print(f"Project {args.project} not found.")
            return
        task = Task(args.title)
        project.add_task(task)
        print(f"Task {args.title} added to project {args.project}.")

if __name__ == "__main__":
    main()