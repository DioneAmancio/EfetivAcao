from jira.client import JIRA

options = {
    'server': 'https://jira.atlassian.com'
}

jira = JIRA(options)
idIssue = 'CLOUD-9469'
issue = jira.issue(idIssue, expand='changelog')
changelog = issue.changelog

for history in changelog.histories:
    for item in history.items:
        dataStart = history.created
            #print ('Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString)

print("**************")
print(dataStart)