import tkinter as tk

def clear(label, number, resul, list):
    print("clear")

def internParen(op_list):
    print("internParen")
    
def result(label, numbers, result, op_list):
    print("result")

def resolve_operations(sub_list):        
    print("resolve_operations")

def comma(label, number, resul, list):
    print("comma")
    
def addSub(label, number, list):                     
    print("addSub")
        
def addSum(label, number, list):      
    print("addSum")
      
def addMul(label, number, list):
    print("addMul")

def addDiv(label, number, list):
    print("addDiv")

def addParenthesesLeft(label, number, list):
    print("addParenthesesLeft")

def addParenthesesRight(label, number, list):
    print("addParenthesesRight")

def add0(label, number, resul, list):
    print("add0")

def add1(label, number, resul, list):
    print("add1")

def add2(label, number, resul, list):
    print("add2")

def add3(label, number, resul, list):
    print("add3")

def add4(label, number, resul, list):
    print("add4")

def add5(label, number, resul, list):
    print("add5")

def add6(label, number, resul, list):
    print("add6")

def add7(label, number, resul, list):
    print("add7")

def add8(label, number, resul, list):
    print("add8")

def add9(label, number, resul, list):  
    print("add9")

def main():
    number = []  
    list = []
    resul = []
    
    window = tk.Tk()
    window.title("Calculadora Simples")

    label = tk.Label(window, pady=50, font="Arial, 16", justify="right")
    label.grid(row=0, column=0, columnspan=10, pady=5, padx=0)
    
    buttonC = tk.Button(window, text="C", padx=30, pady=20, command=lambda: clear(label, number, resul, list), foreground="green", borderwidth=4)
    buttonC.grid(row=1, column=0, padx=5, pady=5)

    buttonDiv = tk.Button(window, text="÷", padx=30, pady=20, command=lambda: addDiv(label, number, list), foreground="green", borderwidth=4)
    buttonDiv.grid(row=1, column=4, padx=5, pady=5)

    button7 = tk.Button(window, text="7", padx=30, pady=20, command=lambda: add7(label, number, resul, list), borderwidth=4)
    button7.grid(row=2, column=0, pady=5, padx=5)

    button8 = tk.Button(window, text="8", padx=30, pady=20, command=lambda: add8(label, number, resul, list), borderwidth=4)
    button8.grid(row=2, column=1, pady=5, padx=5)

    button9 = tk.Button(window, text="9", padx=30, pady=20, command=lambda: add9(label, number, resul, list), borderwidth=4)
    button9.grid(row=2, column=2, pady=5, padx=5)

    buttonMul = tk.Button(window, text="X", padx=30, pady=20, command=lambda: addMul(label, number, list), foreground="green", borderwidth=4)
    buttonMul.grid(row=2, column=4, padx=5,pady=5)

    button4 = tk.Button(window, text="4", padx=30, pady=20, command=lambda: add4(label, number, resul, list), borderwidth=4)
    button4.grid(row=3, column=0, pady=5, padx=5)

    button5 = tk.Button(window, text="5", padx=30, pady=20, command=lambda: add5(label, number, resul, list), borderwidth=4)
    button5.grid(row=3, column=1, pady=5, padx=5)

    button6 = tk.Button(window, text="6", padx=30, pady=20, command=lambda: add6(label, number, resul, list), borderwidth=4)
    button6.grid(row=3, column=2, pady=5, padx=5)

    buttonSub = tk.Button(window, text="-", padx=30, pady=20, command=lambda: addSub(label, number, list), foreground="green", borderwidth=4)
    buttonSub.grid(row=3, column=4, padx=5,pady=5)

    button1 = tk.Button(window, text="1", padx=30, pady=20, command=lambda: add1(label, number, resul, list), borderwidth=4)
    button1.grid(row=4, column=0, pady=5, padx=5)

    button2 = tk.Button(window, text="2", padx=30, pady=20, command=lambda: add2(label, number, resul, list), borderwidth=4)
    button2.grid(row=4, column=1, pady=5, padx=5)

    button3 = tk.Button(window, text="3", padx=30, pady=20, command=lambda: add3(label, number, resul, list), borderwidth=4)
    button3.grid(row=4, column=2, pady=5, padx=5)

    buttonSum = tk.Button(window, text="+", padx=30, pady=20, command=lambda: addSum(label, number, list), foreground="green", borderwidth=4)
    buttonSum.grid(row=4, column=4, padx=5,pady=5)
    
    buttonParenLeft = tk.Button(window, text="(", padx=30, command=lambda: addParenthesesLeft(label, number, list), pady=20,foreground="green", borderwidth=4)
    buttonParenLeft.grid(row=1, column=1, padx=5, pady=5)
    
    buttonParenRight = tk.Button(window, text=")", padx=30, command=lambda: addParenthesesRight(label, number, list), pady=20,foreground="green", borderwidth=4)
    buttonParenRight.grid(row=1, column=2, padx=5, pady=5)

    button0 = tk.Button(window, text="0", padx=30, pady=20, command=lambda: add0(label, number, resul, list), borderwidth=4)
    button0.grid(row=5, column=1, pady=5, padx=5)

    buttonComma = tk.Button(window, text=",", padx=30, pady=20, command=lambda: comma(label, number, resul, list), foreground="green", borderwidth=4)
    buttonComma.grid(row=5, column=2, pady=5, padx=5)

    buttonResul = tk.Button(window, text="=", padx=30, pady=20, command=lambda: result(label, number, resul, list), foreground="green", borderwidth=4)
    buttonResul.grid(row=5, column=4, padx=5,pady=5)
        
    window.geometry("360x530")
    window.resizable(False, False)

    window.mainloop()

if __name__=="__main__":
    main()