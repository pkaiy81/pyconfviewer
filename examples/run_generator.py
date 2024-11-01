import os
from pyconfviewer.config_generator import ConfigGenerator
from pyconfviewer.diff_generator import DiffGenerator

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

# Generate configuration HTML
configs_a = config_generator.load_configs(config_a_dir)
config_generator.generate_config_html(
    configs_a, output_dir=output_dir, output_html_path=config_html
)
print(f"Configuration HTML generated at {config_html}")

# Generate diff HTML
configs_b = config_generator.load_configs(config_b_dir)
diffs = diff_generator.generate_diff(configs_a, configs_b)
diff_generator.generate_diff_html(
    diffs, output_dir=output_dir, output_html_path=diff_html
)
print(f"Diff HTML generated at {diff_html}")
