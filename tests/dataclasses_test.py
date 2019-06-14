import sys

import pytest

from injector import Injector, inject


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Requires Python 3.6+")
def test_dataclass_integration_works():
    import dataclasses

    @inject
    @dataclasses.dataclass
    class Data:
        name: str

    def configure(binder):
        binder.bind(str, to='data')

    injector = Injector([configure])
    assert injector.get(Data).name == 'data'
