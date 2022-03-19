import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE = 'cape_python.png'
SA1_CORNERS = (130,265,180,315)
SA2_CORNERS = (80,255,130,305)
SA3_CORNERS = (105,205,155,255)

class Search():
    def __init__(self,name):
        self.name = name
        self.img = cv.imread(MAP_FILE,cv.IMREAD_COLOR)
        if self.img is None:
            print("Nie można załadować pliku z mapą {}".format(MAP_FILE),file=sys.stderr )
            sys.exit(1)

        self.area_actual = 0
        self.salior_actual = [0,0]

        self.sa1 = self.img[SA1_CORNERS[1]:SA1_CORNERS[3],
                            SA1_CORNERS[0]:SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1]:SA2_CORNERS[3],
                            SA2_CORNERS[0]:SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1]:SA3_CORNERS[3],
                            SA3_CORNERS[0]:SA3_CORNERS[2]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def draw_map(self,last_know):
        cv.line(self.img,(20,370),(70,370),(0,0,0),2)
        cv.putText(self.img,'0',(8,370),cv.FONT_HERSHEY_PLAIN,1,(0,0,0) )
        cv.putText(self.img, '50 mil morskich', (71,370), cv.FONT_HERSHEY_PLAIN,1,(0,0,0) )
        cv.rectangle(self.img,(SA1_CORNERS[0],SA1_CORNERS[1]),(SA1_CORNERS[2],SA1_CORNERS[3]), (0,0,0),1 )
        cv.putText(self.img,'1', (SA1_CORNERS[0]+3,SA1_CORNERS[1]+15), cv.FONT_HERSHEY_PLAIN,1,0 )
        cv.rectangle(self.img, (SA2_CORNERS[0],SA2_CORNERS[1]),(SA2_CORNERS[2],SA2_CORNERS[3]), (0,0,0),1 )
        cv.putText(self.img,'2', (SA2_CORNERS[0]+3, SA2_CORNERS[1]+15),cv.FONT_HERSHEY_PLAIN,1,0 )
        cv.rectangle(self.img,(SA3_CORNERS[0],SA3_CORNERS[1]),(SA3_CORNERS[2],SA3_CORNERS[3]), (0,0,0),1)
        cv.putText(self.img,'3',(SA3_CORNERS[0]+3,SA3_CORNERS[1]+15),cv.FONT_HERSHEY_PLAIN,1,0 )
        cv.putText(self.img,'+',last_know, cv.FONT_HERSHEY_PLAIN,1,(0,0,255))
        cv.putText(self.img,'+ = ostatnia znana lokalizacja', (240,355), cv.FONT_HERSHEY_PLAIN,1,(0,0,255))
        cv.putText(self.img, '* = rzeczywista lokalizacja', (242,370), cv.FONT_HERSHEY_PLAIN,1,(255,0,0))

        cv.imshow('Obszary do przeszukania',self.img)
        cv.moveWindow('Obszary do przeszukania', 750,10)
        cv.waitKey(50000)

    def salior_final_location(self,num_search_areas):
        #zwraca wspołrzedne zeglarza wzgledem podtablicy obszaru poszukiwan
        self.salior_actual[0] = np.random.choice(self.sal.shape[1],1)
        self.salior_actual[1] = np.random.choice(self.sal.shape[0],1)

        area = int random.triangular(1,num_search_areas +1)

        if area == 1:
            x = self.salior_actual[0] + SA1_CORNERS[0]
            y = self.salior_actual[1] + SA1_CORNERS[1]
            self.area_actual = 1
        elif area == 2:
            x = self.salior_actual[0] + SA2_CORNERS[0]
            y = self.salior_actual[1] + SA2_CORNERS[1]
            self.area_actual = 2
        elif area == 3:
            x = self.salior_actual[0] + SA3_CORNERS[0]
            y = self.salior_actual[1] + SA3_CORNERS[1]
            self.area_actual = 3

        return x,y






a = Search('Kordian')
a.draw_map((1,1))