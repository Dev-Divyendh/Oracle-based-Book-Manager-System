import customtkinter as ctk

def show_toast(master, text, color="green", duration=3000):
    toast = ctk.CTkLabel(master, text=text, fg_color=color, text_color="white", corner_radius=8, font=("Segoe UI", 10, "bold"))
    toast.place(relx=0.5, rely=0.95, anchor="center")
    master.after(duration, toast.destroy)
