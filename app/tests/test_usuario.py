import pytest
from app.models.usuario_models import Usuario
from app.config.database import db
import os 

os.system("cls||clear")

@pytest.fixture 

def usuario_valido():
    usuario = Usuario("maria", "maria123@gmail.com", "12345")
    return usuario

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "maria"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "maria123@gmail.com"

def test_senha_valida(usuario_valido):
    assert usuario_valido.senha == "12345"

def test_invalida_nome():
    with pytest.raises(TypeError, match="O nome deve ser um texto !"):
        Usuario(999, "maria123@gmail.com", "12345")

def test_invalida_email():
    with pytest.raises(TypeError, match="O email deve ser um texto !"):
        Usuario("maria", 12345, "12345")

def test_invalida_senha():
    with pytest.raises(TypeError, match="A senha deve ser um texto !"):
        Usuario("maria", "maria123@gmail.com", 12345)

    