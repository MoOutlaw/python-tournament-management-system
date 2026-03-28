# Tournament Management System

A fully functional desktop GUI application for managing sports and academic tournaments, built with Python and Tkinter. Developed as a college IT Project Management assignment, the project demonstrates both applied software development and structured Agile project delivery across four sprints.

---

## Module Context

**Assignment:** IT Project Management
**Institution:** Coventry College
**Level:** National Extended Diploma in IT (Level 3)

---

## Tech Stack

**Language:** Python 3
**GUI Framework:** Tkinter (ttk)
**Data Storage:** Plain text files — no external database required
**Dependencies:** None — built entirely on the Python standard library

---

## Features

- Register individual participants and teams of up to 5 members
- Manage multiple events across two categories:
  - Sports: Football, Basketball, Tennis
  - Academic: Literature, Geography
- Automated points allocation based on finishing position (1st = 5pts, 2nd = 4pts, and so on)
- Live scoreboard that updates in real time as results are entered
- Unique ID generation for each participant and team to prevent duplicates
- Data persistence between sessions using local text files, so no data is lost on close

---
## Proof/Screenshots
<img width="571" height="331" alt="Screenshot 2026-03-28 225010" src="https://github.com/user-attachments/assets/96ff45c6-184c-4b89-bae2-d8ea32b0810f" />
<img width="607" height="441" alt="Screenshot 2026-03-28 224736" src="https://github.com/user-attachments/assets/0f56b76f-59e6-49c4-ba23-23f433297136" />
<img width="575" height="429" alt="Screenshot 2026-03-28 224901" src="https://github.com/user-attachments/assets/ab505d3e-f5b3-4e30-9b63-02102b2c895e" />
<img width="546" height="336" alt="Screenshot 2026-03-28 224928" src="https://github.com/user-attachments/assets/551eecf5-12c8-4f6f-81e9-f72729b9f5bb" />
<img width="565" height="653" alt="Screenshot 2026-03-28 224801" src="https://github.com/user-attachments/assets/37a78eab-ff36-445e-b2f2-54f5450e43fd" />

## How to Run

**Prerequisites:** Python 3 installed on your machine. No additional libraries needed.

**Step 1 — Clone the repository**


```bash
git clone https://github.com/MoOutlaw/tournament-management-system.git
cd tournament-management-system
```

**Step 2 — Run the application**

```bash
python tournament_system.py
```

The GUI will launch immediately. No configuration or setup is required.

---

## Repository Structure

```
├── tournament_system.py                   # Main application file
├── participants_data.txt                  # Persistent storage for participant records
├── scoreboard_data.txt                    # Persistent storage for scores and results
├── Tournament_System Sprint.pdf           # Sprint planning and Agile tracking documents
├── Technical_Support_Management_Report/   # Supporting project management report
└── README.md
```

---

## Project Management

This project was planned and delivered using Agile/Scrum methodology, broken into four sprints. Each sprint had defined goals, tasks, and a review stage before moving to the next phase.

Sprint documentation and a full Gantt chart are included in the repository, covering:

- Sprint planning and backlog definition
- Task allocation and progress tracking across all four sprints
- Timeline management using a Gantt chart
- Final review and evaluation of the delivered system against the original requirements

This approach mirrors how software projects are managed professionally, demonstrating an understanding of iterative development and structured delivery beyond the code itself.

---

## Key Skills Demonstrated

- Python GUI development using Tkinter and ttk widgets
- Application logic design including ID generation, points calculation, and state management
- File-based data persistence without reliance on external libraries or databases
- Agile project management — sprint planning, backlog management, and iterative delivery
- Technical documentation and project reporting
