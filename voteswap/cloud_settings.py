"""CloudSettings read settings from a backing datastore.

When running the site locally, this will read from local_settings.yaml. When
run in production it will read from Google Datastore

Inspired by http://stackoverflow.com/a/35261091
"""

import os

local = (
    False if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine')
    else True)


def load_local_settings():
    import yaml
    with open('local_settings.yaml', 'r') as f:
        local_settings = yaml.load(f)
    if os.path.isfile('local_secrets.yaml'):
        with open('local_secrets.yaml', 'r') as f:
            secrets = yaml.load(f)
        local_settings.update(secrets)
    return local_settings


local_settings = load_local_settings() if local else {}


class CloudSettings(object):
    is_local = local

    @staticmethod
    def get(var):
        try:
            if local:
                return local_settings[var]
            else:
                raise ValueError("Settings not defined yet: {}".format(var))
        except KeyError:
            raise ValueError("No setting found for {}".format(var))
