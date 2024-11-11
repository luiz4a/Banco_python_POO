import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from app.models.usuario_models import Usuario
import os 

os.system("cls||clear")

@pytest.fixture 

def test_criar_usuario(session):
    usuario = Usuario (nome="Maria", email= "Maria123@gmail.com", senha= "12345")
    session.add(usuario)
    session.commit()

    usuario_salvo = session.query(Usuario).filter_by(email="Maria123@gmail.com").first()
    assert usuario_salvo is not None 

def test_nome_valido(test_criar_usuario):
    assert test_criar_usuario.nome == "Maria"

def test_email_valido(test_criar_usuario):
    assert test_criar_usuario.email == "Maria123@gmail.com"

def test_senha_valida(test_criar_usuario):
    assert test_criar_usuario.senha == "12345"


def test_email_duplicado(test_criar_usuario, session):
    usuario1= Usuario(nome="Maria Luiza", email= "MariaDias123@gmail.com", senha= "1234567")
    session.add(usuario1)
    session.commit()

    usuario2= Usuario(nome="Gm Moura", email= "GmMoura123@gmail.com", senha= "81811414")
    session.add(usuario2)
    
    with pytest.raises(IntegrityError):
        session.commit()

def test_autoincremento_id(test_criar_usuario, session):
    usuario1= Usuario(nome="Lucas ", email= "lucas123@gmail.com", senha= "lucas")
    session.ad(usuario1)
    session.commit()

    usuario2= Usuario(nome="exemplo", email= "exemplo@gmail.com", senha= "123456789")
    session.ad(usuario2)
    session.commit()
    