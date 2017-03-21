from jira.client import JIRA

options = {
    'server': 'https://jira.atlassian.com'
}


def listarSiglaProjetosJira():
    projectSigla = []
    jira = JIRA(options)
    projects = jira.projects()

    for i in range(len(projects)):  # Laço para percorrer todos os projetos
        projectSigla.append(projects[i])  # Adiciona em uma lista todos as siglas dos projetos
    return projectSigla


def listarNomeProjetosJira():
    projectsName = []
    jira = JIRA(options)
    projects = jira.projects()
    for i in range(len(projects)):  # Laço para percorrer todos os projetos
        jra = jira.project(str(projects[i]))  # retorna ao nome do projeto onde a sigla (str(projects[i]) foi passada como parâmetro
        projectsName.append(jra.name)  # Adiciona em uma lista todos os nomes dos projetos

    return projectsName

def buscarIssue(NomeProjeto):
    jira = JIRA(options)
    listaProjetos = listarNomeProjetosJira()
    listaSiglas = listarSiglaProjetosJira()
    for i in range(len(listaProjetos)):
        if NomeProjeto in listaProjetos[i]:
            print(listaSiglas[i])
            itemProjeto = 'project='+str(listaSiglas[i])
            issue = jira.search_issues('%s AND issuetype = Bug AND component = "Account Administration" AND created >= 2015-03-02 AND created <= 2015-03-26' %itemProjeto)
            print(issue[0])
            return str(issue[0])


def createdDate(data): 
    idIssue = data
    jira = JIRA(options)
    issue = jira.issue(idIssue, expand='changelog')
    changelog = issue.changelog

    for history in changelog.histories:
        for item in history.items:
            dataStart = history.created
            #print ('Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString)
            print(dataStart)
