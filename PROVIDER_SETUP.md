# Hugging Face embeddings, Qdrant, and Groq

The ingestion and retrieval pipelines share local `BAAI/bge-m3` embeddings.
Generation uses Groq through `ChatGroq`; an OpenAI API key is no longer required.
The `.env` configuration file belongs in the project root.

| Variable | Purpose |
| --- | --- |
| `GROQ_API_KEY` | Required for generation; create it in the [Groq console](https://console.groq.com/keys). |
| `GROQ_CHAT_MODEL` | Defaults to `qwen/qwen3.8-27b`, supporting text and image input. |
| `HF_EMBEDDING_MODEL` | Defaults to `BAAI/bge-m3`. |
| `HF_EMBEDDING_DEVICE` | `cpu` by default; use `cuda` only with a compatible PyTorch/CUDA installation. |
| `HF_TOKEN` | Optional for downloading this public model. No hosted embedding API is used. |
| `QDRANT_URL` | Your Qdrant cluster URL, or `http://localhost:6333` for a running local server. |
| `QDRANT_API_KEY` | Required for authenticated Qdrant deployments, including Qdrant Cloud. |
| `QDRANT_COLLECTION_NAME` | Defaults to the new collection `mm-rag-bge-m3`. |
| `TESSERACT_PATH` | Local OCR executable used by the UI. |

## Setup in Command Prompt

Fill in the blank credentials and URL in `.env`. Existing credentials were preserved;
the collection name was changed to `mm-rag-bge-m3` for the embedding migration.
For a fresh checkout, copy `.env.example` to `.env` first.

```bat
env\Scripts\activate.bat
uv pip install -r requirements.txt
python -m streamlit run UI/app.py
```

Restart an existing app session after installing dependencies or editing configuration.
Select your PDF and ingest it into the new collection. Existing parsed artifacts can
be reused; embeddings must be regenerated. No collections were deleted by this change.

## Embedding compatibility

Yes, Qdrant stores Hugging Face embeddings. BGE-M3 produces 1024-dimensional dense
vectors; this application normalizes them and uses cosine distance. Ingestion and
queries must always use the same model. Do not mix old OpenAI embeddings with BGE
vectors, even when two models happen to have the same dimension. The code checks
collection dimensions and distance before use.

The public model downloads on first use, requires local memory and disk space, and
can be slow on CPU. This implementation uses its dense text embeddings, including
OCR and table text; it does not create native image or sparse embeddings. Inputs
beyond the model's 8192-token limit can be truncated, so keep chunks within that limit.

## Multimodal generation

Groq receives retrieved text and selected images when you ask a question. The default
vision model allows up to three images per request; the UI and generator enforce this.
If choosing a text-only model, set the image count to zero. Account access, quotas,
and model availability are managed by Groq.

References: [BGE-M3 model card](https://huggingface.co/BAAI/bge-m3),
[Qdrant collections](https://qdrant.tech/documentation/manage-data/collections/),
[Groq vision documentation](https://console.groq.com/docs/vision).

Changes were reviewed statically. Dependencies, model downloads, API calls, and
indexing were not executed as part of this migration.
