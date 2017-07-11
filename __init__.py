import urllib2
import json

repositories = ["1888", "1588", "1499", "977"]
private_token = "aHTy85Xzs1hbAjFkY111"

for repository_id in repositories:
    response = urllib2.urlopen("https://git.netcracker.com/api/v4/projects/"
                               + repository_id
                               + "/merge_requests?state=opened&private_token="
                               + private_token
                               ).read()
    json_response = json.loads(response)
    for mr in json_response:
        print mr['author']['name'] + " wait while '" + mr['title'] + "' will be reviewed. You can open it by link: " + mr['web_url']
