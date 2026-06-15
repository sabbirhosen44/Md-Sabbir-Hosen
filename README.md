# Travel Deal Management API

## Overview

Travel Deal Management API is a RESTful backend application built with Flask that allows users to create, search, filter, sort, and retrieve travel deals.

The application follows a modular architecture with separate layers for routes, services, validation, logging, and database operations.

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
DATABASE_URL=sqlite:///your_db_name.db
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

The Postman collection for testing all API endpoints is included in the repository.

### Collection File

https://github.com/sabbirhosen44/Travel-Deal-Management-System/blob/main/postman/Travel%20Deal%20Management%20API.postman_collection.json

### Import into Postman

1. Open Postman.
2. Click **Import**.
3. Select **Upload Files**.
4. Choose the downloaded collection file.
5. Import and start testing the APIs.

---

## API Endpoints

### Create Travel Deal

**POST** `/deals`

### Get All Travel Deals

**GET** `/deals`

### Get Single Travel Deal

**GET** `/deals/<id>`

### Search Travel Deals

**GET** `/deals/search`

Example:

```http
/deals/search?destination=dubai
```

### Filter Travel Deals

**GET** `/deals/filter`

Example:

```http
/deals/filter?min_price=1000&max_price=5000
```

### Sort Travel Deals

**GET** `/deals/sort`

Example:

```http
/deals/sort?sort_by=price&order=asc
```

### Recently Viewed Deals

**GET** `/deals/recent`

---

## Validation Rules

### Travel Deal Validation

- destination cannot be empty
- price must be positive
- rating must be between 1 and 5
- travel_type must be one of:

  - Budget
  - Luxury
  - Adventure
  - Family

### Search Validation

- At least one search parameter is required
- travel_type must be valid

### Filter Validation

- min_price must be a number
- max_price must be a number
- min_price cannot be negative
- max_price cannot be smaller than min_price

### Sort Validation

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
- Search requests
- Invalid requests
- Failed requests
- Recently viewed deal activities

---

## Project Structure

```text
Travel-Deal-Management-System/
│
├── app.py
├── routes/
│   └── deal_routes.py
├── services/
│   └── deal_service.py
├── utils/
│   ├── validators.py
│   └── logger.py
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
