-- MySQL schema for Hospital Management System
CREATE DATABASE IF NOT EXISTS hospital_management
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hospital_management;

CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(30) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    address VARCHAR(255) DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    specialization VARCHAR(120) NOT NULL,
    phone VARCHAR(30) DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS appointments (
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
);
