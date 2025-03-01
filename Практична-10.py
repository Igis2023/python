from tkinter import*
import matplotlib.pyplot as plt

month= ['січень', 'лютий', 'березень', 'квітень', 'травень', 'червень', 'липень', 'серпень', 'вересень', 'жовтень', 'листопад', 'грудень']
mas = [54, 12, 30, 15, 40, 32, 10, 30, 46, 60, 56, 38]



root = Tk()

def btn1_cl():
    s = sum(mas)
    box1.insert(END, "Кількість за рік = "+str(s))
    a = month[mas.index(min(mas))]
    box1.insert(END, "Найменше за рік = "+str(a))
    b = month[mas.index(max(mas))]
    box1.insert(END, "Найбільше за рік = "+str(b))
    k = 0
    for i in range(len(mas)):
        if mas[i] < 40:
            k = k+1
            box1.insert(END, month[i])
    box1.insert(END, "Кількість місяців до 40 мм = "+str(k))

def btn2_cl():
    plt.title('Середньодобова температура за тиждень')
    plt.xlabel('Дні тижня', color = 'gray')
    plt.ylabel('Середньодобова температура', color = 'gray')
    plt.grid(True)
    plt.plot(month, mas, 'r')
    plt.show()

list_1=[]
for i in range (12):
    list_1.append(Label(text = month[i], bg = 'lightblue', width = 7))
    list_1[i].grid(row = 0, column = i, padx = 2, pady = 2)

list_2=[]
for i in range (12):
    list_2.append(Label(text = mas[i], bg = 'lightblue', width = 7))
    list_2[i].grid(row = 1, column = i, padx = 2, pady = 2)

btn1=Button(text='Опрацювати дані', width= 13, height=4, command=btn1_cl)
btn1.grid(row=2, column = 1, padx = 2, pady= 2)

btn2=Button(text='Графік', width= 13, height=4, command=btn2_cl)
btn2.grid(row=3, column = 1, padx = 2, pady= 2)

box1=Listbox(width=50)
box1.grid(row = 3, column = 4, rowspan = 5, columnspan = 5)


root.mainloop()