from sqlalchemy import create_engine, text, Connection, MetaData, Table, Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import Session


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, unique=True),
    Column("fullname", String),
)

address = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.user_id")),
    Column("emeil", String, nullable=False),
)

print(user_table.c.keys())