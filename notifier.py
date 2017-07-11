import time
import json
import imp


def get_plugins(json_input):
    json_input = json.loads(json_input)
    return json_input["plugins"]


def read_config():
    config_file = open('config.json')
    return config_file


def run():
    json_input = read_config().read()
    while True:
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

        time.sleep(5)

run()
