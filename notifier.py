import time
import json
import imp


def get_inputs(json_input):
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
        for input_plugin in get_inputs(json_input):
            path = input_plugin["input"]["script"]
            name = input_plugin["input"]["name"]
            imp.load_source(name, path).input()

        time.sleep(5)

run()
