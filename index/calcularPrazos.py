from datetime import datetime, timedelta

from index.holidayList import feriadosFixos


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