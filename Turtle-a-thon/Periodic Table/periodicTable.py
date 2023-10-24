# Program to display periodic table
import csv
from tkinter import *
import hovering as ho

with open('data.csv', 'r') as d:
    td = list(csv.reader(d))
    data, lan = [], []
    for i in td[1:]:
        if i[-3] != '':
            data.append(i)
        else:
            lan.append(i)
    g1 = []
    for k in range(19):
        for j in data:
            if int(j[-3]) == k:
                g1.append(j)

root = Tk()
root.config(bg='#A5C9BC')
root.title('Periodic Table')

# Centering the window
root_h, root_w = 710, 1200
s_w = root.winfo_screenwidth()
s_h = root.winfo_screenheight()
x_co = int((s_w / 2) - (root_w / 2))
y_co = int((s_h / 2) - (root_h / 2))
root.geometry("{}x{}+{}+{}".format(root_w, root_h, x_co, y_co))


def elements_display(ele_sym: str, ele_name: str, at_no: int, at_mass: float, button_obj):
    ho.create_tool_tip(button_obj, f'Element Symbol: {ele_sym}\nElement Name: {ele_name}\nAtomic Number: {at_no}'
                                   f'\nAtomic Mass: {at_mass}')


def ele_7(ele_list, x_, color):
    for a in range(7):
        du = ele_list[a]
        bu_7 = Button(root, text=du[0], height=4, width=8, bg=color, relief='groove', font=('Times New Roman', 10))
        bu_7.place(x=x_, y=40 + a * 70)
        elements_display(du[0], du[1], du[2], du[3], bu_7)


def ele_6(ele_list, x_, color):
    for a in range(6):
        du = ele_list[a]
        bu_6 = Button(root, text=du[0], height=4, width=8, bg=color, relief='groove', font=('Times New Roman', 10))
        bu_6.place(x=x_, y=110 + a * 70)
        elements_display(du[0], du[1], du[2], du[3], bu_6)


def ele_4(ele_list, x_):
    for a in range(4):
        du = ele_list[a]
        bu_4 = Button(root, text=du[0], height=4, width=8, bg='#EEE3BC', relief='groove',
                      font=('Times New Roman', 10))
        bu_4.place(x=x_, y=250 + a * 70)
        elements_display(du[0], du[1], du[2], du[3], bu_4)


def lan_act(ele, y_):
    for t in range(14):
        fe = ele[t]
        bu_la = Button(root, text=fe[0], height=4, width=8, bg='#8287B4', relief='groove', font=('Times New Roman', 10))
        bu_la.place(x=135 + t * 66, y=y_)
        elements_display(fe[0], fe[1], fe[2], fe[3], bu_la)


ele_7(g1[:7], 3, '#507F9B')
ele_6(g1[7:13], 69, '#507F9B')

for y in range(10):
    ele_4(g1[13 + (4 * y):17 + (4 * y)], 135 + (66 * y))

for z in range(5):
    ele_6(g1[53 + (6 * z):59 + (6 * z)], 795 + (66 * z), '#89B6E4')

ele_7(g1[83:90], 1125, '#89B6E4')
lan_act(lan[:14], 545)
lan_act(lan[14:], 615)

exit_bu = Button(root, text='Exit', command=root.destroy, bg='red', fg='yellow', relief='groove',
                 font=('Times New Roman', 10))
exit_bu.place(x=1100, y=600)
ho.create_tool_tip(exit_bu, "Closes the window")
root.mainloop()
