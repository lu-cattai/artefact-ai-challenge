# Artefact Technical Challenge - AI Agent Junior

This repository contains my solution for the AI Engineer Junior technical challenge. The goal was to build an AI Assistant that can distinguish between general knowledge questions and mathematical calculations, routing them to the appropriate execution path.

## 🚀 How to Run

### Prerequisites
- **Python 3.8+**
- **Ollama**: [Download and install Ollama](https://ollama.com/)
- **Phi-3 Model**: Run the following command in your terminal to download the model:
  ```bash
  ollama run phi3
  ```


### Installation & Execution

1. **Clone this repository**:
```bash
git clone [https://github.com/lu-cattai/artefact-ai-challenge.git](https://github.com/lu-cattai/artefact-ai-challenge.git)
cd YOUR_REPO_NAME

```


2. **(Optional) Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies**:
```bash
pip install ollama

```


4. **Run the agent**:
```bash
python agent.py

```

## 🧠 Implementation Logic

The agent was built using **Object-Oriented Programming (OOP)** for better modularity and scalability. The workflow follows these steps:

1. **Intent Classification**: Every user input is first processed by the `phi3` model to determine if it requires a mathematical calculation (`MATH`) or a general response (`GENERAL`).

2. **Dynamic Routing**:
* **If GENERAL**: The model answers directly using its internal knowledge.
* **If MATH**: The agent triggers a two-step process:
  * **Extraction**: A strict prompt forces the model to extract only the raw numbers and operators (e.g., "128*46").
  * **Tool Execution**: A Python-based `_calculator_tool` cleans the expression using Regex and calculates the exact result using `eval()`, ensuring the precision required by the challenge.


## 💡 What I Learned

* **Model Constraints**: Working with smaller local models like `phi3` showed that prompt engineering must be very specific. Initially, the model tried to solve math problems internally (often incorrectly). I solved this by implementing strict instructions to ensure it only performs extraction.

* **Local LLMs**: Integrating Ollama into a Python workflow provided insights into running AI applications locally, avoiding the need for paid cloud APIs.


## 🛠️ Future Improvements
* **Enhanced Security**: Replace `eval()` with a safer library like `sympy` to prevent potential code injection.

* **Advanced Tools**: Add more "superpowers" like consulting public APIs for weather or news.

* **Memory**: Implement conversation history so the agent can maintain context across multiple turns.
