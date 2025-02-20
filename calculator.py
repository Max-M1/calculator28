import tkinter as tk


class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def add(self, value):
        self.expression += str(value)
        return self.expression

    def clear(self):
        self.expression = ""
        return self.expression

    def calculate(self):
        try:
            result = eval(self.expression)
        except Exception:
            result = "Помилка"
        self.expression = str(result)
        return self.expression


class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("300x400")
        self.controller = None
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 20), justify="right")
        self.entry.pack(fill="both", padx=10, pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(expand=True, fill="both")

        btn_clear = tk.Button(
            self.buttons_frame, text="C", font=("Arial", 18), command=self.on_clear
        )
        btn_clear.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == "=":
                    btn_command = self.on_calculate
                else:
                    btn_command = lambda value=btn_text: self.on_add(value)
                btn = tk.Button(
                    self.buttons_frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=btn_command,
                )
                btn.grid(row=i + 1, column=j, sticky="nsew")

        total_rows = len(buttons) + 1
        total_columns = 4
        for i in range(total_rows):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(total_columns):
            self.buttons_frame.columnconfigure(j, weight=1)

    def on_add(self, value):
        if self.controller:
            self.controller.add_to_expression(value)

    def on_clear(self):
        if self.controller:
            self.controller.clear_entry()

    def on_calculate(self):
        if self.controller:
            self.controller.calculate()

    def update_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)

    def set_controller(self, controller):
        self.controller = controller


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_to_expression(self, value):
        new_expr = self.model.add(value)
        self.view.update_entry(new_expr)

    def clear_entry(self):
        new_expr = self.model.clear()
        self.view.update_entry(new_expr)

    def calculate(self):
        result = self.model.calculate()
        self.view.update_entry(result)


if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.set_controller(controller)
    view.mainloop()
