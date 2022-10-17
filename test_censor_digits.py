from byu_pytest_utils.decorators import max_score

from censor_digits import censor_digits
from test_utils import compare_files, test_files


@max_score(4)
def test_censor_digits_simple():
    censor_digits(test_files / 'censor_digits_only_numbers_sample.txt', test_files / 'output_sample4.txt')
    compare_files(test_files / 'censor_digits_only_numbers_expected.txt', test_files / 'output_sample4.txt')


@max_score(4)
def test_censor_digits_complex():
    censor_digits(test_files / 'censor_digits_complex_sample.txt', test_files / 'output_sample3.txt')
    compare_files(test_files / 'censor_digits_complex_expected.txt', test_files / 'output_sample3.txt')
