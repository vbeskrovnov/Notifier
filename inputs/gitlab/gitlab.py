import urllib2
import json

repositories = ["1888", "1588", "1499", "977"]
private_token = "aHTy85Xzs1hbAjFkY111"


def parse():
    messages = []
    for repository_id in repositories:
        response = urllib2.urlopen("https://git.netcracker.com/api/v4/projects/"
                                   + repository_id
                                   + "/merge_requests?state=opened&private_token="
                                   + private_token
                                   ).read()
        json_response = json.loads(response)
        for mr in json_response:
            if not mr['work_in_progress']:
                author_name = mr['author']['name']
                mr_title = mr['title']
                mr_url = mr['web_url']
                messages.append(author_name + " wait while '" + mr_title
                                + "' will be reviewed. You can open it by link: " + mr_url)
    return messages


def input():
    for message in parse():
        print message
