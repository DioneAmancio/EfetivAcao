listaProjetos = []

def processar(nomeProjeto):
    listaProjetos.append(nomeProjeto)
    return listaProjetos

def validarProjetos ( ):
    for i in range(len(listaProjetos)):
        print("Projeto: ")
        print(listaProjetos[i])
