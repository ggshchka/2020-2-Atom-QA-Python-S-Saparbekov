from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Main(Base):
    # В __tablename__ указывается имя таблицы, которую мы хотим создать
    __tablename__ = 'main'
    # __table_args__ используется для установки кодировки в базе на utf8, т. к. мы записываем в нее кириллицу.
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(200), nullable=False)
    date_of_call = Column(DateTime, nullable=False)

    # Метод __repr__ используется для того, чтобы можно было сделать красивый вывод полей нашей модели
    # при обращении к ней из дебага или просто печати ее содердимого.
    def __repr__(self):
        return f"<main(" \
               f"id='{self.id}'," \
               f"filename='{self.filename}', " \
               f"date_of_call='{self.date_of_call}', " \
               f")>"


class CountOfAllRequests(Base):
    __tablename__ = 'count_of_all_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    # Помимо остальных полей, устанавливаем ForeignKey
    main_id = Column(Integer, ForeignKey(f'{Main.__tablename__}.{Main.id.name}'), nullable=False)

    def __repr__(self):
        return f"<count_of_all_requests(" \
               f"id='{self.id}'," \
               f"value='{self.value}', " \
               f"main_id='{self.main_id}'" \
               f")>"


class CountOfRequestsByMethod(Base):
    __tablename__ = 'count_of_requests_by_method'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer,)
    method = Column(String(10))
    main_id = Column(Integer, ForeignKey(f'{Main.__tablename__}.{Main.id.name}'), nullable=False)

    def __repr__(self):
        return f"<count_of_requests_by_method(" \
               f"id='{self.id}'," \
               f"value='{self.value}', " \
               f"method='{self.method}', " \
               f"main_id='{self.main_id}'" \
               f")>"


class GreatestRequests(Base):
    __tablename__ = 'greatest_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    top = Column(Integer)
    length = Column(Integer)
    ip_address = Column(String(20))
    protocol = Column(String(20))
    method = Column(String(10))
    location = Column(String(200))
    status_code = Column(String(10))
    date = Column(DateTime)
    main_id = Column(Integer, ForeignKey(f'{Main.__tablename__}.{Main.id.name}'), nullable=False)

    def __repr__(self):
        return f"<greatest_requests(" \
               f"id='{self.id}'," \
               f"top='{self.top}'," \
               f"length='{self.length}'," \
               f"ip_address='{self.ip_address}', " \
               f"protocol='{self.protocol}', "\
               f"method='{self.method}', " \
               f"location='{self.location}', " \
               f"status_code='{self.status_code}', " \
               f"date='{self.date}', " \
               f"main_id='{self.main_id}'" \
               f")>"


class RequestsByError(Base):
    __tablename__ = 'requests_by_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    top = Column(Integer)
    location = Column(String(200))
    value = Column(Integer, nullable=False)
    error_type = Column(String(20), nullable=False)
    main_id = Column(
        Integer,
        ForeignKey(f'{Main.__tablename__}.{Main.id.name}'),
        nullable=False
    )

    def __repr__(self):
        return f"<requests_by_error(" \
               f"id='{self.id}'," \
               f"top='{self.top}', " \
               f"location='{self.location}', " \
               f"value='{self.value}', " \
               f"error_type='{self.error_type}', " \
               f"main_id='{self.main_id}'" \
               f")>"