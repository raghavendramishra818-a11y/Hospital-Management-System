"""Tkinter desktop interface for the Hospital Management System."""
import tkinter as tk
from tkinter import ttk, messagebox
from app.database import Database

BG = "#F4F7FB"
NAVY = "#142D4E"
BLUE = "#2563EB"
TEXT = "#172B4D"
MUTED = "#66758A"
WHITE = "#FFFFFF"


class HospitalApp:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("CarePoint | Hospital Management System")
        self.root.geometry("1180x760")
        self.root.minsize(940, 620)
        self.root.configure(bg=BG)
        self._configure_style()
        self._build_shell()
        self.show_dashboard()

    def _configure_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=WHITE, fieldbackground=WHITE,
                        foreground=TEXT, rowheight=34, borderwidth=0,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#EAF0F8",
                        foreground=NAVY, font=("Segoe UI", 10, "bold"),
                        relief="flat")
        style.map("Treeview", background=[("selected", "#DBEAFE")],
                  foreground=[("selected", NAVY)])
        style.configure("TCombobox", padding=7)

    def _build_shell(self):
        self.sidebar = tk.Frame(self.root, bg=NAVY, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        brand = tk.Frame(self.sidebar, bg=NAVY)
        brand.pack(fill="x", padx=20, pady=(28, 32))
        tk.Label(brand, text="✚  CAREPOINT", bg=NAVY, fg=WHITE,
                 font=("Segoe UI", 17, "bold")).pack(anchor="w")
        tk.Label(brand, text="HOSPITAL MANAGEMENT", bg=NAVY, fg="#AFC4DF",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(5, 0))

        self.nav_buttons = {}
        for label, callback in [
            ("▦   Dashboard", self.show_dashboard),
            ("♙   Patients", self.show_patients),
            ("✚   Doctors", self.show_doctors),
            ("▣   Appointments", self.show_appointments),
        ]:
            btn = tk.Button(
                self.sidebar, text=label, command=callback, anchor="w",
                bg=NAVY, fg="#DCE7F5", activebackground="#24476F",
                activeforeground=WHITE, relief="flat", bd=0,
                font=("Segoe UI", 11), padx=22, pady=13, cursor="hand2"
            )
            btn.pack(fill="x", padx=10, pady=3)
            self.nav_buttons[label] = btn

        tk.Label(self.sidebar, text="DEMO / LOCAL APPLICATION",
                 bg=NAVY, fg="#AFC4DF", font=("Segoe UI", 8, "bold")
                 ).pack(side="bottom", pady=22)

        self.main = tk.Frame(self.root, bg=BG)
        self.main.pack(side="right", fill="both", expand=True)

        top = tk.Frame(self.main, bg=WHITE, height=70)
        top.pack(fill="x")
        top.pack_propagate(False)
        self.page_title = tk.Label(top, text="Dashboard", bg=WHITE, fg=NAVY,
                                   font=("Segoe UI", 18, "bold"))
        self.page_title.pack(side="left", padx=28, pady=19)
        self.mode_label = tk.Label(top, text=f"● {self.db.mode.upper()} MODE",
                                   bg=WHITE, fg="#16845B",
                                   font=("Segoe UI", 9, "bold"))
        self.mode_label.pack(side="right", padx=28)

        self.content = tk.Frame(self.main, bg=BG)
        self.content.pack(fill="both", expand=True, padx=28, pady=24)

    def _clear(self, title):
        for widget in self.content.winfo_children():
            widget.destroy()
        self.page_title.config(text=title)

    def _heading(self, title, subtitle):
        tk.Label(self.content, text=title, bg=BG, fg=TEXT,
                 font=("Segoe UI", 21, "bold")).pack(anchor="w")
        tk.Label(self.content, text=subtitle, bg=BG, fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 18))

    def _card(self, parent, label, value, accent):
        card = tk.Frame(parent, bg=WHITE, highlightthickness=1,
                        highlightbackground="#E5EBF3")
        card.pack(side="left", fill="both", expand=True, padx=(0, 14))
        tk.Frame(card, bg=accent, height=4).pack(fill="x")
        tk.Label(card, text=label.upper(), bg=WHITE, fg=MUTED,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=18, pady=(16, 5))
        tk.Label(card, text=str(value), bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=18, pady=(0, 16))

    def _button(self, parent, text, command, primary=True):
        return tk.Button(parent, text=text, command=command,
                         bg=BLUE if primary else "#E8EEF7",
                         fg=WHITE if primary else NAVY,
                         activebackground="#1D4ED8" if primary else "#DCE6F3",
                         activeforeground=WHITE if primary else NAVY,
                         relief="flat", bd=0, padx=16, pady=9,
                         font=("Segoe UI", 9, "bold"), cursor="hand2")

    def show_dashboard(self):
        self._clear("Dashboard")
        self._heading("Good day 👋", "Here's an overview of your hospital records.")
        stats = tk.Frame(self.content, bg=BG)
        stats.pack(fill="x", pady=(0, 24))
        patient_count = self.db.fetch_one("SELECT COUNT(*) AS total FROM patients")["total"]
        doctor_count = self.db.fetch_one("SELECT COUNT(*) AS total FROM doctors")["total"]
        appointment_count = self.db.fetch_one("SELECT COUNT(*) AS total FROM appointments")["total"]
        self._card(stats, "Registered patients", patient_count, BLUE)
        self._card(stats, "Doctors", doctor_count, "#0F9D78")
        self._card(stats, "Appointments", appointment_count, "#E69A24")

        panel = tk.Frame(self.content, bg=WHITE, highlightthickness=1,
                         highlightbackground="#E5EBF3")
        panel.pack(fill="both", expand=True)
        tk.Label(panel, text="Welcome to CarePoint", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=22, pady=(22, 7))
        tk.Label(panel, text=(
            "Use the navigation menu to manage patients, doctors and appointments.\n\n"
            "This reconstructed project starts in local demo mode, so you can explore "
            "the interface without installing MySQL. Configure MySQL later using the "
            "instructions in README.md."
        ), justify="left", bg=WHITE, fg=MUTED,
            font=("Segoe UI", 10), wraplength=700).pack(anchor="w", padx=22, pady=(0, 20))
        self._button(panel, "View patients", self.show_patients).pack(anchor="w", padx=22, pady=8)

    def _table_page(self, title, subtitle, columns, rows, add_command, delete_command, search_key):
        self._clear(title)
        self._heading(title, subtitle)
        toolbar = tk.Frame(self.content, bg=BG)
        toolbar.pack(fill="x", pady=(0, 12))
        search_var = tk.StringVar()
        search = ttk.Entry(toolbar, textvariable=search_var, width=32)
        search.pack(side="left", ipady=6)
        search.insert(0, "")
        self._button(toolbar, "＋  Add new", add_command).pack(side="right")
        self._button(toolbar, "Delete selected", delete_command, False).pack(side="right", padx=8)

        wrap = tk.Frame(self.content, bg=WHITE, highlightthickness=1,
                        highlightbackground="#E5EBF3")
        wrap.pack(fill="both", expand=True)
        tree = ttk.Treeview(wrap, columns=columns, show="headings")
        for col, heading, width in columns:
            tree.heading(col, text=heading)
            tree.column(col, width=width, anchor="w")
        scrollbar = ttk.Scrollbar(wrap, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        scrollbar.pack(side="right", fill="y", pady=8)

        def populate():
            for item in tree.get_children():
                tree.delete(item)
            query = search_var.get().strip().lower()
            for row in rows():
                values = tuple(row.get(col, "") for col, _, _ in columns)
                if not query or query in " ".join(map(str, values)).lower():
                    tree.insert("", "end", values=values, iid=str(row["id"]))

        search_var.trace_add("write", lambda *_: populate())
        populate()
        self.current_tree = tree
        self.current_refresh = populate

    def show_patients(self):
        self._table_page(
            "Patients", "Register and maintain patient information.",
            [("id", "ID", 60), ("name", "Patient name", 220),
             ("age", "Age", 70), ("gender", "Gender", 110),
             ("phone", "Phone", 150), ("address", "Address", 220)],
            lambda: self.db.fetch_all("SELECT id,name,age,gender,phone,address FROM patients ORDER BY id DESC"),
            self.add_patient, self.delete_selected, "name"
        )

    def show_doctors(self):
        self._table_page(
            "Doctors", "Maintain doctor profiles and specializations.",
            [("id", "ID", 60), ("name", "Doctor name", 250),
             ("specialization", "Specialization", 230), ("phone", "Phone", 170)],
            lambda: self.db.fetch_all("SELECT id,name,specialization,phone FROM doctors ORDER BY id DESC"),
            self.add_doctor, self.delete_selected, "name"
        )

    def show_appointments(self):
        self._table_page(
            "Appointments", "Schedule and review patient appointments.",
            [("id", "ID", 55), ("patient", "Patient", 190),
             ("doctor", "Doctor", 190), ("appointment_date", "Date", 150),
             ("reason", "Reason", 210), ("status", "Status", 110)],
            lambda: self.db.fetch_all(
                """SELECT a.id, p.name AS patient, d.name AS doctor,
                          a.appointment_date, a.reason, a.status
                   FROM appointments a
                   JOIN patients p ON p.id=a.patient_id
                   JOIN doctors d ON d.id=a.doctor_id
                   ORDER BY a.id DESC"""
            ),
            self.add_appointment, self.delete_selected, "patient"
        )

    def _form(self, title, fields, on_save):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.configure(bg=WHITE)
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        tk.Label(dialog, text=title, bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=22, pady=(20, 12))
        entries = {}
        body = tk.Frame(dialog, bg=WHITE)
        body.pack(fill="both", padx=22)
        for label, key, options in fields:
            tk.Label(body, text=label, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(7, 3))
            if options:
                widget = ttk.Combobox(body, values=options, state="readonly", width=38)
                widget.current(0)
            else:
                widget = ttk.Entry(body, width=41)
            widget.pack(fill="x", ipady=5)
            entries[key] = widget

        def save():
            values = {key: widget.get().strip() for key, widget in entries.items()}
            if any(not value for value in values.values()):
                messagebox.showwarning("Missing information", "Please complete every field.", parent=dialog)
                return
            try:
                on_save(values)
                dialog.destroy()
                self._refresh_current_page()
            except (ValueError, TypeError) as exc:
                messagebox.showerror("Invalid information", str(exc), parent=dialog)
            except Exception as exc:
                messagebox.showerror("Could not save", str(exc), parent=dialog)

        self._button(dialog, "Save record", save).pack(anchor="e", padx=22, pady=20)
        dialog.wait_window()

    def add_patient(self):
        self._form("Add patient", [
            ("Full name", "name", None), ("Age", "age", None),
            ("Gender", "gender", ["Female", "Male", "Other", "Prefer not to say"]),
            ("Phone", "phone", None), ("Address", "address", None)
        ], self._save_patient)

    def _save_patient(self, v):
        age = int(v["age"])
        if not 0 <= age <= 120:
            raise ValueError("Enter an age between 0 and 120.")
        self.db.execute(
            "INSERT INTO patients (name,age,gender,phone,address) VALUES (?,?,?,?,?)",
            (v["name"], age, v["gender"], v["phone"], v["address"])
        ).close()

    def add_doctor(self):
        self._form("Add doctor", [
            ("Full name", "name", None), ("Specialization", "specialization", None),
            ("Phone", "phone", None)
        ], lambda v: self.db.execute(
            "INSERT INTO doctors (name,specialization,phone) VALUES (?,?,?)",
            (v["name"], v["specialization"], v["phone"])
        ).close())

    def add_appointment(self):
        patients = self.db.fetch_all("SELECT id,name FROM patients ORDER BY name")
        doctors = self.db.fetch_all("SELECT id,name FROM doctors ORDER BY name")
        if not patients or not doctors:
            messagebox.showinfo("Records needed", "Add at least one patient and one doctor first.")
            return
        patient_options = [f'{p["id"]} - {p["name"]}' for p in patients]
        doctor_options = [f'{d["id"]} - {d["name"]}' for d in doctors]
        def save(v):
            patient_id = int(v["patient"].split(" - ", 1)[0])
            doctor_id = int(v["doctor"].split(" - ", 1)[0])
            self.db.execute(
                "INSERT INTO appointments (patient_id,doctor_id,appointment_date,reason,status) VALUES (?,?,?,?,?)",
                (patient_id, doctor_id, v["date"], v["reason"], "Scheduled")
            ).close()
        self._form("Schedule appointment", [
            ("Patient", "patient", patient_options),
            ("Doctor", "doctor", doctor_options),
            ("Date (YYYY-MM-DD)", "date", None),
            ("Reason", "reason", None)
        ], save)

    def delete_selected(self):
        selected = self.current_tree.selection() if hasattr(self, "current_tree") else ()
        if not selected:
            messagebox.showinfo("Select a record", "Select a row first.")
            return
        if not messagebox.askyesno("Confirm deletion", "Delete the selected record? Related appointments may also be removed."):
            return
        delete_queries = {
            "Patients": "DELETE FROM patients WHERE id=?",
            "Doctors": "DELETE FROM doctors WHERE id=?",
            "Appointments": "DELETE FROM appointments WHERE id=?",
        }
        query = delete_queries.get(self.page_title.cget("text"))
        if query:
            self.db.execute(query, (int(selected[0]),)).close()
            self._refresh_current_page()

    def _refresh_current_page(self):
        page = self.page_title.cget("text")
        if page == "Patients":
            self.show_patients()
        elif page == "Doctors":
            self.show_doctors()
        elif page == "Appointments":
            self.show_appointments()
        else:
            self.show_dashboard()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self.root.mainloop()

    def _on_close(self):
        self.db.close()
        self.root.destroy()
