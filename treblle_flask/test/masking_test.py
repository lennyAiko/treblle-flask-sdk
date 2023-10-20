from . import mask_json_values


def test_mask_values():
    items = mask_json_values(
        {"password": "vanlenny", "cvv": "275"}, ["password", "cvv"]
    )
    password, cvv = items.values()
    if password != "*" * len(password):
        assert False
    if cvv != "*" * len(cvv):
        assert False
    assert True
