from peewee import fn

from entities import Search


class SearchModel:
    @staticmethod
    def get_searches():
        searches = Search\
            .select(*[Search.id, Search.keyword])\
            .order_by(Search.id.desc())

        return searches

    @staticmethod
    def get_search_keywords():
        min_id = fn.Min(Search.id)
        searches = Search\
            .select(*[Search.keyword, min_id.alias('id')])\
            .group_by(Search.keyword)\
            .order_by(min_id.desc())

        return [x.keyword for x in searches]

    @staticmethod
    def save(keyword):
        search = Search(keyword=keyword)
        search.save()
