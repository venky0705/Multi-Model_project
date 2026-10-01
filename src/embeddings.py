"""Shared local BGE embeddings for ingestion and retrieval."""

import os
from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings


DEFAULT_EMBEDDING_MODEL = "BAAI/bge-m3"
DEFAULT_COLLECTION = "mm-rag-bge-m3"


@lru_cache(maxsize=1)
def get_embeddings() -> HuggingFaceEmbeddings:
    """Load once per process; no hosted embedding API key is required."""
    return HuggingFaceEmbeddings(
        model_name=os.getenv("HF_EMBEDDING_MODEL") or DEFAULT_EMBEDDING_MODEL,
        model_kwargs={"device": os.getenv("HF_EMBEDDING_DEVICE") or "cpu"},
        encode_kwargs={"normalize_embeddings": True, "batch_size": 8},
    )


def validate_collection_vectors(info, dimension: int) -> None:
    """Reject incompatible collections before indexing or retrieval."""
    vectors = info.config.params.vectors
    if isinstance(vectors, dict) or getattr(vectors, "size", None) != dimension:
        raise ValueError(
            f"Collection must have unnamed {dimension}-dimensional vectors. "
            "Use a new collection and re-ingest with the same embedding model."
        )
    distance = getattr(vectors.distance, "value", vectors.distance)
    if str(distance).lower() != "cosine":
        raise ValueError("The embedding collection must use cosine distance.")
