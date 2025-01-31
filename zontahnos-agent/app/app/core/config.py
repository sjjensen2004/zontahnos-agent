import os
import yaml

# Define the YAML config file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")


class Config:
    """Configuration loader for YAML environment variables."""

    def __init__(self, file_path):
        self.config = {}
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                self.config = yaml.safe_load(file)  # Load YAML safely

    def get(self, key, default=None):
        """Retrieve a config value, returning default if missing."""
        return self.config.get(key, default)


# Create a global config object
config = Config(CONFIG_FILE)
