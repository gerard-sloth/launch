# Launch

An attempt to connect to the company's MongoDB database using Python and PyMongo.

## Setup

1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install dependencies: `uv sync`
3. Create `.env` with MongoDB credentials:
   ```
   MONGO_USER=your_username
   MONGO_PASSWORD=your_password
   MONGO_HOST=your_cluster.mongodb.net
   ```
4. Run: `uv run python main.py`

## Features

- Lists databases and collections
- Shows sample documents
