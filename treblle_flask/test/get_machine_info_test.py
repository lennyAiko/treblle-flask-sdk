from . import machine_info


def test_get_info():
    assert isinstance(machine_info(), dict)


def test_size_info():
    assert len(machine_info()) == 4
