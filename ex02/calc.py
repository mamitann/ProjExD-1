import tkinter as tk
import tkinter.messagebox as tkm
import math

def button_click(event):
    btn = event.widget
    num = btn["text"]
    
    

    if num == "=":
        pass
        siki = entry.get() # 数式の文字列
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    elif num == "AC": #表示文字列削除
        entry.delete(0,tk.END)
    elif num == "x^2": #累乗の計算
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        ans = int(siki) * int(siki)
        entry.insert(tk.END,ans)
    elif num == "%": #%表示
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        ans = int(siki) / 100
        entry.insert(tk.END,ans)
    elif num == "10^x": #10の累乗
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        ans = 10 ** int(siki)
        entry.insert(tk.END,ans)
    elif num == "√": #平方根の計算
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        ans = math.sqrt(int(siki))
        entry.insert(tk.END,ans)
    else: 
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        
        entry.insert(tk.END, num)
    

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for num in range(9, -1, -1):
    if num==0:
        c = 2
    button = tk.Button(root, text=f"{num}", width=4, height=1, font=("", 30))
    button.grid(row=r, column=2-c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["+", "-","*","/","=","AC","x^2","10^x","√","%"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("", 30),bg="grey")
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
root.mainloop()

