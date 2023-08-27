import tkinter as tk
from tkinter import ttk

def parse_logs():
    # This function is a placeholder.
    # You can place your logic to read and parse logs here.
    return "Sample log data"

def create_gui():
    root = tk.Tk()
    root.title("IIS Monitoring Tool")

    # Create the main tabbed interface
    tab_control = ttk.Notebook(root)

    # Create the first tab
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Monitor')

    # Create columns for 'request', 'port', and 'response' in the first tab
    tree = ttk.Treeview(tab1, columns=('Request', 'Port', 'Response'), show='headings')
    tree.heading('Request', text='Request')
    tree.heading('Port', text='Port')
    tree.heading('Response', text='Response')
    tree.pack(padx=10, pady=10)

    # Create the second tab
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Logs')

    # Text widget for displaying parsed logs in the second tab
    log_display = tk.Text(tab2, wrap=tk.WORD)
    log_data = parse_logs()
    log_display.insert(tk.END, log_data)
    log_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    tab_control.pack(expand=1, fill='both')

    root.mainloop()

if __name__ == '__main__':
    create_gui()
