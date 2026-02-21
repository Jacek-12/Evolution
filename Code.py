# Hier kommt der Code hin.
import tkinter as tk

def start_anzeige():

    root = tk.Tk()
    root.title("Status")

    
    root.configure(bg="white")

 
    label = tk.Label(
        root, 
        text="Das ist ein vorschlag", 
        font=("Helvetica", 60, "bold"), 
        fg="green", 
        bg="black"
    )
    
   
    label.pack(expand=True, padx=50, pady=50)

   
    root.mainloop()

if __name__ == "__main__":
    start_anzeige()
