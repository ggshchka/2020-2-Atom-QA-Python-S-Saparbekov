from models.models import Base, CountOfAllRequests, Main, CountOfRequestsByMethod, GreatestRequests, RequestsByError
from orm_client.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

        self.create_table_main()
        self.create_table_count_of_all_requests()
        self.create_table_count_of_requests_by_method()
        self.create_table_greatest_requests()
        self.create_table_requests_by_error()


    def create_table_main(self):
        if not self.engine.dialect.has_table(self.engine, 'main'):
            Base.metadata.tables['main'].create(self.engine)

    def create_table_count_of_all_requests(self):
        if not self.engine.dialect.has_table(self.engine, 'count_of_all_requests'):
            Base.metadata.tables['count_of_all_requests'].create(self.engine)

    def create_table_count_of_requests_by_method(self):
        if not self.engine.dialect.has_table(self.engine, 'count_of_requests_by_method'):
            Base.metadata.tables['count_of_requests_by_method'].create(self.engine)

    def create_table_greatest_requests(self):
        if not self.engine.dialect.has_table(self.engine, 'greatest_requests'):
            Base.metadata.tables['greatest_requests'].create(self.engine)

    def create_table_requests_by_error(self):
        if not self.engine.dialect.has_table(self.engine, 'requests_by_error'):
            Base.metadata.tables['requests_by_error'].create(self.engine)

    def add_main(self, filename, date_of_call):
        main = Main(
            filename=filename,
            date_of_call=date_of_call
        )
        self.connection.session.add(main)
        # Записываем созданную запись в базу
        self.connection.session.commit()
        # Возвращаем объект для работы из тестов
        return main

    def add_count_of_all_requests(self, value, main_id):
        el = CountOfAllRequests(
            value=value,
            main_id=main_id
        )
        self.connection.session.add(el)
        self.connection.session.commit()
        return el

    def add_count_of_requests_by_method(self, value, method, main_id):
        el = CountOfRequestsByMethod(
            value=value,
            method=method,
            main_id=main_id
        )
        self.connection.session.add(el)
        self.connection.session.commit()
        return el

    def add_greatest_requests(self, top, length, ip_address,
                              protocol, method, location,
                              status_code, date, main_id):
        el = GreatestRequests(
            top=top,
            length=length,
            ip_address=ip_address,
            protocol=protocol,
            method=method,
            location=location,
            status_code=status_code,
            date=date,
            main_id=main_id
        )
        self.connection.session.add(el)
        self.connection.session.commit()
        return el

    def add_requests_by_error(self, top, location,
                              value, error_type, main_id):
        el = RequestsByError(
            top=top,
            location=location,
            value=value,
            error_type=error_type,
            main_id=main_id
        )
        self.connection.session.add(el)
        self.connection.session.commit()
        return el
