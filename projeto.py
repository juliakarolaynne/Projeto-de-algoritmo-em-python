# Função principal do menu
def menu():
  # Exibe as opções de módulos disponíveis
  print('''Para começar escolhar um dos módulos a seguir de acordo com a funcionalidade que deseja no momento:

  1 - Matemática
    -> Operações simples
    -> Tabuada
    -> Fatorial
    -> Fibonacci
    -> Soma de matrizes
    -> Orçamento mensal
  2 - Texto
    -> Modificar texto
    -> Contagem de ocorrências
    -> Recortes de textos
    -> Gerador de senhas
    -> Contagem de palavras
  3 - Escola
    -> Cálculo de média aritmética de notas
    -> Média ponderada de notas
    -> Cálculo de porcentagem de faltas
    -> Livros da biblioteca
  4 - Miscelâneas
    -> Codificar mensagem
    -> Decodificar mensagem
    -> Gerar árvore de Natal
    -> Ordenar playlist
  ''')
  # Solicita ao usuário que escolha um módulo
  escolha = int(input("Digite o número do modulo: "))

  # Chama a função correspondente ao módulo escolhido
  if escolha == 1:
    menu_matematica()
  elif escolha == 2:
    menu_texto()
  elif escolha == 3:
    menu_escola()
  elif escolha == 4:
    menu_miscelaneas()
  else:
    # Mensagem de erro para escolha inválida
    print('Opção inválida...')

# Função do menu de matemática
def menu_matematica():
  # Exibe as opções de funcionalidades de matemática
  print('''Escolha uma funcionalidade para se execultada:

  1 - Operações simples
  2 - Tabuada
  3 - Fatorial
  4 - Fibonacci
  5 - Soma de matrizes
  6 - Orçamento mensal
  ''')
  # Solicita ao usuário que escolha uma funcionalidade
  escolha = int(input("Digite o número da funcionalidade: "))

  # Chama a função correspondente à funcionalidade escolhida
  if escolha == 1:
    operacoes_simples()
  elif escolha == 2:
    tabuada()
  elif escolha == 3:
    fatorial()
  elif escolha == 4:
    fibonacci()
  elif escolha == 5:
    matrizes()
  elif escolha == 6:
    orcamento_mensal()
  else:
    # Mensagem de erro para escolha inválida
    print("Opção inválida...")

# Função do menu de texto
def menu_texto():
    # Exibe as opções de funcionalidades de texto
    print('''Escolha uma funcionalidade para ser executada:
    1 - Modificar texto
    2 - Contagem de ocorrências
    3 - Recortes de textos
    4 - Gerador de senhas
    5 - Contagem de palavras
    ''')
    # Solicita ao usuário que escolha uma funcionalidade
    escolha = int(input("Digite o número da funcionalidade: "))

    #Chama a função correspondente à funcionalidade escolhida
    if escolha == 1:
        mofificar_texto()
    elif escolha == 2:
        contagem_ocorrencia()
    elif escolha == 3:
        recorte_texto()
    elif escolha == 4:
        gerador_senha()
    elif escolha == 5:
        contagem_palavra()
    else:
        # Mensagem de erro para escolha inválida
        print("Opção inválida...")

# Função do menu de escola
def menu_escola():
    # Exibe as opções de funcionalidades de escola
    print('''Escolha uma funcionalidade para se execultada:
    1 - Cálculo de média aritmética de notas
    2 - Média ponderada de notas
    3 - Cálculo de porcentagem de faltas
    4 - Livros da biblioteca
    ''')
    # Solicita ao usuário que escolha uma funcionalidade
    escolha = int(input("Digite o número da funcionalidade: "))

    #Chama a função correspondente à funcionalidade escolhida
    if escolha == 1:
       media_aritmedica()
    elif escolha == 2:
       media_ponderada()
    elif escolha == 3:
       faltas()
    elif escolha == 4:
       biblioteca()
    else:
       # Mensagem de erro para escolha inválida
       print('Opção inválida...')

# Função do menu de miscelâleas
def menu_miscelaneas():
    # Exibe as opções de funcionalidades de miscelâneas
    print('''Escolha uma funcionalidade para se execultada:
    1 - Codificar mensagem
    2 - Decodificar mensagem
    3 - Gerar árvore de Natal
    4 - Ordenar playlist
    ''')
    # Solicita ao usuário que escolha uma funcionalidade
    escolha = int(input("Digite o número da funcionalidade: "))

    #Chama a função correspondente à funcionalidade escolhida
    if escolha == 1:
       codificar()
    elif escolha == 2:
       decodificar()
    elif escolha == 3:
       arvore_natal()
    elif escolha == 4:
       playlist()
    else:
       # Mensagem de erro para escolha inválida
       print('Opção inválida...')
        
# Módulo Matemática

# Função para realizar operações simples
def operacoes_simples():
    while True:
        # Solicita ao usuário que escolha uma operação
        operacao = int(input('''Qual operação deseja realizar:

        1 - somar
        2 - subtrair
        3 - multiplicar
        4 - dividir
        5 - sair

        '''))

        # Verifica se o usuário deseja sair
        if operacao == 5:
            print('Saindo...')
            break

        # Solicita os valores para a operação
        valor = int(input('Digite o primeiro valor a ser realizada operação: '))
        valor2 = int(input('Digite o segundo valor a ser realizada operação: '))

        # Realiza a operação escolhida e exibe o resultado
        if operacao == 1:
            print('Resultado: ', valor + valor2)
        elif operacao == 2:
            print('Resultado: ', valor - valor2)
        elif operacao == 3:
            print('Resultado: ', valor * valor2)
        elif operacao == 4:
            print('Resultado: ', valor / valor2)
        else:
            # Mensagem de erro para escolha inválida
            print('Algo deu errado, tente novamente...')

# Função para exibir a tabuada de um número
def tabuada():
    # Solicita ao usuário o valor para a tabuada
    n = int(input('Qual será o valor da tabuada: '))

    # Loop para calcular e exibir a tabuada de 0 a 10
    for v in range(11):
        print(f'{n} x {v} = {v * n}')

# Função para calcular o fatorial de um número
def fatorial():
    # Solicita ao usuário o número para calcular o fatorial
    numero = int(input('Qual número deseja saber o fatorial: '))

    # Inicializa o contador e o resultado
    cont = 1
    resultado = 1

    # Loop para calcular o fatorial
    while cont <= numero:
        resultado *= cont  # Multiplica o resultado pelo contador
        cont += 1  # Incrementa o contador

    # Exibe o resultado do fatorial
    print('Resultado: ', resultado)

# Função para encontrar o n-ésimo termo da sequência de Fibonacci
def fibonacci():
    # Solicita ao usuário o termo da sequência de Fibonacci que deseja encontrar
    n = int(input('Qual termo deseja encontrar: '))

    # Inicializa os dois primeiros termos da sequência
    ultimo, penultimo = 1, 1

    # Verifica se o termo desejado é o primeiro ou o segundo
    if n == 1 or n == 2:
        termo = 1
    else:
        # Inicializa o contador a partir do terceiro termo
        cont = 3
        # Loop para calcular o n-ésimo termo da sequência de Fibonacci
        while cont <= n:
            termo = ultimo + penultimo  # Calcula o próximo termo
            penultimo = ultimo  # Atualiza o penúltimo termo
            ultimo = termo  # Atualiza o último termo
            cont += 1  # Incrementa o contador

    # Exibe o resultado do n-ésimo termo da sequência de Fibonacci
    print('Resultado: ', termo)

# Função para somar duas matrizes
def matrizes():
    # Instruções para o usuário sobre como inserir as matrizes
    print('''Para a soma de matrizes lembre-se de passar os valores da seguinte forma:
    as linhas são separadas por meio de um ponto-e-vírgula e os elementos de cada linha são separados por um espaço em branco
    ex.: "1 2 3; 4 5 6; 7 8 9"
    --------------------------------------------------------------------------------------------------------------------------''')

    # Solicita ao usuário que insira as duas matrizes
    n1 = input('Digite a primeira matriz: ')
    n2 = input('Digite a segunda matriz: ')

    # Converte as entradas de string para listas de inteiros
    matriz1 = [list(map(int, linha.split())) for linha in n1.split(';')]
    matriz2 = [list(map(int, linha.split())) for linha in n2.split(';')]

    # Verifica se as matrizes têm as mesmas dimensões
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes devem ter as mesmas dimensões")
    else:
        # Calcula a soma das matrizes
        matriz_soma = [
            [matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))]
            for i in range(len(matriz1))
        ]

        # Converte a matriz resultante de volta para o formato de string
        resultado = '; '.join(' '.join(map(str, linha)) for linha in matriz_soma)

        # Exibe o resultado da soma das matrizes
        print("Resultado da soma das matrizes:")
        print(resultado)

# Função para gerenciar o orçamento mensal
def orcamento_mensal():
    # Lista para armazenar os itens do orçamento
    itens = []
    # Variáveis para armazenar o total de débitos e créditos
    total_debitos = 0
    total_creditos = 0
    # Dicionário para categorizar os itens
    categorias = {}

    while True:
        # Solicita ao usuário os detalhes do item
        nome = input('Qual o nome do item: ')
        descricao = input('Descreva o item: ')
        valor = float(input('Qual o valor do item? AVISO: em caso de valor de débito, utilize um sinal "-" antes do valor: '))
        categoria = input('Qual a categoria do item (ex: alimentação, transporte, lazer, etc): ')

        # Cria um dicionário com os detalhes do item e adiciona à lista
        item = {'item': f'{nome}', 'Descrição': f'{descricao}', 'valor': valor, 'categoria': categoria}
        itens.append(item)

        # Atualiza o total de débitos ou créditos
        if valor < 0:
            total_debitos += abs(valor)
        else:
            total_creditos += valor

        # Atualiza a contagem de itens por categoria
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

        # Pergunta ao usuário se deseja finalizar o orçamento
        sair = input('Deseja finalizar esse orçamento? (S/N) ').lower()
        if sair == 's':
            print('Finalizando...')
            break

    # Exibe o total de débitos e créditos
    print(f'Total de débitos: {total_debitos:.2f}')
    print(f'Total de créditos: {total_creditos:.2f}')
    # Exibe a categorização das despesas
    print('Categorização das despesas:')
    for cat, count in categorias.items():
        print(f'Categoria {cat}: {count} item(ns)')

    # Exibe os detalhes dos itens
    print('Detalhes dos itens:')
    for item in itens:
        print(item)



# Chama a função principal do menu
menu()