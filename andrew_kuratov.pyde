x = 0
t = 0
y = 0
bg = 0 
r = 0
flag = 0
# переменная
flag = 0
def setup():
    size(600,400)
    
def draw():
    global bg,r,y,flag,flag2
     # обводка      
    strokeWeight(0)
     # цвет кнопак
    fill(255,255,255)
    # кнопки
    rect(0,50,100,50)
    rect(400,0,100,50)
    rect(300,0,100,50)
    rect(200,0,100,50)
    rect(500,0,100,50)
    rect(100,0,100,50)
    rect(0,0,100,50)
    rect(100,50,100,50)
    # цвет текста
    fill(0)
    # название кнопок
    text(u"больше",230,30)
    text(u"меньше",430,30)
    text(u"цвет",340,30)
    text(u"100 кружочков",510,30)
    text(u"фон",140,30)
    text(u"сохранить",20,30)
    text(u"сбросить всё",15,80)
    text(u"любой фон",118,80)
    fill(255,255,255)
    if mousePressed:
        if r < 0 :
            r = 1
        strokeWeight(r)
        line(mouseX,mouseY,pmouseX,pmouseY)
    if flag == 1:
        strokeWeight(0)
        #палитра
        fill(255,0,0)
        rect(0,350,50,50)
        fill(255,160,16)
        rect(50,350,50,50)
        fill(255,254,32)
        rect(100,350,50,50)
        fill(0,192,0)
        rect(150,350,50,50)
        fill(80,208,255)
        rect(200,350,50,50)
        fill(0,32,255)
        rect(250,350,50,50)
        
        fill(160,32,255)
        rect(300,350,50,50)
        fill(255,96,208)
        rect(350,350,50,50)
        fill(0)
        rect(400,350,50,50)
        fill(255,255,255)
        rect(450,350,50,50)
        fill(255,208,160)
        rect(500,350,50,50)
        fill(160,128,96)
        rect(550,350,50,50)
      #условия  
def mouseClicked():
    global bg,r,t, flag
    if mouseX > 200 and mouseX < 300 and mouseY > 0 and mouseY < 50:
        r = r + 10
    
    if mouseX > 400 and mouseX < 500 and mouseY > 0 and mouseY < 50:
        r = r - 10
        
    if mouseX > 500 and mouseX < 600 and mouseY > 0 and mouseY < 50:
       for i in range(100):
           point(random(0,600),random(0,400))
           
    if mouseX > 100 and mouseX < 200 and mouseY > 0 and mouseY < 50:
       for x in range(0,650,50):
           for t in range(0,450,50):
               fill(random(0,255),random(0,255),random(0,255))
               ellipse(x,t,50,50)
       x = x + 50
       t = t + 50
    if mouseX  > 0 and mouseX < 100 and mouseY > 0  and mouseY < 50:
       save('qwerty.png')
       background(0)
       fill(255,255,255)
       text(u"cтоп",300,300)

    if mouseX > 0 and mouseX < 100 and mouseY > 50 and mouseY < 100:
       background(200,200,200)
    if mouseX > 100 and mouseX < 200 and mouseY > 50 and mouseY < 100:
       background(random(0,255),random(0,255),random(0,255))
    if mouseX > 0 and mouseX < 50 and mouseY > 350 and mouseY < 400:
       stroke(255,0,0)
    if mouseX > 50 and mouseX < 100 and mouseY > 350 and mouseY < 400:
       stroke(255,160,16)
    if mouseX > 100 and mouseX < 150 and mouseY > 350 and mouseY < 400:
       stroke(255,254,32)
    if mouseX > 150 and mouseX < 200 and mouseY > 350 and mouseY < 400:
       stroke(0,192,0)
    if mouseX > 200 and mouseX < 250 and mouseY > 350 and mouseY < 400:
       stroke(80,208,255)
    if mouseX > 250 and mouseX < 300 and mouseY > 350 and mouseY < 400:
       stroke(0,32,255)
    if mouseX > 300 and mouseX < 350 and mouseY > 350 and mouseY < 400:
       stroke(160,32,255)
    if mouseX > 350 and mouseX < 400 and mouseY > 350 and mouseY < 400:
       stroke(255,96,208)
    if mouseX > 400 and mouseX < 450 and mouseY > 350 and mouseY < 400:
       stroke(0)
    if mouseX > 450 and mouseX < 500 and mouseY > 350 and mouseY < 400:
       stroke(255,255,255)
    if mouseX > 500 and mouseX < 550 and mouseY > 350 and mouseY < 400:
       stroke(255,208,160)
    if mouseX > 550 and mouseX < 600 and mouseY > 350 and mouseY < 400:
       stroke(160,128,96)
    if mouseX > 300 and mouseX < 400 and mouseY > 0 and mouseY < 50:
       flag = 1 
