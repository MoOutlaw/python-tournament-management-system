import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os

# Constants
APP_TITLE = "Tournament Management System"
DATA_FILE = "participants_data.txt"
SCOREBOARD_FILE = "scoreboard_data.txt"
POINTS_MAP = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
EVENTS = [
    ("Football", "Sports"),
    ("Basketball", "Sports"),
    ("Tennis", "Sports"),
    ("Literature", "Academics"),
    ("Geography", "Academics"),
]

# Validation Constants
MAX_INDIVIDUALS = 20
MAX_TEAM_MEMBERS = 5

# Global Data Storage
individuals_list = []
teams_list = []
scoreboard_data = []

# Utility Functions
def create_unique_id(prefix):
    """Generate a unique ID with a given prefix."""
    return f"{prefix}{random.randint(1, 50)}"

def load_data():
    """Load participant data from a file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                individuals_list.append(line.strip())

    if os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, "r") as file:
            for line in file:
                scoreboard_data.append(tuple(line.strip().split(",")))

def save_data():
    """Save participant and scoreboard data to files."""
    with open(DATA_FILE, "w") as file:
        for individual in individuals_list:
            file.write(f"{individual}\n")

    with open(SCOREBOARD_FILE, "w") as file:
        for entry in scoreboard_data:
            file.write(",".join(map(str, entry)) + "\n")

# Classes
class Individual:
    def __init__(self, name):
        self.name = name
        self.id = create_unique_id("I")
        individuals_list.append(self)

class Team:
    def __init__(self, name, members):
        self.name = name
        self.id = create_unique_id("T")
        self.members = members
        teams_list.append(self)

# GUI Setup Functions
def setup_main_window():
    """Create the main GUI window."""
    def open_registration_window():
        RegistrationWindow(main_window)

    def open_scoreboard_window():
        ScoreboardWindow(main_window)

    def manage_individuals():
        IndividualsWindow(main_window)

    def manage_teams():
        TeamsWindow(main_window)

    # Main Window Buttons
    tk.Button(main_window, text="Register Participants", command=open_registration_window).pack(pady=10)
    tk.Button(main_window, text="View Scoreboard", command=open_scoreboard_window).pack(pady=10)
    tk.Button(main_window, text="Manage Individuals", command=manage_individuals).pack(pady=10)
    tk.Button(main_window, text="Manage Teams", command=manage_teams).pack(pady=10)

class RegistrationWindow:
    """GUI for participant registration."""
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Participant Registration")
        self.total_individuals = len(individuals_list)
        self.total_teams = len(teams_list)
        self.setup_ui()

    def setup_ui(self):
        # Event Selection
        self.window.geometry("350x350")  # Set a size for the window
        tk.Label(self.window, text="Select Event:").pack(pady=5)
        self.event_selection = ttk.Combobox(self.window, values=[f"{event[0]} - {event[1]}" for event in EVENTS])
        self.event_selection.pack(pady=5)

        # Form Entries
        tk.Label(self.window, text="Participant Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Register as:").pack(pady=5)
        self.participant_type = tk.StringVar(value="Individual")
        tk.Radiobutton(self.window, text="Individual", variable=self.participant_type, value="Individual").pack()
        tk.Radiobutton(self.window, text="Team", variable=self.participant_type, value="Team").pack()
        tk.Button(self.window, text="Add Participant", command=self.add_participant).pack(pady=10)
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=5)

    def add_participant(self):
        """Register a participant."""
        name = self.name_entry.get().strip()
        selected_event = self.event_selection.get().strip()

        if not name or not selected_event:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        if self.participant_type.get() == "Individual":
            if self.total_individuals >= MAX_INDIVIDUALS:
                messagebox.showwarning(
                    "Registration Full",
                    f"The maximum number of individuals ({MAX_INDIVIDUALS}) has been reached. Registration is closed."
                )
                return

            Individual(name)
            self.total_individuals += 1
        else:
            if self.total_teams >= MAX_INDIVIDUALS // MAX_TEAM_MEMBERS:
                messagebox.showwarning(
                    "Registration Full",
                    "The maximum number of teams has been reached. Registration is closed."
                )
                return

            team_size = simpledialog.askinteger(
                "Team Size", "Enter number of members (max 5):", minvalue=1, maxvalue=MAX_TEAM_MEMBERS
            )
            if not team_size:
                return  # User canceled input

            members = []
            for i in range(team_size):
                member_name = simpledialog.askstring("Team Member", f"Enter name of member {i + 1}:")
                if not member_name:
                    messagebox.showerror("Input Error", "All team member names are required.")
                    return
                members.append(member_name)

            Team(name, members)
            self.total_teams += 1

        save_data()
        messagebox.showinfo("Success", f"{name} registered successfully for {selected_event}!")

class ScoreboardWindow:
    """GUI for viewing and updating the scoreboard."""
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Scoreboard")
        self.setup_ui()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.window, columns=("Participant", "Event", "Points"))
        self.tree.heading("#0", text="Rank")
        self.tree.heading("#1", text="Participant")
        self.tree.heading("#2", text="Event")
        self.tree.heading("#3", text="Points")
        self.tree.pack(expand=True, fill="both", pady=10)

        tk.Label(self.window, text="Participant ID:").pack(pady=5)
        self.participant_id_entry = tk.Entry(self.window)
        self.participant_id_entry.pack(pady=5)

        tk.Label(self.window, text="Event Name:").pack(pady=5)
        self.event_entry = ttk.Combobox(self.window, values=[event[0] for event in EVENTS])
        self.event_entry.pack(pady=5)

        tk.Label(self.window, text="Rank:").pack(pady=5)
        self.rank_entry = tk.Entry(self.window)
        self.rank_entry.pack(pady=5)

        tk.Button(self.window, text="Update Score", command=self.update_score).pack(pady=10)
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=10)
        self.refresh_tree()

    def update_score(self):
        participant_id = self.participant_id_entry.get().strip()
        event = self.event_entry.get().strip()
        rank = self.rank_entry.get().strip()

        if not participant_id or not event or not rank:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            rank = int(rank)
            if rank < 1 or rank > 5:
                raise ValueError("Rank must be between 1 and 5.")
        except ValueError:
            messagebox.showerror("Input Error", "Rank must be a number between 1 and 5.")
            return

        participant_name = self.find_participant_name(participant_id)
        if not participant_name:
            messagebox.showerror("Error", "Invalid Participant ID.")
            return

        points = POINTS_MAP.get(rank, 0)
        scoreboard_data.append((participant_name, event, points))
        save_data()
        self.refresh_tree()
        messagebox.showinfo("Success", "Score updated successfully!")

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        sorted_data = sorted(scoreboard_data, key=lambda x: x[2], reverse=True)
        for i, (participant, event, points) in enumerate(sorted_data, start=1):
            self.tree.insert("", "end", text=str(i), values=(participant, event, points))

    def find_participant_name(self, participant_id):
        for individual in individuals_list:
            if isinstance(individual, Individual) and individual.id == participant_id:
                return individual.name

        for team in teams_list:
            if isinstance(team, Team) and team.id == participant_id:
                return team.name

        return None

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        sorted_data = sorted(scoreboard_data, key=lambda x: -int(x[2]))
        for i, (name, event, points) in enumerate(sorted_data, start=1):
            self.tree.insert("", "end", text=i, values=(name, event, points))


class IndividualsWindow:
    """GUI for managing individuals."""
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Manage Individuals")
        self.setup_ui()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.window, columns=("Name", "ID"))
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="ID")
        self.tree.pack(expand=True, fill="both", pady=10)

        tk.Button(self.window, text="Edit Selected", command=self.edit_individual).pack(pady=5)
        tk.Button(self.window, text="Remove Selected", command=self.remove_individual).pack(pady=5)
        tk.Button(self.window, text="Refresh", command=self.refresh_tree).pack(pady=5)
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=5)
        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for individual in individuals_list:
            if isinstance(individual, Individual):
                self.tree.insert("", "end", values=(individual.name, individual.id))

    def edit_individual(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No individual selected.")
            return

        item = self.tree.item(selected_item)
        current_name = item['values'][0]
        individual_id = item['values'][1]

        new_name = simpledialog.askstring("Edit Individual", f"Edit name for {current_name}:")
        if not new_name:
            return

        for individual in individuals_list:
            if isinstance(individual, Individual) and individual.id == individual_id:
                individual.name = new_name
                save_data()
                self.refresh_tree()
                messagebox.showinfo("Success", "Individual updated successfully!")
                break

    def remove_individual(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No individual selected.")
            return

        item = self.tree.item(selected_item)
        individual_id = item['values'][1]

        for individual in individuals_list:
            if isinstance(individual, Individual) and individual.id == individual_id:
                individuals_list.remove(individual)
                save_data()
                self.refresh_tree()
                messagebox.showinfo("Success", "Individual removed successfully!")
                break


class TeamsWindow:
    """GUI for managing teams."""
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Manage Teams")
        self.setup_ui()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.window, columns=("Name", "ID", "Members"))
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="ID")
        self.tree.heading("#3", text="Members")
        self.tree.pack(expand=True, fill="both", pady=10)

        tk.Button(self.window, text="Edit Selected", command=self.edit_team).pack(pady=5)
        tk.Button(self.window, text="Remove Selected", command=self.remove_team).pack(pady=5)
        tk.Button(self.window, text="Refresh", command=self.refresh_tree).pack(pady=5)
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=5)
        self.refresh_tree()

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for team in teams_list:
            if isinstance(team, Team):
                members = ", ".join(team.members)
                self.tree.insert("", "end", values=(team.name, team.id, members))

    def edit_team(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No team selected.")
            return

        item = self.tree.item(selected_item)
        current_name = item['values'][0]
        team_id = item['values'][1]

        new_name = simpledialog.askstring("Edit Team", f"Edit name for {current_name}:")
        if not new_name:
            return

        for team in teams_list:
            if isinstance(team, Team) and team.id == team_id:
                team.name = new_name
                save_data()
                self.refresh_tree()
                messagebox.showinfo("Success", "Team updated successfully!")
                break

    def remove_team(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No team selected.")
            return

        item = self.tree.item(selected_item)
        team_id = item['values'][1]

        for team in teams_list:
            if isinstance(team, Team) and team.id == team_id:
                teams_list.remove(team)
                save_data()
                self.refresh_tree()
                messagebox.showinfo("Success", "Team removed successfully!")
                break

if __name__ == "__main__":
    load_data()
    main_window = tk.Tk()
    main_window.title(APP_TITLE)
    setup_main_window()
    main_window.geometry("350x200")  # Set a size for the window
    main_window.mainloop()
