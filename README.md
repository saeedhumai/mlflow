# MLflow DSPy Text Classification

A machine learning project that demonstrates text classification using MLflow and DSPy, leveraging OpenAI's GPT models.

## Project Overview

This project implements a text classification system using:
- MLflow for experiment tracking and model management
- DSPy for prompt engineering and model optimization
- OpenAI's GPT models for text classification
- Reuters-21578 dataset for training and testing

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install mlflow dspy openai python-dotenv pandas numpy
```

3. Configure environment:
- Create a `.env` file
- Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

- `ml.py`: Main script for model configuration
- `mlfl.ipynb`: Jupyter notebook containing the text classification implementation
- `data/`: Directory containing training and test datasets
- `mlruns/`: MLflow tracking directory

## Usage

1. Start MLflow server:
```bash
mlflow ui
```

2. Run the Jupyter notebook:
```bash
jupyter notebook mlfl.ipynb
```

## Features

- Text classification using DSPy's BootstrapFewShotWithRandomSearch
- MLflow experiment tracking and model versioning
- Automated logging of model metrics and parameters
- Dataset handling with train/test split functionality

## License

MIT

## Contributing

Feel free to open issues and pull requests for improvements. 