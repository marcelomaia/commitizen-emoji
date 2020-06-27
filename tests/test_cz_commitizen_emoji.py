from cz_commitizen_emoji import CommitizenEmojiCz


def test_answer(config, messages):
    cz = CommitizenEmojiCz(config)
    answers, expected = messages
    message = cz.message(answers)
    assert message == expected
