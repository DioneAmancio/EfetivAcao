from jira.client import JIRA
import getIssues

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
            return created


def dataRevisao (idIssue): #Retorna a data em que a issue foi resolvida. Serve para saber se a RT foi concluída no prazo.
    options = {'server': 'https://jira.atlassian.com'}
    jira = JIRA(options)
    issue = jira.issue(idIssue)

    for field_name in issue.raw['fields']:
        if field_name == "resolutiondate":
            resolutiondate = issue.raw['fields'][field_name]
            return resolutiondate

def validarProjetos ( ):
    for i in range(len(listaProjetos)):
        idIssue = getIssues.buscarIssue(listaProjetos[i])
        teste1 = dataCriacao(idIssue)
        teste2 = dataRevisao(idIssue)







