import re
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from model.classes import Base, Alunos, InformacoesAlunos, Adm

# Configuração do SQLite
engine = create_engine('sqlite:///estudos1.db', echo=True)
Session = sessionmaker(bind=engine)

# Criação das tabelas (uma única vez)
Base.metadata.create_all(engine)

def adm_senha(senhaadm):
    if len(senhaadm) <6:
        print("Senha muito curta")
        return False
    if re.search(r'[A-Za-z]',senhaadm) and re.search(r'[0-9]',senhaadm):
        return True
    print("A senha deve ter uma letra e número!")
    return False

def adm_email(emailadm: str) -> bool:
    emailadm = emailadm.strip()

    provedores = ['gmail', 'yahoo', 'outlook', 'hotmail', 'uol', 'bol', 'icloud']
    dominios = ['com', 'org', 'net', 'edu', 'gov', 'br']

    padrao = r'^[A-Za-z0-9._%+-]+@(' + '|'.join(provedores) + r')\.(' + '|'.join(dominios) + r')$'
    return bool(re.fullmatch(padrao, emailadm))

def cadastro_adm():
    session = Session()
    try:
        nomeadm = input("Digite o seu nome: ").strip()
        emailadm = input("Digite seu email: ").strip()
        senhaadm = input("Digite sua senha: ")

        if not adm_senha(senhaadm):
            return False
        if not adm_email(emailadm):
            print("Email inválido!")
            return False

        existente = session.query(Adm).filter_by(emailadm=emailadm).first()
        if existente:
            print("Esse email já está cadastrado!")
            return False

        senha_hash = bcrypt.hashpw(senhaadm.encode('utf-8'), bcrypt.gensalt())

        novo_adm = Adm(
            nomeadm=nomeadm,
            emailadm=emailadm,
            senhaadm=senha_hash,
            admboolean=True
        )
        session.add(novo_adm)
        session.commit()
        print(f"Adm '{nomeadm}' cadastrado com sucesso! ID: {novo_adm.id}")
        return True

    except IntegrityError:
        session.rollback()
        print("Erro: esse email já existe.")
        return False
    finally:
        session.close()

def login_adm(emailadm, senhaadm):
    session = Session()
    try:
        adm_obj = session.query(Adm).filter_by(emailadm=emailadm).first()
        if not adm_obj:
            print("Email ou senha invalidos!")
            return False

        if bcrypt.checkpw(senhaadm.encode('utf-8'), adm_obj.senhaadm):
            print(f"Login bem-sucedido! Bem-vindo, {adm_obj.nomeadm} (ID: {adm_obj.id})")
            return True
        else:
            print("Email ou senha invalidos!")
            return False
    finally:
        session.close()
if __name__ == "__main__":
    while True:
        print("\n1 - Cadastro\n2 - Login\n3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastro_adm()
        elif opcao == "2":
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            login_adm(email, senha)
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")