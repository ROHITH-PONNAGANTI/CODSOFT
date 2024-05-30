import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")
        master.geometry("665x400+550+250")
        master.configure(bg="#333333")

        self.create_widgets()

        self.conn = sql.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
        self.retrieve_database()

    def create_widgets(self):
        self.functions_frame = tk.Frame(self.master, bg="#555555")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.task_label = tk.Label(self.functions_frame, text="TO-DO LIST\nEnter the Task Title:",
                                   font=("Helvetica", 14, "bold"), bg="#555555", fg="#FFFFFF")
        self.task_label.place(x=20, y=30)

        self.task_entry = tk.Entry(self.functions_frame, font=("Arial", 14), width=42, fg="#333333", bg="#FFFFFF")
        self.task_entry.place(x=180, y=30)

        self.add_button = tk.Button(self.functions_frame, text="Add Task", width=15, bg='#008080',
                                    font=("Arial", 14, "bold"), command=self.add_task, fg="#FFFFFF")
        self.add_button.place(x=18, y=80)

        self.del_button = tk.Button(self.functions_frame, text="Delete Task", width=15, bg='#800000',
                                    font=("Arial", 14, "bold"), command=self.delete_task, fg="#FFFFFF")
        self.del_button.place(x=240, y=80)

        self.del_all_button = tk.Button(self.functions_frame, text="Delete All", width=15, bg='#800000',
                                        font=("Arial", 14, "bold"), command=self.delete_all_tasks, fg="#FFFFFF")
        self.del_all_button.place(x=460, y=80)

        self.exit_button = tk.Button(self.functions_frame, text="Exit / Close", width=52, bg='#808000',
                                     font=("Arial", 14, "bold"), command=self.close, fg="#FFFFFF")
        self.exit_button.place(x=17, y=330)

        self.task_listbox = tk.Listbox(self.functions_frame, width=70, height=9, font=("Arial", 12),
                                        selectmode='SINGLE', bg="#FFFFFF", fg="#333333",
                                        selectbackground="#008080", selectforeground="#FFFFFF")
        self.task_listbox.place(x=17, y=140)

    def add_task(self):
        task_string = self.task_entry.get().strip()
        if task_string:
            self.tasks.append(task_string)
            self.cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))
            self.list_update()
            self.task_entry.delete(0, 'end')
        else:
            messagebox.showinfo('Error', 'Field is Empty.')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            selection_index = self.task_listbox.curselection()
            if selection_index:
                selected_task = self.task_listbox.get(selection_index)
                self.tasks.remove(selected_task)
                self.cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
                self.list_update()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            self.tasks.clear()
            self.cursor.execute('DELETE FROM tasks')
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        self.master.destroy()

    def retrieve_database(self):
        self.tasks = []
        for row in self.cursor.execute('SELECT title FROM tasks'):
            self.tasks.append(row[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
