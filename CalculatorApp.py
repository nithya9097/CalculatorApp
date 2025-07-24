import tkinter as tk
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.display.configure(state="normal")
        self.num1 = 0
        self.operator = ""
        self.start_new_number = True
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]
        row = 1
        col = 0
        for text in buttons:
            btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                            command=lambda t=text: self.handle_input(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        # Make rows and columns resize with window
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def handle_input(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
            self.num1 = 0
            self.operator = ""
            self.start_new_number = True
        elif text == "=":
            self.calculate_result()
            self.start_new_number = True
        elif text in "+-*/":
            if self.display.get():
                try:
                    self.num1 = float(self.display.get())
                    self.operator = text
                    self.start_new_number = True
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
        else:
            if self.start_new_number:
                self.display.delete(0, tk.END)
                self.start_new_number = False
            self.display.insert(tk.END, text)

    def calculate_result(self):
        if not self.operator or not self.display.get():
            return
        try:
            num2 = float(self.display.get())
            result = 0
            if self.operator == "+":
                result = self.num1 + num2
            elif self.operator == "-":
                result = self.num1 - num2
            elif self.operator == "*":
                result = self.num1 * num2
            elif self.operator == "/":
                if num2 == 0:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    return
                result = self.num1 / num2

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.operator = ""
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.geometry("300x400")
    root.mainloop()
