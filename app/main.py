from models.usuario_models import Usuario
from repositories.usuario_repositories import UsuarioRepository
from services.usuario_services import UsuarioService
from config.database  import Session 

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService (repository)

    #Solicitando dados para o usuario 
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    service.criar_usuario(nome=nome, email=email, senha=senha)

# Listar todos os usuário cadastrados.
    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios() 
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} Email: {usuario.email} Senha: {usuario.senha}")


if __name__ == "__main__":
    main()