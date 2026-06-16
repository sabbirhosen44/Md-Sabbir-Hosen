# Travel Deal Management API

## Overview

Travel Deal Management API is a RESTful backend application built with Flask that allows users to create, update, delete, search, filter, sort, and retrieve travel deals.

The application follows a modular architecture with separate layers for routes, services, validation, logging, statistics tracking, and database operations.

---

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Python-Dotenv

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/sabbirhosen44/Travel-Deal-Management-System.git

cd Travel-Deal-Management-System
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///travel_deals.db
```

### Run Application

```bash
python3 app.py
```

Server will start on:

```text
http://127.0.0.1:5000
```

---

## Postman Collection

Collection File:

https://github.com/sabbirhosen44/Travel-Deal-Management-System/blob/main/postman/Travel%20Deal%20Management%20API.postman_collection.json

---

## API Endpoints

| Method | Endpoint         | Description                   |
| ------ | ---------------- | ----------------------------- |
| POST   | `/deals`         | Create a travel deal          |
| GET    | `/deals`         | Get all travel deals          |
| GET    | `/deals/<id>`    | Get a single travel deal      |
| PUT    | `/deals/<id>`    | Update a travel deal          |
| DELETE | `/deals/<id>`    | Delete a travel deal          |
| GET    | `/deals/search`  | Search travel deals           |
| GET    | `/deals/filter`  | Filter travel deals by budget |
| GET    | `/deals/sort`    | Sort travel deals by price    |
| GET    | `/deals/recent`  | Recently viewed deals         |
| GET    | `/deals/popular` | Most viewed deals             |
| GET    | `/stats`         | API usage statistics          |

---

## Validation Rules

- destination cannot be empty

- price must be positive

- rating must be between 1 and 5

- travel_type must be one of:

  - Budget
  - Luxury
  - Adventure
  - Family

- min_price must be a number

- max_price must be a number

- min_price cannot be negative

- max_price cannot be smaller than min_price

- sort_by must be `price`

- order must be `asc` or `desc`

---

## Logging

Application logs are stored in:

```text
logs/app.log
```

Tracked events:

- Successful operations
- Failed operations
- Invalid requests
- Search activities
- Deal view activities

---

## Statistics Tracking

The application tracks:

- Total API requests
- Successful requests
- Failed requests
- Most searched destination
- Most viewed deal
- Deal view count

---

## Project Structure

```text
Travel-Deal-Management-System/
│
├── app.py
├── routes/
│   └── deal_routes.py
├── services/
│   ├── deal_service.py
│   └── stat_service.py
├── utils/
│   ├── validators.py
│   ├── logger.py
│   └── statistics.py
├── database/
│   ├── db.py
│   └── models.py
├── logs/
│   ├── .gitkeep
│   └── app.log
├── postman/
│   └── Travel Deal Management API.postman_collection.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
