from datetime import datetime
from datetime import timedelta
from datetime import date



def feriadosMoveis():
    FeriadosMoveis = []

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
        mes = 04

    else:
        dia = (d + e + 22)
        mes = 03

    if (dia == 26 and mes == 04):
        dia = 19

    elif (dia == 25 and mes == 04 and d == 28 and a > 10):
        dia = 18

    pascoa = str(dia) + '/' + str(mes) + '/' + str(ano)
    datetime.strptime(pascoa, '%d/%m/%Y').date()

    carnavalTerça = pascoa
    carnavalTerça = carnavalTerça.timedelta(days=-45)

def feriadosFixos():
    ano = date.today ()
    ano = str (ano.year)
    listaFeriados = []
    #feriadosNacionais = ('01/01/ 21/04/ 01/01/ 07/07/ 12/10/ 02/11/ 15/11/ 25/12/ )
    #feriadosEstaduaisEMunicipais = ('19/03/ 25/03/ 15/08/ ')
    feriados = ('01/01/ 21/04/ 01/01/ 07/07/ 12/10/ 02/11/ 15/11/ 25/12/ 19/03/ 25/03/ 15/08/').split (' ')
    for i in range (len (feriados)):
        data = feriados[i]
        data += ano
        listaFeriados.append (datetime.strptime (data, '%d/%m/%Y').date ())
    return listaFeriados

def calcularPrazos(dataFim, diasUteis):
    dataFimSP = datetime.strptime (dataFim, '%d/%m/%Y').date ()
    prazoSubmeter = dataFimSP
    feriado = feriadosFixos ()
    prazo = 0
    while (prazo != diasUteis):
        if ((prazoSubmeter.weekday () != 5 and prazoSubmeter.weekday () != 6) and (prazoSubmeter not in feriado)):
            prazo = prazo + 1
        prazoSubmeter += timedelta (days=1)
    print (prazoSubmeter)



