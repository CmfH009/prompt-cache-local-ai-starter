#!/usr/bin/env python3
"""Minimal stdlib-only demo showing why prompt caches silently miss — and how canonicalization fixes it.

Full exporters (Anthropic/OpenAI/Gemini), SQLite WAL response cache, and local Ollama
oracles are included in the $15 Gumroad Pro Kit (Prompt Cache & Local AI Kit v1.0).
"""
import hashlib
import json


def normalize_text(text: str) -> str:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def canonical_hash(system_text: str, tools: list) -> str:
    payload = {
        "system": normalize_text(system_text),
        "tools": sorted(tools, key=lambda t: t["name"]),
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def naive_hash(system_text: str, tools: list) -> str:
    payload = {"system": system_text, "tools": tools}
    encoded = json.dumps(payload, sort_keys=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    tool_a = {"name": "search_docs", "params": {"limit": 10, "query": "str"}}
    tool_b = {"name": "run_sql", "params": {"sql": "str", "timeout": 5}}

    # Variant 1: Linux LF, tool_a first
    n1 = naive_hash("You are a reviewer.\n", [tool_a, tool_b])
    c1 = canonical_hash("You are a reviewer.\n", [tool_a, tool_b])

    # Variant 2: Windows CRLF + trailing space, tool_b first, reversed dict keys
    tool_a_reordered = {"name": "search_docs", "params": {"query": "str", "limit": 10}}
    n2 = naive_hash("You are a reviewer.\r\n  ", [tool_b, tool_a_reordered])
    c2 = canonical_hash("You are a reviewer.\r\n  ", [tool_b, tool_a_reordered])

    print("Naive SHA-256 match?    ", n1 == n2, f"({n1[:12]} vs {n2[:12]}) -> CACHE MISS!")
    print("Canonical SHA-256 match?", c1 == c2, f"({c1[:12]} == {c2[:12]}) -> 100% CACHE HIT!")
    print("\nGet the full Anthropic/OpenAI/Gemini exporters + SQLite WAL cache + Ollama CLI:")
    print("-> $15 Gumroad Pro Kit: Prompt Cache & Local AI Kit v1.0")


if __name__ == "__main__":
    main()
