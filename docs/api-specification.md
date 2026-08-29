# API Specification

## Overview

The platform exposes REST APIs and GraphQL schema support for secure SaaS operations across tenant, branch, customer, appointment, queue, billing, and analytics domains.

## REST resource groups

### Auth
- POST /api/v1/auth/signup
- POST /api/v1/auth/login
- POST /api/v1/auth/sso/google
- POST /api/v1/auth/sso/microsoft
- POST /api/v1/auth/password-reset
- POST /api/v1/auth/mfa/verify

### Tenant
- GET /api/v1/tenants
- POST /api/v1/tenants
- GET /api/v1/tenants/{id}
- PATCH /api/v1/tenants/{id}

### Branch
- GET /api/v1/branches
- POST /api/v1/branches
- GET /api/v1/branches/{id}

### Customer
- GET /api/v1/customers
- POST /api/v1/customers
- GET /api/v1/customers/{id}
- PATCH /api/v1/customers/{id}

### Appointment
- GET /api/v1/appointments
- POST /api/v1/appointments
- PATCH /api/v1/appointments/{id}/reschedule
- POST /api/v1/appointments/{id}/cancel

### Queue
- POST /api/v1/queues/tokens
- GET /api/v1/queues/live
- POST /api/v1/queues/{id}/call
- POST /api/v1/queues/{id}/transfer

### Analytics
- GET /api/v1/analytics/dashboard
- GET /api/v1/analytics/wait-time
- GET /api/v1/analytics/sla

### Billing
- GET /api/v1/billing/subscriptions
- POST /api/v1/billing/invoices
- GET /api/v1/billing/usage

## GraphQL concepts

- queries: tenant, branch, customer, appointment, queueStats
- mutations: createTenant, bookAppointment, updateQueueStatus, createInvoice
- subscriptions: liveQueueUpdate, notificationStream

## OpenAPI notes

The backend shall generate an OpenAPI 3.1 schema and Swagger UI from the FastAPI application.
