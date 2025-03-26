import turtle as t

def DrawPolygon(dis, n):
    for i in range(n):
        t.forward(dis)
        t.left(360/n)
    t.done()

#DrawPolygon(100, 5)
DrawPolygon(100, 6)
#DrawPolygon(100, 7)
#DrawPolygon(100, 8)
