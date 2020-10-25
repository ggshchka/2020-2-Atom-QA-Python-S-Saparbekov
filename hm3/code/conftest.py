import pytest

from api.client import MyTargetClient


@pytest.fixture(scope='function')
def client():
    return MyTargetClient(user='sff_ff@mail.ru', password='sff_ff001')
