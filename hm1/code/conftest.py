"""
conftest.py plugins: modules auto-discovered in test directories
"""
import random
import string
import pytest


@pytest.fixture(scope='class')
def rand_int():
    """
    :return: Generated int number from -100 to 100
    """
    return random.randint(-100, 100)


@pytest.fixture(scope='function')
def rand_2_strings():
    """
    :return: Generated tuple of 2 strings with length from 1 to 50
    """
    size = random.randint(1, 50)
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size)),\
           ''.join(random.choice(chars) for _ in range(size))


@pytest.fixture
def rand_list():
    """
    :return: Generated list
    """
    return [random.randrange(-100, 100, 1)
            for i in range(random.randint(1, 20))]


@pytest.fixture
def rand_dict():
    """
    :return: Generated dictionary
    """
    return {'key'+str(i): random.randrange(10)
            for i in range(random.randint(1, 30))}
