class MovieController:
    def __init__(self, session_service):
        self.session_service = session_service

    def post_attendance(self, session_id, quantity):
        # O controller apenas repassa e retorna o resultado
        status, message = self.session_service.registrar_presenca(session_id, quantity)
        return message