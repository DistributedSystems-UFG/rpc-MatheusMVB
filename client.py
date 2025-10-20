import rpyc
from constRPYC import PORT, SERVER
import os

class Client:

    conn = rpyc.connect(SERVER, PORT) # Connect to the server
    os.system('clear')
    print(f"Conectado ao Servidor {SERVER}:{PORT}")
    while True:
        print("\n--- MENU ---")
        print("1. Exibir lista")
        print("2. Adicionar valor")
        print("3. Remover valor")
        print("4. Ordenar lista")
        print("5. Pesquisar valor")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            print("Lista atual:", conn.root.exposed_values())

        elif op == "2":
            val = int(input("Valor a adicionar: "))
            print(conn.root.exposed_append(val))
    
        elif op == "3":
            val = int(input("Valor a remover: "))
            print(conn.root.exposed_remove(val))

        elif op == "4":
            print(conn.root.exposed_sort())

        elif op == "5":
            val = int(input("Valor a pesquisar: "))
            print(conn.root.exposed_search(val))


        elif op == "0":
            print("Encerrando conexão...")
            conn.close()
            break

        else:
            print("Opção inválida!")
        input("Pressione enter para continuar...")
        os.system('clear')

Client()
