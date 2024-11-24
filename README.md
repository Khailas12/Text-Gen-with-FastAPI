# Text Generation with FastAPI
This project implements a **Text Generation API** using **FastAPI**. It leverages pre-trained models from the Hugging Face library to generate text responses based on user-provided prompts. The application supports multiple models (e.g., `gpt2`, `distilgpt2`) and allows fine-tuning of generation parameters.
## 1. FastAPI Framework:
The core of the application is built using **FastAPI**, a modern web framework for building APIs with Python. FastAPI is known for its speed, automatic OpenAPI documentation generation, and ease of use, which makes it an excellent choice for developing APIs quickly.

## 2. Hugging Face Models:
The project utilizes pre-trained language models from **Hugging Face's Transformers library**, specifically:

- **GPT-2**: A transformer-based model for natural language processing tasks, including text generation. It's known for producing human-like text based on given prompts.
- **DistilGPT-2**: A smaller and more efficient version of GPT-2, providing similar capabilities with reduced computational requirements.

These models are used to generate text, and they are pre-loaded into memory when the FastAPI application starts up. This ensures that text generation can occur quickly without the need to load the models on every request.

## 3. Text Generation Process:
When a user sends a prompt to the API, the following happens:

- The user specifies a **prompt** along with several optional parameters, such as `max_length`, `temperature`, `top_p`, and `top_k`.
  - **max_length**: Determines the maximum length of the generated text.
  - **temperature**: Controls the randomness of the output (higher values make the output more random).
  - **top_p** and **top_k**: Parameters for controlling the sampling method, where `top_p` refers to nucleus sampling and `top_k` refers to the number of top tokens considered at each generation step.

- The API passes this prompt and the parameters to the pre-trained models, and the models generate text based on the prompt.
- The generated text is then returned as a response to the user.

## 4. Multiple Model Support:
The API supports multiple models for text generation. By default, it includes **GPT-2** and **DistilGPT-2**, allowing users to select or compare outputs from different models. The generated text for each model is included in the response, giving users multiple options based on the same input prompt.

## 5. Asynchronous Operation:
The application is designed to handle multiple requests concurrently. It uses asynchronous programming to ensure that requests are processed efficiently, particularly when generating text from large models. This prevents the server from blocking while waiting for the model to generate text, allowing it to serve other requests in parallel.

## 6. Parameter Fine-Tuning:
The user has the ability to fine-tune the text generation process by adjusting various parameters:

- **temperature**: Controls randomness (higher values mean more unpredictable text).
- **top_p** and **top_k**: Control how the model samples words, with `top_p` implementing nucleus sampling and `top_k` considering only the top `k` most probable tokens.
- **max_length**: Defines the maximum number of tokens to generate.
- **num_return_sequences**: Specifies how many different sequences of text to generate for a single prompt.

These settings allow for a highly customizable text generation experience, tailored to the needs of different users or use cases.

## Table of Contents

- [Text Generation with FastAPI](#text-generation-with-fastapi)
  - [1. FastAPI Framework:](#1-fastapi-framework)
  - [2. Hugging Face Models:](#2-hugging-face-models)
  - [3. Text Generation Process:](#3-text-generation-process)
  - [4. Multiple Model Support:](#4-multiple-model-support)
  - [5. Asynchronous Operation:](#5-asynchronous-operation)
  - [6. Parameter Fine-Tuning:](#6-parameter-fine-tuning)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
- [How to Run](#how-to-run)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Clone the repository:](#clone-the-repository)
  - [Run the Application](#run-the-application)
    - [Start the FastAPI application:](#start-the-fastapi-application)
- [Endpoints](#endpoints)
  - [`POST /generate-text/`](#post-generate-text)
    - [Request Body](#request-body)
    - [Response](#response)
    - [JSON Example:](#json-example)
  - [Features](#features)
  - [Code Highlights](#code-highlights)
    - [`main.py`](#mainpy)
    - [`gen/repository/gen.py`](#genrepositorygenpy)
    - [`routers/gen_text.py`](#routersgen_textpy)
  - [Customization](#customization)
  - [Contributing](#contributing)
  - [License](#license)


## Project Structure
```plaintext
├── gen
│   ├── main.py                # Application entry point, starts FastAPI app
│   ├── repository
│   │   ├── gen.py             # Core logic for text generation, including model loading and text generation functions
│   ├── routers
│   │   ├── gen_text.py        # Defines the API route for text generation
│   └── schemas.py             # Contains request and response schema definitions used by the API
├── README.md                  # Project documentation, setup instructions, and usage details
└── requirements.txt           # Lists the Python dependencies for the project

```

---

# How to Run

## Prerequisites
- **Python** (>= 3.8)
- **Pipenv** (optional, for virtual environment management)

## Installation

### Clone the repository:
```bash
git clone https://github.com/Khailas12/Text-Gen-with-FastAPI.git
cd Text-Gen-with-FastAPI
```

---
## Run the Application

### Start the FastAPI application:
```bash
uvicorn gen.main:app --reload
```

# Endpoints

## `POST /generate-text/`
Generate text using multiple models based on the input prompt.

### Request Body
```json
{
  "prompt": "string",
  "max_length": 100,
  "num_return_sequences": 1,
  "temperature": 1.0,
  "top_p": 0.9,
  "top_k": 50
}
```
### Response

### JSON Example:
```json
{
  "generated_texts": {
    "gpt2": ["Generated text by GPT-2 model"],
    "distilgpt2": ["Generated text by DistilGPT-2 model"]
  }
}
```
---

## Features

- **Multiple Models**: Supports multiple text-generation models (`gpt2`, `distilgpt2`).
- **Custom Parameters**: Configure text generation with parameters like:
  - `temperature`
  - `top_p`
  - `top_k`
  - `max_length`
  - `num_return_sequences`
- **Asynchronous Processing**: Handles multiple requests concurrently for scalability.
- **Resource Management**: Models are loaded at startup and released during shutdown.
---

## Code Highlights

### `main.py`
- **Startup Event**: Loads models into memory.
- **Shutdown Event**: Releases resources and clears loaded models.

### `gen/repository/gen.py`
- Implements the core logic for text generation using Hugging Face pipelines.
- Handles exceptions and provides sanitized responses.
- Supports concurrent execution with `async_gen_text`.

### `routers/gen_text.py`
- Defines the API route for text generation.

---
## Customization
- **Add More Models**: Extend the `models` dictionary in `gen/repository/gen.py`.
- **Modify Default Parameters**: Adjust `max_length`, `temperature`, or other parameters as needed.

## Contributing
Feel free to open issues or submit pull requests if you'd like to improve this project!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
