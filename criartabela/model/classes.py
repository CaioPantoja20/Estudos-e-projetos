from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey

Base = declarative_base()

class Alunos(Base):
    __tablename__ = 'alunos'

    matricula = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(LargeBinary, nullable=False)

    # Relacionamento 1:1
    informacoes = relationship("InformacoesAlunos", back_populates="aluno", uselist=False)


class InformacoesAlunos(Base):
    __tablename__ = 'informacoes_alunos_pessoais'

    matricula = Column(Integer, ForeignKey('alunos.matricula'), primary_key=True)
    presenca = Column(Boolean, default=False)
    rua = Column(String)
    cidade = Column(String)
    telefone = Column(String)
    cep = Column(String)
    horas_estudadas= Column(String)
    aluno = relationship("Alunos", back_populates="informacoes")
    
class Adm(Base):
    __tablename__ = 'administrador'

    id = Column(Integer, primary_key= True,autoincrement=True)
    nomeadm = Column(String,nullable=False)
    emailadm = Column(String,unique=True,nullable=False)
    senhaadm = Column(LargeBinary,nullable=False)
    admboolean = Column(Boolean,nullable = False,default=False)
