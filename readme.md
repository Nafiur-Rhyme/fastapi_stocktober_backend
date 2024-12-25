# Stocktober

A FastAPI backend for a stock market simulation web application, providing APIs for stock trading, portfolio management, and transaction history.

## Features
- RESTful APIs for managing stocks and user portfolios.
- Integration-ready for frontend clients (e.g., Next.js).
- Easy-to-extend modular structure.
- Built-in OpenAPI documentation available at `/docs`.

---

## Tech Stack
- **Framework**: FastAPI
- **Database**: SQLite (or your configured database)
- **Language**: Python 3.9+
- **ORM**: SQLAlchemy
- **Testing**: Pytest

---

## Project Structure
```
app/
├── api/           # API routes
├── core/          # Configuration and utilities
├── db/            # Database models and session setup
├── schemas/       # Pydantic schemas
├── services/      # Business logic
├── tests/         # Unit tests
└── main.py        # Application entry point
```

---

## Installation

### Prerequisites
- Python 3.9 or higher
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone `https://github.com/Nafiur-Rhyme/fastapi_stocktober_backend`
   cd fastapi_stocktober_backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## API Documentation
Access the interactive API documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Environment Variables
Configure the application using a `.env` file in the root directory:
```
DATABASE_URL=sqlite:///./test.db
DEBUG=True
```

---

## Testing
Run tests using `pytest`:
```bash
pytest
```

---

## Contributing
Feel free to contribute by submitting issues or pull requests.

---

## Contact
For questions or feedback, please reach out at `nafiur.rhyme@gmail.com` or `tofa.hossainmoon@gmail.com`.