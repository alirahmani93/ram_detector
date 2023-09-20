import pytest

from src.core.backend import store_ram_data, convert_byte_to_megabyte


def test_get_memory():
    a, b, c = store_ram_data()
    assert type(a) == float
    assert type(b) == float
    assert type(c) == float


@pytest.mark.parametrize('value', [10 ** 6, 1000000, 1000000.5])
def test_convert_byte_to_megabyte(value):
    v = convert_byte_to_megabyte(value)
    assert v == (value / (10 ** 6))
