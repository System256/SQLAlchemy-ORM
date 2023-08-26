from sqlalchemy import create_engine, String, ForeignKey, BigInteger, select
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, Session


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String)


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
    email: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)
        user = UserModel(user_id=1, name='Roman', fullname='Paltsev')
        session.add(user)
    with session.begin():
        res = session.execute(select(UserModel).where(UserModel.user_id == 1))
        user = res.scalar()