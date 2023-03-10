"""За билетами на премьеру нового мюзикла выстроилась очередь из N человек,
каждый из которых хочет купить 1 билет. На всю очередь работала только одна
касса, поэтому продажа билетов шла очень медленно, приводя «постояльцев»
очереди в отчаяние. Самые сообразительные быстро заметили, что, как правило,
несколько билетов в одни руки кассир продаёт быстрее, чем когда эти же билеты
продаются по одному. Поэтому они предложили нескольким подряд стоящим людям
отдавать деньги первому из них, чтобы он купил билеты на всех.

Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни
руки, поэтому договориться таким образом между собой могли лишь 2 или 3 подряд
стоящих человека.

Известно, что на продажу i-му человеку из очереди одного билета кассир тратит
Ai секунд, на продажу двух билетов — Bi секунд, трех билетов — Ci секунд.
Напишите программу, которая подсчитает минимальное время, за которое могли быть
обслужены все покупатели.

Обратите внимание, что билеты на группу объединившихся людей всегда покупает
первый из них. Также никто в целях ускорения не покупает лишних билетов
(то есть билетов, которые никому не нужны).

Формат ввода
На вход программы поступает сначала число N — количество покупателей в очереди
(1 ≤ N ≤ 5000). Далее идет N троек натуральных чисел Ai, Bi, Ci. Каждое из этих
чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.

Формат вывода
Требуется вывести одно число — минимальное время в секундах, за которое могли
быть обслужены все покупатели.

Пример
Ввод	    Вывод
5
5 10 15
2 10 15
5 5 5
20 20 1
20 1 1      12"""


n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
a = [p[i][0] for i in range(len(p))]
b = [p[i][1] for i in range(len(p))]
c = [p[i][2] for i in range(len(p))]
d = [0] * (n+1)
d[1] = a[0]
if n > 1:
    d[2] = min(a[0]+a[1], b[0])
if n > 2:
    d[3] = min(d[2]+a[2], d[1]+b[1], c[0])
for i in range(n+1):
    if i >= 4:
        d[i] = (min(d[i-1]+a[i-1], d[i-2]+b[i-2], d[i-3]+c[i-3]))
print(d[n])