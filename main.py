import pickle
import datetime


#Modulos que utilizarei
def create_bin(nome_arquivo, dados):
    with open(f'{nome_arquivo}', 'wb') as f:
        pickle.dump(dados, f, pickle.HIGHEST_PROTOCOL)

def read_bin(nome_arquivo):
    dados_bin = pickle.loads(nome_arquivo)
    return dados_bin

def cadastrar_motorista():
    nome = str(input('Cadastrar novo motorista:\nNome: ')).strip()
    cnh = int(input('CNH: '))
    nasc = str(input('Data de Nascimento(Use vírgula: DD,MM,AAAA): '))


#Dados já castrados
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
create_bin(nome_arquivo='multas.bin', dados=dados_cadastratos)


#Lendo os dados de um arquivo binário
dados = read_bin('multas.bin')

print(dados)



