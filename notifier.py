import json
import imp
import schedule
import time


def get_plugins(json_input):
    json_input = json.loads(json_input)
    return json_input["plugins"]


def get_time_of_notification():
    json_input = read_config().read()
    configuration = json.loads(json_input)
    return configuration["timeOfNotification"]


def read_config():
    config_file = open('config.json')
    return config_file


def job():
    json_input = read_config().read()

    print "Processing..."
    for plugin in get_plugins(json_input):
        input_path = plugin["input"]["script"]
        input_name = plugin["input"]["name"]
        output_path = plugin["output"]["script"]
        output_name = plugin["output"]["name"]

        input_script = imp.load_source(input_name, input_path)
        output_script = imp.load_source(output_name, output_path)

        for message in input_script.input():
            output_script.output(message)


def run():
    while True:
        schedule.run_pending()
        time.sleep(1)


def init_scheduling():
    time_of_notification = get_time_of_notification()
    schedule.every().day.at(time_of_notification).do(job)

init_scheduling()
run()
