import pytest


@pytest.fixture
def num_too_small_with_desc() -> float:
    return 12345.11


@pytest.fixture
def num_too_small() -> float:
    return 12345


@pytest.fixture
def num_too_large() -> float:
    return 12345678012345789


@pytest.fixture
def num_ten_million() -> float:
    return 12345678


@pytest.fixture
def num_ten_million_with_desc(num_ten_million) -> float:
    return num_ten_million + 0.11


@pytest.fixture
def num_ten_million_with_zero_desc_in_pretty_number() -> float:
    return 12045678


@pytest.fixture
def num_hundred_billion() -> float:
    return 123456789012


@pytest.fixture
def num_trillion() -> float:
    return 1234567890123
