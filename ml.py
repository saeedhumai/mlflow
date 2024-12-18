# Set OpenAI API Key to the environment variable. You can also pass the token to dspy.LM()
import getpass
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
import dspy

# Define your model. We will use OpenAI for simplicity
model_name = "gpt-4o-mini"

# Leverage default authentication inside the Databricks context (notebooks, workflows, etc.)
# Note that an OPENAI_API_KEY environment must be present. You can also pass the token to dspy.LM()
lm = dspy.LM(
    model=f"openai/{model_name}",
    max_tokens=500,
    temperature=0.1,
)
dspy.settings.configure(lm=lm)


import mlflow

mlflow.set_experiment("DSPy Quickstart")

mlflow.dspy.autolog()
