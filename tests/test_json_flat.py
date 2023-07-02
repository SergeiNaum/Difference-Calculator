import pytest
import ast
from gendif import generate_diff


@pytest.fixture
def expected_value():
    with open('fixtures/expec_ans_flat_json.txt', 'r') as file:
        content = file.read().strip()
        return ast.literal_eval(content)


# @pytest.fixture
# def export_file(file_name1, file_name2):
#     with open(file_name1, 'r') as file1, open(file_name2, 'r') as file2:
#         return file1.read().strip(), file2.read().strip()


def test_json_flat(expected_value):
    # f1, f2 = export_file('file1.json', 'file2.json')
    result = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
    assert result == expected_value