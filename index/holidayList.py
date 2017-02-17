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
    sextaSanta = date.fromordinal(pascoa.toordinal() - 2)
    corpusChristi = date.fromordinal(pascoa.toordinal() + 60)

    FeriadosMoveis.append(tercaCarnaval)
    FeriadosMoveis.append(sextaSanta)
    FeriadosMoveis.append(pascoa)
    FeriadosMoveis.append(corpusChristi)

    return FeriadosMoveis


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


def feriadosPonte(fMoveis, fFixos):
    feriadoPonte = []
    feriados = []
    feriados.append(fMoveis)
    feriados.append(fFixos)
    for i in range(len(feriados)):
        feriados[i] = datetime.strptime(feriados[i], '%d/%m/%Y').date()
        if feriados[i].weekday() == 1:
            feriadoPonte.append(date.fromordinal(feriados[i].toordinal() - 1))
        elif feriados[i].weekday() == 3:
            feriadoPonte.append(date.fromordinal(feriados[i].toordinal() + 1))

    return feriadoPonte

fixo = feriadosFixos()
movel = feriadosMoveis()
ponte = feriadosPonte(movel, fixo)











