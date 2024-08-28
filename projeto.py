# Importa o módulo random, que contém funções para gerar números aleatórios
import random

# Atalhos para cores
r = '\033[31m'  # Vermelho
g = '\033[32m'  # Verde
b = '\033[34m'  # Azul
y = '\033[33m'  # Amarelo
rs = '\033[0;0m'  # Resetar cor

# Função principal do menu
def menu():
  # Exibe as opções de módulos disponíveis
    print(f'''Para começar escolhar um dos módulos a seguir de acordo com a funcionalidade que deseja no momento:

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
          
    {y} Digite 0 para sair. {rs}     
  ''')
    # Solicita ao usuário que escolha um módulo
    return int(input("Digite o número do modulo: "))

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
    print(f"{r} Opção inválida...{rs}")

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
        modificar_texto()
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
        print(f"{r} Opção inválida...{rs}")

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
       print(f"{r} Opção inválida...{rs}")

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
       print(f"{r} Opção inválida...{rs}")
        
# Módulo Matemática

# Função para realizar operações simples
def operacoes_simples():
    # Loop infinito para manter o programa executando até que o usuário escolha sair
    while True:
        try:
            # Exibe o menu de operações e solicita que o usuário escolha uma
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
            # Verifica se a operação escolhida é inválida
            elif operacao not in [1, 2, 3, 4]:
                print('Operação invalida. Tente novamente.')
                continue # Retorna ao início do loop para o usuário escolher novamente

            # Solicita os valores para a operação
            valor = float(input('Digite o primeiro valor a ser realizada operação: '))
            valor2 = float(input('Digite o segundo valor a ser realizada operação: '))

            # Realiza a operação escolhida e exibe o resultado
            if operacao == 1:
                print('Resultado: ', valor + valor2)
            elif operacao == 2:
                print('Resultado: ', valor - valor2)
            elif operacao == 3: 
                print('Resultado: ', valor * valor2)
            elif operacao == 4:
                try:
                    print('Resultado: ', valor / valor2)
                except ZeroDivisionError: # Trata o erro de divisão por zero
                    print('Erro: Divisão por zero não é permitida.')
        # Trata o erro de entrada inválida (quando o usuário insere algo que não é número)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Função para exibir a tabuada de um número
def tabuada():
    # Solicita ao usuário o valor para a tabuada
    n = int(input('Qual será o valor da tabuada: '))
    # Solicita ao usuário até qual número a tabuada deve ser calculada
    limite = int(input('Até qual número deseja calcular a tabuada: '))

    # Loop para calcular e exibir a tabuada até o valor fornecido pelo usuário
    for v in range(1, limite + 1):
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

# Função para calcular a sequência de Fibonacci dos primeiros n números
def fibonacci():
    # Solicita ao usuário o número de termos da sequência de Fibonacci que deseja calcular
    n = int(input('Quantos termos deseja calcular na sequência de Fibonacci: '))

    # Inicializa a lista com os dois primeiros termos da sequência
    sequencia = [1, 1]

    # Calcula os termos da sequência até o n-ésimo termo
    for i in range(2, n):
        proximo_termo = sequencia[-1] + sequencia[-2] # Soma os dois últimos termos
        sequencia.append(proximo_termo)

    # Exibe a sequência de Fibonacci
    print('Sequência de Fibonacci:', sequencia[:n])

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

# Módulo texto

# Função para modificar o texto de acordo com a escolha do usuário
def modificar_texto():
    # Solicita ao usuário que insira o texto a ser modificado
    texto = input('Digite o texto que deseja modificar: ')
    # Solicita ao usuário que escolha o tipo de modificação
    modificar = int(input('''Qual modificação deseja realizar no texto:
    1 - Caixa alta
    2 - Caixa baixa
    3 - Capitalizado
    '''))

    # Verifica a escolha do usuário e aplica a modificação correspondente
    if modificar == 1:
        # Converte o texto para caixa alta
        print(texto.upper())
    elif modificar == 2:
        # Converte o texto para caixa baixa
        print(texto.lower())
    else:
        # Capitaliza o texto (primeira letra maiúscula, restante minúsculas)
        print(texto.capitalize())

# Função para contar a ocorrência de uma palavra em um texto
def contagem_ocorrencia():
    # Solicita ao usuário que insira o texto a ser analisado e converte para minúsculas
    texto = input('Digite o texto que deseja analisar: ').lower()
    # Solicita ao usuário que insira a palavra a ser contada e converte para minúsculas
    palavra = input('Qual palavra deseja ver a contagem de ocorrência: ').lower()
    # Divide o texto em palavras usando o espaço como delimitador
    analise = texto.split(' ')

    # Conta e exibe o número de ocorrências da palavra no texto
    print(f'A palavra {palavra} aparece {analise.count(palavra)} no texto ')

# Função para recortar partes de um texto com base em um termo de busca
def recorte_texto():
    # Solicita ao usuário que insira o texto a ser recortado e converte para minúsculas
    texto = input('Digite o texto que deseja recortar: ').lower()
    # Solicita ao usuário que insira o termo de busca
    termo = input('Qual termo deseja buscar: ')

    # Inicializa a posição de busca
    posicao = 0

    while True:
        # Encontra a posição do termo no texto a partir da posição atual
        posicao = texto.find(termo, posicao)

        # Se o termo não for encontrado, sai do loop
        if posicao == -1: 
            break

        # Calcula a posição inicial e final do recorte, garantindo que não ultrapasse os limites do texto
        inicio = max(0, posicao - 3)
        fim = min(len(texto), posicao + len(termo) + 3)

        # Exibe a ocorrência encontrada com um recorte de 3 caracteres antes e depois do termo
        print(f"Ocorrência encontrada: '{texto[inicio:fim]}' ")

        # Atualiza a posição para continuar a busca após o termo encontrado
        posicao += len(termo)

        # Pergunta ao usuário se deseja continuar a busca
        continuar = input("Deseja continuar buscando? (S/N): ").lower()
        if continuar == 'n':
            break

# Função para gerar uma senha aleatória
def gerador_senha():
    try:
        # Solicita ao usuário o tamanho da senha
        tamanho = int(input('Digite quantos caracteres a senha precisa ter: '))
        # Define os caracteres possíveis para a senha
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?@#$%*"

        # Gera a senha aleatória escolhendo caracteres aleatórios da lista
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        # Exibe a senha gerada
        print(senha)
    except ValueError:
        # Trata o erro de entrada inválida (quando o usuário insere algo que não é número)
        print('Entrada inválida! Por favor, insira um número.')

# Função para contar a ocorrência de cada palavra em um texto
def contagem_palavra():
    # Solicita ao usuário que insira o texto a ser analisado
    texto = input('Digite o texto que faremos a contagem de palavras: ')
    # Divide o texto em palavras usando o espaço como delimitador
    t = texto.split(' ')
    # Dicionário para armazenar a contagem de cada palavra
    contagem = {}

    # Loop para contar as ocorrências de cada palavra
    for palavra in t:
        if palavra in contagem:
            # Incrementa a contagem se a palavra já estiver no dicionário
            contagem[palavra] += 1
        else:
            # Adiciona a palavra ao dicionário com contagem inicial de 1
            contagem[palavra] = 1

    # Exibe a contagem de palavras
    print('Contagem de palavras: ')
    for palavra, quantidade in contagem.items():
        print(f'{palavra}: {quantidade}')

# Módulo escola

# Função para validar a entrada de notas
def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            # Verifica se o valor está dentro do intervalo permitido
            if valor < 0 or valor > 10:
                print('Por favor, insira uma nota válida entre 0 e 10.')
            else:
                return valor
        except ValueError:
            # Trata o erro de entrada inválida (não numérica)
            print('Entrada inválida. Digite um número válido.')

# Função para validar entradas inteiras
def validar_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            # Trata o erro de entrada inválida (não numérica)
            print('Entrada inválida. Digite um número inteiro válido.')

# Função para calcular a média aritmética das notas
def media_aritmedica():
    # Inicializa o contador de notas e a soma das notas
    cont = 1
    soma_nota = 0

    while True:
        # Solicita ao usuário que insira uma nota
        nota = validar_float(f'Digite a nota - {cont}: ')
        # Adiciona a nota à soma total
        soma_nota += nota
        # Calcula a média aritmética atual
        nota_final = soma_nota / cont

        # Pergunta ao usuário se deseja finalizar o cálculo
        sair = input('Deseja finalizar o cálculo? (S/N) ').lower()
        if sair == 's':
            print('Finalizando...')
            break

        # Incrementa o contador de notas
        cont += 1
    
    # Exibe a média aritmética das notas fornecidas até o momento
    print(f'A média aritmética das notas fornecidas é {nota_final:.2f}')

# Função para calcular a média ponderada das notas
def media_ponderada():
    # Inicializa o contador de notas, a soma ponderada das notas e a soma dos pesos
    cont = 1
    soma_nota = 0
    soma_peso = 0

    while True:
        # Solicita ao usuário que insira uma nota
        nota = validar_float(f'Digite a nota - {cont}: ')
        # Solicita ao usuário que insira o peso da nota
        peso = validar_float(f'Qual o peso da nota - {cont}: ')
        # Adiciona a nota ponderada à soma total das notas ponderadas
        soma_nota += nota * peso
        # Adiciona o peso à soma total dos pesos
        soma_peso += peso
        # Calcula a média ponderada atual
        media = soma_nota / soma_peso

        # Pergunta ao usuário se deseja finalizar o cálculo da média ponderada
        sair = input('Deseja finalizar o cálculo de média ponderada? (S/N) ').lower()
        if sair == 's':
            print('Finalizando...')
            break

        # Incrementa o contador de notas
        cont += 1

    # Exibe a média ponderada das notas fornecidas até o momento
    print(f'A média ponderada das notas fornecidas é {media:.2f}')

# Função para calcular a porcentagem de faltas de um aluno
def faltas():
    # Solicita ao usuário a carga horária total da disciplina
    carga = validar_int('Carga horária da disciplina? ')
    # Solicita ao usuário a quantidade de horas/aulas por encontro
    hora_aula = validar_int('Quantidade de horas/aulas por encontro: ')
    # Solicita ao usuário a quantidade de faltas do aluno
    faltas = validar_int('Quantidade de faltas: ')

    # Calcula o número total de aulas
    aulas = carga / hora_aula
    # Calcula a porcentagem de faltas
    porcentagem = (faltas / aulas) * 100
    # Calcula o limite de faltas permitido (25% do total de aulas)
    limite = aulas * 0.25
    # Calcula quantas faltas ainda são permitidas
    restantes = limite - faltas

    # Verifica se o aluno ultrapassou o limite de faltas
    if porcentagem > 25:
        print('Esse aluno já atingiu ou ultrapassou o limite de faltas e está reprovado por falta')
    else:
        print(f'Este aluno pode faltar {restantes:.0f} dias sem ser reprovado')

# Função para gerenciar a biblioteca
def biblioteca():
    # Lista para armazenar os livros cadastrados
    livros = []
    # Dicionário para armazenar a quantidade de livros por categoria
    categorias = {}
    # Solicita ao usuário a data atual no formato AAAAMMDD
    data = validar_int('Digite a data de hoje (formato AAAAMMDD): ')
    # Dicionário para armazenar os livros em atraso por categoria
    atrasos = {}

    while True:
        # Solicita ao usuário os detalhes do livro
        titulo = input('Qual o título do livro: ')
        isbn = validar_int('Digite o ISBN do livro: ')
        categoria = input('Em qual categoria ele se encaixa: ')
        emprestimo = validar_int('Digite a data de empréstimo deste título (formato AAAAMMDD): ')
        devolucao = validar_int('Digite a data prevista de devolução (formato AAAAMMDD): ')

        # Cria um dicionário com os detalhes do livro e adiciona à lista de livros
        livro = {'Titulo': titulo, 'ISBN': isbn, 'Categoria': categoria, 'Data do empréstimo': emprestimo, 'Data prevista devolução': devolucao}
        livros.append(livro)

        # Atualiza a quantidade de livros por categoria
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

        # Verifica se o livro está em atraso
        if devolucao < data:
            if categoria in atrasos:
                atrasos[categoria]['quantidade'] += 1
                atrasos[categoria]['livros'].append(livro)
            else:
                atrasos[categoria] = {'quantidade': 1, 'livros': [livro]}
        
        # Pergunta ao usuário se deseja cadastrar outro livro
        continuar = input('Deseja cadastrar outro livro? (s/n): ').lower()
        if continuar != 's':
            break

    # Exibe os livros cadastrados
    print("Livros cadastrados:", livros)
    # Exibe a quantidade de livros por categoria
    print("Quantidade de livros por categoria:", categorias)
    # Exibe a quantidade de livros em atraso por categoria
    print("Quantidade de livros em atraso por categoria:", {cat: atrasos[cat]['quantidade'] for cat in atrasos})
    
    # Exibe os detalhes dos livros em atraso
    print("Livros em atraso:")
    for categoria in atrasos:
        print(f"Categoria: {categoria}")
        for livro in atrasos[categoria]['livros']:
            print(f"- Título: {livro['Titulo']}, ISBN: {livro['ISBN']}")

# Módulo miscelâneas

# Função para validar o formato de duração da música
def validar_duracao(mensagem):
    while True:
        # Solicita ao usuário que insira a duração da música
        duracao = input(mensagem)
        # Divide a entrada em partes usando ':' como delimitador
        partes = duracao.split(':')

        # Verifica se a duração está no formato MM:SS
        if len(partes) == 2:
            minutos, segundos = partes

            # Verifica se ambas as partes são números
            if minutos.isdigit() and segundos.isdigit():
                minutos = int(minutos)
                segundos = int(segundos)

                # Verifica se segundos estão no intervalo correto (0 a 59) e minutos são não negativos
                # Também pode adicionar uma verificação para limitar minutos a um intervalo razoável, se desejado
                if 0 <= segundos < 60 and minutos >= 0:
                    return duracao
                
        # Mensagem de erro para duração inválida
        print('Duração inválida. Por favor, insira no formato MM:SS onde MM e SS são valores não negativos e SS < 60.')

# Função para codificar um texto
def codificar():
    # Solicita ao usuário que insira o texto a ser codificado
    texto = input('Digite o texto que será codificado: ')
    # Solicita ao usuário que insira um número para a codificação
    n = validar_int('Digite um número: ')
    # Lista para armazenar os valores codificados
    codificar = []

    # Loop para cada caractere no texto
    for elemento in texto:
        # Obtém o valor ASCII do caractere
        ascii = ord(elemento)
        # Multiplica o valor ASCII pelo número fornecido
        cod = ascii * n
        # Adiciona o valor codificado à lista como string
        codificar.append(str(cod))

    # Junta os valores codificados em uma única string, separados por espaços
    codificado = ' '.join(codificar)
    # Exibe o texto codificado
    print(codificado)

# Função para decodificar uma mensagem codificada
def decodificar():
    # Solicita ao usuário que insira a mensagem codificada
    texto = input('Digite a mensagem codificada para ser decodificada: ')
    # Solicita ao usuário que insira o número usado na codificação
    n = validar_int('Digite um número: ')
    # Divide a mensagem codificada em partes usando espaços como delimitadores
    codificados = texto.split()
    # Lista para armazenar os caracteres decodificados
    decodificar = []

    # Loop para cada elemento na lista de partes codificadas
    for elemento in codificados:
        # Converte o elemento de volta para um número inteiro
        ascii = int(elemento)
        # Divide o valor pelo número fornecido para obter o valor ASCII original
        dec = ascii // n
        # Converte o valor ASCII de volta para um caractere
        caractere = chr(dec)
        # Adiciona o caractere decodificado à lista
        decodificar.append(caractere)

    # Junta os caracteres decodificados em uma única string
    decodificado = ''.join(decodificar)
    # Exibe a mensagem decodificada
    print(decodificado)

# Função para desenhar uma árvore de Natal
def arvore_natal():
    # Solicita ao usuário que insira o tamanho da árvore (número de linhas)
    linhas = validar_int('Digite o tamanho da árvore (número de linhas): ')

    # Loop para desenhar cada linha da árvore
    for cont in range(linhas):
        # Desenha uma linha da árvore com espaços, barras e asteriscos
        print(' ' * (linhas - cont - 1) + '/' + '*' * (2 * cont + 1) + '\\')

    # Desenha o tronco da árvore
    print(' ' * (linhas - 1) + '|')

# Função para gerenciar uma playlist de músicas
def playlist():
    # Lista para armazenar as músicas
    musicas = []

    while True:
        # Solicita ao usuário os detalhes da música
        nome = input('Digite o nome da música: ')
        artista = input('Digite o nome do artista: ')
        album = input('Digite o álbum que essa música faz parte: ')
        genero = input('Digite o gênero da música: ')
        duracao = validar_duracao('Digite a duração dessa música [ex.: 10:30]: ')

        # Cria um dicionário com os detalhes da música e adiciona à lista
        musica = {'Nome': nome, 'Artista': artista, 'Álbum': album, 'Gênero': genero, 'Duração': duracao}
        musicas.append(musica)

        # Pergunta ao usuário se deseja finalizar a organização da playlist
        continuar = input('Deseja finalizar a organização da playlist? (s/n): ').lower()
        if continuar == 's':
            break

    while True:
        try:
            # Solicita ao usuário a ordem de visualização das músicas
            ordem = int(input('''Qual ordem deseja visualizar suas músicas:
            1 - nome da música
            2 - artista
            3 - álbum
            4 - gênero
            5 - duração
            ''' ))

            # Ordena a lista de músicas com base na escolha do usuário
            if ordem == 1:
                musicas.sort(key=lambda x: x['Nome'])
            elif    ordem == 2:
                musicas.sort(key=lambda x: x['Artista'])
            elif    ordem == 3:
                musicas.sort(key=lambda x: x['Álbum'])
            elif    ordem == 4:
                musicas.sort(key=lambda x: x['Gênero'])
            elif    ordem == 5:
                # Função para converter a duração da música em segundos
                def duracao_em_segundos(duracao):
                    minutos, segundos = map(int, duracao.split(':'))
                    return minutos * 60 + segundos

                # Ordena a lista de músicas pela duração em segundos
                musicas.sort(key=lambda x: duracao_em_segundos(x['Duração']))
            else:
                # Levanta uma exceção para escolha inválida
                raise ValueError
        except ValueError:
            # Mensagem de erro para escolha inválida
            print('Escolha inválida. Por favor, selecione uma opção entre 1 e 5')

        # Exibe a lista de músicas organizada
        for musica in musicas:
            print(f"Nome: {musica['Nome']}, Artista: {musica['Artista']}, Álbum: {musica['Álbum']}, Gênero: {musica['Gênero']}, Duração: {musica['Duração']}")


# Main do projeto
# Inicializa a escolha com um valor diferente de 0 para entrar no loop
escolha = -1

# Chama o menu até a pessoa dizer que quer sair. Para sair, deve-se digitar 0
while escolha != 0:
    escolha = menu()  # Chama a função menu e atribui a escolha

    # Verifica se a escolha está dentro do intervalo permitido
    if escolha < 0 or escolha > 4:
        print(f"{r}Opção inválida{rs}")  # Mensagem de erro para opção inválida
    elif escolha == 0:
        print('Saindo...')
    elif escolha == 1:
        menu_matematica()  # Chama a função correspondente ao módulo de matemática
    elif escolha == 2:
        menu_texto()  # Chama a função correspondente ao módulo de texto
    elif escolha == 3:
        menu_escola()  # Chama a função correspondente ao módulo de escola
    elif escolha == 4:
        menu_miscelaneas()  # Chama a função correspondente ao módulo de miscelâneas

    # Pausa para o usuário pressionar ENTER antes de continuar
    input('\n\t Tecle ENTER para continuar')
