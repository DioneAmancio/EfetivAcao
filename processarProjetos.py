from jira.client import JIRA
from getIssues import *
from datetime import datetime, timedelta
from holidayList import *

listaProjetos = []

def processar(nomeProjeto):
    listaProjetos.append(nomeProjeto)
    return listaProjetos

def dataCriacao(idIssue): #retorna a data em que a issue foi criada. Serve para a validação de submissão de RT, realização de RAG e submissão de BHP

    options = {'server': 'https://jira.atlassian.com'}
    jira = JIRA(options)
    issue = jira.issue(idIssue)

    for field_name in issue.raw['fields']:
        if field_name == "created":
            created = issue.raw['fields'][field_name]
            return str(created)


def dataRevisao (idIssue): #Retorna a data em que a issue foi resolvida. Serve para saber se a RT foi concluída no prazo.
    options = {'server': 'https://jira.atlassian.com'}
    jira = JIRA(options)
    issue = jira.issue(idIssue)

    for field_name in issue.raw['fields']:
        if field_name == "resolutiondate":
            resolutiondate = issue.raw['fields'][field_name]
            return str(resolutiondate)

def calcularPrazos(dataFim, diasUteis):
    dataFimSP = datetime.strptime (dataFim, '%d/%m/%Y').date ()
    prazoSubmeter = dataFimSP
    feriado = feriadosFixos () + feriadosMoveis() + feriadosPonte(feriadosFixos()+feriadosMoveis())
    prazo = 1
    while (prazo < diasUteis):
        if ((prazoSubmeter.weekday () != 5 and prazoSubmeter.weekday () != 6) and (prazoSubmeter not in feriado)):
            prazo = prazo + 1
        prazoSubmeter += timedelta (days=1)
    print (prazoSubmeter)

def validarProjetos ( ):
    for i in range(len(listaProjetos)):
        idIssue = buscarIssueRDP(listaProjetos[i])
        datainicio = dataCriacao(idIssue)
        datarevisado = dataRevisao(idIssue)
        print(datainicio)
        print(datarevisado)

