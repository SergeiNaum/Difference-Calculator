import pathlib
import pytest
import ast
from gendif import generate_diff


@pytest.fixture(scope='function')
def expected_value():
    home_dir = str(pathlib.Path.cwd())
    file1 = 'expec_ans_flat_json.txt'
    f1 = f'{home_dir}/tests/fixtures/{file1}'

    with open(f1, 'r') as file:
        content = file.read().strip()
        return ast.literal_eval(content)


def test_json_flat(expected_value):
    home_dir = str(pathlib.Path.cwd())
    file1 = 'file1.json'
    file2 = 'file2.json'
    file_path1 = f'{home_dir}/tests/fixtures/{file1}'
    file_path2 = f'{home_dir}/tests/fixtures/{file2}'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_value


def test_yaml_flat(expected_value):
    home_dir = str(pathlib.Path.cwd())
    file1 = 'file1.yml'
    file2 = 'file2.yml'
    file_path1 = f'{home_dir}/tests/fixtures/{file1}'
    file_path2 = f'{home_dir}/tests/fixtures/{file2}'
    result = generate_diff(file_path1, file_path2)
    assert result == expected_value


if __name__ == '__main__':
    pytest.main()
