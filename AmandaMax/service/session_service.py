class SessionService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_presenca(self, session_id, quantidade):
        sessao = self.repository.buscar_por_id(session_id)
        
        if not sessao:
            return False, "Erro: Sessão não encontrada."

        # Validação da RN02: Não exceder a capacidade
        if sessao.current_attendance + quantidade > sessao.capacity:
            espaco_restante = sessao.capacity - sessao.current_attendance
            return False, f"Erro: Capacidade excedida. Restam apenas {espaco_restante} lugares."

        # Se passou na regra, atualiza
        sessao.current_attendance += quantidade
        self.repository.atualizar(sessao)
        return True, f"Sucesso! {quantidade} lugar(es) registrados para '{sessao.movie_title}'."