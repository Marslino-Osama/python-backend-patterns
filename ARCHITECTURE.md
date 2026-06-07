# Architecture Guide

## Layered Backend Architecture

```text
HTTP/API Layer -> Service Layer -> Repository Layer -> Database/External Services
```

## API Layer

Responsibilities:

- request parsing
- authentication/authorization hooks
- response formatting
- HTTP status codes

Should not contain business rules.

## Service Layer

Responsibilities:

- business logic
- orchestration
- transaction decisions
- domain-level validation

## Repository Layer

Responsibilities:

- SQLAlchemy queries
- persistence abstraction
- mapping database errors to application errors

## Modules

Modules in `modules/` should expose reusable APIs and keep framework-specific adapters separate when possible.

## Error Handling

Use explicit application exceptions and map them to HTTP responses at the API boundary.

## Configuration

Use environment variables parsed through a settings object. Do not hardcode secrets.
