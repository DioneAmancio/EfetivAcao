from jira.client import JIRA

options = {
    'server': 'https://jira.atlassian.com'
}

jira = JIRA(options)
projects = jira.projects()



i = 0
print(projects)
while i< len(projects):
    print(projects[i])
    i = i+1


