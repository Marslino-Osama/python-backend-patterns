# Python Backend Patterns & System Design

A practical learning repository for production-ready Python backend patterns, distributed systems concepts, and scalability techniques through hands-on implementation.

## Mission

Learn Python backend development and system design by building real-world projects with reusable, production-grade modules. No tutorial-only examples, no hello-world-only demos; the goal is practical, composable backend systems.

## Repository Structure

```text
python-backend-patterns/
├── README.md
├── LEARNING_CONTEXT.md
├── AI_RULES.md
├── FRAMEWORK_GUIDE.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── pyproject.toml
├── Makefile
├── .env.example
├── docker-compose.yml
│
├── modules/
│   ├── auth_jwt/          # JWT authentication system
│   ├── rbac/              # Role-based access control
│   ├── smtp_otp/          # Email verification and OTP
│   ├── file_upload/       # Local/S3-compatible file handling
│   ├── rate_limiter/      # Redis-based rate limiting
│   └── audit_log/         # Activity tracking
│
├── projects/
│   ├── phase-1-foundation/
│   ├── phase-2-scaling/
│   └── phase-3-reliability/
│
└── examples/
    ├── production-api-fastapi/
    └── production-api-flask/
```

## Learning Path

### Phase 1: Foundation Modules, Weeks 1-4

| # | Project | Concepts Learned | Status |
|---|---------|------------------|--------|
| 01 | `auth-jwt-basics` | Registration, login, JWT access tokens | Not Started |
| 02 | `auth-jwt-hardened` | Refresh tokens, token rotation, blacklisting, rate limiting | Not Started |
| 03 | `rbac-permissions` | Roles, permissions, hierarchical access | Not Started |
| 04 | `smtp-otp-verification` | Email sending, OTP generation/validation | Not Started |
| 05 | `file-upload-storage` | Multipart uploads, local/S3 storage, validation | Not Started |
| 06 | `api-integration-ai` | External APIs, OpenAI-compatible clients, streaming | Not Started |

### Phase 2: Scaling Patterns, Weeks 5-10

| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 07 | `caching-strategies` | Redis, cache-aside, invalidation | Not Started |
| 08 | `database-replication` | Read replicas, routing reads/writes, pooling | Not Started |
| 09 | `indexing-performance` | Query optimization, explain plans | Not Started |
| 10 | `async-writes-queue` | Celery/RQ/Arq, background jobs | Not Started |
| 11 | `batch-processing` | Bulk operations, transaction batching | Not Started |
| 12 | `database-sharding` | Tenant isolation, horizontal partitioning | Not Started |
| 13 | `websockets-realtime` | WebSockets, connection management, pub/sub | Not Started |
| 14 | `sse-notifications` | Server-Sent Events, event streaming | Not Started |
| 15 | `long-polling` | Long polling vs WebSockets/SSE | Not Started |
| 15b | `websockets-realtime-flask` | Same pattern in Flask | Not Started |

### Phase 3: Reliability & Advanced Patterns, Weeks 11-16

| # | Project | Concepts | Status |
|---|---------|----------|--------|
| 16 | `retry-patterns` | Exponential backoff, jitter, retry policies | Not Started |
| 17 | `circuit-breaker` | Failure detection, fallbacks, recovery | Not Started |
| 18 | `idempotency` | Idempotent endpoints, duplicate detection | Not Started |
| 19 | `self-healing` | Health checks, graceful degradation | Not Started |
| 20 | `message-queues` | RabbitMQ/NATS/Kafka, dead letter queues | Not Started |
| 21 | `worker-pools` | Async workers, process pools, resource control | Not Started |
| 22 | `workflow-engine` | Temporal, saga pattern, long-running workflows | Not Started |
| 23 | `cqrs-pattern` | Command/query separation, event sourcing basics | Not Started |
| 24 | `microservices-basic` | Service boundaries and inter-service communication | Not Started |
| 25 | `production-api-fastapi` | Capstone with FastAPI | Not Started |
| 25b | `production-api-flask` | Capstone with Flask | Not Started |

## Quick Start

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- PostgreSQL 15+
- Redis 7+
- Git

### Local Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
cp .env.example .env
make test
```

### Run the FastAPI reference app

```bash
cd examples/production-api-fastapi
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run with Docker

```bash
docker compose up --build
```

## Technology Stack

### Core

- Language: Python 3.12+
- Primary API framework: FastAPI
- Alternative implementation: Flask
- Data validation: Pydantic v2
- ORM: SQLAlchemy 2.x
- Migrations: Alembic
- Database: PostgreSQL 15+
- Cache: Redis 7+
- Testing: Pytest

### Infrastructure

- Docker and Docker Compose
- RabbitMQ, NATS, or Kafka for queues depending on project phase
- S3-compatible object storage for file-upload modules
- OpenTelemetry-ready logging/observability patterns

## Project Structure Convention

Each project follows this layout:

```text
project-name/
├── README.md
├── LEARNINGS.md
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── pyproject.toml
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   └── middleware/
│
├── migrations/
└── tests/
```

## Learning Approach

1. Read the project README.
2. Build the smallest working vertical slice.
3. Test it locally.
4. Break it intentionally.
5. Refactor into modules.
6. Document what you learned.

## License

MIT License.
