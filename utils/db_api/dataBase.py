from gino import Gino
from gino.schema import GinoSchemaVisitor

from data.config import POSTGRESULI

db = Gino()

async def create_db():
    await db.set_bind(POSTGRESULI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()