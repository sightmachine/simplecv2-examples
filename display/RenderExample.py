#!/usr/bin/python
from simplecv import *
from simplecv.core.drawing.layer import DrawingLayer
import os

img = Image("../../sampleimages/color.jpg")
lineL = DrawingLayer((img.width,img.height))
a = (20,20)
b = (20,100)
c = (100,100)
d = (100,20)
lineL.line(a,b,alpha=128,width=5)
lineL.line(b,c,alpha=128)
lineL.line(c,d, antialias=True)
lineL.line(d,a,color=Color.PUCE)
lineL.line(a,c,color=Color.PLUM, alpha=52)
lineL.line(b,d,width=5)
img.add_drawing_layer(lineL)
temp = img.apply_layers()
print "line: %s" % temp.save(temp=True)
img.clear_layers()

linesL = DrawingLayer((img.width,img.height))
a = (20,20)
b = (20,100)
c = (100,100)
d = (100,20)
pts = (a,b,c,d,a)
linesL.lines(pts,alpha=128)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
linesL.lines(pts,color=Color.BEIGE,width=10)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
linesL.lines(pts,antialias=True)
img.add_drawing_layer(linesL)
temp = img.apply_layers()
print "lines: %s" % temp.save(temp=True)
img.clear_layers()

rectTR = DrawingLayer((img.width,img.height))
tr = (150,50)
wh = (200,100)
rectTR.rectangle(tr,wh,color=Color.BLUE)
tr = (170,70)
rectTR.rectangle(tr,wh,color=Color.PUCE, width=5)
tr = (190,90)
rectTR.rectangle(tr,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
tr = (210,110)
rectTR.rectangle(tr,wh,color=Color.GREEN,filled=True)
img.add_drawing_layer(rectTR)
temp = img.apply_layers()
print "rectTR: %s" % temp.save(temp=True)
img.clear_layers()

rectC = DrawingLayer((img.width,img.height))
cxy = (img.width/2,img.height/2)
wh = (200,100)
rectC.centered_rectangle(cxy,wh,color=Color.BLUE)
wh = (180,80)
rectC.centered_rectangle(cxy,wh,color=Color.PUCE, width=5)
wh = (160,60)
rectC.centered_rectangle(cxy,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
wh = (140,40)
rectC.centered_rectangle(cxy,wh,color=Color.GREEN,filled=True)
img.add_drawing_layer(rectC)
temp = img.apply_layers()
print "rectC: %s" % temp.save(temp=True)
img.clear_layers()

polyL = DrawingLayer((img.width,img.height))
a = (50,img.height-50)
b = (250,img.height-50)
c = (150,50)
pts = (a,b,c)
polyL.polygon(pts,alpha=128)
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,antialias=True,width=3,alpha=210,filled=True,color=Color.LIME)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,color=Color.BEIGE,width=10)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,antialias=True,width=3,alpha=210)
img.add_drawing_layer(polyL)
temp = img.apply_layers()
print "poly: %s" % temp.save(temp=True)
img.clear_layers()

circleL = DrawingLayer((img.width,img.height))
c = (img.width/2,img.height/2)
r = 150
circleL.circle(c,r,color=Color.RED,filled=True)
r = 130
circleL.circle(c,r,color=Color.ORANGE,alpha=128,filled=True)
r = 110
circleL.circle(c,r,color=Color.YELLOW,alpha=128,width=10)
r = 100
circleL.circle(c,r,color=Color.GREEN)
r = 90
circleL.circle(c,r,color=Color.BLUE,alpha=172)
img.add_drawing_layer(circleL)
temp = img.apply_layers()
print "circle: %s" % temp.save(temp=True)
img.clear_layers()

ellipseL = DrawingLayer((img.width,img.height))
cxy = (img.width/2,img.height/2)
wh = (200,100)
ellipseL.ellipse(cxy,wh,color=Color.BLUE)
wh = (180,80)
ellipseL.ellipse(cxy,wh,color=Color.PUCE, width=5)
wh = (160,60)
ellipseL.ellipse(cxy,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
wh = (140,40)
ellipseL.ellipse(cxy,wh,color=Color.GREEN,filled=True)
img.add_drawing_layer(ellipseL)
temp = img.apply_layers()
print "ellipse: %s" % temp.save(temp=True)
img.clear_layers()

bez = DrawingLayer((img.width,img.height))
a = (20,20)
b = (img.width-20,20)
c = (img.height-20,img.width-20)
d = (20,img.height-20)
e = (img.width/2,img.height/2)
pts = (a,b,c,d,e)
bez.bezier(pts,30)
img.add_drawing_layer(bez)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
bez.bezier(pts,5,color=Color.RED)
img.add_drawing_layer(bez)
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
bez.bezier(pts,30,color=Color.GREEN, alpha=128)
img.add_drawing_layer(bez)
temp = img.apply_layers()
print "bez: %s" % temp.save(temp=True)
img.clear_layers()

words = DrawingLayer((img.width,img.height))
words.set_default_color(Color.RED)
pos = (30,30)
words.set_font_size(30)
words.text("THIS IS BIG",pos)
pos = (50,50)
words.set_font_size(10)
words.text("THIS IS SMALL",pos)
pos = (70,70)
words.set_font_size(20)
words.text("THIS IS medium",pos)
pos = (90,90)
words.set_font_bold(True)
words.text("THIS IS bold",pos)
pos = (110,110)
words.set_font_italic(True)
words.text("THIS IS italic",pos)
pos = (130,130)
words.set_font_underline(True)
words.text("THIS IS underline",pos)
words.set_font_bold(False)
words.set_font_italic(False)
words.set_font_underline(False)
pos = (150,150)
words.text("THIS IS PUCE, YES PUCE",pos,color=Color.PUCE)
pos = (170,170)
words.text("This is magical text",pos,color=Color.PLUM,alpha=128)
pos = (190,190)
words.ez_view_text("Can you read this better?",pos)
img.add_drawing_layer(words)
temp = img.apply_layers()
print "words: %s" % temp.save(temp=True)
img.clear_layers()

#Now lets do some layer stuff
img.add_drawing_layer(lineL)
img.add_drawing_layer(circleL)
img.add_drawing_layer(bez)
img.add_drawing_layer(words)
temp = img.apply_layers([0,2,3])
print "layers: %s" % temp.save(temp=True)
img.clear_layers()

#now lets do some blanket alpha work
lineL.set_layer_alpha(128)
circleL.set_layer_alpha(128)
bez.set_layer_alpha(128)
words.set_layer_alpha(128)
img.add_drawing_layer(lineL)
img.add_drawing_layer(circleL)
img.add_drawing_layer(bez)
img.add_drawing_layer(words)
temp = img.apply_layers()
print "flatlayers: %s" % temp.save(temp=True)
img.clear_layers()

sprites = DrawingLayer((img.width,img.height))
sprites.sprite("../../sampleimages/logo.png",(0,0),alpha=128, rot=45,scale=1.5)
mySprite = Image("../../sampleimages/logo.png").to_pygame_surface()
sprites.sprite(mySprite,(100,100),alpha=128, rot=45,scale=1.5)
sprites.sprite(mySprite,(200,0))
sprites.sprite(mySprite,(0,200), rot=45,scale=1)
img.add_drawing_layer(sprites)
temp = img.apply_layers()
print "sprites: %s" % temp.save(temp=True)
img.clear_layers()