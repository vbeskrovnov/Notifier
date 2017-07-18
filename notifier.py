import time
import json
import imp


def get_plugins(json_input):
    json_input = json.loads(json_input)
    return json_input["plugins"]


def load_plugin(name):
    mod = __import__(name)
    return mod


def call_plugin(name, *args, **kwargs):
    plugin = load_plugin(name)
    plugin.plugin_main(*args, **kwargs)


def read_config():
    f = open('config.json')
    return f


def run():
    json_input = read_config().read()
    while True:
        print "Processing..."
        for plugin in get_plugins(json_input):
            input_path = plugin["input"]["script"]
            input_name = plugin["input"]["name"]
            output_path = plugin["output"]["script"]
            output_name = plugin["output"]["name"]

            input_plugin = imp.load_source(input_name, input_path)
            output_plugin = imp.load_source(output_name, output_path)

            for message in input_plugin.input():
                output_plugin.output(message)

        time.sleep(5)

run()
