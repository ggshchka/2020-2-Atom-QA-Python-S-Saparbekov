import pytest

from orm_client.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(
        user='root',
        password='passw',
        db_name='TEST_PYTHON_ORM'
    )