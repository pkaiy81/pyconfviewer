import os
import json

class ConfigGenerator:
    def __init__(self):
        # Define the base path where the templates are stored (relative to this script's directory)
        self.base_dir = os.path.dirname(__file__)  # This will be 'src/pyconfviewer'

    def generate_config_html(self, configs, output_dir='static/json', output_html_path='output/config_report.html'):
        # 1. Save the configs to a JSON file
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        json_output_path = os.path.join(output_dir, 'configs.json')
        with open(json_output_path, 'w') as json_file:
            json.dump(configs, json_file, indent=4)
        
        # 2. Define the template path relative to this script's directory
        html_template_path = os.path.join(self.base_dir, 'templates', 'config_viewer.html')
        
        # 3. Generate the HTML that loads the JSON data via fetch()
        self._generate_html(html_template_path, output_html_path)

    def _generate_html(self, template_path, output_html_path):
        # 4. Read the template file
        with open(template_path, 'r') as template_file:
            html_content = template_file.read()

        # 5. Write the content to the output HTML file
        with open(output_html_path, 'w') as output_html_file:
            output_html_file.write(html_content)
