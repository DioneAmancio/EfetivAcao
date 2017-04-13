from datetime import datetime, timedelta, date

def calduloDaPascoa():
    ano = date.today()
    ano = int(ano.year)

    x = 24
    y = 5
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = ((19 * a + x) % 30)
    e = ((2 * b + 4 * c + 6 * d + y) % 7)

    if ((d + e) > 9):
        dia = (d + e - 9)
        mes = 4

    else:
        dia = (d + e + 22)
        mes = 3

    if (dia == 26 and mes == 4):
        dia = 19

    elif (dia == 25 and mes == 4 and d == 28 and a > 10):
        dia = 18

    pascoa = str(dia) + '/' + str(mes) + '/' + str(ano)
    pascoa = datetime.strptime(pascoa, '%d/%m/%Y').date()

    return pascoa

def feriadosMoveis():
    FeriadosMoveis = []
    pascoa = calduloDaPascoa()
    tercaCarnaval = date.fromordinal(pascoa.toordinal() - 47)
    segundaCarnaval = date.fromordinal(pascoa.toordinal() - 48)
    quartaCinzas = date.fromordinal(pascoa.toordinal() - 46)
    sextaSanta = date.fromordinal(pascoa.toordinal() - 2)
    corpusChristi = date.fromordinal(pascoa.toordinal() + 60)

    FeriadosMoveis.append(segundaCarnaval)
    FeriadosMoveis.append(tercaCarnaval)
    FeriadosMoveis.append(quartaCinzas)
    FeriadosMoveis.append(sextaSanta)
    FeriadosMoveis.append(corpusChristi)

    return FeriadosMoveis


def feriadosFixos():
    ano = date.today ()
    ano = str (ano.year)
    listaFeriados = []
    #feriadosNacionais = ('01/01/ 21/04/ 01/01/ 07/07/ 12/10/ 02/11/ 15/11/ 25/12/ )
    #feriadosEstaduaisEMunicipais = ('19/03/ 25/03/ 15/08/ ')
    feriados = ('01/01/ 21/04/ 07/09/ 12/10/ 02/11/ 15/11/ 25/12/ 19/03/ 25/03/ 15/08/').split (' ')

    for i in range (len (feriados)):
        data = feriados[i]
        data += ano
        listaFeriados.append (datetime.strptime (data, '%d/%m/%Y').date ())
    return listaFeriados


def feriadosPonte(fPontes):
    feriadoPonte = []
    for i in range(len(fPontes)):
        if fPontes[i].weekday() == 1 and (date.fromordinal(fPontes[i].toordinal() - 1) not in fPontes):
            feriadoPonte.append(date.fromordinal(fPontes[i].toordinal() - 1))
        if fPontes[i].weekday() == 3 and (date.fromordinal(fPontes[i].toordinal() + 1) not in fPontes):
            feriadoPonte.append(date.fromordinal(fPontes[i].toordinal() + 1))

    return feriadoPonte



Feriados = feriadosMoveis() + feriadosFixos() #Inserindo os feriados na lista Feriados
FeriadosPontes = feriadosPonte(Feriados) #Calculando os feriados pontes com base nos feriados
Feriados = Feriados + FeriadosPontes #Incluindo em uma unica lista os feriados e feriados pontes


def calcularPrazos(dataBase, diasUteis):
    '''DataBase é a data em que a sprint acabou, e será tomada como base para a contagem dos prazos'''
    if(type(dataBase) is str):
        dataFim = datetime.strptime(dataBase, '%d/%m/%Y').date()
    prazoSubmeter = dataFim
    prazo = 1
    while (prazo < diasUteis):
        if ((prazoSubmeter.weekday() != 5 and prazoSubmeter.weekday() != 6) and (prazoSubmeter not in Feriados)):
            prazo = prazo + 1
        prazoSubmeter += timedelta(days=1)
    return prazoSubmeter