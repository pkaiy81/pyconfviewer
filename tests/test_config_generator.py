import unittest
import os
import shutil
from src.pyconfviewer.config_generator import ConfigGenerator
from src.pyconfviewer.diff_generator import DiffGenerator
import yaml
import json
import configparser
from dotenv import dotenv_values


class TestConfigAndDiffGenerator(unittest.TestCase):
    def setUp(self):
        # Define the paths for the mock configs
        self.config_a_dir = "tests/mock_configs/config_a"
        self.config_b_dir = "tests/mock_configs/config_b"
        self.output_dir = "tests/output"
        self.config_html = os.path.join(self.output_dir, "config_report.html")
        self.diff_html = os.path.join(self.output_dir, "diff_report.html")

        # Ensure output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Initialize generators
        self.config_generator = ConfigGenerator()
        self.diff_generator = DiffGenerator()

    def test_generate_config_html(self):
        # Mock data loading
        configs_a = self._load_configs(self.config_a_dir)

        # Generate the HTML report for configs_a
        self.config_generator.generate_config_html(
            configs_a, output_dir=self.output_dir, output_html_path=self.config_html
        )

        # Assert HTML report is generated
        self.assertTrue(os.path.exists(self.config_html))

        # Optionally, assert that the HTML contains certain expected elements
        with open(self.config_html, "r") as f:
            html_content = f.read()
            self.assertIn("<title>Configuration Viewer</title>", html_content)

    def test_generate_diff_html(self):
        # Mock data loading
        configs_a = self._load_configs(self.config_a_dir)
        configs_b = self._load_configs(self.config_b_dir)

        # Generate the diff between config_a and config_b
        diffs = self.diff_generator.generate_diff(configs_a, configs_b)
        self.diff_generator.generate_diff_html(
            diffs, output_dir=self.output_dir, output_html_path=self.diff_html
        )

        # Assert HTML diff report is generated
        self.assertTrue(os.path.exists(self.diff_html))

        # Optionally, check the diff data in the HTML
        with open(self.diff_html, "r") as f:
            html_content = f.read()
            self.assertIn("<title>Configuration Diff Viewer</title>", html_content)

    def _load_configs(self, config_dir):
        """Helper function to load mock config files."""
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
                    section: dict(config.items(section))
                    for section in config.sections()
                }
            elif file_name == ".env":
                configs[file_name] = dotenv_values(file_path)
        return configs

    def tearDown(self):
        # Cleanup generated files
        for file in [self.config_html, self.diff_html]:
            if os.path.exists(file):
                os.remove(file)

        # Remove the output directory and all its contents
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)


if __name__ == "__main__":
    unittest.main()
