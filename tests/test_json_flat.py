import pytest
import ast
import os
from gendif import generate_diff


@pytest.fixture(scope='function')
def expected_value():
    file_path = 'tests/fixtures/expec_ans_flat_json.txt'
    # file_path = os.path.join(os.getcwd(), 'fixtures/expec_ans_flat_json.txt')
    with open(file_path, 'r') as file:
        content = file.read().strip()
        return ast.literal_eval(content)


def test_json_flat(expected_value):
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    # file_path1 = os.path.join(os.getcwd(), 'fixtures/file1.json')
    # file_path2 = os.path.join(os.getcwd(), 'fixtures/file2.json')
    result = generate_diff(file_path1, file_path2)
    assert result == expected_value



if __name__ == '__main__':
    pytest.main()