from datetime import datetime
from datetime import timedelta
from datetime import date


def feriadosFixos():
    ano = date.today ()
    ano = str (ano.year)
    listaFeriados = []
    feriados = ('01/01/ 21/04/ 01/01/ 07/07/ 12/10/ 02/11/ 15/11/ 25/12/ 19/03/ 25/03/ 15/08/').split (' ')
    # feriadosEstaduaisEMunicipais = ('19/03/ 25/03/ 15/08/ ')
    for i in range (len (feriados)):
        data = feriados[i]
        data += ano
        listaFeriados.append (datetime.strptime (data, '%d/%m/%Y').date ())
    return listaFeriados


def calcularPrazos(diasUteis):
    dataFimSP = datetime.strptime (parametro, '%d/%m/%Y').date ()
    prazoSubmeter = dataFimSP
    feriado = feriadosFixos ()
    while (diasUteis != 7):
        if ((prazoSubmeter.weekday () != 5 and prazoSubmeter.weekday () != 6) and (prazoSubmeter not in feriado)):
            diasUteis = diasUteis + 1
        prazoSubmeter += timedelta (days=1)
    print (prazoSubmeter)



