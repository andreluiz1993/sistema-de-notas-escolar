# Dados iniciais
login_correto = "André"
senha_correta = 1234
tentativas = 0
opcao = 0

# Dicionário de alunos e notas
alunos = {
    "Paula": [0, 0, 0, 0],
    "Bruno": [0, 0, 0, 0],
    "André": [0, 0, 0, 0],
    "Carol": [0, 0, 0, 0],
    "Larissa": [0, 0, 0, 0]
}

# Boas-vindas
print("Bom dia")
login = input("Por favor, insira seu login: ")
senha = int(input("Informe a senha: "))

# Verificação de login e senha
while login != login_correto or senha != senha_correta:
    if tentativas < 2:
        tentativas += 1
        print("Login e/ou senha incorretos, tente novamente!")
        login = input("Por favor, insira seu login: ")
        senha = int(input("Informe a senha: "))
    else:
        print("Número de tentativas excedido! Acesso temporariamente bloqueado!")
        break
else:
    print()
    print("Seja bem-vindo(a),", login_correto)
    print('''
    Selecione a opção desejada:
    1 - Registro de notas
    2 - Consulta de notas
    3 - Calcular as médias
    4 - Fechar sistema
    ''')
    
    while opcao != 4:
        opcao = int(input("Qual a opção desejada?: "))

        if opcao == 1:  # Registro de notas
            print("=== Registro de Notas ===")
            for aluno in alunos.keys():
                print(f"\nRegistrando notas para {aluno}:")
                for i in range(4):
                    while True:
                        try:
                            nota = float(input(f"Informe a nota {i + 1}: "))
                            if 0 <= nota <= 10:
                                alunos[aluno][i] = nota
                                break
                            else:
                                print("A nota deve estar entre 0 e 10. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida! Digite um número.")
            print("\nNotas registradas com sucesso!")
                        
        elif opcao == 2:  # Consulta de notas
            print()
            print("=== Consulta de Notas ===")
            for aluno, notas in alunos.items():
                print(f"{aluno}: {notas}")
        
        elif opcao == 3:  # Calcular as médias
            print()
            print("=== Média dos alunos===")
            for aluno, notas in alunos.items():
                print()
                print(f"{aluno}: {sum(notas)/4}")
                if sum(notas)/4 >= 6:
                    print(f"{aluno} foi aprovado(a)!")
                else:
                    print(f"{aluno} foi reprovado(a)!")        
        elif opcao == 4:  # Fechar sistema
            print()
            print("Sistema encerrado. Até mais!")
        else:
            print("Opção inválida!")
