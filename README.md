Absolutely\! Including instructions for environment variables is a crucial best practice, especially for API tests that often require credentials or specific URLs.

Here's the updated `README.md` for the RESTful-Booker API tests, incorporating the `.env-copy` setup instructions.

-----

# Automated API Tests for RESTful-Booker API

## 📝 Project Description

This repository contains a suite of automated API tests developed to verify the functionality of the **RESTful-Booker API** ([https://restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)).

The tests are written in **Python** using the **Pytest** testing framework and the `requests` library for making HTTP calls.

The primary goal of this project is to ensure the stability and correctness of the key endpoints of the RESTful-Booker API.

## 🚀 Requirements

To successfully run these automated API tests on your local machine, please ensure you have the following tools installed:

  * **Python 3.9+** (latest stable version is recommended)
  * **Git** (for cloning the repository)

## 🛠️ Installation and Setup

Follow these step-by-step instructions to prepare your environment and install the necessary dependencies.

### 1\. Clone the Repository

Open your terminal or command prompt and execute the following command:

```bash
git clone https://github.com/kyryl01011/4.2-homework-task2.git
cd 4.2-homework-task2
```

### 2\. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

```bash
python3 -m venv venv
```

After creating the virtual environment, activate it:

  * **For macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
  * **For Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
  * **For Windows (Command Prompt / CMD):**
    ```cmd
    .\venv\Scripts\activate.bat
    ```

### 3\. Install Python Dependencies

Install all required Python libraries listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4\. Configure Environment Variables

This project uses environment variables to store sensitive information (like API credentials) or configurable parameters.

1.  **Create a `.env` file:** Copy the provided `env-copy` file and rename it to `.env` in the root directory of the project.

    ```bash
    cp env-copy .env
    ```

    *(For Windows CMD, use `copy env-copy .env`)*

2.  **Edit the `.env` file:** Open the newly created `.env` file and fill in your specific credentials or configuration details according to the template provided inside.

## 🚀 Running Tests

Once the installation and setup are complete, you are ready to run the tests.

### Run All Tests

This command will execute all tests discovered by Pytest.

```bash
python -m pytest
```

You can also run specific test files or tests using Pytest's command-line options. For example:

  * **Run tests in a specific file:**
    ```bash
    pytest tests/test_booking.py
    ```
  * **Run tests by keyword:**
    ```bash
    pytest -k "create_booking"
    ```

## 📚 API Documentation

For a deeper understanding of the API functionality tested by this project, you can refer to the official RESTful-Booker API documentation:
[https://restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)

-----