import pytest


def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_converting():
    import data
    import converter
    assert converter.converting(data.input_data) == data.output_data


