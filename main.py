import pickle


#Modulos
def criar_bin(nome_arquivo, dados):
    '''
    Função para criar o arquivo binario (.bin) a partir de uma lista de dados
    :param nome_arquivo: nome do arquivo .bin que vai ser criado
    :param dados: conjunto de listas ou dicionarios
    '''
    with open(f'{nome_arquivo}', 'wb') as f:
        pickle.dump(dados, f, pickle.HIGHEST_PROTOCOL)

    print(f'O arquivo {nome_arquivo} foi atualizado com sucesso!')


def carregar_bin(nome_arquivo):
    '''
    Serve para carregar os dados de um arquivo binario (.bin) para serem manipulados
    :param nome_arquivo: nome do arquivo que vai ser carregado
    :return: o conjunto de arquivos em forma de lista
    '''
    with open(f'{nome_arquivo}', 'rb') as f:
        dados_bin = pickle.load(f)
        return dados_bin


def cadastrar_motorista():
    '''
    Função para cadastrar um motorista
    '''
    #Recebendo Dados
    nome = str(input('Cadastrar novo motorista:\nNome: ')).strip()
    cnh = str(input('CNH: ')).strip()
    cnh = str(verificar_cnh_disponivel(numero_cnh=cnh))
    dia = str(input('Data de Nascimento:\n-Dia: ')).strip()
    mes = str(input('-Mês: ')).strip()
    ano = str(input('-Ano: ')).strip()
    data_nascimento = (dia, mes, ano)
    #Verificação por parte do usuário
    print(f'''
Verifique as informações.
Nome: {nome}
CNH: {cnh}
Data de Nascimento: {data_nascimento}
    ''')
    #Salvar ou não os dados recebidos
    resposta = receber_resposta('Deseja salvar as informações em multas.bin ou alterar algum valor?\n1- Quero salvar\n2-Quero alterar um valor\n->', opcoes= ['1', '2'])
    if resposta == '1':
        motoristas[f'{cnh}'] = (f'{nome}', data_nascimento)
        novos_dados = [motoristas, veiculos, infracoes, naturezas]
        criar_bin(nome_arquivo='multas.bin', dados=novos_dados)
    elif resposta == '2':
        cadastrar_motorista()
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def cadastrar_veiculo():
    '''
    Função para cadastrar um novo veículo
    '''
    #Recebendo dados
    modelo = str(input('Cadastrar um novo veículo:\nModelo: ')).strip()
    placa = str(input('Placa (Ex. FLA 2016): ')).strip().upper()
    placa = str(verificar_placa_disponivel(numero_placa=placa)).upper()
    print(placa)
    cnh_dono = str(input('CNH: ')).strip()
    cnh_dono = str(verificar_cnh_existe(numero_cnh=cnh_dono))
    cor = str(input('Cor do veículo: '))
    #Verificação dos dados por parte do usuário
    print(f'''
Verifique as informações.
Modelo: {modelo}
Placa: {placa}
CNH do Proprietário: {cnh_dono}
Cor: {cor}
        ''')
    #Salvar ou não os dados recebidos
    resposta = receber_resposta(
        'Deseja salvar as informações em multas.bin ou alterar algum valor?\n1- Quero salvar\n2-Quero alterar um valor\n->',
        opcoes=['1', '2'])
    if resposta == '1':
        veiculos[f'{placa}'] = (f'{cnh_dono}',f'{modelo}', f'{cor}')
        novos_dados = [motoristas, veiculos, infracoes, naturezas]
        criar_bin(nome_arquivo='multas.bin', dados=novos_dados)
    elif resposta == '2':
        cadastrar_veiculo()
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def alterar_proprietario():
    '''
    Função para alterar o proprietário de um veículo
    '''
    #Recebendo dados
    placa = str(input('Placa (Ex. FLA 2016): ')).strip().upper()
    placa = str(verificar_placa_existe(numero_placa=placa)).upper()
    cnh_novo = str(input('CNH do novo proprietário: ')).strip()
    cnh_novo = str(verificar_cnh_existe(numero_cnh=cnh_novo))
    #Verificação dos dados feita pelo usuário
    print(f'''
Verifique as informações.
Placa: {placa}
CNH: {cnh_novo}
Dados obtidos pela placa: {veiculos[f'{placa}']}
Dados obtidos pelo CNH: {motoristas[f'{cnh_novo}']}
''')
    #Salvar ou não os dados recebidos
    resposta = receber_resposta(
        'Deseja salvar as informações em multas.bin ou alterar algum valor?\n1- Quero salvar\n2-Quero alterar um valor\n->',
        opcoes=['1', '2'])
    if resposta == '1':
        cnh_alterado = {f'{placa}' : (f'{cnh_novo}', veiculos[f'{placa}'][1], veiculos[f'{placa}'][2])}
        veiculos.update(cnh_alterado)
        novos_dados = [motoristas, veiculos, infracoes, naturezas]
        criar_bin(nome_arquivo='multas.bin', dados=novos_dados)
    elif resposta == '2':
        alterar_proprietario()
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def cadastrar_infracao():
    '''
    Função pra cadastrar infração
    '''
    #Recebendo dados
    numero_infracao = infracoes[-1][0] + 1
    dia = str(input('Data da Infração:\n-Dia: ')).strip()
    mes = str(input('-Mês: ')).strip()
    ano = str(input('-Ano: ')).strip()
    data_infracao = (dia, mes, ano)
    placa_infracao = str(input('Placa (Ex. FLA 2016): ')).strip().upper()
    placa_infracao = str(verificar_placa_existe(numero_placa=placa_infracao)).upper()
    resposta = receber_resposta(pergunta='Qual a natureza da infração que você está denunciando?\n1- Leve\n2- Média\n3- Grave\n4- Gravíssima\n->', opcoes=['1','2','3','4'])
    natureza_infracao = descobrir_natureza(opcao=resposta)
    # Verificação dos dados feita pelo usuário
    print(f'''
    Verifique as informações.
    Numero da infração: {numero_infracao}
    Data: {data_infracao}
    Placa: {placa_infracao}
    Dados obtidos pela placa: {veiculos[f'{placa_infracao}']}
    Natureza da infração: {natureza_infracao}
    ''')
    #Salvar ou não os dados recebidos
    resposta = receber_resposta(
        'Deseja salvar as informações em multas.bin ou alterar algum valor?\n1- Quero salvar\n2-Quero alterar um valor\n->',
        opcoes=['1', '2'])
    if resposta == '1':
        infracoes.append([numero_infracao, data_infracao, f'{placa_infracao}', f'{natureza_infracao}'])
        novos_dados = [motoristas, veiculos, infracoes, naturezas]
        criar_bin(nome_arquivo='multas.bin', dados=novos_dados)
    elif resposta == '2':
        cadastrar_infracao()
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def valores_padroes():
    '''
    Cria um arquivo binário(.bin) somente os primeiros valores inseridos pelo Enzo
    '''
    #Dados já castrados pelo Enzo
    motoristas = {"01234567" : ("Seu Madruga", (15,10,2019)),
                  "12345678" : ("Dona Florinda", (14,10,2019))}
    veiculos = {"FLA 1981": ("12345678", "Fusca", "Preto"),
                "ALE 2014": ("12345678", "Brasilia", "Prata"),
                "BRU 0071": ("01234567", "Chevette", "Branco")}
    infracoes = [(1,(15,10,2018),"BRU 0071","Gravissima"),
                (2,(16,10,2018),"BRU 0071","Gravissima"),
                (3,(17,10,2018),"ALE 2014","Leve")]
    naturezas = {"Leve" : 3, "Media" : 4,
                "Grave" : 5, "Gravissima" : 7}

    dados_cadastratos = [motoristas, veiculos, infracoes, naturezas]
    #Colocar os dados dentro de um arquivo binário
    criar_bin(nome_arquivo='multas.bin', dados=dados_cadastratos)


def verificar_placa_disponivel(numero_placa):
    '''
    Função que verifica se a placa já foi cadastrada
    :param numero_placa: codigo da nova placa inserido pelo usuario
    :return: uma string com o valor de uma placa válida ainda não registrada
    '''
    placa_duplicada = False
    novo_numero_placa = ''
    #Procura se ja existe uma placa com esse codigo
    for key in veiculos:
        if str(numero_placa) == str(key):
            placa_duplicada = True
            break
        else:
            placa_duplicada = False
    #Pede pro usuario digitar uma placa ate ser uma sem cadastro
    while placa_duplicada:
        print('!!!Essa placa já está cadastrada!!!')
        novo_numero_placa = str(input('Digite uma placa válida: ')).strip().upper()
        for key in veiculos:
            if str(novo_numero_placa) == str(key):
                placa_duplicada = True
                break
            else:
                placa_duplicada = False

        if not placa_duplicada:
            return novo_numero_placa
    else:
        return numero_placa


def verificar_cnh_disponivel(numero_cnh):
    '''
    Função pra verificar se a cnh ja foi cadastrada
    :param numero_cnh: numero do novo cnh inserido pelo usuario
    :return: string com o número de uma cnh que ainda não foi registrada
    '''
    cnh_duplicada = False
    novo_numero_cnh = ''
    #Pesquisa se já existe esse cnh registrado
    for key in motoristas:
        if str(numero_cnh) == str(key):
            cnh_duplicada = True
            break
        else:
            cnh_duplicada = False
    #Pede pro usuario digitar um cnh ate ser um sem cadastro
    while cnh_duplicada:
        print('!!!Esse número de CNH já foi cadastrado!!!')
        novo_numero_cnh = str(input('Digite uma CNH válida: ')).strip()
        for key in motoristas:
            if str(novo_numero_cnh) == str(key):
                cnh_duplicada = True
                break
            else:
                cnh_duplicada = False

        if not cnh_duplicada:
            return novo_numero_cnh
    else:
        return numero_cnh


def verificar_cnh_existe(numero_cnh):
    '''
    Função para verificar se o cnh existe
    :param numero_cnh: numero do cnh inserido pelo usuario
    :return: string com um número de cnh válido que está cadastrado
    '''
    cnh_existe = False
    #Pesquisa se esse cnh existe
    for key in motoristas:
        if str(numero_cnh) == str(key):
            cnh_existe = True
            break
        else:
            cnh_existe = False
    #Pede pro usuario digitar um cnh ate ser um cadastrado
    while not cnh_existe:
        print('!!!Esse número de CNH NÃO está cadastrado!!!')
        novo_numero_cnh = str(input('Digite um número de CNH existente: ')).strip().upper()
        for key in motoristas:
            if str(novo_numero_cnh) == str(key):
                cnh_existe = True
                break
            else:
                cnh_existe = False

        if cnh_existe:
            return novo_numero_cnh
    else:
        return numero_cnh


def verificar_placa_existe(numero_placa):
    '''
    Função para verificar se a placa existe
    :param numero_placa: codigo da placa inserida pelo usuario
    :return: string com o codigo de uma placa que está cadastrada
    '''
    placa_existe = False
    novo_numero_placa = ''
    #Pesquisa se essa placa existe
    for key in veiculos:
        if str(numero_placa) == str(key):
            placa_existe = True
            break
        else:
            placa_existe = False
    #Pede pro usuario digitar uma placa ate ser uma cadastrada
    while not placa_existe:
        print('!!!Essa placa NÃO está cadastrada!!!')
        novo_numero_placa = str(input('Digite uma placa existente: ')).strip().upper()
        for key in veiculos:
            if str(novo_numero_placa) == str(key):
                placa_existe = True
                break
            else:
                placa_existe = False

        if placa_existe:
            return novo_numero_placa
    else:
        return numero_placa


def descobrir_natureza(opcao=str()):
    '''
    Função para descobrir a natureza da infracao
    :param opcao: opcao escolhida pelo usuario
    :return: string com algum desses valores [Leve, Grave, Media ou Gravissima]
    '''
    if opcao == '1':
        return 'Leve'
    elif opcao == '2':
        return 'Media'
    elif opcao == '3':
        return 'Grave'
    elif opcao == '4':
        return 'Gravissima'
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def receber_resposta(pergunta=str(), opcoes=list()):
    '''
    Função para verificar as repostas para evitar opções invalidas
    :param pergunta: pergunta que sera feita ao usuário
    :param opcoes: respostas que podem ser aceitas
    :return: string com a opção que o usuario escolheu
    '''
    resposta = str(input(pergunta)).strip()
    while resposta not in opcoes:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!!')
        resposta = str(input(pergunta)).strip()

    return str(resposta)


def mostrar_menu():
    '''
    Função que imprime o menu e mostra as opções
    '''
    print('!!!BEM-VINDO!!!')
    print('Selecione alguma opção abaixo:')
    print('''
1- Cadastrar um novo motorista
2- Cadastrar um novo veículo
3- Alterar proprietário de um veículo
4- Cadastrar uma nova infração
5- Sair do sistema
    ''')
    #Recebendo a resposta
    resposta = receber_resposta(pergunta='Digite o número da opção desejada: ', opcoes=['1','2','3', '4', '5'])

    if resposta == '1':
        cadastrar_motorista()
    elif resposta == '2':
        cadastrar_veiculo()
    elif resposta == '3':
        alterar_proprietario()
    elif resposta == '4':
        cadastrar_infracao()
    elif resposta == '5':
        exit()
    else:
        print('Ocorreu um erro inesperado, por favor tente novamente')


def ver_dados(arquivo=list()):
    '''
    Função que print todos os dados extraidos do arquivo .bin
    :param arquivo: uma lista com os valores que foram extraidos anteriormente
    '''
    for dado in arquivo:
        print(dado)

#inicio do programa

#Lendo os dados armazenados no arquivo binário
dados = carregar_bin(nome_arquivo='multas.bin')

#Separando os dados retirandos do arquivo binário
motoristas = dados[0]
veiculos = dados[1]
infracoes = dados[2]
naturezas = dados[3]


mostrar_menu()

#Utilizadas para controle
#valores_padroes()
#ver_dados(dados)
