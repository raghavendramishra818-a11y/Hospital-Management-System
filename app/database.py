"""Database layer: SQLite demo mode by default, optional MySQL mode."""
from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent


def load_env_file(path: Path = ROOT / ".env") -> None:
    """Load simple KEY=VALUE settings without requiring python-dotenv."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


class Database:
    def __init__(self, sqlite_path: str | Path | None = None):
        load_env_file()
        self.mode = os.getenv("DB_MODE", "sqlite").lower()
        self.sqlite_path = Path(sqlite_path) if sqlite_path else ROOT / "data" / "hospital_demo.db"
        self.sqlite_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = None
        self._connect()
        self._create_tables()
        self._seed_demo_data()

    def _connect(self):
        if self.mode == "mysql":
            try:
                import mysql.connector
            except ImportError as exc:
                raise RuntimeError(
                    "MySQL mode needs mysql-connector-python. Run: "
                    "python -m pip install -r requirements.txt"
                ) from exc

            config = {
                "host": os.getenv("DB_HOST", "localhost"),
                "port": int(os.getenv("DB_PORT", "3306")),
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASSWORD", ""),
            }
            database_name = os.getenv("DB_NAME", "hospital_management")
            # Create the database if it does not exist, then connect to it.
            server = mysql.connector.connect(**config)
            cur = server.cursor()
            cur.execute(
                f"CREATE DATABASE IF NOT EXISTS `{database_name}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
            cur.close()
            server.close()
            self.connection = mysql.connector.connect(
                **config, database=database_name
            )
        else:
            self.mode = "sqlite"
            self.connection = sqlite3.connect(self.sqlite_path)
            self.connection.row_factory = sqlite3.Row
            self.connection.execute("PRAGMA foreign_keys = ON")

    def execute(self, sql: str, params: tuple[Any, ...] = ()):
        if self.mode == "mysql":
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql.replace("?", "%s"), params)
        else:
            cursor = self.connection.cursor()
            cursor.execute(sql, params)
        self.connection.commit()
        return cursor

    def fetch_all(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict]:
        cursor = self.execute(sql, params)
        rows = cursor.fetchall()
        cursor.close()
        return [dict(row) for row in rows]

    def fetch_one(self, sql: str, params: tuple[Any, ...] = ()) -> dict | None:
        rows = self.fetch_all(sql, params)
        return rows[0] if rows else None

    def _create_tables(self):
        if self.mode == "mysql":
            statements = [
                """CREATE TABLE IF NOT EXISTS patients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(120) NOT NULL,
                    age INT NOT NULL,
                    gender VARCHAR(30) NOT NULL,
                    phone VARCHAR(30) NOT NULL,
                    address VARCHAR(255) DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB""",
                """CREATE TABLE IF NOT EXISTS doctors (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(120) NOT NULL,
                    specialization VARCHAR(120) NOT NULL,
                    phone VARCHAR(30) DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB""",
                """CREATE TABLE IF NOT EXISTS appointments (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    patient_id INT NOT NULL,
                    doctor_id INT NOT NULL,
                    appointment_date VARCHAR(30) NOT NULL,
                    reason VARCHAR(255) DEFAULT '',
                    status VARCHAR(30) NOT NULL DEFAULT 'Scheduled',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CONSTRAINT fk_appointment_patient FOREIGN KEY (patient_id)
                        REFERENCES patients(id) ON DELETE CASCADE,
                    CONSTRAINT fk_appointment_doctor FOREIGN KEY (doctor_id)
                        REFERENCES doctors(id) ON DELETE CASCADE
                ) ENGINE=InnoDB""",
            ]
        else:
            statements = [
                """CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT DEFAULT '',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )""",
                """CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT NOT NULL,
                    phone TEXT DEFAULT '',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )""",
                """CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    doctor_id INTEGER NOT NULL,
                    appointment_date TEXT NOT NULL,
                    reason TEXT DEFAULT '',
                    status TEXT NOT NULL DEFAULT 'Scheduled',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(patient_id) REFERENCES patients(id) ON DELETE CASCADE,
                    FOREIGN KEY(doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
                )""",
            ]
        for statement in statements:
            cursor = self.execute(statement)
            cursor.close()

    def _seed_demo_data(self):
        """Add clearly fictional sample records only when tables are empty."""
        if self.fetch_one("SELECT COUNT(*) AS total FROM patients")["total"] == 0:
            self.execute(
                "INSERT INTO patients (name, age, gender, phone, address) VALUES (?, ?, ?, ?, ?)",
                ("Aarav Sharma", 28, "Male", "9000000001", "Pune"),
            ).close()
            self.execute(
                "INSERT INTO patients (name, age, gender, phone, address) VALUES (?, ?, ?, ?, ?)",
                ("Mira Desai", 35, "Female", "9000000002", "Pune"),
            ).close()
        if self.fetch_one("SELECT COUNT(*) AS total FROM doctors")["total"] == 0:
            self.execute(
                "INSERT INTO doctors (name, specialization, phone) VALUES (?, ?, ?)",
                ("Dr. Ananya Rao", "Cardiology", "9000000011"),
            ).close()
            self.execute(
                "INSERT INTO doctors (name, specialization, phone) VALUES (?, ?, ?)",
                ("Dr. Kabir Mehta", "General Medicine", "9000000012"),
            ).close()

    def close(self):
        if self.connection:
            self.connection.close()
