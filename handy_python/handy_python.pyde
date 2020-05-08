add_library('handy')

from org.gicentre.handy import *

import os


xpos = [0, 0, 0, 0]
thin = 8
thick = 36
global kfactor

def setup():
    
    kfactor = 1
    size(800,800);
    noLoop();
   
    global h1, h2, h3, h4
    global points
    points = None

    h1 = HandyPresets.createPencil(this);
    h2 = HandyPresets.createColouredPencil(this);
    h3 = HandyPresets.createWaterAndInk(this);
    h4 = HandyPresets.createMarker(this);

def draw():
    global sc
    foldpath = r"C:\Users\binoy\Desktop\curdir"

    background(255);
    
    for ifno, fpath in enumerate(os.listdir(foldpath)):
        with open(os.path.join(foldpath, fpath)) as fin:
            hdr = fin.readline()
            (minx, maxx, miny, maxy, lwid) = [float(v) for v in hdr.strip().split(",")]
            #print(minx, maxx, miny, maxy)
            
            wid0 = maxx - minx
            hgt0 = maxy - miny
            ws = width/wid0
            hs = height/hgt0
            
            sc = min([hs, ws])*1.0
            woff = 0.15*wid0*sc*0
            points = []
            # try:
            for l in fin:
                if l.strip():
                    x,y = [float(v.strip())*sc*1.0 for v in l.strip().split(",")]
                    points.append(( (x-minx*sc)+woff,(y-maxy*sc)))
        
        # for i in range(5):
        
        #fill(206+random(-30,30),76+random(-30,30),52+random(-30,30),160);
        # h1.rect(random(10,200),random(10,50),80,50);
        # h2.rect(random(310,520),random(10,50),80,50);
        # h3.rect(random(10,200),random(100,140),80,50);
        # h4.rect(random(310,520),random(100,140),80,50);  
        xarr = [v[0] for v in points]
        yarr = [-v[1] for v in points]
        fill(40+random(-30,30),76+random(-30,30),200+random(-30,30),255);
        h = h1
        h.setFillGap(12.2)
        h.setBackgroundColour(color(0,0));
        h.setRoughness(3.3); 
        h.setFillWeight(1);
        h.setHachurePerturbationAngle(32)
        h.setIsAlternating(True);
        h.shape(xarr, yarr)
        #exit()
    save(r"C:\Users\binoy\Desktop\curve_sketcher\samples\out4.png")
    #saveFrame("line-######.png");
