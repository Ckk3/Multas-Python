import pickle


#Modulos que utilizarei
def criar_bin(nome_arquivo, dados):
    with open(f'{nome_arquivo}', 'wb') as f:
        pickle.dump(dados, f, pickle.HIGHEST_PROTOCOL)

    print(f'O arquivo {nome_arquivo} foi atualizado com sucesso!')

def carregar_bin(nome_arquivo):
    with open(f'{nome_arquivo}', 'rb') as f:
        dados_bin = pickle.load(f)
        return dados_bin

def cadastrar_motorista():
    nome = str(input('Cadastrar novo motorista:\nNome: ')).strip()
    cnh = str(input('CNH: ')).strip()
    cnh = str(verificar_cnh(numero_cnh=cnh))
    dia = str(input('Data de Nascimento:\n-Dia: ')).strip()
    mes = str(input('-Mês: ')).strip()
    ano = str(input('-Ano: ')).strip()
    data_nascimento = (dia, mes, ano)
    print(f'''
Verifique as informações.
Nome: {nome}
CNH: {cnh}
Data de Nascimento: {data_nascimento}
    ''')

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
    modelo = str(input('Cadastrar um novo veículo:\nModelo: ')).strip()
    placa = str(input('Placa (Ex. FLA 2016): ')).strip().upper()
    placa = str(verificar_placa(numero_placa=placa)).upper()
    print(placa)
    cnh_dono = str(input('CNH do proprietário: ')).strip()
    cor = str(input('Cor do veículo: '))
    print(f'''
Verifique as informações.
Modelo: {modelo}
Placa: {placa}
CNH do Proprietário: {cnh_dono}
Cor: {cor}
        ''')

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
    print('altera')


def cadastrar_infracao():
    print('intra')


def valores_padroes():
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

def verificar_placa(numero_placa):
    placa_duplicada = False
    novo_numero_placa = ''
    for key in veiculos:
        if str(numero_placa) == str(key):
            placa_duplicada = True
            break
        else:
            placa_duplicada = False

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

def verificar_cnh(numero_cnh):

    cnh_duplicada = False
    novo_numero_cnh = ''
    for key in motoristas:
        if str(numero_cnh) == str(key):
            cnh_duplicada = True
            break
        else:
            cnh_duplicada = False

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


def receber_resposta(pergunta=str(), opcoes=list()):
    resposta = str(input(pergunta)).strip()
    while resposta not in opcoes:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!!')
        resposta = str(input(pergunta)).strip()

    return str(resposta)


def mostrar_menu():
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



#Lendo os dados de um arquivo binário
dados = carregar_bin(nome_arquivo='multas.bin')

#Separando os dados retirandos do .bin
motoristas = dados[0]
veiculos = dados[1]
infracoes = dados[2]
naturezas = dados[3]


mostrar_menu()
#for f in dados:
#    print(f)

