import os
from pathlib import Path

import yaml

from minisweagent import package_dir
from minisweagent.agents.default import DefaultAgent
from minisweagent.environments.local import LocalEnvironment
from minisweagent.models.litellm_model import LitellmModel

def main():
    # Load the OpenRouter configuration
    config_path = Path(package_dir / "config" / "openrouter.yaml")
    config = yaml.safe_load(config_path.read_text())

    # Get the model configuration
    model_config = config["model"]


    # Create the agent
    agent = DefaultAgent(
        LitellmModel(**model_config),
        LocalEnvironment(cwd="workspace"),
        **yaml.safe_load(Path(package_dir / "config" / "default.yaml").read_text())["agent"],
    )

    # Run a simple task
    task = "Write a script in python that prints hello and run it."
    print(agent.run(task))

    return agent

if __name__ == "__main__":
    main()
