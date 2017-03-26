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

def buscarIssueRDP(NomeProjeto):
    jira = JIRA(options)
    listaProjetos = listarNomeProjetosJira()
    listaSiglas = listarSiglaProjetosJira()
    for i in range(len(listaProjetos)):
        if NomeProjeto in listaProjetos[i]:
            itemProjeto = 'project='+str(listaSiglas[i])
            issue = jira.search_issues('%s AND issuetype = Bug AND status = Closed ORDER BY created DESC' %itemProjeto) #Falta ajustar a JQL de acordo com as necessidades
            #print("Field:", field_name, "Value:", issue.raw['fields'][field_name])   --Será necessário para usar na migração
            return str(issue[0])


def buscarIssueRAG(NomeProjeto):
    jira = JIRA(options)
    listaProjetos = listarNomeProjetosJira()
    listaSiglas = listarSiglaProjetosJira()
    for i in range(len(listaProjetos)):
        if NomeProjeto in listaProjetos[i]:
            itemProjeto = 'project='+str(listaSiglas[i])
            issue = jira.search_issues('%s AND issuetype = Bug AND status = Closed ORDER BY created DESC' %itemProjeto) #Falta ajustar a JQL de acordo com as necessidades
            return str(issue[0])


def buscarIssueBHP(NomeProjeto):
    jira = JIRA(options)
    listaProjetos = listarNomeProjetosJira()
    listaSiglas = listarSiglaProjetosJira()
    for i in range(len(listaProjetos)):
        if NomeProjeto in listaProjetos[i]:
            itemProjeto = 'project='+str(listaSiglas[i])
            issue = jira.search_issues('%s AND issuetype = Bug AND status = Closed ORDER BY created DESC' %itemProjeto) #Falta ajustar a JQL de acordo com as necessidades
            return str(issue[0])