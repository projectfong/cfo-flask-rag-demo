# CFO Flask RAG Demo

Author: projectfong  
Copyright (c) 2025 Fong  
All Rights Reserved

---

## Summary

This repository contains a **public-safe Flask demonstration** that simulates a simple Retrieval-Augmented Generation (RAG) service.  
It exposes limited, static endpoints for controlled demonstration and internal testing purposes.  
The demo does not perform live AI inference or query any external data sources.  

---

## Purpose

The intent of this repository is to:
- Provide a reproducible Flask-based API structure for testing and auditing RAG-style query behavior.  
- Demonstrate timestamped logging, safe error handling, and minimal response exposure.  
- Serve as a controlled, non-production sample for governance and evidence validation environments.  
- Reinforce isolation and safe-by-default behavior for internal research.

Use is strictly limited to demonstration and research under All Rights Reserved terms.

---

## Core Components

| Component | Description | Notes |
|------------|--------------|--------|
| **Flask App (`src/main.py`)** | Exposes `/api/healthz` and `/api/query` endpoints. | Returns static example data. |
| **Dockerfile** | Containerizes the demo for reproducible local runs. | Runs on port `8002`. |
| **requirements.txt** | Python dependencies. | Minimal Flask-only footprint. |
| **LICENSE.md** | License and restrictions. | All Rights Reserved:contentReference[oaicite:5]{index=5} |
| **DISCLAIMER.md** | Warranty and liability disclaimer. | For non-production use:contentReference[oaicite:6]{index=6} |
| **NOTICE.md** | Attribution and ownership statement. | Required metadata:contentReference[oaicite:7]{index=7} |
| **SECURITY.md** | Defines isolation, hardening, and responsible use. | Internal posture only:contentReference[oaicite:8]{index=8} |

---

## Databases and Storage

| Storage Element | Description | Persistence |
|-----------------|--------------|--------------|
| None | No external or local database. | N/A |
| `/evidence/` | Optional folder for local audit and verification logs. | Manual, not auto-created. |

**Validation Step:**  
Ensure `/evidence/` exists locally if you intend to capture runtime logs or build evidence.

---

## Folder and File Layout

```

cfo-flask-rag-demo/
├── DISCLAIMER.md
├── LICENSE.md
├── NOTICE.md
├── SECURITY.md
├── Dockerfile
├── requirements.txt
├── evidence/
│   ├── logs/
│   ├── hashes/
│   └── review/
└── src/
    └── main.py

```

- `/evidence/logs/` — local execution or audit logs.  
- `/evidence/hashes/` — file integrity or hash verification records.  
- `/evidence/review/` — manual review notes or verification artifacts.  

---

## Evidence Structure

```

/evidence/
├── logs/
│   └── demo_YYYY-MM-DD.log
├── hashes/
│   └── sha256sum.txt
└── review/
    └── validation_report.md

```

- Each entry in `/evidence/logs/` must include UTC ISO8601 timestamps.  
- Hash files under `/evidence/hashes/` support reproducibility verification.  
- Review folder provides space for validation results or documentation control.

---

## Installation (System Mode) 

For production or persistent environments within **private or isolated deployments**,  
this repository may include an optional `setup.sh` installer available only in internal or private Gitea mirrors.  
The installer configures the application as a `systemd`-managed service instead of running it in a container.

### Steps

1. Copy the repository to `/opt/cfo-flask-rag-demo` or another secure directory.
2. Review `flaskrag.service` (Not included) and confirm all paths match your environment.
3. Run the setup script with elevated privileges:

```bash
sudo ./setup.sh
```

The script performs the following:

* Installs Python dependencies using `pip install -r requirements.txt`.
* Copies the systemd unit file to `/etc/systemd/system/flaskrag.service`.
* Reloads the systemd daemon and enables the service.
* Starts the Flask RAG background service automatically.
* Verifies the running status with UTC timestamped output.

**Example output**

```
[SETUP] [2025-11-08T00:00:00Z] Installing Python requirements...
[SETUP] [2025-11-08T00:00:02Z] Enabling flaskrag service...
[SETUP] [2025-11-08T00:00:04Z] [OK] Flask RAG service is now running.
```

### Verification

To confirm the service is active:

```bash
sudo systemctl status flaskrag --no-pager
```

To stop or restart:

```bash
sudo systemctl stop flaskrag
sudo systemctl restart flaskrag
```

All runtime logs are stored in `/opt/cfo-flask-rag-demo/evidence/logs/`.

---

## Installation with Logs

### Build
```bash
docker build -t cfo-flask-rag-demo .
```

### Create Container

```bash
docker run --rm -p 8002:8002 cfo-flask-rag-demo
```

Expected log output:

```
[2025-11-08T18:00:00+00:00] HEALTHZ ok
[2025-11-08T18:00:05+00:00] QUERY recv_len=24
```

### Verify

Visit:
[http://localhost:8002/api/healthz](http://localhost:8002/api/healthz)
Expected response:

```json
{"status": "ok"}
```

---

## CLI and Dashboard

### API Commands

#### Health Check

```bash
curl -s http://localhost:8002/api/healthz
```

Response:

```json
{"status":"ok"}
```

#### Query Example

```bash
curl -s -X POST -H "Content-Type: application/json" \
    -d '{"query": "Explain RAG concepts"}' \
    http://localhost:8002/api/query
```

Response:

```json
{
  "query": "Explain RAG concepts",
  "results": [
    {"id": "doc-001", "title": "Demo Policy Overview", "snippet": "This is a demo snippet about policies...", "score": 0.91},
    {"id": "doc-002", "title": "RAG Concepts", "snippet": "Retrieval-augmented generation explained...", "score": 0.84},
    {"id": "doc-003", "title": "System Architecture", "snippet": "How router, vessel, and embed connect...", "score": 0.79}
  ],
  "meta": {"source": "cfo-flask-rag-demo", "ts": "2025-11-08T00:00:00Z"}
}
```

---

## UI Screenshots and Logs

No graphical UI is included in this demo.
The primary interface is via CLI or HTTP API responses.
Logs display timestamped actions for traceability.

---

## Security and Isolation Notes

* Operates as a **local-only demo**; not network-hardened.
* All actions produce UTC timestamped logs for visibility.
* No authentication, TLS, or external secrets are used.
* Should be deployed only in isolated lab or sandbox environments.
* Refer to [SECURITY.md](./SECURITY.md) for full security posture.

**Validation Result:**
Environment safe for internal or educational demonstration.

---

## License

All rights reserved under [LICENSE.md](./LICENSE.md).
No commercial redistribution, sublicensing, or modification is permitted.
See also:

* [NOTICE.md](./NOTICE.md)
* [DISCLAIMER.md](./DISCLAIMER.md)
* [SECURITY.md](./SECURITY.md)

---

## Revision Control

| Version   | Date       | Summary                                                                               | Author      |
| --------- | ---------- | ------------------------------------------------------------------------------------- | ----------- |
| **1.0.0** | 2025-11-08 | Initial publication of `README.md` for `cfo-flask-rag-demo`. | projectfong |
