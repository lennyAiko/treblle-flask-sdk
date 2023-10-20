from . import treblle_base_url


def test_base_url():
    assert isinstance(treblle_base_url(), str)


def test_size_url():
    assert len(treblle_base_url()) > 1
