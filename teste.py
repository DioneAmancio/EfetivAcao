from jira.client import JIRA

options = {'server': 'https://10.101.40.70:8443'}

jira = JIRA(options, basic_auth=('login', 'senha'))

projects = jira.projects()
nameProjecTest = 'CLOUD'

i = 0
print(projects)
while i< len(projects):
    proj = str(projects[i])
    if proj in nameProjecTest:
        print(projects[i])
    i = i+1

