# FastAPI Backend Tests

## How to Run

1. Make sure you have all dependencies installed:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Run tests from the project root:
   ```bash
   pytest
   ```

## Test Structure
- Tests use the Arrange-Act-Assert (AAA) pattern for clarity.
- Located in `test_app.py`.
- Uses FastAPI's `TestClient` and `pytest`.
