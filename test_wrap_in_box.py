from byu_pytest_utils.decorators import max_score

from wrap_in_box import wrap_in_box


@max_score(2)
def test_wrap_in_box_hi():
    observed = wrap_in_box("hi")
    expected = "------\n| hi |\n------"
    assert observed == expected


@max_score(2)
def test_wrap_in_box_how_r_u():
    observed = wrap_in_box("how r u?")
    expected = "------------\n| how r u? |\n------------"
    assert observed == expected


@max_score(3)
def test_wrap_in_box_im_good_thanks():
    observed = wrap_in_box("I'm good thanks!")
    expected = "--------------------\n| I'm good thanks! |\n--------------------"
    assert observed == expected
