import collections
import json
import os
import requests


def send(func):
    """
    A function to send messages on slack
    decorator for sending messages.
    """
    def inner(*args, **kwargs):

        if os.environ.get("SLACK_WEBHOOK"):
            webhook = os.environ.get("SLACK_WEBHOOK")
        else:
            raise Exception("No webhooks found")

        msg = func(*args, **kwargs)

        data = dict()

        if isinstance(msg, str):
            data["text"] = msg
            requests.post(webhook, json.dumps(data))

        elif isinstance(msg, list):
            data["text"] = '\n'.join(msg)
            requests.post(webhook, json.dumps(data))

        elif isinstance(msg, (dict, collections.defaultdict, collections.OrderedDict)):
            values = []
            for k, v in msg.items():
                values.append(str(k) + ": " + str(v))
            data["text"] = '\n'.join(values)
            requests.post(webhook, json.dumps(data))

        elif isinstance(msg, dict) and use_raw is True:
            requests.post(webhook, json.dumps(msg))

        else:
            raise Exception(
                "Type for variable: msg, is currently not supported")

    return inner
