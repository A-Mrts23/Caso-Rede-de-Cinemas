class MovieView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        print("=== Sistema de Gestão de Cinema ===")
        print("Sessões disponíveis:")
        print("1 - Vingadores (Capacidade: 100)")
        print("2 - O Poderoso Chefão (Capacidade: 50)")
        print("Digite 'sair' para encerrar.\n")

        while True:
            try:
                entrada = input("Digite o ID da sessão e a quantidade (ex: 1 5): ").strip()
                if entrada.lower() == 'sair':
                    print("Encerrando o sistema...")
                    break

                partes = entrada.split()
                if len(partes) != 2:
                    print("Formato inválido. Use: ID quantidade")
                    continue

                session_id = int(partes[0])
                quantidade = int(partes[1])

                if quantidade <= 0:
                    print("Quantidade deve ser positiva.")
                    continue

                message = self.controller.post_attendance(session_id, quantidade)
                print(message)
                print()

            except ValueError:
                print("IDs e quantidades devem ser números inteiros.")
            except KeyboardInterrupt:
                print("\nEncerrando...")
                break