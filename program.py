
import time
from tkinter import *
root = Tk()


def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(1000, timing)

clock=Label(root, font=("times",6,"bold"))
clock.place(x = 850, y = 70)
timing()
   
def cicle_t(event):
	T = float(ent_4.get())
	n = float(ent_3.get())
	if n > 0:
		c = T * 3600 / n
		lab_answer = Label(root, text = f'Цикл детали :  {c:.1f} сек')
		lab_answer.place(x = 50, y = 100)

def total_time(event):
	c = float(ent_1.get())
	n = float(ent_3.get())
	T = c * n / 3600
	lab_answer = Label(root, text = f'Общее врямя производства :  {T:.1f} ч')
	lab_answer.place(x = 50, y = 200)

def part_one(event):
	T = float(ent_4.get())
	c = float(ent_1.get())
	if c > 0:
		n = T * 3600 / c
		lab_answer = Label(root, text = f'Количество деталей {n:.0f} шт ')
		lab_answer.place(x = 50 , y = 300)

def total_massa(event):
	m = float(ent_5.get())
	n = float(ent_3.get())
	M = m * n / 1000
	lab_answer = Label(root, text = f'Количество материала  {M:.0f}  кг')
	lab_answer.place(x = 50 , y = 400)

def part_weight(event):
	M = float(ent_2.get())
	n = float(ent_3.get())
	if n > 0:
		m = M * 1000 / n
		lab_answer = Label(root, text = f'Вес одной деталей {m:.0f} гр ')
		lab_answer.place(x = 50 , y = 500)

def part_two(event):
	M = float(ent_2.get())
	m = float(ent_5.get())
	if m > 0:
		n = M * 1000 / m
		lab_answer = Label(root, text = f'Количество деталей {n:.0f} шт')
		lab_answer.place(x = 50, y = 600)

def container(event):
	N = float(ent_3.get())
	p = float(ent_6.get())
	if p > 0:
		count = N / p
		lab_answer = Label(root, text = f'Тара  {count:.0f} шт')
		lab_answer.place(x = 50, y = 700)

lab = Label(root, text =  'Производственный калькулятор')
lab.pack()

ent_1 = Entry(root, width = 6 , font = (' ' , 8))
ent_1.place(x = 740, y = 1200)
leb_cicle = Label(root, text = 'Цикл одной детали  ')
leb_cicle.place(x = 10, y = 1200)
leb_c = Label(root, text = 'сек.')
leb_c.place(x = 930, y = 1200)

ent_2 = Entry(root, width = 6 , font = (' ' , 8))
ent_2.place(x = 740, y = 1400)
leb_weight = Label(root, text = 'Масса материала  ')
leb_weight.place(x = 10, y = 1400)
leb_m = Label(root, text = 'кг.')
leb_m.place(x = 930, y = 1400)

ent_3 = Entry(root, width = 6 , font = (' ' , 8))
ent_3.place(x = 740, y = 1300)
leb_part = Label(root, text = 'Количество деталей ')
leb_part.place(x = 10, y = 1300)
leb_n = Label(root, text = 'шт.')
leb_n.place(x = 930, y = 1300)

ent_4 = Entry(root, width = 6 , font = (' ' , 8))
ent_4.place(x = 740, y = 1100)
leb_time = Label(root, text = 'Время производства  ')
leb_time.place(x = 10, y = 1100)
leb_t = Label(root, text = 'ч.м')
leb_t.place(x = 930, y = 1100)

ent_5 = Entry(root, width = 6 , font = (' ' , 8))
ent_5.place(x = 740, y = 1500)
leb_massa= Label(root, text = 'Вес одной детали ')
leb_massa.place(x = 10, y = 1500)
leb_gr = Label(root, text = 'гр.')
leb_gr.place(x = 930, y = 1500)

ent_6 = Entry(root, width = 6 , font = (' ' , 8))
ent_6.place(x = 740, y = 1600)
leb_cont= Label(root, text = 'В упаковке ')
leb_cont.place(x = 10, y = 1600)
leb_pcs = Label(root, text = 'шт.')
leb_pcs.place(x = 930, y = 1600)

btn_cicle = Button(root,  text ='цикл  T/n' , width = 10 , height = 1 , bg = 'white' , fg = 'black')
btn_massa = Button(root, text = 'Масса  m * n', width = 10 , height = 1 , bg = 'white', fg = 'black')
btn_part = Button(root, text = 'кол - во  T/c', width = 9 , height = 1 , bg = 'white', fg = 'black')
btn_time = Button(root, text = 'Время  c * n', width = 10,  height = 1 , bg = 'white', fg = 'black')
btn_weight = Button(root, text = 'вес  M/n', width = 10,  height = 1 , bg = 'white', fg = 'black')
btn_namb = Button(root, text = 'кол - во M/m', width = 9, height = 1, bg = 'white', fg = 'black')
btn_enter = Button(root, text = 'Ввод', width = 9, height = 1, bg = 'green', fg = 'black')
btn_clear = Button(root, text = 'Очистить', width = 9, height = 1, bg = 'red', fg = 'black')
btn_cont = Button(root, text = 'Tapa.    n / p', width = 10, height = 1, bg = 'white', fg = 'black')


btn_cicle.bind('<ButtonPress>', cicle_t)
btn_time.bind('<ButtonPress>', total_time)
btn_part.bind('<ButtonPress>', part_one)
btn_massa.bind('<ButtonPress>', total_massa)
btn_weight.bind('<ButtonPress>',  part_weight)
btn_namb.bind('<ButtonPress>', part_two)
btn_cont.bind('<ButtonPress>', container)

btn_cicle.place(x =378, y =1700 )
btn_massa.place(x = 15, y = 1800)
btn_part.place(x = 740, y = 1700)
btn_time.place(x = 15, y = 1700)
btn_weight.place(x = 378, y = 1800)
btn_namb.place(x = 740, y = 1800)
btn_enter.place(x = 740, y = 1900)
btn_clear.place(x = 740, y = 2000)
btn_cont.place(x = 15, y = 1900)






root.mainloop()