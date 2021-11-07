from cz_commitizen_emoji import CommitizenEmojiCz


def test_answer(config, messages):
    cz = CommitizenEmojiCz(config)
    answers, expected = messages
    message = cz.message(answers)
    assert message == expected

def test_schema_pattern(config):
    cz = CommitizenEmojiCz(config)
    assert r"🐛 fix" in cz.schema_pattern()
