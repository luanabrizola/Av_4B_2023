from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Time, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:postgres@localhost:5432/dw2')
conn = engine.connect()
print(engine)


Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Passagem(Base):
    __tablename__ = 'passagem'
    idpassagem = Column(Integer, primary_key=True)
    data_ida = Column(TIMESTAMP, nullable=False)
    data_volta = Column(TIMESTAMP)
    idorigem = Column(Integer, nullable=False)
    iddestino = Column(Integer, nullable=False)
    duracao = Column(Time, nullable=False)
    idclassevoo = Column(Integer, nullable=False)

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")

passagens = [
    Passagem(idpassagem=1, data_ida='2020-05-25 04:30', data_volta='2020-06-01 19:15', idorigem=1, iddestino=2, duracao='04:04', idclassevoo=2),
    Passagem(idpassagem=2, data_ida='2020-06-01 10:00', data_volta='2020-06-08 20:30', idorigem=10, iddestino=1, duracao='01:10', idclassevoo=4),
    Passagem(idpassagem=3, data_ida='2020-07-14 14:00', data_volta='2020-07-17 10:00', idorigem=13, iddestino=5, duracao='01:30', idclassevoo=2),
    Passagem(idpassagem=4, data_ida='2020-08-29 09:45', data_volta='2020-09-04 12:00', idorigem=3, iddestino=6, duracao='03:15', idclassevoo=1),
    Passagem(idpassagem=5, data_ida='2020-09-15 14:30', data_volta='2020-09-22 17:45', idorigem=8, iddestino=7, duracao='02:45', idclassevoo=3),
    Passagem(idpassagem=6, data_ida='2020-10-05 08:00', data_volta='2020-10-12 10:30', idorigem=11, iddestino=8, duracao='02:00', idclassevoo=2),
    Passagem(idpassagem=7, data_ida='2020-11-20 11:15', data_volta='2020-11-27 13:45', idorigem=4, iddestino=9, duracao='01:30', idclassevoo=4),
    Passagem(idpassagem=8, data_ida='2020-12-10 15:30', data_volta='2020-12-17 18:00', idorigem=2, iddestino=3, duracao='02:15', idclassevoo=1),
    Passagem(idpassagem=9, data_ida='2021-01-05 07:45', data_volta='2021-01-12 10:15', idorigem=6, iddestino=11, duracao='02:30', idclassevoo=2),
    Passagem(idpassagem=10, data_ida='2021-02-18 13:00', data_volta=None, idorigem=5, iddestino=12,duracao='03:00', idclassevoo=3)
]
session.add_all(passagens)
session.commit()
session.close() 