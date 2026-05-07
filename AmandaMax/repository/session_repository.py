from model.session import Session

class SessionRepository:
    def __init__(self):
        # Dados iniciais para teste
        self.data = {
            1: Session(1, "Vingadores", 100, 90),
            2: Session(2, "O Poderoso Chefão", 50, 10)
        }

    def buscar_por_id(self, session_id):
        return self.data.get(session_id)

    def atualizar(self, session):
        self.data[session.id] = session
        return True