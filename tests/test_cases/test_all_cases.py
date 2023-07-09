import pytest
import pathlib
import aiofiles
import asyncio

from gendiff.gendif import generate_diff
from gendiff.formatter import format

FIXTURES_FOLDER = 'fixtures'

names = [
    ('file1.json', 'file2.json', 'stylish_plain'), ('file1.yml', 'file2.yml', 'stylish_plain'),  # noqa: E501
    ('file1_tree.json', 'file2_tree.json', 'json'), ('file1_tree.yml', 'file2_tree.yml', 'json'),  # noqa: E501
    ('file1_tree.json', 'file2_tree.json', 'plain'), ('file1_tree.yml', 'file2_tree.yml', 'plain'),  # noqa: E501
    ('file1_tree.yml', 'file2_tree.yml', 'stylish'), ('file1_tree.json', 'file2_tree.json', 'stylish')  # noqa: E501
]


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()  # noqa: E501
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def result_render(request):
    file1, file2, format_name = request.param  # noqa: E501

    result_path = (
                    pathlib.Path(__file__).parent.parent  # noqa:E126
                    / FIXTURES_FOLDER  # noqa:E126
                    / format_name  # noqa:E126
    )
    async with aiofiles.open(result_path, mode='r') as file:

        content = await file.read()
        content = content.replace('- wow:', '- wow: ')

    file_path1 = (
                    pathlib.Path(__file__).parent.parent  # noqa:E126
                    / FIXTURES_FOLDER  # noqa:E126
                    / file1  # noqa:E126
    )
    file_path2 = (
                    pathlib.Path(__file__).parent.parent  # noqa:E126
                    / FIXTURES_FOLDER  # noqa:E126
                    / file2  # noqa:E126
    )

    return content, format_name, file_path1, file_path2


@pytest.mark.parametrize('result_render', names, indirect=True,
                         ids=["_".join(a) for a in names])
@pytest.mark.asyncio
async def test_diff_files(result_render):
    content, format_name, file_path1, file_path2 = result_render
    if format_name in ('stylish_plain', 'stylish'):
        format_name = 'stylish'
    assert content == generate_diff(file_path1,
                                    file_path2,
                                    format_name=format_name)


@pytest.mark.asyncio
async def test_unknown_format():
    with pytest.raises(ValueError, match=r'Unknown format'):
        format({}, 'unknown_format')
