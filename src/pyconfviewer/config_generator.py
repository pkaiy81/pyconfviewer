import os
import json
from jinja2 import Environment, FileSystemLoader


class ConfigGenerator:
    def __init__(self):
        # Define the base path where the templates are stored (relative to this script's directory)
        self.base_dir = os.path.dirname(__file__)  # This will be 'src/pyconfviewer'
        template_path = os.path.join(self.base_dir, "templates")
        self.env = Environment(loader=FileSystemLoader(template_path))

    def generate_config_html(
        self, configs, output_dir="output", output_html_path="output/config_report.html"
    ):
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Convert configs to JSON string with escaped quotes
        configs_json = json.dumps(configs).replace('"', '\\"')

        # Render HTML with embedded JSON data
        template = self.env.get_template("config_viewer.html")
        rendered_html = template.render(configs_json=configs_json)

        # Write the rendered HTML to the output path
        with open(output_html_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
