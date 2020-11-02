import argparse

import pytest

from log_analysis import options
from models.models import GreatestRequests, Main
from orm_client.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test(self):
        arg = argparse.Namespace
        arg.command = 'g'
        filename = '../logs/access.log'
        options(arg, filename, self.mysql, self.builder)

        res = self.mysql.session.query(GreatestRequests).filter_by(
            ip_address='178.32.218.13'
        )
        assert res.all()[0].ip_address == '178.32.218.13'
        assert res.all()[0].top == 2
        res.delete()
        assert res.all() == []
        self.mysql.session.commit()

        self.mysql.session.query(GreatestRequests).delete()
        self.mysql.session.query(Main).delete()
        self.mysql.session.commit()
