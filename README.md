# Learn FastAPI ⚡

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python)](https://www.python.org/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Schemas](https://img.shields.io/badge/Validation-Pydantic%20v2-e92063.svg?logo=pydantic)](https://docs.pydantic.dev/)
[![Server Engine](https://img.shields.io/badge/ASGI-Starlette%20%7C%20Uvicorn-purple.svg)](https://www.uvicorn.org/)
[![Production Ready](https://img.shields.io/badge/Status-Enterprise%20Grade-brightgreen.svg)](https://github.com/TheLearningHubOrg/learn-fastapi)

**An exhaustive, production-grade masterclass from absolute zero to staff-level FastAPI and asynchronous Python microservices architecture.**  
Master high-throughput ASGI concurrency, Pydantic v2 validation internals, SQLAlchemy 2.0 async sessions, hierarchical dependency injection, OAuth2/JWT security, and containerized Kubernetes deployments.

[Getting Started](#1-stage-1-async-python--fastapi-foundations) • [Pydantic v2](#2-stage-2-request-validation--pydantic-v2-mastery) • [Dependency Injection](#3-stage-3-hierarchical-dependency-injection) • [Async Database ORM](#4-stage-4-async-database-engines--sqlalchemy-20) • [Security & Auth](#5-stage-5-enterprise-security--authentication) • [Production & Docker](#6-stage-6-background-tasks-websockets--production) • [Staff Handbook](#7-stage-7-staff-backend-architect-interview-handbook--cheatsheet)

<br/>

<a href="https://www.buymeacoffee.com/manthanank">
  <img src="https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow?style=for-the-badge&logo=buy-me-a-coffee" alt="Buy Me A Coffee" width="180">
</a>

</div>

---

## 🗺️ 7-Stage Pedagogical Roadmap

```mermaid
flowchart LR
    S1["Stage 1: Async Python & ASGI"] --> S2["Stage 2: Pydantic v2 Validation"]
    S2 --> S3["Stage 3: Hierarchical DI"]
    S3 --> S4["Stage 4: SQLAlchemy 2.0 Async"]
    S4 --> S5["Stage 5: OAuth2 & JWT Security"]
    S5 --> S6["Stage 6: Lifespans, Celery & Docker"]
    S6 --> S7["Stage 7: Staff Architect Handbook & Cheatsheet"]
```

| Stage | Domain Focus | Core Concepts & Production Outcomes |
| :--- | :--- | :--- |
| **Stage 1** | **Async Python & ASGI Foundations** | WSGI vs ASGI, uvloop, event loop execution model, Starlette primitives, route decorators, automatic OpenAPI/Swagger generation. |
| **Stage 2** | **Pydantic v2 Validation Mastery** | Core rust-backed Pydantic validation, `Annotated` parameters, custom field validators, schema serialization, model inheritance. |
| **Stage 3** | **Hierarchical Dependency Injection** | Inversion of control with `Depends()`, sub-dependencies, `yield` teardown contexts, caching mechanics, test mocking. |
| **Stage 4** | **Async Database Engines & SQLAlchemy 2.0** | `create_async_engine`, connection pooling, `AsyncSession` transactions, relationship loaders (`selectinload`), Alembic migrations. |
| **Stage 5** | **Enterprise Security & Authentication** | OAuth2 Password Bearer flow, Argon2 password hashing, RS256/HS256 JWT tokens, role-based access control (RBAC), CORS middleware. |
| **Stage 6** | **Background Tasks, WebSockets & Deployment** | Lifespan context managers, background task threads, distributed task queues (Celery/Redis), WebSockets, multi-stage Docker builds. |
| **Stage 7** | **Staff Architect Interview Handbook** | 40+ staff-level scenario Q&As, GIL bottlenecks vs event loop blocking, connection exhaustion mitigation, enterprise cheatsheet. |

---

## 📋 Table of Contents
- [1. Stage 1: Async Python & FastAPI Foundations](#1-stage-1-async-python--fastapi-foundations)
  - [1.1 WSGI vs. ASGI Architecture & The Event Loop](#11-wsgi-vs-asgi-architecture--the-event-loop)
  - [1.2 Application Bootstrapping & Route Routing](#12-application-bootstrapping--route-routing)
  - [1.3 Query, Path, Header, and Cookie Parameters](#13-query-path-header-and-cookie-parameters)
  - [1.4 Automatic OpenAPI & Redoc Generation](#14-automatic-openapi--redoc-generation)
- [2. Stage 2: Request Validation & Pydantic v2 Mastery](#2-stage-2-request-validation--pydantic-v2-mastery)
  - [2.1 The Pydantic v2 Rust Engine (pydantic-core)](#21-the-pydantic-v2-rust-engine-pydantic-core)
  - [2.2 Defining Request & Response Schemas](#22-defining-request--response-schemas)
  - [2.3 Advanced Field Validation & Custom Types](#23-advanced-field-validation--custom-types)
  - [2.4 Serialization & Computed Fields](#24-serialization--computed-fields)
- [3. Stage 3: Hierarchical Dependency Injection](#3-stage-3-hierarchical-dependency-injection)
  - [3.1 The Dependency Injection Tree with `Depends()`](#31-the-dependency-injection-tree-with-depends)
  - [3.2 Scoped Lifecycles with `yield` & Resource Teardown](#32-scoped-lifecycles-with-yield--resource-teardown)
  - [3.3 Parameterized Class-Based Dependencies](#33-parameterized-class-based-dependencies)
  - [3.4 Overriding Dependencies in Integration Tests](#34-overriding-dependencies-in-integration-tests)
- [4. Stage 4: Async Database Engines & SQLAlchemy 2.0](#4-stage-4-async-database-engines--sqlalchemy-20)
  - [4.1 PostgreSQL Engine with `asyncpg` & Connection Pooling](#41-postgresql-engine-with-asyncpg--connection-pooling)
  - [4.2 Declarative Base & Mapped Column Typings](#42-declarative-base--mapped-column-typings)
  - [4.3 Async Repository Pattern & Transactions](#43-async-repository-pattern--transactions)
  - [4.4 Alembic Async Migrations](#44-alembic-async-migrations)
- [5. Stage 5: Enterprise Security & Authentication](#5-stage-5-enterprise-security--authentication)
  - [5.1 OAuth2 Password Flow with Bearer Tokens](#51-oauth2-password-flow-with-bearer-tokens)
  - [5.2 JWT Token Generation & Verification](#52-jwt-token-generation--verification)
  - [5.3 Role-Based Access Control (RBAC)](#53-role-based-access-control-rbac)
  - [5.4 Enterprise Security Headers & CORS](#54-enterprise-security-headers--cors)
- [6. Stage 6: Background Tasks, WebSockets & Production](#6-stage-6-background-tasks-websockets--production)
  - [6.1 Modern `lifespan` Application State Management](#61-modern-lifespan-application-state-management)
  - [6.2 Native Background Tasks vs. Distributed Celery Workers](#62-native-background-tasks-vs-distributed-celery-workers)
  - [6.3 Full-Duplex WebSockets with Connection Managers](#63-full-duplex-websockets-with-connection-managers)
  - [6.4 Multi-Stage Docker & Production Gunicorn+Uvicorn Configuration](#64-multi-stage-docker--production-gunicornuvicorn-configuration)
- [7. Stage 7: Staff Backend Architect Interview Handbook & Cheatsheet](#7-stage-7-staff-backend-architect-interview-handbook--cheatsheet)
  - [7.1 Enterprise Production Cheatsheet](#71-enterprise-production-cheatsheet)
  - [7.2 Staff & Principal Architect Interview Q&A (40 Scenarios)](#72-staff--principal-architect-interview-qa-40-scenarios)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 1. Stage 1: Async Python & FastAPI Foundations

### 1.1 WSGI vs. ASGI Architecture & The Event Loop
Traditional Python web frameworks (Django, Flask) adhere to the **WSGI** (Web Server Gateway Interface) standard: a synchronous, blocking protocol where each concurrent HTTP request binds a dedicated OS worker thread or process.

FastAPI is built on **ASGI** (Asynchronous Server Gateway Interface) powered by **Starlette**:

```mermaid
graph TD
    subgraph WSGI ["Traditional WSGI (Flask / Django)"]
        Req1["Request 1"] --> Thread1["Thread 1 (Blocked during DB I/O)"]
        Req2["Request 2"] --> Thread2["Thread 2 (Blocked during API I/O)"]
        Req3["Request 3"] --> Queue["Thread Pool Exhaustion (High Latency)"]
    end

    subgraph ASGI ["Asynchronous ASGI (FastAPI / Starlette)"]
        AReq1["Request 1"] --> Loop["Single OS Thread Event Loop"]
        AReq2["Request 2"] --> Loop
        AReq3["Request 3"] --> Loop
        Loop -->|Non-blocking await| DB["Postgres / Redis (Async I/O)"]
    end
```

> [!IMPORTANT]
> When defining route handlers:
> - Use `async def` when performing non-blocking I/O operations (`await db.execute(...)`, `await client.get(...)`).
> - Use standard `def` when performing CPU-bound or blocking operations; FastAPI automatically offloads standard `def` routes to an internal threadpool (`anyio.to_thread`) to avoid blocking the main event loop!

### 1.2 Application Bootstrapping & Route Routing
Production directory layout:

```
src/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   └── router.py
├── core/
│   ├── config.py
│   └── database.py
├── models/
├── schemas/
└── main.py
```

Clean application entry point:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize DB connection pool, Redis client
    print("[INFO] Application startup: initializing resources")
    yield
    # Shutdown: Close database pools, flush telemetry
    print("[INFO] Application shutdown: releasing resources")

app = FastAPI(
    title="Enterprise Core API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://admin.company.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/healthz", tags=["System"])
async def health_check():
    return {"status": "healthy", "service": "core-api"}
```

---

## 2. Stage 2: Request Validation & Pydantic v2 Mastery

### 2.1 The Pydantic v2 Rust Engine (pydantic-core)
FastAPI utilizes Pydantic v2, which replaced Python validation logic with `pydantic-core` written in **Rust**. This yields up to **5× to 20× faster serialization and deserialization throughput**.

### 2.2 Defining Request & Response Schemas

```python
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=100)
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        return v

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    
    # Enable automatic conversion from SQLAlchemy ORM entities
    model_config = ConfigDict(from_attributes=True)
```

---

## 3. Stage 3: Hierarchical Dependency Injection

### 3.1 The Dependency Injection Tree with `Depends()`
FastAPI provides one of the most powerful dependency injection engines in backend development. Dependencies can form trees, share singletons, or execute sub-dependencies:

```mermaid
graph TD
    Endpoint["POST /api/v1/orders"]
    Endpoint --> Auth["Depends(get_current_active_user)"]
    Endpoint --> DB["Depends(get_async_session)"]
    Auth --> Token["Depends(oauth2_scheme)"]
    Auth --> DB
```

### 3.2 Scoped Lifecycles with `yield` & Resource Teardown

```python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import async_session_factory

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Yields a database session that automatically commits or rolls back."""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

---

## 4. Stage 4: Async Database Engines & SQLAlchemy 2.0

### 4.1 PostgreSQL Engine with `asyncpg` & Connection Pooling

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://postgres:secret@localhost:5432/enterprise_db"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

class Base(DeclarativeBase):
    pass
```

### 4.2 Declarative Base & Mapped Column Typings

```python
import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
```

---

## 5. Stage 5: Enterprise Security & Authentication

### 5.1 OAuth2 Password Flow with Bearer Tokens & Argon2

```python
from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

SECRET_KEY = "SUPER_SECRET_PRODUCTION_KEY_ROTATE_REGULARLY"
ALGORITHM = "HS256"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=60)) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

---

## 6. Stage 6: Background Tasks, WebSockets & Production

### 6.1 Multi-Stage Docker Build for Production

```dockerfile
# Multi-Stage Production Dockerfile for FastAPI
FROM python:3.12-slim as builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final Runtime Image
FROM python:3.12-slim

WORKDIR /app
RUN addgroup --system appgroup && adduser --system --group appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY ./src /app/src

ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]
```

---

## 7. Stage 7: Staff Backend Architect Interview Handbook & Cheatsheet

### 7.1 Enterprise Production Cheatsheet

| Component | Recommended Tool | Command / Syntax Pattern |
| :--- | :--- | :--- |
| **ASGI Web Server** | Uvicorn / Gunicorn | `gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker` |
| **Database Driver** | asyncpg | `postgresql+asyncpg://user:pass@host/db` |
| **Migrations** | Alembic | `alembic revision --autogenerate -m "create users"` |
| **Password Hashing**| Argon2id | `CryptContext(schemes=["argon2"])` |
| **Dependency Injection** | `Depends()` | `db: AsyncSession = Depends(get_db_session)` |
| **Background Queue** | Celery + Redis | `celery -A src.tasks worker --loglevel=info` |

### 7.2 Staff & Principal Architect Interview Q&A (40 Scenarios)

#### Q1: What happens if you execute a blocking synchronous library (`time.sleep` or synchronous `requests.get`) inside an `async def` route handler?
> **Answer**: It blocks the entire operating system thread hosting the asyncio event loop. All other concurrent requests waiting on that worker process are stalled and cannot advance, resulting in massive latency spikes and connection timeouts. If synchronous operations must be used, declare the route as regular `def` (which FastAPI offloads to a thread pool) or execute via `anyio.to_thread.run_sync()`.

#### Q2: How does Pydantic v2 achieve up to 20x speedup over Pydantic v1?
> **Answer**: Pydantic v2 moved the entire validation and parsing engine (`pydantic-core`) to Rust. Instead of validating nested dictionaries through Python bytecode and recursive object instantiations, JSON payloads are directly validated in compiled native code with minimal Python-C bridge overhead.

#### Q3: Why is `selectinload` preferred over `joinedload` in asynchronous SQLAlchemy 2.0?
> **Answer**: In `joinedload`, a single SQL statement joins tables, which can cause severe Cartesian product data duplication when fetching one-to-many collections. `selectinload` executes a second query using an `IN` clause with primary keys, ensuring clean memory allocation and preventing database lock contention in high-throughput async workloads.

#### Q4: How do you gracefully manage database connection pooling when scaling FastAPI across multiple Uvicorn worker processes?
> **Answer**: Connection pools are created per-process. If each Uvicorn worker allocates a pool of 20 connections and you run 8 workers per container across 5 Kubernetes pods, the database faces $20 \times 8 \times 5 = 800$ connections. To prevent PostgreSQL connection saturation, configure lower container pool sizes (e.g. 5-10) and deploy an intermediate connection pooler like **PgBouncer** running in transaction-pooling mode.

*(36 additional Staff-level architecture scenarios detailed inside repository documentation...)*

---

## 🤝 Contributing
Contributions are welcomed! Fork the repository, create a feature branch, and submit a PR conforming to the unified curriculum architecture.

## 📄 License
Released under the [MIT License](LICENSE).
