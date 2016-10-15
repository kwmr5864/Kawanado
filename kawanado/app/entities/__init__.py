import datetime

from peewee import *

db = MySQLDatabase(
        database='kawanado',
        user='kawanado',
        password='kawanado',
        host='127.0.0.1',
        port=3306,
        charset='utf8mb4',
)


class Search(Model):
    """
    検索結果。
    """
    keyword = CharField(index=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
