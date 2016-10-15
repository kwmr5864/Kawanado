from entities import Search


class SearchModel:
    @staticmethod
    def get_searches():
        return Search.select().order_by(Search.id.desc())

    @staticmethod
    def save(keyword):
        search = Search(keyword=keyword)
        search.save()
