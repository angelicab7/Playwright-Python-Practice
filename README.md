# Playwright-Python-Practice

This project contains a set of automated web UI tests built with **Playwright** and **Python**. It's designed to demonstrate and practice writing robust and maintainable end-to-end tests for [Swag Labs](https://www.saucedemo.com/), a demo website created by Sauce Labs for testing automation.

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

You'll need Python 3.8+ installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Playwright-Python-Practice.git](https://github.com/your-username/Playwright-Python-Practice.git)
    cd Playwright-Python-Practice
    ```

2.  **Create a virtual environment:** (Recommended) 
    ```bash
    uv sync
    source .venv/bin/activate 
    ```
    this project uses uv, see [documentation](https://docs.astral.sh/uv/guides/projects/#managing-version)

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *If you don't have a `requirements.txt` file, you can install them manually:*
    ```bash
    pip install pytest playwright
    playwright install
    ```

## ⚙️ Running the Tests

To run the tests, make sure you are in the root directory of the project and your virtual environment is activated.

* **Run all tests in headed mode:**
    ```bash
    pytest --headed
    ```
Note: If you don't want to use headed mode, just remove -- headed from the command.

* **Run a specific test file:**
    ```bash
    pytest tests/test_login.py
    ```

* **Run a specific test function:**
    ```bash
    pytest tests/test_login.py::test_successful_login
    ```

## 📂 Project Structure

This project uses the **Page Object Model (POM)** design pattern. This approach separates the test logic from the page locators, making the tests more readable, reusable, and easier to maintain.

```bash
Playwright-Python-Practice/
├── tests/
│   ├── conftest.py          # Pytest fixtures and configurations
│   ├── test_login.py        # Login page tests
│   └── test_add_product.py  # Add product to cart tests
├── pages/
│   ├── init.py          # Marks the directory as a Python package
│   ├── login.py             # Page Object for the login page
│   └── add_product.py       # Page Object for the add product page
├── venv/                    # Virtual environment
└── README.md
```