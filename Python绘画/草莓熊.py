#-*- coding: UTF-8 -*-
import turtle as t
 
"""
=================================================
@Project ->Adversity Awake 草莓熊系列
@类别     : 草莓熊->草莓熊之2
@Author  : 逆境清醒
@Date    : 2022/9/30 3:02
@Desc    :https://blog.csdn.net/weixin_69553582
=================================================
"""
# 设置背景颜色，窗口位置以及大小
 
t.colormode(255)# 颜色模式
t.speed(0)
t.screensize(850,760,"white")#画布大小背景颜色
t.setup(width=850, height=760,startx=None, starty=None) #绘图窗口的大小和起始坐标
#t.bgpic("di_800.gif")
t.title("阿杜草莓熊！")#设置绘图窗口的标题
t.resizemode('noresize')  #大小调整模式:auto,user,noresize
t.tracer(1)   
 
 
 
scolor=["#E6005C","#00BFFF","#538a30","#F28500"]   # 深色列表
qcolor=["#FF007F","#87CEFA","#7fbc2b","#FFA500"]  # 浅色列表
blsize=80                     # blsize值，blsize，是大等腰直角三角形的斜边风车等比例缩放
bs=2**0.5/2*blsize             # bs是直角边，2**0.5 表示数学中的“根号2”
# zjsjxxb是小等腰直角三角形的斜边，zjb是直角边
zjb=blsize/2 # zjb是小等腰直角三角形的直角边
zjsjxxb=2**0.5 *zjb  # zjsjxxb是小等腰直角三角形的斜边
length=1.7*blsize # 风车杆长
width=2/15*blsize # 风车杆宽
 
def fongche():#风车 
    t.penup()
    t.goto(-205,-42)
    t.begin_fill()
    t.pensize(4)
    t.pencolor("#321320")
    t.fillcolor("#D2B48C")
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(-220,80)
    t.pendown()
    t.setheading(-90)
    t.pensize(width)
    t.pencolor("#5f4a1d")
    t.forward(length)
    t.pensize(2)
    t.backward(length)
    t.setheading(90)
    
    for i in range(4):
        # 小等腰直角三角形
        t.color(scolor[i])  # 遍历深色列表scolor
        t.begin_fill()
        t.forward(zjb)
        t.left(90)
        t.forward(zjb)
        t.left(135)
        t.forward(zjsjxxb)
        t.end_fill()
        #t.pencolor(scolor[i])
        #t.pensize(4)
 
        # 大等腰直角三角形
        t.color(qcolor[i])  # 遍历浅色列表qcolor
        t.begin_fill()
        t.backward(zjsjxxb)
        t.right(90)
        t.forward(bs)
        t.left(135)
        t.forward(blsize)
        t.end_fill()
        #t.pencolor(scolor[i])
        #t.pensize(4)
 
        # 旋转180度后，画下一片风车叶片
        t.right(180)
        t.penup()
 
mling_circle_list = iter([  # 每段弧线（半径，弧角度数）
    (18, 360), (14, 360), (10, 360), (6, 360),
    (18, 360), (14, 360), (10, 360), (6, 360),
])
 
 
def mling_draw_eyeball(zb1,zb2,zb3,zb4):  
    for zb, color_ in zip([zb1,zb2,zb3,zb4], ['#ffffff', '#482d08', '#000000', '#ffffff']):
        t.penup()
        t.goto(*zb)
        t.pendown()
        t.begin_fill()
        t.setheading(0)
        t.color(color_)
        t.pencolor('#000000')
        t.pensize(2)
        t.circle(*next(mling_circle_list))
        t.end_fill()
 
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#cb3263")
t.pensize(4)
t.goto(120,110)
t.pendown()
t.begin_fill()
t.goto(200,0)
t.left(-40)
t.circle(-110,105)
t.left(75)
t.goto(170,-110)
t.left(-80)
t.circle(30,40)
t.left(60)
t.circle(-80,70)
t.left(83)
t.circle(-35,95)
t.goto(60,-270)
t.left(-80)
t.circle(-65,70)
t.left(63)
t.circle(35,30)
t.left(130)
t.circle(-65,70)
t.goto(-120,-270)
t.left(-110)
t.circle(-35,80)
t.left(83)
t.circle(-80,50)
t.left(60)
t.circle(-80,60)
t.left(60)
t.circle(30,30)
t.left(20)
t.circle(80,80)
t.left(-105)
t.circle(-70,150)
t.left(50)
t.circle(-170,50)
t.goto(120,110)
#Author:Adversity Awake
t.end_fill()
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#ffffff")
t.pensize(4)
t.goto(90,60)
t.pendown()
t.begin_fill()
t.right(30)
t.circle(-130,360)
t.end_fill()
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#f3d2ad")
t.pensize(4)
t.goto(-250,-55)
t.seth(0)
t.pendown()
t.begin_fill()
t.right(-55)
t.circle(-45,270)
t.goto(-220,-75)
t.goto(-250,-55)
t.end_fill()
 
fongche()
 
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#f3d2ad")
t.pensize(4)
t.goto(185,-90)
t.pendown()
t.begin_fill()
t.right(140)
t.circle(43,95)
t.goto(185,-90)
t.end_fill()
t.penup()
t.seth(0)
t.pencolor('#321320')
t.fillcolor('#cb3263')
t.pensize(4)
t.begin_fill()
t.goto(21,0)
t.pendown()
t.circle(123,134)
t.left(-90)
t.circle(40,185)
t.left(-60)
t.circle(120,60)
t.left(-90)
t.circle(50,200)
t.left(-90)
t.circle(100,100)
t.left(-12)
t.circle(100,40)
t.goto(21,0)
t.penup()
#Author:Adversity Awake
t.end_fill()
t.penup()
t.goto(0, 0)
t.seth(0)
t.pencolor('#321320')
t.fillcolor('#ffffff')
t.pensize(4)
t.begin_fill()
t.goto(-70,210)
t.left(140)
t.pendown()
t.circle(30,200)
t.goto(-70,210)
t.penup()
t.end_fill()
t.penup()
t.goto(0, 0)
t.seth(0)
t.pencolor('#321320')
t.fillcolor('#ffffff')
t.pensize(4)
t.begin_fill()
t.goto(90,220)
t.left(45)
t.pendown()
t.circle(22,200)
t.goto(90,220)
t.penup()
t.end_fill()
t.penup()
t.goto(0, 0)
t.seth(0)
t.pencolor('#321320')
t.fillcolor('#ffffff')
t.pensize(4)
t.begin_fill()
t.left(-98)
t.left(90)
t.goto(18,10)
t.pendown()
t.circle(100,134)
t.left(10)
t.circle(110,30)
t.left(10)
t.circle(160,40)
t.circle(85,40)
t.left(2)
t.circle(95,40)
t.left(5)
t.circle(95,60)
t.goto(18,10)
t.penup()
t.end_fill()
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#8f3a52")
t.pensize(2)
t.goto(25,240)
t.pendown()
t.begin_fill()
t.goto(60,235)
t.left(30)
t.fd(8)
t.left(90)
t.fd(22)
t.circle(90, 8)
t.left(20)
t.circle(90, 8)
t.left(20)
t.circle(90, 20)
t.left(40)
t.circle(50, 20)
t.end_fill()
t.penup()
t.pensize(12)
t.goto(-2,250)
t.pencolor("#4D1F00")
t.fillcolor("#4D1F00")
t.pendown()
t.goto(60,240)
t.end_fill()
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#8f3a52")
t.pensize(2)
t.goto(-55,193)
t.pendown()
t.begin_fill()
t.left(65)
t.circle(-90, 25)
t.goto(-10,230)
t.left(30)
t.fd(8)
t.left(90)
t.fd(18)
t.circle(90, 8)
t.left(20)
t.circle(90, 10)
t.left(40)
t.circle(90, 30)
t.left(30)
t.circle(40, 20)
t.penup()
t.end_fill()
t.pensize(12)
t.goto(-63,195)
t.pencolor("#4D1F00")
t.fillcolor("#4D1F00")
t.pendown()
t.left(100)
t.circle(-85,45)
t.end_fill()
 
mling_draw_eyeball((-20,180), (-23,185), (-25,188), (-30,200)) 
mling_draw_eyeball((30, 193), (27, 200), (25,203), (20,213)) 
 
t.penup()
p = t.home()
t.pencolor("#321320")
t.fillcolor("#8f3a52")
t.pensize(3)
t.goto(25,105)
p = t.pos()
t.pendown()
t.begin_fill()
t.circle(85, 65)
t.left(16)
t.circle(30, 55)
t.left(20)
t.circle(145, 58)
t.left(8)
t.circle(20, 55)
t.left(8)
t.circle(50, 65)
t.left(-5)
t.circle(310, 8)
t.end_fill()
t.penup()
t.goto(0, 0)
t.seth(0)
t.pencolor('#321320')
t.fillcolor('#a93e54')
t.pensize(3)
t.begin_fill()
t.left(-20)
t.goto(9,66)
t.pendown()
t.circle(68,40)
t.left(10)
t.circle(65,40)
t.left(160)
t.circle(-75,85)
t.left(158)
t.circle(48,37)
t.goto(9,66)
t.penup()
t.end_fill()
t.color('#321320')
t.penup()
t.goto(260,60)
t.pendown()
t.write("愿\n阿\n杜\n的\n日\n子\n如\n诗\n如\n画",align="center",font=("黑体",20,"normal"))
t.penup()
t.goto(230,60)
t.pendown()
#t.write("幸\n福\n绕\n行\n\n忧\n愁\n远\n走",align="center",font=("黑体",20,"normal"))
t.penup()
t.goto(290,183)
t.pendown()
t.write("\n杜\n林\n娟\n",align="center",font=("黑体",10,"normal"))
t.hideturtle()
t.done()
 
 