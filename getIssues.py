from jira.client import JIRA

options = {
    'server': 'https://jira.atlassian.com'
}

jira = JIRA(options)
projects = jira.projects()
nameProjecTest = 'loud'

'''def acessarProjetos(projectName):
    jira = JIRA(options)
    projects = jira.projects()'''


