from pathlib import Path

test_files = Path(__file__).parent / "test_files"


def compare_files(file_1, file_2):
    with open(file_1) as f1:
        with open(file_2) as f2:
            expected = f1.read().strip()
            observed = f2.read().strip()
            assert observed == expected
