import urllib2
import json

repositories = []
private_token = ""
gitlab_url = ""


def parse():
    messages = []
    for repository_id in repositories:
        repository_id = url_encoding(repository_id)
        response = urllib2.urlopen(gitlab_url + "api/v4/projects/"
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


def url_encoding(repository_id):
    return repository_id.replace("/", "%2F")


def input():
    return parse()
