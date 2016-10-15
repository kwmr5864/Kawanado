from entities import Search


class SearchModel:
    @staticmethod
    def get_searches():
        searches = Search.select(*[Search.id, Search.keyword]).order_by(Search.id.desc())

        return searches

    @staticmethod
    def save(keyword):
        search = Search(keyword=keyword)
        search.save()
