from flask import Flask, jsonify
import os
import psycopg

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "devopsdb"),
    "user": os.getenv("DB_USER", "devopsuser"),
    "password": os.getenv("DB_PASSWORD", "devopspass123")
}

@app.route("/")
def home():
    return jsonify({
        "project": "AWS DevOps Platform",
        "status": "Running",
        "message": "Application is working!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/db-health")
def db_health():
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                result = cur.fetchone()

        return jsonify({
            "database": "PostgreSQL",
            "status": "connected",
            "version": result[0]
        }), 200

    except Exception as e:
        return jsonify({
            "database": "PostgreSQL",
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)