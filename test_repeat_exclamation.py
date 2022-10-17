from byu_pytest_utils.decorators import max_score

from repeat_exclamation import repeat_exclamation


@max_score(2)
def test_repeat_exclamation_three_times():
    observed = repeat_exclamation("hello world", "!", 3)
    expected = "hello world!!!"
    assert observed == expected


@max_score(2)
def test_repeat_exclamation_ten_times():
    observed = repeat_exclamation("how r u", "?", 10)
    expected = "how r u??????????"
    assert observed == expected


@max_score(3)
def test_repeat_exclamation_zero_times():
    observed = repeat_exclamation("hi", ".", 0)
    expected = "hi"
    assert observed == expected
