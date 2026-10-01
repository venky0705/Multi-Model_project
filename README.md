# Multi-Model Project

This Streamlit app answers questions about PDFs with a RAG pipeline. It uses
local BGE-M3 embeddings, Qdrant vector storage, and Groq for answer generation.
See [Provider setup](PROVIDER_SETUP.md) and [.env.example](.env.example).

For Streamlit Community Cloud, configure the required credentials under
**Manage app → Settings → Secrets**. The hosted service cannot read your local
`.env` file. Provide `OWNER_PASSWORD`, `GROQ_API_KEY`, `QDRANT_URL`, and
`QDRANT_API_KEY` using TOML syntax:

```toml
OWNER_PASSWORD = "choose-a-private-password"
GROQ_API_KEY = "your-groq-api-key"
QDRANT_URL = "your-qdrant-cluster-endpoint"
QDRANT_API_KEY = "your-qdrant-api-key"
```

Add `HF_EMBEDDING_MODEL`, `HF_EMBEDDING_DEVICE`, `GROQ_CHAT_MODEL`, and
`QDRANT_COLLECTION_NAME` there too if you want to override their defaults.

## Hosted default PDF

The app starts with `data/uploads/Vemala Venkatesh CV.pdf.pdf`. That exact PDF
is included in the repository; other files under `data/` remain ignored. On the
first visitor session, the app parses the bundled PDF and indexes it in the
`mm-rag-bge-m3` Qdrant collection if it is not already indexed. This first
preparation may take a few minutes while the embedding model loads.

The bundled PDF is a personal CV. Its contents will be visible to people with
access to the GitHub repository and may be discussed by users of the deployed
app; keep the repository private if that is not intended.

When the owner selects and prepares another PDF, the app remembers that choice
for visitors after logout.

## Technology and requirements

- **Python:** 3.12 (the current local environment uses CPython 3.12.13).
- **Environment and package manager:** [uv](https://docs.astral.sh/uv/).
- **Virtual environment directory:** `env`.
- **Dependencies:** listed in `requirements.txt`.

## Project structure

```text
Multi-Model_project/
|-- data/
|   `-- uploads/
|       `-- Vemala Venkatesh CV.pdf.pdf  # Hosted default PDF
|-- env/                # Local virtual environment (ignored by Git)
|-- .env                # Local secrets (ignored by Git)
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

This installs the project dependencies, including Streamlit, Qdrant, Groq, and the local Hugging Face embedding packages.

To inspect installed packages:

```bat
uv pip list
```

## Run the app

With dependencies installed and environment variables configured, start the app:

```bat
python -m streamlit run UI/app.py
```

For local use, enter credentials in the root `.env`. For Streamlit Community
Cloud, enter them under **Manage app → Settings → Secrets**. The first hosted
visitor automatically prepares the default resume in Qdrant if needed.

## End a development session

Leave the virtual environment with:

```bat
deactivate
```
