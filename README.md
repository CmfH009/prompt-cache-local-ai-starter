# $0-Cloud Local Pre-Commit AI Code Reviewer + Prompt Cache Cost-Saver (Free Companion)

Catch bugs before `git commit` for **$0 in cloud tokens**, and stop paying twice for every repeated LLM system prompt.

Why do cloud LLM prompt caches silently miss? Two invisible culprits:
1. **Dictionary key ordering** (`{"a": 1, "b": 2}` vs `{"b": 2, "a": 1}`)
2. **Line endings & trailing whitespace** (`\r\n` on Windows vs `\n` on Linux/macOS)

A single byte difference invalidates the entire prefix hash — forcing you to pay full uncached input token rates again.

## Try the Free Demo (Stdlib Only)
```bash
python cache_miss_demo.py
```

## Read the Thin-Laptop Tuning Guide
See [THIN_LAPTOP_TUNING.md](THIN_LAPTOP_TUNING.md) for practical 16 GB ultrabook settings (`OLLAMA_MAX_LOADED_MODELS=1`, `num_ctx=4096`, `num_thread=4`).

## 15-Second Terminal GIF Demo Recipe (Full Kit)
```bash
# 1. Local $0-cloud pre-commit diff review
git diff | python local-ollama-oracles/oracle_cli.py critic --review-diff

# 2. Live $ Saved counter on every cached call
python prompt-cache-toolkit/examples/savings_demo.py
# -> [prompt-cache] HIT | Saved $0.0135 this call ($0.01 session total)
```

---

## Want the Full Production Kit? ($15 Gumroad Pro Kit)
Upgrade to **$0-Cloud Local Pre-Commit AI Code Reviewer + Prompt Cache Cost-Saver (v1.0.1)** on Gumroad ($15) to get:
- **`git_pre_commit_critic.py`**: Drop-in local Git pre-commit diff reviewer (`--warn-only` / `--strict`) powered by local Ollama at **$0 cloud token cost**.
- **`savings_tracker.py` (`CacheSavingsMiddleware`)**: Live `$ Saved` stdout counter + SQLite WAL ledger across Anthropic, OpenAI, and Gemini (`[prompt-cache] HIT | Saved $0.0135 this call ($1.42 session total)`).
- **`prompt-cache-toolkit`**: Full Anthropic (`cache_control`), OpenAI, and Gemini (`CachedContent`) exporters + `CAGEngine` + `SQLiteResponseCache` (WAL mode + TTL).
- **`local-ollama-oracles`**: `oracle_cli.py` (`critic`, `coder`, `thinker`) with `--json`, `--num-ctx`, `--num-thread`, and automatic `/api/tags` model fallback.
- Reproducible benchmark suite + installers (`install.ps1` / `install.sh`).
