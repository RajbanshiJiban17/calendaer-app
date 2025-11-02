import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkcalendar import Calendar

calendar_events = {} # dictionary file  to store
def add_event():
    date = cal.get_date()
    event = simpledialog.askstring("Event", f"{date} Choose Event")
    if event:
        if date in calendar_events:
            calendar_events[date].append(event)
        else:
            calendar_events[date] = [event]
        messagebox.showinfo("Success", f"Event '{event}' {date} Added")
        view_events()

# Function to remove event
def remove_event():
    date = cal.get_date()
    if date in calendar_events:
        events = calendar_events[date]
        if not events:
            messagebox.showinfo("Info", f"{date} No Event Found")
            return
        # Select event to remove
        event = simpledialog.askstring("Event Deleted", f"{date} Events: {events}\nDo you want delete event choose one!")
        if event in events:
            events.remove(event)
            if not events:
                del calendar_events[date]
            messagebox.showinfo("Success", f"Event '{event}' {date} Deleted Sucess")
            view_events()
        else:
            messagebox.showerror("Error", "Not Found")
    else:
        messagebox.showinfo("Info", f"{date} No Search Found")

        

# Function to view events
def view_events():
    events_listbox.delete(0, tk.END)
    date = cal.get_date()
    if date in calendar_events:
        for event in calendar_events[date]:
            events_listbox.insert(tk.END, event)
    else:
        events_listbox.insert(tk.END, "No Found।")      
        
root = tk.Tk()
root.title("Calendar App")
root.geometry("600x400")

# Calendar widget
cal = Calendar(root, selectmode="day")
cal.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Event", command=add_event, width=20, bg="lightgreen")
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(button_frame, text="Delete Event", command=remove_event, width=20, bg="lightcoral")
remove_btn.grid(row=0, column=1, padx=5)

view_btn = tk.Button(button_frame, text="View Event", command=view_events, width=20, bg="lightblue")
view_btn.grid(row=0, column=2, padx=5)

# Listbox to show events
events_listbox = tk.Listbox(root, width=80)
events_listbox.pack(pady=20)
    
root.mainloop()      



