import tkinter as tk
from tkinter import messagebox

# Function to clear the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Function to copy text to clipboard
def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Code copied to clipboard!")

# Function to show the generated code
def show_generated_code(code):
    clear_screen()
    create_label(root, "Generated Code:")
    code_text = tk.Text(root, height=10, width=50, bg="white")
    code_text.insert(tk.END, code)
    code_text.pack(pady=10)

    tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(code), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

# Helper function to create labels
def create_label(parent, text, font=("Verdana", 14, "bold")):
    label = tk.Label(parent, text=text, font=font, bg="white")
    label.pack(pady=10)
    return label

# Function to add more fields dynamically with optional checkbox
def add_field(entries_list, parent_frame, with_checkbox=False):
    entry_frame = tk.Frame(parent_frame, bg="white")
    entry_frame.pack(pady=5)
    
    entry = tk.Entry(entry_frame)
    entry.pack(side=tk.LEFT, padx=5)
    entries_list.append(entry)
    
    if with_checkbox:
        var = tk.IntVar()
        tk.Checkbutton(entry_frame, text="Args", variable=var, bg="white").pack(side=tk.LEFT)
        return var

# Input page for creating a class
def class_input_page():
    clear_screen()
    
    fields_entries = []
    create_label(root, "Enter Class Information")
    
    create_label(root, "Class Name:", font=("Verdana", 12))
    class_name_entry = tk.Entry(root)
    class_name_entry.pack(pady=5)
    
    create_label(root, "Fields (one per box):", font=("Verdana", 12))
    
    fields_frame = tk.Frame(root, bg="white")
    fields_frame.pack(pady=5)
    
    for _ in range(4):
        add_field(fields_entries, fields_frame)
    
    tk.Button(root, text="Add Field", command=lambda: add_field(fields_entries, fields_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    tk.Button(root, text="Generate Class", command=lambda: generate_class(class_name_entry, fields_entries), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_class(class_name_entry, fields_entries):
    class_name = class_name_entry.get().strip().lower()
    fields = [entry.get().strip().lower() for entry in fields_entries if entry.get().strip()]
    
    class_code = f"class {class_name}:\n    \"\"\"\n    Class representing {class_name}.\n\n    Args:\n"
    for field in fields:
        class_code += f"        {field} (str): Description of {field}.\n"
    class_code += "    \"\"\"\n\n    def __init__(self, " + ", ".join(fields) + "):\n"
    class_code += "".join([f"        self.{field} = {field}\n" for field in fields])
    
    if not fields:
        class_code += "    pass\n"
    
    # Add example and formatted print statements
    class_code += f"\n{class_name}_instance = {class_name}(" + ", ".join(["'<add text>'"] * len(fields)) + ")\n"
    for field in fields:
        class_code += f"print(f\"{field.capitalize()}: {{{class_name}_instance.{field}}}\")\n"
    
    show_generated_code(class_code)


# Input page for creating a function
def function_input_page():
    clear_screen()
    
    params_entries = []
    params_checkboxes = []
    
    create_label(root, "Enter Function Information")
    
    create_label(root, "Function Name:", font=("Verdana", 12))
    func_name_entry = tk.Entry(root)
    func_name_entry.pack(pady=5)
    
    create_label(root, "Parameters (one per box):", font=("Verdana", 12))
    
    params_frame = tk.Frame(root, bg="white")
    params_frame.pack(pady=5)
    
    for _ in range(4):
        params_checkboxes.append(add_field(params_entries, params_frame, with_checkbox=True))
    
    tk.Button(root, text="Add Parameter", command=lambda: params_checkboxes.append(add_field(params_entries, params_frame, with_checkbox=True)), font=("Verdana", 12, "bold")).pack(pady=5)
    
    print_params_var = tk.IntVar()
    tk.Checkbutton(root, text="Print Greeting", variable=print_params_var, font=("Verdana", 12), bg="white").pack(pady=5)
    
    tk.Button(root, text="Generate Function", command=lambda: generate_function(func_name_entry, params_entries, params_checkboxes, print_params_var), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_function(func_name_entry, params_entries, params_checkboxes, print_params_var):
    func_name = func_name_entry.get().strip().lower()
    params = [entry.get().strip().lower() for entry in params_entries if entry.get().strip()]
    params_with_defaults = [
        f"{param}='default_value'" if checkbox.get() == 1 else param
        for param, checkbox in zip(params, params_checkboxes)
    ]
    
    func_code = f"def {func_name}({', '.join(params_with_defaults)}):\n"
    
    # Auto-generate docstring
    func_code += f"    \"\"\"\n    Function to {func_name}.\n\n    Args:\n"
    for param in params:
        func_code += f"        {param} (str): Description of {param}.\n"
    func_code += "    \"\"\"\n\n"
    
    if print_params_var.get() == 1 and len(params) >= 2:
        func_code += f"    print(f\"Hello, {{{params[0]}}}! You are {{{params[1]}}} years old.\")\n"
    
    func_code += "    # TODO: Add your logic here\n"
    
    show_generated_code(func_code)

# Input page for creating a tuple
def tuple_input_page():
    clear_screen()
    
    tuple_entries = []
    create_label(root, "Enter Tuple Values")
    
    create_label(root, "Values (one per box):", font=("Verdana", 12))
    
    tuple_frame = tk.Frame(root, bg="white")
    tuple_frame.pack(pady=5)
    
    for _ in range(4):
        add_field(tuple_entries, tuple_frame)
    
    tk.Button(root, text="Add Value", command=lambda: add_field(tuple_entries, tuple_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    tk.Button(root, text="Generate Tuple", command=lambda: generate_tuple(tuple_entries), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_tuple(tuple_entries):
    values = [entry.get().strip().lower() for entry in tuple_entries if entry.get().strip()]
    tuple_code = f"my_tuple = ({', '.join(values)})\n"
    show_generated_code(tuple_code)

# Input page for creating a list
def list_input_page():
    clear_screen()
    
    list_entries = []
    create_label(root, "Enter List Information")
    
    create_label(root, "List Name:", font=("Verdana", 12))
    list_name_entry = tk.Entry(root)
    list_name_entry.pack(pady=5)
    
    create_label(root, "Items (one per box):", font=("Verdana", 12))
    
    list_frame = tk.Frame(root, bg="white")
    list_frame.pack(pady=5)
    
    for _ in range(4):
        add_field(list_entries, list_frame)
    
    tk.Button(root, text="Add Item", command=lambda: add_field(list_entries, list_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    tk.Button(root, text="Generate List", command=lambda: generate_list(list_name_entry, list_entries), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_list(list_name_entry, list_entries):
    list_name = list_name_entry.get().strip()
    items = [entry.get().strip().lower() for entry in list_entries if entry.get().strip()]
    list_code = f"{list_name} = [{', '.join(items)}]\n"
    show_generated_code(list_code)

# Input page for creating a dictionary
def dict_input_page():
    clear_screen()
    
    dict_keys_entries = []
    dict_values_entries = []
    
    create_label(root, "Enter Dictionary Information")
    
    create_label(root, "Dictionary Name:", font=("Verdana", 12))
    dict_name_entry = tk.Entry(root)
    dict_name_entry.pack(pady=5)
    
    create_label(root, "Keys (one per box):", font=("Verdana", 12))
    
    keys_frame = tk.Frame(root, bg="white")
    keys_frame.pack(pady=5)
    
    for _ in range(3):
        add_field(dict_keys_entries, keys_frame)
    
    tk.Button(root, text="Add Key", command=lambda: add_field(dict_keys_entries, keys_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    
    create_label(root, "Values (one per box):", font=("Verdana", 12))
    
    values_frame = tk.Frame(root, bg="white")
    values_frame.pack(pady=5)
    
    for _ in range(3):
        add_field(dict_values_entries, values_frame)
    
    tk.Button(root, text="Add Value", command=lambda: add_field(dict_values_entries, values_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    
    tk.Button(root, text="Generate Dictionary", command=lambda: generate_dict(dict_name_entry, dict_keys_entries, dict_values_entries), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_dict(dict_name_entry, dict_keys_entries, dict_values_entries):
    dict_name = dict_name_entry.get().strip()
    keys = [entry.get().strip().lower() for entry in dict_keys_entries if entry.get().strip()]
    values = [entry.get().strip() for entry in dict_values_entries if entry.get().strip()]
    
    if len(keys) != len(values):
        messagebox.showerror("Error", "Keys and values must be equal in number!")
        return
    
    dict_code = f"{dict_name} = {{{', '.join(f'{k}: {v}' for k, v in zip(keys, values))}}}\n"
    show_generated_code(dict_code)

# Input page for creating a set
def set_input_page():
    clear_screen()
    
    set_entries = []
    create_label(root, "Enter Set Information")
    
    create_label(root, "Set Name:", font=("Verdana", 12))
    set_name_entry = tk.Entry(root)
    set_name_entry.pack(pady=5)
    
    create_label(root, "Items (one per box):", font=("Verdana", 12))
    
    set_frame = tk.Frame(root, bg="white")
    set_frame.pack(pady=5)
    
    for _ in range(4):
        add_field(set_entries, set_frame)
    
    tk.Button(root, text="Add Item", command=lambda: add_field(set_entries, set_frame), font=("Verdana", 12, "bold")).pack(pady=5)
    tk.Button(root, text="Generate Set", command=lambda: generate_set(set_name_entry, set_entries), font=("Verdana", 12, "bold")).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold")).pack(pady=10)

def generate_set(set_name_entry, set_entries):
    set_name = set_name_entry.get().strip()
    items = [entry.get().strip().lower() for entry in set_entries if entry.get().strip()]
    set_code = f"{set_name} = {{{', '.join(items)}}}\n"
    show_generated_code(set_code)

# Main menu
def main_menu():
    clear_screen()
    create_label(root, "Python Code Generator", font=("Helvetica", 16, "bold"))
    
    buttons = [
        ("Create Class", class_input_page),
        ("Create Function", function_input_page),
        ("Create Tuple", tuple_input_page),
        ("Create List", list_input_page),
        ("Create Dictionary", dict_input_page),
        ("Create Set", set_input_page)
    ]
    
    for text, command in buttons:
        tk.Button(root, text=text, command=command, font=("Verdana", 12, "bold"), width=20).pack(pady=10)
    
    tk.Button(root, text="Exit", command=root.quit, font=("Verdana", 12, "bold"), width=20).pack(pady=10)

# Initialize Tkinter window
root = tk.Tk()
root.title("Python Structure Generator")
root.geometry("350x450")
root.configure(bg="white")

# Start with the main menu
main_menu()

root.mainloop()
