from repository.repository import DB_atlas


class Service:
    @staticmethod
    def get_stock():
        return DB_atlas.get_stock()

    @staticmethod
    def get_sell_in(sell_in):
        return DB_atlas.get_sell_in(sell_in)

    @staticmethod
    def get_quality(quality):
        return DB_atlas.get_quality(quality)

    @staticmethod
    def get_item(item):
        return DB_atlas.get_item(item)

    @staticmethod
    def delete_item(name, sell_in, quality):
        eliminado = DB_atlas.delete_item(name, sell_in, quality)
        return {
            "Item": {
                "name": name,
                "sell_in": sell_in,
                "quality": quality,
            },
            "Eliminado": True
            if eliminado.deleted_count == 1
            else "No se ha encontrado item",
        }
