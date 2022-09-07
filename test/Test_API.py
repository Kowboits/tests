from API.API_Get import create_folder, get_info
import pytest

def test_create_folder():
    print(get_info('tests'))
    assert get_info('tests') == 'dir'