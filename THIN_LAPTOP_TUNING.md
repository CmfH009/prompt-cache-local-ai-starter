# Thin-Laptop Local AI Tuning (16 GB RAM, Integrated GPU)

Practical settings for running small local models on an ultrabook-class machine
(tested on a 28 W mobile Core i7 with integrated graphics).

## 1. Pick Models That Fit
| Role | Model | Approx RAM |
|---|---|---|
| Code review / reasoning | `gemma3:4b` or `gemma4:e2b` | ~3.5–4.6 GB |
| Code generation | `qwen2.5-coder:3b` | ~2.0–2.5 GB |
| Embeddings | `nomic-embed-text` | ~0.3 GB |

Keep total loaded models under half your RAM. Set `OLLAMA_MAX_LOADED_MODELS=1`.

## 2. Cap Threads to Avoid Thermal Throttling
Thin laptops throttle when all cores spin. Use roughly half the physical cores:
```text
OLLAMA_NUM_PARALLEL=1
# per-request option: {"options": {"num_thread": 4}}
```

## 3. Shrink Context
`num_ctx` 4096 is plenty for diff review; 32k contexts balloon the KV cache.

## 4. Cache Aggressively
Pair local models with a SQLite WAL response cache and deterministic prompt canonicalization so repeated prompts never re-run inference.

---
*Looking for the turnkey `SQLiteResponseCache`, Anthropic/OpenAI/Gemini exporters, and Git pre-commit critic? Grab the **$15 Gumroad Pro Kit (Prompt Cache & Local AI Kit v1.0)**.*
