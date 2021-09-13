#import required dependencies
import cv2
import pandas as pd

#path to the test image
img_path = 'image3.jpg'

#reading the image
img = cv2.imread(img_path)
img = cv2.resize(img, (700, 500))

clicked = False

#initialising the values of r, g, b, position of x, position of y
r = 0
g = 0
b = 0
xpos = 0
ypos = 0

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']

#reading the database of colors
data = pd.read_csv('colors.csv', names=index,header=None)

#function to get the name of color
def getcolorname(R, G, B):
    minimum = 10000
    for i in range(len(data)):

        
        distance= abs(R- int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"])) + abs(B- int(data.loc[i,"B"]))

        if(distance <= minimum):
            minimum = distance
            color_name = data.loc[i, 'color_name']

    return color_name

def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:

        global b, g, r, xpos, ypos, clicked

        clicked = True
        xpos = x
        ypos = y

        #Assiging the values of BGR to b, g, r
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', draw_function)

while True:
    
    #displaying the image 
    cv2.imshow('Color Detector', img)
    if(clicked):

        cv2.rectangle(img, (0,10), (750,60), (b,g,r),  -1)

        #getting the name of color
        text=getcolorname(r, g, b) + ' R=' + str(r) + ' G='+ str(g) + ' B=' + str(b)
        
        #display the colorname along with the rgb values
        cv2.putText(img, text, (45, 45), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
      
        if(r+g+b >=600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()