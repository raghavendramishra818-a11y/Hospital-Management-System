# 🏥 Hospital Management System

### A Python-Based Desktop Application for Hospital Management

**A collaborative school project, reconstructed and documented for learning, demonstration and further development.**

---

## 📌 Table of Contents

1. [About the Project](#-about-the-project)
2. [Project Background](#-project-background)
3. [Project Objectives](#-project-objectives)
4. [Features](#-features)
5. [Technology Stack](#-technology-stack)
6. [Application Overview](#-application-overview)
7. [Project Architecture](#-project-architecture)
8. [Folder Structure](#-folder-structure)
9. [System Requirements](#-system-requirements)
10. [Installation and Setup](#-installation-and-setup)
11. [Database Configuration](#-database-configuration)
12. [How to Run the Application](#-how-to-run-the-application)
13. [How to Use the Application](#-how-to-use-the-application)
14. [Testing and Debugging](#-testing-and-debugging)
15. [Security and Privacy](#-security-and-privacy)
16. [Known Limitations](#-known-limitations)
17. [Future Improvements](#-future-improvements)
18. [Original School Project Team](#-original-school-project-team)
19. [Reconstruction and AI Acknowledgements](#-reconstruction-and-ai-acknowledgements)
20. [Contributing](#-contributing)
21. [License](#-license)
22. [Disclaimer](#-disclaimer)

---

## 📖 About the Project

The **Hospital Management System (HMS)** is a Python-based desktop application developed to demonstrate how basic hospital management activities can be organized using a graphical user interface and a database.

The application provides a centralized interface for managing:

- Patient information
- Doctor information
- Appointment records
- Basic hospital dashboard information

The application is designed to demonstrate fundamental software development concepts, including Python programming, graphical user interface development, database connectivity, CRUD operations, SQL queries and application organization.

This repository contains a reconstructed version of a school project originally developed collaboratively by three students.

**Important:** The original source files were unavailable during reconstruction. Therefore, this repository contains a newly prepared implementation inspired by the original project, not the recovered original source code.

## 🎓 Project Background

This project originally began as a school-level programming project developed by three students.

At that time, the team developed a Hospital Management System using Python and a MySQL database.

The original application was designed to run as a desktop program rather than a website.

The project was not uploaded to GitHub when it was originally developed because the team was not familiar with GitHub and version control at the time.

Later, the team decided to reconstruct the project and publish it on GitHub so that other students, beginners and developers could explore the implementation and learn from it.

The purpose of this repository is to preserve the project's learning journey, make the reconstructed source code accessible and provide a foundation for future improvements.

## 🎯 Project Objectives

The main objectives are:

1. Demonstrate how Python can be used to develop a desktop application.
2. Understand how a graphical interface interacts with application logic.
3. Learn how to connect Python applications with databases.
4. Demonstrate basic patient, doctor and appointment management.
5. Understand SQL queries and database relationships.
6. Practice organizing a software project into multiple files and modules.
7. Learn software testing, debugging and documentation.
8. Introduce students to Git and GitHub.
9. Encourage collaborative software development.

## 🚀 Features

The current reconstructed implementation includes the following features.

### 1. Dashboard

The dashboard provides an overview of the application and navigation to its main sections.

### 2. Patient Management

Users can:

- Add patient records.
- Search for existing patient records.
- Delete patient records.

### 3. Doctor Management

Users can:

- Add doctor records.
- Search for doctors.
- Delete doctor records.

### 4. Appointment Management

Users can:

- Create appointments.
- Search appointment records.
- Delete appointments.
- View related patient and doctor information through database queries.

### 5. Database Integration

The application supports:

- SQLite demonstration mode.
- Optional MySQL configuration.
- Database initialization.
- SQL-based data operations.

### 6. Desktop Interface

The application uses Tkinter to provide a graphical interface in a separate desktop window.

**Note:** The current feature list describes the reconstructed version. It does not claim that every feature of the original school project has been recovered.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Desktop graphical user interface |
| SQLite | Local demonstration database |
| MySQL | Optional database backend |
| MySQL Connector/Python | Python-to-MySQL connectivity |
| SQL | Database queries and operations |
| Git | Version control |
| GitHub | Source code hosting |
| Python unittest | Automated testing |

### Why Python?

Python provides a beginner-friendly programming environment and supports desktop development, database connectivity and automated testing.

### Why Tkinter?

Tkinter is a standard Python GUI toolkit that allows developers to build desktop applications.

### Why SQLite?

SQLite allows the application to run in demonstration mode without installing a separate database server.

### Why MySQL?

MySQL provides a relational database system suitable for learning database management and structured data storage.

---

## 🖥️ Application Overview

The application is intended to run in a separate desktop window.

Its main sections are:

| Section | Purpose |
|---|---|
| Dashboard | Application overview |
| Patients | Manage patient records |
| Doctors | Manage doctor records |
| Appointments | Manage appointments |

Screenshots of the actual running application should be added here after the Windows interface has been tested.

For example:

```markdown
![Hospital Management System Dashboard](docs/screenshots/dashboard.png)
```

Create a `docs/screenshots/` folder and place genuine screenshots there if you want to display them in this README.

Do not use illustrative mockups as screenshots of the actual application.

---

## 🏗️ Project Architecture

The application is organized into separate modules.

### Presentation Layer

Responsible for displaying the desktop interface and receiving user interactions.

Main file:

- `app/ui.py`

### Application Entry Point

Responsible for starting the application.

Main file:

- `main.py`

### Database Layer

Responsible for database connectivity and data operations.

Main file:

- `app/database.py`

### Database Schema

Contains the SQL structure for the MySQL database.

Main file:

- `database/schema.sql`

### Testing Layer

Contains automated tests for database functionality.

Main file:

- `tests/test_database.py`

The separation of these components makes the project easier to understand, maintain and extend.

---

## 📂 Folder Structure

```text
Hospital-Management-System/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── ui.py
│
├── database/
│   └── schema.sql
│
├── tests/
│   ├── __init__.py
│   └── test_database.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── start.bat
├── README.md
└── LICENSE
```

### Explanation of Important Files

**`main.py`**

The main entry point used to launch the desktop application.

**`app/ui.py`**

Contains the graphical user interface and application pages.

**`app/database.py`**

Contains the database connection and data management functionality.

**`database/schema.sql`**

Contains the MySQL database schema.

**`tests/test_database.py`**

Contains automated tests for database operations.

**`requirements.txt`**

Lists the Python packages required by the project.

**`.env.example`**

Provides an example configuration for database settings.

**`.gitignore`**

Specifies files and folders that should not be committed to Git.

**`start.bat`**

A Windows launcher that prepares the Python environment and starts the application.

**`README.md`**

Contains the project's documentation and instructions.

---

## 💻 System Requirements

Before running the application, make sure your system has:

- Windows 10 or Windows 11.
- Python 3.10 or newer.
- A working Python installation with Tkinter support.
- Internet access for the initial dependency installation.
- GitHub access if you want to download the project.

For the default SQLite demonstration mode, a separate MySQL Server installation is not required.

For MySQL mode, a running MySQL Server is required.

---

## ⚙️ Installation and Setup

There are two ways to prepare the application.

### Method 1: Download the Project

1. Open this GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open the extracted project folder.

### Method 2: Clone the Repository Using Git

Open a terminal and execute:

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with the actual URL of this repository.

Move into the project folder:

```bash
cd Hospital-Management-System
```

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Install Python and enable the option:

**Add Python to PATH**

Verify the installation:

```bash
python --version
```

### Step 2: Create a Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python projects.

Execute:

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

For Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

Execute:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs the dependencies listed by the project.

---

## 🗄️ Database Configuration

The application supports two database modes.

### Option A: SQLite Demonstration Mode

SQLite is the default mode.

Advantages:

- No separate database server installation.
- Suitable for local demonstrations.
- Automatically creates the local database when initialized.
- Uses fictional sample data when appropriate.

Simply run the application without configuring MySQL mode.

The local database is stored under:

```text
data/hospital_demo.db
```

This database is generated when the application runs.

### Option B: MySQL Mode

To use MySQL:

1. Install MySQL Server.
2. Start the MySQL service.
3. Create the required database and user.
4. Copy `.env.example` to `.env`.
5. Enter your own database configuration.

Example:

```env
DB_MODE=mysql
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=hospital_management
```

Replace the example values with your actual configuration.

If required, execute the SQL statements in:

```text
database/schema.sql
```

Then start the application.

**Important:** Do not upload your `.env` file or database password to GitHub.

MySQL mode must be tested against an actual MySQL Server before it can be considered verified.

---

## ▶️ How to Run the Application

### Method 1: Windows Launcher

Double-click:

```text
start.bat
```

The launcher is designed to:

1. Create a virtual environment if one does not exist.
2. Activate the environment.
3. Install project dependencies.
4. Launch the application.

### Method 2: Run Using Python

Open the terminal in the project directory and execute:

```bash
python main.py
```

The application should open in a separate desktop window.

---

## 📘 How to Use the Application

### 1. Open the Dashboard

Launch the application.

The dashboard provides access to the main sections.

### 2. Manage Patients

Open the Patients section.

You can:

- Enter patient information.
- Add a patient.
- Search for a patient.
- Delete a patient record.

### 3. Manage Doctors

Open the Doctors section.

You can:

- Enter doctor information.
- Add a doctor.
- Search for a doctor.
- Delete a doctor record.

### 4. Manage Appointments

Open the Appointments section.

You can:

- Create an appointment.
- Select related patient and doctor records.
- Search appointment records.
- Delete appointments.

Use fictional data when exploring the application.

---

## 🧪 Testing and Debugging

Testing helps identify problems before distributing software.

This project includes basic automated database tests.

### Run the Unit Tests

Execute:

```bash
python -m unittest discover -s tests -v
```

### Code Quality Checks

Ruff can be used to identify Python linting issues:

```bash
ruff check .
```

### Security Checks

Bandit can be used to identify potentially unsafe Python coding patterns:

```bash
bandit -r app main.py
```

Install these tools if necessary:

```bash
pip install ruff bandit
```

These checks are useful but do not prove that the complete application is bug-free or secure.

### Additional Testing

The following areas should also be tested:

- Desktop interface behaviour.
- Patient record operations.
- Doctor record operations.
- Appointment creation and deletion.
- SQLite database behaviour.
- MySQL connection and operations.
- Input validation.
- Error handling.

---

## 🔐 Security and Privacy

This project is intended for educational use.

Please follow these precautions:

1. Never use actual patient information.
2. Never publish database passwords.
3. Never commit `.env` files.
4. Use fictional demonstration records.
5. Validate user input.
6. Review database permissions.
7. Do not treat the application as a secure production hospital system.

Healthcare information is sensitive. Real hospital systems require appropriate security, privacy, access controls, audit logging, backups and legal compliance.

---

## ⚠️ Known Limitations

The current reconstruction has several limitations:

- The original school project source code was unavailable.
- The current implementation is a reconstruction, not the original recovered application.
- The current feature set may differ from the original submission.
- The desktop interface still requires complete Windows testing.
- MySQL integration requires verification against a real server.
- The project has not undergone a professional security audit.
- The application is not designed for real hospital operations.

These limitations should be updated as testing and development progress.

---

## 🔮 Future Improvements

Possible future improvements include:

- Patient record editing.
- Doctor record editing.
- Improved appointment scheduling.
- User authentication and role-based access.
- Better input validation.
- Reporting and data export.
- Improved dashboard visualizations.
- Database backup and recovery.
- More comprehensive automated tests.
- Improved interface accessibility.
- Additional documentation and screenshots.

Future features should be implemented and tested before being advertised as available.

---

## 👥 Original School Project Team

This project was originally developed collaboratively by two students.

We acknowledge the contributions of the original team members.

| Contributor | Contribution |
| Raghavendra Nath Mishra | Led the project development, contributed to core Python programming, database integration, system implementation, debugging, and overall project coordination. |
| Gatik Kumar | Contributed to Python coding, debugging, and implementation of application features. |



---

## 🤖 Reconstruction and AI Acknowledgements

The current repository contains a reconstructed implementation prepared because the original source files were unavailable.

**AI assistance: ChatGPT by OpenAI**

ChatGPT assisted with:

- Reconstruction planning.
- Technical architecture discussions.
- Python code drafting.
- Database implementation guidance.
- Debugging explanations.
- Testing guidance.
- Documentation and README preparation.

The human project owner and contributors remain responsible for reviewing, validating, testing and maintaining the published implementation.

ChatGPT is acknowledged as an AI assistance tool, not as an original student team member or a human project contributor.

---

## 🤝 Contributing

Contributions and suggestions are welcome.

If you are a beginner, you can contribute by:

- Reporting bugs.
- Suggesting improvements.
- Improving documentation.
- Adding useful tests.
- Improving code readability.
- Suggesting practical features.

### Basic Contribution Workflow

1. Fork the repository.
2. Clone your fork.
3. Create a new branch.
4. Make your changes.
5. Test your changes.
6. Commit your work.
7. Open a Pull Request.

Example:

```bash
git checkout -b feature/my-improvement
git add .
git commit -m "Improve application functionality"
git push origin feature/my-improvement
```

Then open a Pull Request on GitHub.

---

## 📄 License

This project includes a LICENSE file.

Please review it before redistributing or modifying the project.

The original contributors should agree with the licensing and publication arrangements.

---

## ⚖️ Disclaimer

This project is an educational software reconstruction created for learning and demonstration purposes.

It is not a certified medical application, hospital information system or production healthcare solution.

Do not use it to store or process real patient records.

The reconstructed source code should not be represented as the original school submission.

---

## ⭐ Support the Project

If you find this project useful:

- Give the repository a Star.
- Explore the source code.
- Report issues.
- Suggest improvements.
- Share it with other learners.

**Thank you for exploring our Hospital Management System!**

*Built from a school-project learning experience, reconstructed for the developer community.*