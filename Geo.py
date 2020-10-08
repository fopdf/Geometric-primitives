import graphics as gr

class Geo:
 
 def prim():
    win = gr.GraphWin("Прямоугольник", 300, 300)
    obj = gr.Rectangle(gr.Point(50, 50), gr.Point(200, 250))
    obj.draw(win)
    win.getMouse()
    win.close()
 def krug():
    win = gr.GraphWin("Круг", 400, 400)
    obj = gr.Circle(gr.Point(200, 200), 50)
    obj.draw(win)
    win.getMouse()
    win.close()
 def elip():
    win = gr.GraphWin("Эллипс", 300, 300)
    obj = gr.Oval(gr.Point(100, 100), gr.Point(250, 200))
    obj.draw(win)
    win.getMouse()
    win.close()







