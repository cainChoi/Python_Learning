import turtle as t
n = 50
t.color('green')
t.speed(0)
for x in range(n):
    t.circle(80)    #원은 중심점이 기준이 아님.
    t.left(360/n)
t.done()