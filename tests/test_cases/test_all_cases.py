import pytest
import pathlib
import aiofiles
import asyncio

from gendiff.gendif import generate_diff
from gendiff.formatter import format

FIXTURES_FOLDER = 'fixtures'

names = [
    ('file1.json', 'file2.json', 'stylish_plain'),
    ('file1.yml', 'file2.yml', 'stylish_plain'),
    ('file1_tree.json', 'file2_tree.json', 'json'),
    ('file1_tree.yml', 'file2_tree.yml', 'json'),
    ('file1_tree.json', 'file2_tree.json', 'plain'),
    ('file1_tree.yml', 'file2_tree.yml', 'plain'),
    ('file1_tree.yml', 'file2_tree.yml', 'stylish'),
    ('file1_tree.json', 'file2_tree.json', 'stylish')
]


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def result_render(request):
    file1, file2, format_name = request.param

    result_path = (
        pathlib.Path(__file__).parent.parent
        / FIXTURES_FOLDER
        / format_name
    )
    async with aiofiles.open(result_path, mode='r') as file:

        content = await file.read()
        content = content.replace('- wow:', '- wow: ')

    file_path1 = (
        pathlib.Path(__file__).parent.parent
        / FIXTURES_FOLDER
        / file1
    )
    file_path2 = (
        pathlib.Path(__file__).parent.parent
        / FIXTURES_FOLDER
        / file2
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
