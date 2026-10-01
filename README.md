# Multi-Model Project

For the current Hugging Face embedding, Groq generation, and Qdrant setup,
see [Provider setup](PROVIDER_SETUP.md). Configuration variable names are provided
in [.env.example](.env.example).

A Python project workspace with a directory for data-parsing notebooks. The project currently contains the initial folder structure; application code, model implementations, and dependencies have not yet been added.

## Technology and requirements

- **Python:** 3.12 (the current local environment uses CPython 3.12.13).
- **Environment and package manager:** [uv](https://docs.astral.sh/uv/).
- **Virtual environment directory:** `env`.
- **Dependencies:** managed through `requirements.txt`, which is currently empty.

## Project structure

```text
Multi-Model_project/
|-- data-parsing/
|   `-- ex.ipynb         # Empty notebook placeholder for data-parsing work
|-- env/                # Local virtual environment, created during setup
|-- .env                # Local configuration file (ignored by Git)
|-- .gitignore          # Git ignore rules
|-- requirements.txt    # Python dependencies
`-- README.md           # Project documentation
```

## Setup

Open Windows Command Prompt (cmd) in the project root directory and run the following commands.

### 1. Install uv

If uv is not installed, follow the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/). Then verify it is available:

```bat
uv --version
```

### 2. List Python versions

List available Python versions, including installed interpreters and versions available to download:

```bat
uv python list
```

To show only installed versions:

```bat
uv python list --only-installed
```

This project uses **Python 3.12**. You can install it explicitly with:

```bat
uv python install 3.12
```

### 3. Create the virtual environment

The general command is `uv venv env --python <python-version>`. For this project, use:

```bat
uv venv env --python 3.12
```

This creates an isolated environment named `env` using Python 3.12. By default, uv downloads a suitable interpreter if one is unavailable. See the [uv environment documentation](https://docs.astral.sh/uv/pip/environments/).

If the project already has a working Python 3.12 environment in `env`, skip creation and activate it.

### 4. Activate the environment

**Windows Command Prompt:**

```bat
env\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source env/bin/activate
```

Verify the active interpreter:

```bat
python --version
python -c "import sys; print(sys.executable)"
```

The version should be `Python 3.12.x`, and the executable path should point inside `env`.

### 5. Install dependencies

With the environment activated, run:

```bat
uv pip install -r requirements.txt
```

The requirements file is currently empty, so no project packages are installed yet. Add required packages to it as the project develops, then rerun this command.

To inspect installed packages:

```bat
uv pip list
```

## Development status

`data-parsing/ex.ipynb` is currently an empty file, not a runnable notebook. Create and save a valid notebook in that location before using it. When working in an editor, select the Python interpreter from `env` and configure a notebook kernel if needed.

There is currently no application entry point, training command, or test suite in the repository. Add execution instructions here as those components are implemented.

The local `.env` file is ignored by Git. No required environment variables or automatic `.env` loading are defined yet.

## End a development session

Leave the virtual environment with:

```bat
deactivate
```
