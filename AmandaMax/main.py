import sys
import os

# Esse bloco garante que o Python encontre suas pastas mesmo se o VS Code se perder
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importações das camadas (Ajustadas para o seu sistema de Cinema)
from repository.session_repository import SessionRepository
from service.session_service import SessionService
from controller.movie_controller import MovieController
from view.movie_view import MovieView

def bootstrap():
    """
    Função principal que faz a Injeção de Dependências.
    Ela liga o Repositório no Serviço, o Serviço no Controller e o Controller na View.
    """
    print("Iniciando Sistema de Gestão de Cinema...")

    # 1. Instância do Repositório (Dados)
    # Aqui criamos o objeto que simula o Banco de Dados
    repository = SessionRepository()

    # 2. Instância do Serviço (Regras de Negócio)
    # Passamos o repository para o service (Injeção)
    service = SessionService(repository)

    # 3. Instância do Controller (Orquestrador)
    # Passamos o service para o controller. 
    # Usamos o nome MovieController para bater com seu arquivo atual.
    controller = MovieController(service)

    # 4. Instância da View (Interface)
    # A view recebe o controller para interagir com o usuário
    view = MovieView(controller)

    # 5. Execução do Menu
    view.exibir_menu()

if __name__ == "__main__":
    try:
        bootstrap()
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
    except Exception as e:
        print(f"Erro crítico ao iniciar o sistema: {e}")