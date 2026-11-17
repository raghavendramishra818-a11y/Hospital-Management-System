import tempfile
import unittest
from pathlib import Path
from app.database import Database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db = Database(Path(self.temp_dir.name) / "test.db")

    def tearDown(self):
        self.db.close()
        self.temp_dir.cleanup()

    def test_demo_seed_creates_patients_and_doctors(self):
        patients = self.db.fetch_one("SELECT COUNT(*) AS total FROM patients")["total"]
        doctors = self.db.fetch_one("SELECT COUNT(*) AS total FROM doctors")["total"]
        self.assertGreaterEqual(patients, 1)
        self.assertGreaterEqual(doctors, 1)

    def test_can_insert_patient(self):
        self.db.execute(
            "INSERT INTO patients (name, age, gender, phone, address) VALUES (?, ?, ?, ?, ?)",
            ("Test Patient", 20, "Other", "9999999999", "Test City"),
        ).close()
        row = self.db.fetch_one("SELECT * FROM patients WHERE name=?", ("Test Patient",))
        self.assertIsNotNone(row)
        self.assertEqual(row["age"], 20)


if __name__ == "__main__":
    unittest.main()
