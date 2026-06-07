# auth_jwt

JWT authentication utilities: password hashing, token creation, token verification, refresh flows.

## Design Goal

Keep the reusable business logic independent from FastAPI or Flask. Add small framework adapters only when necessary.
