# import sqlite3
# import re
# from sqlalchemy import create_engine, Column, Integer, String, Boolean, LargeBinary, ForeignKey
# from sqlalchemy.orm import declarative_base, Relationship, sessionmaker


# from sqlalchemy import create_engine, Column, Integer, String, Boolean, LargeBinary, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# engine = create_engine('sqlite:///estudos1.db', echo=True)
# Base = declarative_base()

# class Usuario(Base):
#     __tablename__ = 'usuarios'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nome = Column(String(50), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     senha = Column(LargeBinary, nullable=False)
#     admboll = Column(Boolean, nullable=True, default=False)

#     informacoes = relationship("InformacoesPessoais", back_populates="usuario")
#     frequencia = relationship("Frequencia_alunos", back_populates="usuario")

# class InformacoesPessoais(Base):
#     __tablename__ = 'informacoes_pessoais'

#     id = Column(Integer, primary_key=True)
#     usuario_id = Column(Integer, ForeignKey('usuarios.id'))
#     rua = Column(String)
#     cidade = Column(String)
#     telefone = Column(String)
#     cep = Column(String)

#     usuario = relationship("Usuario", back_populates="informacoes")
# class Frequenciaalunos(Base):
#     __tablename__ = 'frequencia'
#     id = Column(Integer, ForeignKey('usuarios.id'))
#     nome = Column(String, ForeignKey('usario.nome'))
#     precenca = Column(Boolean, nullable=True,default= False)

#     usuario = relationship("Usuario",back_populates="frequencia" )


# # Cria as tabelas
# Base.metadata.create_all(engine)

# # Sessão
# Session = sessionmaker(bind=engine)
# session = Session()
