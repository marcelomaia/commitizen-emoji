from commitizen.cz.base import BaseCommitizen
from commitizen.cz.utils import multiple_line_breaker, required_validator


def parse_scope(text):
    if not text:
        return ""

    scope = text.strip().split()
    if len(scope) == 1:
        return scope[0]

    return "-".join(scope)


def parse_subject(text):
    if isinstance(text, str):
        text = text.strip(".").strip()

    return required_validator(text, msg="Subject is required.")


class CommitizenEmojiCz(BaseCommitizen):
    def questions(self) -> list:
        questions: List[Dict[str, Any]] = [
            {
                "type": "list",
                "name": "prefix",
                "message": "Select the type of change you are committing",
                "choices": [
                    {
                        "value": "🐛 fix",
                        "name": "🐛 fix: A bug fix",
                    },
                    {
                        "value": "🎉 feat",
                        "name": "🎉 feat: A new feature",
                    },
                    {"value": "🗒️ docs", "name": "🗒️ docs: Documentation only changes"},
                    {
                        "value": "😎 style",
                        "name": (
                            "😎 style: Changes that do not affect the "
                            "meaning of the code (white-space, formatting,"
                            " missing semi-colons, etc)"
                        ),
                    },
                    {
                        "value": "🛠️ refactor",
                        "name": (
                            "🛠️ refactor: A code change that neither fixes "
                            "a bug nor adds a feature"
                        ),
                    },
                    {
                        "value": "🚀 perf",
                        "name": "🚀 perf: A code change that improves performance",
                    },
                    {
                        "value": "🧪 test",
                        "name": (
                            "🧪 test: Adding missing or correcting " "existing tests"
                        ),
                    },
                    {
                        "value": "🏗️ build",
                        "name": (
                            "🏗️ build: Changes that affect the build system or "
                            "external dependencies (example scopes: pip, docker, npm)"
                        ),
                    },
                    {
                        "value": "🛸 ci",
                        "name": (
                            "🛸 ci: Changes to our CI configuration files and "
                            "scripts (example scopes: GitLabCI)"
                        ),
                    },
                ],
            },
            {
                "type": "input",
                "name": "scope",
                "message": (
                    "Scope. Could be anything specifying place of the "
                    "commit change (users, db, poll):\n"
                ),
                "filter": parse_scope,
            },
            {
                "type": "input",
                "name": "subject",
                "filter": parse_subject,
                "message": (
                    "Subject. Concise description of the changes. "
                    "Imperative, lower case and no final dot:\n"
                ),
            },
            {
                "type": "input",
                "name": "time",
                "message": "Time spent (i.e. 3h 15m) (optional):\n",
                "filter": lambda x: "⏰ " + x.strip() if x else "",
            },
            {
                "type": "input",
                "name": "tasks",
                "message": "Tasks ID(s) separated by spaces (optional):\n",
                "filter": lambda x: x.strip() if x else "",
            },
            {
                "type": "confirm",
                "message": "Is this a BREAKING CHANGE?",
                "name": "is_breaking_change",
                "default": False,
            },
            {
                "type": "input",
                "name": "body",
                "message": (
                    "Body. Motivation for the change and contrast this "
                    "with previous behavior:\n"
                ),
                "filter": multiple_line_breaker,
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        prefix = answers["prefix"]
        scope = answers["scope"]
        subject = answers["subject"]
        body = answers["body"]
        is_breaking_change = answers["is_breaking_change"]
        time = answers["time"]
        tasks = answers["tasks"]
        extra = ''

        if scope:
            scope = f"({scope})"
        if is_breaking_change:
            body = f"BREAKING CHANGE 🚨: {body}"
        if body:
            body = f"\n\n{body}"

        if time:
            extra += f" >>> {time}"
        if tasks:
            tasks_text = ' '.join([f'#{task_id}' for task_id in tasks.split()]
            extra += f" >>> Tasks: {tasks_text}"

        message=f"{prefix}{scope}: {subject}{extra}{body}"

        return message


discover_this=CommitizenEmojiCz
