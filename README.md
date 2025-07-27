# Microservices Communication Testing
Two simple FastAPI microservices designed for exploring and testing different communication patterns between services.

## Services
User Service - Manages user data with basic CRUD operations. Runs on port 8000.
Notification Service - Handles notifications with basic CRUD operations. Runs on port 8000.

## Purpose
These services provide a minimal foundation for experimenting with microservice communication patterns such as:

- HTTP request-response
- RPC calls
- Message queues
- Event-driven communication
- Circuit breakers and retry mechanisms

Both services use in-memory storage and have no external dependencies, making them ideal for quick experimentation and testing different integration approaches.