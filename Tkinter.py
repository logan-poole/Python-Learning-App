# Created by Logan Poole - Poole Empire Director
import tkinter as tk
from tkinter import ttk, messagebox

class TkinterElementSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Element Selector")
        self.root.geometry("900x700")  # Expanded window size to accommodate new options

        # Create the main notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Create tabs for different element groups
        self.create_input_widgets_tab()
        self.create_selection_widgets_tab()
        self.create_display_widgets_tab()
        self.create_container_widgets_tab()
        self.create_interactive_widgets_tab()

        # Layout options
        layout_frame = ttk.Frame(self.root)
        layout_frame.pack(pady=10)

        ttk.Label(layout_frame, text="Choose Layout:").grid(row=0, column=0, padx=5)
        self.layout_var = tk.StringVar(value="pack")
        ttk.Combobox(layout_frame, textvariable=self.layout_var, values=["pack", "grid", "place"], state="readonly").grid(row=0, column=1, padx=5)

        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.review_button = tk.Button(button_frame, text="Review Selections", command=self.show_selected_widgets)
        self.review_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear Selections", command=self.clear_selections)
        self.clear_button.grid(row=0, column=1, padx=5)

    def create_input_widgets_tab(self):
        input_widgets_frame = ttk.Frame(self.notebook)
        self.notebook.add(input_widgets_frame, text="Input Widgets")

        self.input_widgets_vars = {}
        input_widgets = ["Entry", "Text", "Spinbox", "Combobox"]

        for i, widget in enumerate(input_widgets):
            var = tk.BooleanVar()
            self.input_widgets_vars[widget] = {
                "var": var,
                "count": tk.IntVar(value=1),
                "callback": tk.StringVar(),
                "width": tk.IntVar(value=10)
            }

            ttk.Checkbutton(input_widgets_frame, text=widget, variable=var).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # Display the actual widget next to the label
            if widget == "Entry":
                tk.Entry(input_widgets_frame).grid(row=i, column=1, padx=5)
            elif widget == "Text":
                tk.Text(input_widgets_frame, height=1, width=15).grid(row=i, column=1, padx=5)
            elif widget == "Spinbox":
                tk.Spinbox(input_widgets_frame, from_=0, to=10).grid(row=i, column=1, padx=5)
            elif widget == "Combobox":
                ttk.Combobox(input_widgets_frame, values=["Option 1", "Option 2", "Option 3"]).grid(row=i, column=1, padx=5)

            # Add Spinbox for quantity
            ttk.Label(input_widgets_frame, text="Quantity:").grid(row=i, column=2, padx=5)
            tk.Spinbox(input_widgets_frame, from_=1, to=10, textvariable=self.input_widgets_vars[widget]["count"]).grid(row=i, column=3, padx=5)

            # Add entry for function callback
            ttk.Label(input_widgets_frame, text="Function:").grid(row=i, column=4, padx=5)
            tk.Entry(input_widgets_frame, textvariable=self.input_widgets_vars[widget]["callback"]).grid(row=i, column=5, padx=5)

            # Add width option
            ttk.Label(input_widgets_frame, text="Width:").grid(row=i, column=6, padx=5)
            tk.Spinbox(input_widgets_frame, from_=1, to=50, textvariable=self.input_widgets_vars[widget]["width"]).grid(row=i, column=7, padx=5)

    def create_selection_widgets_tab(self):
        selection_widgets_frame = ttk.Frame(self.notebook)
        self.notebook.add(selection_widgets_frame, text="Selection Widgets")

        self.selection_widgets_vars = {}
        selection_widgets = ["Button", "Checkbutton", "Radiobutton", "Scale", "Listbox"]

        for i, widget in enumerate(selection_widgets):
            var = tk.BooleanVar()
            self.selection_widgets_vars[widget] = {
                "var": var,
                "count": tk.IntVar(value=1),
                "callback": tk.StringVar(),
                "width": tk.IntVar(value=10)
            }

            ttk.Checkbutton(selection_widgets_frame, text=widget, variable=var).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # Display the actual widget next to the label
            if widget == "Button":
                tk.Button(selection_widgets_frame, text="Button").grid(row=i, column=1, padx=5)
            elif widget == "Checkbutton":
                tk.Checkbutton(selection_widgets_frame, text="Checkbutton").grid(row=i, column=1, padx=5)
            elif widget == "Radiobutton":
                tk.Radiobutton(selection_widgets_frame, text="Option 1").grid(row=i, column=1, padx=5)
            elif widget == "Scale":
                tk.Scale(selection_widgets_frame, from_=0, to=100).grid(row=i, column=1, padx=5)
            elif widget == "Listbox":
                tk.Listbox(selection_widgets_frame, height=3).grid(row=i, column=1, padx=5)

            # Add Spinbox for quantity
            ttk.Label(selection_widgets_frame, text="Quantity:").grid(row=i, column=2, padx=5)
            tk.Spinbox(selection_widgets_frame, from_=1, to=10, textvariable=self.selection_widgets_vars[widget]["count"]).grid(row=i, column=3, padx=5)

            # Add entry for function callback
            ttk.Label(selection_widgets_frame, text="Function:").grid(row=i, column=4, padx=5)
            tk.Entry(selection_widgets_frame, textvariable=self.selection_widgets_vars[widget]["callback"]).grid(row=i, column=5, padx=5)

            # Add width option
            ttk.Label(selection_widgets_frame, text="Width:").grid(row=i, column=6, padx=5)
            tk.Spinbox(selection_widgets_frame, from_=1, to=50, textvariable=self.selection_widgets_vars[widget]["width"]).grid(row=i, column=7, padx=5)

    def create_display_widgets_tab(self):
        display_widgets_frame = ttk.Frame(self.notebook)
        self.notebook.add(display_widgets_frame, text="Display Widgets")

        self.display_widgets_vars = {}
        display_widgets = ["Label", "Message", "Canvas"]

        for i, widget in enumerate(display_widgets):
            var = tk.BooleanVar()
            self.display_widgets_vars[widget] = {
                "var": var,
                "count": tk.IntVar(value=1),
                "callback": tk.StringVar(),
                "width": tk.IntVar(value=10)
            }

            ttk.Checkbutton(display_widgets_frame, text=widget, variable=var).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # Display the actual widget next to the label
            if widget == "Label":
                tk.Label(display_widgets_frame, text="Label").grid(row=i, column=1, padx=5)
            elif widget == "Message":
                tk.Message(display_widgets_frame, text="Message content").grid(row=i, column=1, padx=5)
            elif widget == "Canvas":
                tk.Canvas(display_widgets_frame, width=100, height=50).grid(row=i, column=1, padx=5)

            # Add Spinbox for quantity
            ttk.Label(display_widgets_frame, text="Quantity:").grid(row=i, column=2, padx=5)
            tk.Spinbox(display_widgets_frame, from_=1, to=10, textvariable=self.display_widgets_vars[widget]["count"]).grid(row=i, column=3, padx=5)

            # Add entry for function callback
            ttk.Label(display_widgets_frame, text="Function:").grid(row=i, column=4, padx=5)
            tk.Entry(display_widgets_frame, textvariable=self.display_widgets_vars[widget]["callback"]).grid(row=i, column=5, padx=5)

            # Add width option
            ttk.Label(display_widgets_frame, text="Width:").grid(row=i, column=6, padx=5)
            tk.Spinbox(display_widgets_frame, from_=1, to=50, textvariable=self.display_widgets_vars[widget]["width"]).grid(row=i, column=7, padx=5)

    def create_container_widgets_tab(self):
        container_widgets_frame = ttk.Frame(self.notebook)
        self.notebook.add(container_widgets_frame, text="Container Widgets")

        self.container_widgets_vars = {}
        container_widgets = ["Frame", "LabelFrame", "Toplevel", "PanedWindow"]

        for i, widget in enumerate(container_widgets):
            var = tk.BooleanVar()
            self.container_widgets_vars[widget] = {
                "var": var,
                "count": tk.IntVar(value=1),
                "callback": tk.StringVar(),
                "width": tk.IntVar(value=10)
            }

            ttk.Checkbutton(container_widgets_frame, text=widget, variable=var).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # Display the actual widget next to the label
            if widget == "Frame":
                tk.Frame(container_widgets_frame, width=100, height=50, relief="sunken", borderwidth=2).grid(row=i, column=1, padx=5)
            elif widget == "LabelFrame":
                tk.LabelFrame(container_widgets_frame, text="LabelFrame", width=100, height=50).grid(row=i, column=1, padx=5)
            elif widget == "Toplevel":
                tk.Button(container_widgets_frame, text="Toplevel Button").grid(row=i, column=1, padx=5)
            elif widget == "PanedWindow":
                tk.PanedWindow(container_widgets_frame).grid(row=i, column=1, padx=5)

            # Add Spinbox for quantity
            ttk.Label(container_widgets_frame, text="Quantity:").grid(row=i, column=2, padx=5)
            tk.Spinbox(container_widgets_frame, from_=1, to=10, textvariable=self.container_widgets_vars[widget]["count"]).grid(row=i, column=3, padx=5)

            # Add entry for function callback
            ttk.Label(container_widgets_frame, text="Function:").grid(row=i, column=4, padx=5)
            tk.Entry(container_widgets_frame, textvariable=self.container_widgets_vars[widget]["callback"]).grid(row=i, column=5, padx=5)

            # Add width option
            ttk.Label(container_widgets_frame, text="Width:").grid(row=i, column=6, padx=5)
            tk.Spinbox(container_widgets_frame, from_=1, to=50, textvariable=self.container_widgets_vars[widget]["width"]).grid(row=i, column=7, padx=5)

    def create_interactive_widgets_tab(self):
        interactive_widgets_frame = ttk.Frame(self.notebook)
        self.notebook.add(interactive_widgets_frame, text="Interactive Widgets")

        self.interactive_widgets_vars = {}
        interactive_widgets = ["Progressbar", "Scrollbar", "Treeview", "Notebook"]

        for i, widget in enumerate(interactive_widgets):
            var = tk.BooleanVar()
            self.interactive_widgets_vars[widget] = {
                "var": var,
                "count": tk.IntVar(value=1),
                "callback": tk.StringVar(),
                "width": tk.IntVar(value=10)
            }

            ttk.Checkbutton(interactive_widgets_frame, text=widget, variable=var).grid(row=i, column=0, padx=5, pady=5, sticky="w")

            # Display the actual widget next to the label
            if widget == "Progressbar":
                ttk.Progressbar(interactive_widgets_frame, length=100).grid(row=i, column=1, padx=5)
            elif widget == "Scrollbar":
                tk.Scrollbar(interactive_widgets_frame).grid(row=i, column=1, padx=5)
            elif widget == "Treeview":
                ttk.Treeview(interactive_widgets_frame).grid(row=i, column=1, padx=5)
            elif widget == "Notebook":
                ttk.Notebook(interactive_widgets_frame, width=100, height=50).grid(row=i, column=1, padx=5)

            # Add Spinbox for quantity
            ttk.Label(interactive_widgets_frame, text="Quantity:").grid(row=i, column=2, padx=5)
            tk.Spinbox(interactive_widgets_frame, from_=1, to=10, textvariable=self.interactive_widgets_vars[widget]["count"]).grid(row=i, column=3, padx=5)

            # Add entry for function callback
            ttk.Label(interactive_widgets_frame, text="Function:").grid(row=i, column=4, padx=5)
            tk.Entry(interactive_widgets_frame, textvariable=self.interactive_widgets_vars[widget]["callback"]).grid(row=i, column=5, padx=5)

            # Add width option
            ttk.Label(interactive_widgets_frame, text="Width:").grid(row=i, column=6, padx=5)
            tk.Spinbox(interactive_widgets_frame, from_=1, to=50, textvariable=self.interactive_widgets_vars[widget]["width"]).grid(row=i, column=7, padx=5)

    def show_selected_widgets(self):
        selected_window = tk.Toplevel(self.root)
        selected_window.title("Selected Widgets")
        selected_window.geometry("600x700")

        # Textbox to display selected widgets code
        code_display = tk.Text(selected_window, wrap="none")
        code_display.pack(expand=True, fill="both")

        # Add scrollbars
        y_scroll = tk.Scrollbar(selected_window, orient="vertical", command=code_display.yview)
        y_scroll.pack(side="right", fill="y")
        code_display.configure(yscrollcommand=y_scroll.set)

        x_scroll = tk.Scrollbar(selected_window, orient="horizontal", command=code_display.xview)
        x_scroll.pack(side="bottom", fill="x")
        code_display.configure(xscrollcommand=x_scroll.set)

        # Generate code for selected widgets
        code = self.generate_code()
        code_display.insert(tk.END, code)

        # Copy to clipboard button
        copy_button = tk.Button(selected_window, text="Copy to Clipboard", command=lambda: self.copy_to_clipboard(code))
        copy_button.pack(pady=10)

    def generate_code(self):
        code_lines = [
            "# Generated Tkinter Code",
            "import tkinter as tk",
            "from tkinter import ttk",
            "",
            "def main():",
            "    root = tk.Tk()",
            "    root.title('Generated Tkinter App')",
            "    root.geometry('800x600')",
            "",
            "    # Create widgets"
        ]

        # Input Widgets
        if any(values["var"].get() for values in self.input_widgets_vars.values()):
            code_lines.append("\n    # Input Widgets")
            for widget, values in self.input_widgets_vars.items():
                if values["var"].get():
                    count = values["count"].get()
                    callback = values["callback"].get() or "None"
                    width = values["width"].get()
                    for n in range(1, count + 1):
                        var_name = f"{widget.lower()}{n}"
                        if widget == "Entry":
                            code_lines.append(f"    {var_name} = tk.Entry(root, width={width})")
                        elif widget == "Text":
                            code_lines.append(f"    {var_name} = tk.Text(root, height=2, width={width})")
                        elif widget == "Spinbox":
                            code_lines.append(f"    {var_name} = tk.Spinbox(root, from_=0, to=10, width={width})")
                        elif widget == "Combobox":
                            code_lines.append(f"    {var_name} = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'], width={width})")
                        # Apply layout
                        code_lines.append(f"    {var_name}.{self.layout_var.get()}()\n")

        # Selection Widgets
        if any(values["var"].get() for values in self.selection_widgets_vars.values()):
            code_lines.append("\n    # Selection Widgets")
            for widget, values in self.selection_widgets_vars.items():
                if values["var"].get():
                    count = values["count"].get()
                    callback = values["callback"].get() or "None"
                    width = values["width"].get()
                    for n in range(1, count + 1):
                        var_name = f"{widget.lower()}{n}"
                        if widget == "Button":
                            code_lines.append(f"    {var_name} = tk.Button(root, text='Button', command={callback})")
                        elif widget == "Checkbutton":
                            code_lines.append(f"    {var_name} = tk.Checkbutton(root, text='Checkbutton')")
                        elif widget == "Radiobutton":
                            code_lines.append(f"    {var_name} = tk.Radiobutton(root, text='Option 1')")
                        elif widget == "Scale":
                            code_lines.append(f"    {var_name} = tk.Scale(root, from_=0, to=100)")
                        elif widget == "Listbox":
                            code_lines.append(f"    {var_name} = tk.Listbox(root, height=3)")
                        # Apply layout
                        code_lines.append(f"    {var_name}.{self.layout_var.get()}()\n")

        # Display Widgets
        if any(values["var"].get() for values in self.display_widgets_vars.values()):
            code_lines.append("\n    # Display Widgets")
            for widget, values in self.display_widgets_vars.items():
                if values["var"].get():
                    count = values["count"].get()
                    callback = values["callback"].get() or "None"  # Not typically used for display widgets
                    width = values["width"].get()
                    for n in range(1, count + 1):
                        var_name = f"{widget.lower()}{n}"
                        if widget == "Label":
                            code_lines.append(f"    {var_name} = tk.Label(root, text='Label')")
                        elif widget == "Message":
                            code_lines.append(f"    {var_name} = tk.Message(root, text='Message content', width={width*10})")
                        elif widget == "Canvas":
                            code_lines.append(f"    {var_name} = tk.Canvas(root, width=100, height=50)")
                        # Apply layout
                        code_lines.append(f"    {var_name}.{self.layout_var.get()}()\n")

        # Container Widgets
        if any(values["var"].get() for values in self.container_widgets_vars.values()):
            code_lines.append("\n    # Container Widgets")
            for widget, values in self.container_widgets_vars.items():
                if values["var"].get():
                    count = values["count"].get()
                    callback = values["callback"].get() or "None"  # Not typically used for container widgets
                    width = values["width"].get()
                    for n in range(1, count + 1):
                        var_name = f"{widget.lower()}{n}"
                        if widget == "Frame":
                            code_lines.append(f"    {var_name} = tk.Frame(root, width=100, height=50, relief='sunken', borderwidth=2)")
                        elif widget == "LabelFrame":
                            code_lines.append(f"    {var_name} = tk.LabelFrame(root, text='LabelFrame', width=100, height=50)")
                        elif widget == "Toplevel":
                            code_lines.append(f"    {var_name} = tk.Toplevel(root)")
                        elif widget == "PanedWindow":
                            code_lines.append(f"    {var_name} = tk.PanedWindow(root)")
                        # Apply layout
                        code_lines.append(f"    {var_name}.{self.layout_var.get()}()\n")

        # Interactive Widgets
        if any(values["var"].get() for values in self.interactive_widgets_vars.values()):
            code_lines.append("\n    # Interactive Widgets")
            for widget, values in self.interactive_widgets_vars.items():
                if values["var"].get():
                    count = values["count"].get()
                    callback = values["callback"].get() or "None"  # Not typically used for some interactive widgets
                    width = values["width"].get()
                    for n in range(1, count + 1):
                        var_name = f"{widget.lower()}{n}"
                        if widget == "Progressbar":
                            code_lines.append(f"    {var_name} = ttk.Progressbar(root, length=100)")
                        elif widget == "Scrollbar":
                            code_lines.append(f"    {var_name} = tk.Scrollbar(root)")
                        elif widget == "Treeview":
                            code_lines.append(f"    {var_name} = ttk.Treeview(root)")
                        elif widget == "Notebook":
                            code_lines.append(f"    {var_name} = ttk.Notebook(root, width=100, height=50)")
                        # Apply layout
                        code_lines.append(f"    {var_name}.{self.layout_var.get()}()\n")

        # Finalize the code with mainloop
        code_lines.append("\n    root.mainloop()\n")
        code_lines.append("\nif __name__ == '__main__':")
        code_lines.append("    main()")

        # Join all lines into a single string
        generated_code = "\n".join(code_lines)
        return generated_code

    def copy_to_clipboard(self, code):
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("Copied", "Code copied to clipboard!")

    def clear_selections(self):
        for widget_dict in [self.input_widgets_vars, self.selection_widgets_vars, self.display_widgets_vars, self.container_widgets_vars, self.interactive_widgets_vars]:
            for widget in widget_dict.values():
                widget["var"].set(False)
                widget["count"].set(1)
                widget["callback"].set("")
                widget["width"].set(10)
        self.layout_var.set("pack")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterElementSelectorApp(root)
    root.mainloop()
