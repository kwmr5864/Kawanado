from peewee import IntegrityError
from entities import db, Search

if __name__ == '__main__':
    try:
        db.create_tables([Search], True)
        db.close()
    except IntegrityError as e:
        print(e)
