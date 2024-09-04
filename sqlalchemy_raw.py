from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Configs
engine = create_engine("postgresql://user_mosc:1234@localhost:5432/cinema")
conn = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Filme (titulo: {self.titulo} - ano: {self.ano})"
    

# Insert
data_insert = Filmes(titulo = "Vingadores 3", genero="Acao", ano=2019)
session.add(data_insert)
session.commit()

# delete
session.query(Filmes).filter(Filmes.titulo == "Alguma coisa").delete()
session.commit()

# Update
session.query(Filmes).filter(Filmes.genero == "Drama").update({"ano": 1999})
session.commit()

# Select
data = session.query(Filmes).all()
print(data)

session.close()