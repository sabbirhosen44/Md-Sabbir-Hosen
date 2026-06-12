# Travel Deal Management API

## Overview

Travel Deal Management API is a RESTful backend application built with Flask that allows users to create and retrieve travel deals.

The application follows a modular architecture with separate layers for routes, services, validation, and database operations.

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

[Travel Deal Management API.postman_collection.json](https://github.com/sabbirhosen44/Travel-Deal-Management-System/blob/main/postman/Travel%20Deal%20Management%20API.postman_collection.json)

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

---

## Project Structure

```text
travel-deal-api/
│
├── app.py
├── routes/
├── services/
├── utils/
├── database/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
