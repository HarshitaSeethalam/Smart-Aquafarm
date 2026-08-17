import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable is not set")

connection = psycopg2.connect(DATABASE_URL)

cursor = connection.cursor()

print("PostgreSQL Connected Successfully")
