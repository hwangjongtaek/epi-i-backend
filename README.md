<div align="center">
  <img src="static/imgs/epi-i-logo-500.jpg" alt="Epi-i Logo"/>
</div>

# Epi-i Backend

Helps guardians of children with epilepsy systematically and objectively record seizure symptoms and life patterns. The goal is to contribute to the child's treatment plan by providing accumulated data as accurate information during medical consultations.

This repository contains the backend API for the Epi-i project, built with FastAPI and Supabase.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database & Auth**: [Supabase](https://supabase.io/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Linting/Formatting**: [Ruff](https://github.com/astral-sh/ruff)
- **Testing**: [Pytest](https://pytest.org/)

## Project Structure

```
/
├── app/                  # Main application module
│   ├── main.py           # FastAPI app entry point
│   ├── core/             # Core components (config, etc.)
│   ├── db/               # Database connection (Supabase)
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   └── api/              # API endpoints (routers)
├── tests/                # Test suite
├── .env.template         # Environment variable template
├── .gitignore
├── pyproject.toml        # Project configuration and dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) installed

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/epi-i-backend.git
    cd epi-i-backend
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```
    Activate it:
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    uv pip install -e .[test]
    ```

4.  **Set up environment variables:**
    -   Copy the template:
        ```bash
        cp .env.template .env
        ```
    -   Fill in your Supabase URL and Key in the `.env` file.

### Running the Application

To start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Running Tests & Linting

-   **To run tests:**
    ```bash
    pytest
    ```

-   **To check for linting errors:**
    ```bash
    ruff check .
    ```

-   **To format the code:**
    ```bash
    ruff format .
    ```
