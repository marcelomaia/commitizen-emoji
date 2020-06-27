import pytest
from commitizen import defaults
from commitizen.config import BaseConfig
from commitizen.cz.base import BaseCommitizen


@pytest.fixture()
def config():
    _config = BaseConfig()
    _config.settings.update({"name": defaults.name})
    return _config


@pytest.fixture(params=[
    # anwsers, expected
    (
        {
            "prefix": "📜 docs",
            "scope": "models",
            "subject": "person was undocumented",
            "body": "When no plant of the field was yet in the image of God he created them; male and female he created them.",
            "is_breaking_change": False,
            "time": "1h 15m",
            "tasks": "1515 2233 2222"
        }, "📜 docs(models): person was undocumented >>> 1h 15m >>> Tasks: #1515 #2233 #2222\n\nWhen no plant of the field was yet in the image of God he created them; male and female he created them."
    ),
    (
        {
            "prefix": "🔧 refactor",
            "scope": "dto",
            "subject": "bla bla",
            "body": "The woman said to him, Where are you?",
            "is_breaking_change": False,
            "time": "",
            "tasks": ""
        }, "🔧 refactor(dto): bla bla\n\nThe woman said to him, Where are you?"
    ),
    (
        {
            "prefix": "🚦 test",
            "scope": "controllers",
            "subject": "xpto",
            "body": "So out of the heavens and the earth and the woman, and between your offspring and hers; he will strike his heel.",
            "is_breaking_change": True,
            "time": "30m",
            "tasks": "666 420"
        }, "🚦 test(controllers): xpto >>> 30m >>> Tasks: #666 #420\n\nBREAKING CHANGE 🚨: So out of the heavens and the earth and the woman, and between your offspring and hers; he will strike his heel."
    ),(
        {
            "prefix": "🚧 build",
            "scope": "docker",
            "subject": "xpto",
            "body": "He drove out the man; and at the east of the garden at the time of the evening breeze, and the man and put him in the garden of Eden, to till the ground the LORD God walking in the image of God he created them; male and female he created them.",
            "is_breaking_change": False,
            "time": "",
            "tasks": ""
        }, "🚧 build(docker): xpto\n\nHe drove out the man; and at the east of the garden at the time of the evening breeze, and the man and put him in the garden of Eden, to till the ground the LORD God walking in the image of God he created them; male and female he created them."
    ),
])
def messages(request):
    return request.param
