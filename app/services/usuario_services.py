from models.usuario_models import Usuario
from repositories.usuario_repositories import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository
    def criar_usuario (self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario (nome = nome, email=email, senha=senha)
            
            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)
            
            if not novo_usuario:
                print("Usuário já cadastrado!")
            return
            
            if consulta_usuario:
                print("Usuário já Existe no Banco de dados.")
                return
            
            self.repository.salvar_usuario (usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print(f"ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios (self):
        return self.repository.listar_todos_usuarios()
    
