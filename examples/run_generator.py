import os
from pyconfviewer.config_generator import ConfigGenerator
from pyconfviewer.diff_generator import DiffGenerator
import yaml
import json
import configparser
from dotenv import dotenv_values

# Define paths
config_a_dir = "tests/mock_configs/config_a"
config_b_dir = "tests/mock_configs/config_b"
output_dir = "output"
config_html = os.path.join(output_dir, "config_report.html")
diff_html = os.path.join(output_dir, "diff_report.html")

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

config_generator = ConfigGenerator()
diff_generator = DiffGenerator()


def load_configs(config_dir):
    configs = {}
    for file_name in os.listdir(config_dir):
        file_path = os.path.join(config_dir, file_name)
        if file_name.endswith(".yaml"):
            with open(file_path, "r") as f:
                configs[file_name] = yaml.safe_load(f)
        elif file_name.endswith(".json"):
            with open(file_path, "r") as f:
                configs[file_name] = json.load(f)
        elif file_name.endswith(".ini"):
            config = configparser.ConfigParser()
            config.read(file_path)
            configs[file_name] = {
                section: dict(config.items(section)) for section in config.sections()
            }
        elif file_name == ".env":
            configs[file_name] = dotenv_values(file_path)
    return configs


# Generate configuration HTML
configs_a = load_configs(config_a_dir)
config_generator.generate_config_html(
    configs_a, output_dir=output_dir, output_html_path=config_html
)
print(f"Configuration HTML generated at {config_html}")

# Generate diff HTML
configs_b = load_configs(config_b_dir)
diffs = diff_generator.generate_diff(configs_a, configs_b)
diff_generator.generate_diff_html(
    diffs, output_dir=output_dir, output_html_path=diff_html
)
print(f"Diff HTML generated at {diff_html}")
