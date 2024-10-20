import os
import json
import yaml
import configparser
from dotenv import dotenv_values

class ConfigLoader:
    def __init__(self):
        self.configs = {}

    def load_configs(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                filepath = os.path.join(root, file)
                if file.endswith(('.yaml', '.yml')):
                    self.configs[file] = self._load_yaml(filepath)
                elif file.endswith('.json'):
                    self.configs[file] = self._load_json(filepath)
                elif file.endswith('.ini'):
                    self.configs[file] = self._load_ini(filepath)
                elif file == '.env':
                    self.configs[file] = self._load_env(filepath)
                else:
                    # Not supported file format
                    pass

    def _load_yaml(self, filepath):
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)

    def _load_json(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)

    def _load_ini(self, filepath):
        config = configparser.ConfigParser()
        config.read(filepath)
        return {section: dict(config.items(section)) for section in config.sections()}

    def _load_env(self, filepath):
        return dotenv_values(filepath)
