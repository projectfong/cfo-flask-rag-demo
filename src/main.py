#!/usr/bin/env python3
# -------------------------------------------------------
# src/main.py
# -------------------------------------------------------
# Purpose Summary:
#   - Public-safe Flask demo for cfo-flask-rag.
#   - Exposes /api/healthz and /api/query (returns canned retrieval results).
# Audit:
#   - All actions print ISO 8601 UTC timestamps.
#   - Fails safe with 4xx/5xx and never exposes internal details.
# -------------------------------------------------------

from flask import Flask, request, jsonify
from datetime import datetime, timezone

def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()

app = Flask(__name__)

@app.get("/api/healthz")
def healthz():
    print(f"[{_ts()}] HEALTHZ ok")
    return jsonify({"status": "ok"})

@app.post("/api/query")
def query():
    try:
        data = request.get_json(silent=True) or {}
        q = (data.get("query") or "").strip()
        print(f"[{_ts()}] QUERY recv_len={len(q)}")
        if not q:
            return jsonify({"detail": "query required"}), 400

        docs = [
            {"id": "doc-001", "title": "Demo Policy Overview", "snippet": "This is a demo snippet about policies...", "score": 0.91},
            {"id": "doc-002", "title": "RAG Concepts", "snippet": "Retrieval-augmented generation explained...", "score": 0.84},
            {"id": "doc-003", "title": "System Architecture", "snippet": "How router, vessel, and embed connect...", "score": 0.79},
        ]
        return jsonify({"query": q, "results": docs, "meta": {"source": "cfo-flask-rag-demo", "ts": _ts()}})
    except Exception as e:
        print(f"[{_ts()}] ERROR {e}")
        return jsonify({"detail": "internal error"}), 500

# Gunicorn entrypoint example:
#   gunicorn -w 2 -t 120 -b 0.0.0.0:8002 "src.main:app"
