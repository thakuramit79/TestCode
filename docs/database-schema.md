# Database Schema

## Core entities

### Tenant
- id
- name
- slug
- status
- plan_id
- branding_json
- settings_json
- created_at
- updated_at

### TenantUser
- id
- tenant_id
- user_id
- role
- is_active
- last_login_at

### Branch
- id
- tenant_id
- name
- code
- address
- latitude
- longitude
- working_hours_json
- timezone
- status

### ServiceCategory
- id
- tenant_id
- name
- description
- status

### Service
- id
- tenant_id
- branch_id
- category_id
- name
- description
- duration_minutes
- sla_minutes
- price
- status

### Agent
- id
- tenant_id
- branch_id
- user_id
- full_name
- skills_json
- working_hours_json
- status

### Customer
- id
- tenant_id
- first_name
- last_name
- email
- phone
- kyc_status
- notes_json
- created_at

### Appointment
- id
- tenant_id
- branch_id
- customer_id
- service_id
- agent_id
- scheduled_start
- scheduled_end
- status
- channel
- notes
- created_at

### QueueToken
- id
- tenant_id
- branch_id
- service_id
- customer_id
- token_number
- queue_type
- priority_level
- status
- created_at
- called_at
- completed_at

### QueueEvent
- id
- queue_token_id
- event_type
- actor_id
- metadata_json
- created_at

### Notification
- id
- tenant_id
- recipient_type
- recipient_id
- channel
- template_key
- payload_json
- status
- sent_at

### Invoice
- id
- tenant_id
- subscription_id
- amount
- currency
- status
- issued_at
- due_at

### Subscription
- id
- tenant_id
- plan_code
- status
- billing_cycle
- trial_ends_at
- started_at
- expires_at

## Relationships

- Tenant has many branches, users, services, subscriptions, and customers
- Branch belongs to a tenant and hosts agents, appointments, and queue tokens
- Service belongs to a tenant and branch and can be assigned to multiple agents
- Customer has many appointments and queue tokens
- Appointment references branch, service, customer, and optional agent
- QueueToken tracks real-time customer flow and events
- Notification tracks all outbound communication events

## Indexing recommendations

- tenant_id + branch_id + status on queue tokens
- customer_id + tenant_id on appointments and customers
- scheduled_start on appointment table
- service_id and branch_id on resources
- created_at on audit tables
