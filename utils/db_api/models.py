from sqlalchemy import (Column, Integer, String, Sequence)

from sqlalchemy import sql
from utils.db_api.dataBase import db


class Item(db.Model):
    __tablename__ = "items"
    query: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)
    category_code = Column(db.String(20))
    category_name = Column(db.String(20))

    subcategory_code = Column(db.String(20))
    subcategory_name = Column(db.String(20))

    name = Column(db.String(50))
    photo = Column(db.String(250))
    price = Column(Integer)

    def __repr__(self):
        # Показывает краткое содержимое записи в таблице
        return f"""
    Товар №{self.id} - {self.name}
    Цена {self.price}
    """
