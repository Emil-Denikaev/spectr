from gino import Gino
from gino.schema import GinoSchemaVisitor

from data.config import POSTGRESULI
from utils.db_api import add_to_data

db = Gino()

async def create_db():
    await db.set_bind(POSTGRESULI)
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
    await add_to_data.add_items()