from byu_pytest_utils.decorators import max_score

from cougars import cougars
from test_utils import compare_files, test_files


@max_score(4)
def test_cougars_simple():
    cougars(test_files / 'cougars_simple_sample.txt', 'output_sample2.txt')
    compare_files(test_files / 'cougars_simple_expected.txt', 'output_sample2.txt')


@max_score(4)
def test_cougars_extra_lines():
    cougars(test_files / 'cougars_extra_lines_sample.txt', 'output_sample1.txt')
    compare_files(test_files / 'cougars_extra_lines_expected.txt', 'output_sample1.txt')
