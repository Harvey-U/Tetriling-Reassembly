from copy import deepcopy
import pygame
import random
import numpy as np
import time
import random




# ///Drawing Onto Screen/// this should be removed in the final submission



def draw_tiles (target,grid_solution,colours,tilesToCheckY,tilesToCheckX): #gridMade is a 2 dimensional grid which is the current state of the grid 
    for i in tilesToCheckY: #i is the y coordinate, numbered from 0
        for j in tilesToCheckX: #j is the x coordinate, numbered from 0
            if grid_solution[i][j][0] != 0:
                pygame.draw.rect(screen,(colours[int((grid_solution[i][j][0])-1)]),((j-3)*25,(i-3)*25,25,25))
            if target[i][j] != 0:
                pygame.draw.rect(screen,(200,200,200),((j-3)*25+8,(i-3)*25+8,10,10))

def draw_number_possibilities (list_pieces_fit,target,colours,tilesToCheckY,tilesToCheckX): #gridMade is a 2 dimensional grid which is the current state of the grid 
    for i in tilesToCheckY: #i is the y coordinate, numbered from 0
        for j in tilesToCheckX: #j is the x coordinate, numbered from 0
            if target[i][j] != 0:
                text = font.render(str(len(list_pieces_fit[i][j])), True, (0, 128, 0))
                screen.blit(text,((j-3)*25+8,(i-3)*25+8))

def draw_number_neighbours (neighboursGrid,target,colours,tilesToCheckY,tilesToCheckX): #gridMade is a 2 dimensional grid which is the current state of the grid 
    for i in tilesToCheckY: #i is the y coordinate, numbered from 0
        for j in tilesToCheckX: #j is the x coordinate, numbered from 0
            if target[i][j] != 0:
                text = font.render((str(neighboursGrid[i][j])), True, (0, 0, 128))
                #screen.blit(text,((j-3)*50+8,(i-3)*50+8))

def mouseInfo(list_pieces_fit):
    mousePosition = pygame.mouse.get_pos()
    xPos = mousePosition[0]
    yPos = mousePosition[1]
    tileOnX = int((xPos/25)+3)
    tileOnY = int((yPos/25)+3)
    text = font2.render(str(list_pieces_fit[tileOnY][tileOnX]), True, (0, 0, 0))
    screen.blit(text,(xPos,yPos))
           
def generate_colours():
    colours = []
    for i in range(19):
        colours.append (((random.random() * 256),(random.random() * 256),(random.random() * 256)))
        #colours.append (((0),(0),(0)))
    return colours


def draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX):
    screen.fill((255,255,255))
    #printPossibilities()
    draw_tiles(grid_target,grid_solution,colours,tilesToCheckY,tilesToCheckX) #Target and Solution Should Always be the same size
    if whatdraw == 0:
        draw_number_possibilities (list_pieces_fit,grid_target,colours,tilesToCheckY,tilesToCheckX)
    #elif whatdraw == 1:
    #    draw_number_neighbours(neighboursGrid,grid_target,colours)
    mouseInfo(list_pieces_fit)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    whatdraw = 0
                elif event.key == pygame.K_DOWN:
                    whatdraw = 1

    return(whatdraw)

#Initialising Drawing Will be deleated in final submission
colours = generate_colours() #Generating the colours for the 19 different pieces 
pygame.init() #Initialising screen
screen = pygame.display.set_mode((1000,1000)) #Setting size of window
pygame.display.set_caption('Grid Display') #Setting title of window
screen.fill((255, 255, 255))#Make Background White
font = pygame.font.SysFont("comicsansms", 15)
font2 = pygame.font.SysFont("comicsansms", 20)
whatdraw=0




# ///Raw Data///

#Rank Order Tree
rankOrderTree = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],[37,38,39,40],[41,42,43,44],[45,46,47,48],[49,50,51,52],[53,54,55,56],[57,58,59,60],[61,62,63,64],[65,66,67,68],[69,70,71,72],[73,74,75,76],
                 [77,78,79,80],[81,82,83,84],[85,86,87,88],[89,90,91,92],[93,94,95,96],[97,98,99,100],[101,102,103,104],[105,106,107,108],[109,110,111,112],[113,114,115,116],[117,118,119,120],[121,122,123,124],[125,126,127,128],[129,130,131,132],[133,134,135,136],[137,138,139,140],[141,142,143,144],[145,146,147,148],[149,150,151,152],
                 [153,154,155,156],[157,158,159,160],[161,162,163,164],[165,166,167,168],[169,170,171,172],[173,174,175,176],[177,178,179,180],[181,182,183,184],[185,186,187,188],[189,190,191,192],[193,194,195,196],[197,198,199,200],[201,202,203,204],[205,206,207,208],[209,210,211,212],[213,214,215,216],[217,218,219,220],[221,222,223,224],[225,226,227,228],
                 [229,230,231,232],[233,234,235,236],[237,238,239,240],[241,242,243,244],[245,246,247,248],[249,250,251,252],[253,254,255,256],[257,258,259,260],[261,262,263,264],[265,266,267,268],[269,270,271,272],[273,274,275,276],[277,278,279,280],[281,282,283,284],[285,286,287,288],[289,290,291,292],[293,294,295,296],[297,298,299,300],[301,302,303,304]]

#Stores the graph which is used to find which pieces fit where
pieceTree = [
    [
        [0,0],
        [
            [
                [1,0],
                [
                    [
                        [0,1],
                        [
                            [[1,1],1],
                            [[2,0],10],
                            [[1,-1],16],
                            [[0,2],7]
                        ]
                    ],

                    [
                        [1,-1],
                        [
                            [[2,0],14],
                            [[2,-1],19],
                            [[1,-2],5]
                        ]
                    ],
                            
                    [
                        [2,0],
                        [
                            [[3,0],2],
                            [[2,1],4],
                            [[2,-1],8]
                        ]
                    ],
                            
                    [
                        [1,1],
                        [
                            [[1,2],11],
                            [[2,0],12],
                            [[1,-1],13],
                            [[2,1],17]
                        ]
                    ]
                ]
            ],

            [
                [0,1],
                [
                    [
                        [1,1],
                        [
                            [[1,2],18],
                            [[2,1],6]
                        ]
                    ],
                    
                    
                    [
                        [0,2],
                        [
                            [[0,3],3],
                            [[1,2],9],
                            [[1,1],15]
                        ]
                    ]
                ]
            ]
        ]
    ]
]

#Piece coordinates stored in format [y,x]
#
tetris_coords = np.array([
                          [[0, 1], [1, 0], [1, 1]], # Piece ID 1
                          [[1, 0], [2, 0], [3, 0]], # Piece ID 2
                          [[0, 1], [0, 2], [0, 3]], # Piece ID 3
                          [[1, 0], [2, 0], [2, 1]], # Piece ID 4
                          [[1, -2], [1, -1], [1, 0]], # Piece ID 5
                          [[0, 1], [1, 1], [2, 1]], # Piece ID 6
                          [[0, 1], [0, 2], [1, 0]], # Piece ID 7
                          [[1, 0], [2, -1], [2, 0]], # Piece ID 8
                          [[0, 1], [0, 2], [1, 2]], # Piece ID 9
                          [[0, 1], [1, 0], [2, 0]], # Piece ID 10
                          [[1, 0], [1, 1], [1, 2]], # Piece ID 11
                          [[1, 0], [1, 1], [2, 0]], # Piece ID 12
                          [[1, -1], [1, 0], [1, 1]], # Piece ID 13
                          [[1, -1], [1, 0], [2, 0]], # Piece ID 14
                          [[0, 1], [0, 2], [1, 1]], # Piece ID 15
                          [[0, 1], [1, -1], [1, 0]], # Piece ID 16
                          [[1, 0], [1, 1], [2, 1]], # Piece ID 17
                          [[0, 1], [1, 1], [1, 2]], # Piece ID 18
                          [[1, -1], [1, 0], [2, -1]] # Piece ID 19
                         ])

tetris_coords_2 = np.zeros((19,3,2))
for i in range (len(tetris_coords)):
    tetris_coords_2[i][0][0] = (0 - tetris_coords[i][0][0])
    tetris_coords_2[i][0][1] = (0 - tetris_coords[i][0][1])

    tetris_coords_2[i][1][0] = ((tetris_coords[i][1][0]) - (tetris_coords[i][0][0]))
    tetris_coords_2[i][1][1] = ((tetris_coords[i][1][1]) - (tetris_coords[i][0][1]))

    tetris_coords_2[i][2][0] = ((tetris_coords[i][2][0]) - (tetris_coords[i][0][0]))
    tetris_coords_2[i][2][1] = ((tetris_coords[i][2][1]) - (tetris_coords[i][0][1]))

tetris_coords_3 = np.zeros((19,3,2))
for i in range (len(tetris_coords)):
    tetris_coords_3[i][0][0] = (0 - tetris_coords[i][1][0])
    tetris_coords_3[i][0][1] = (0 - tetris_coords[i][1][1])

    tetris_coords_3[i][1][0] = ((tetris_coords[i][0][0]) - (tetris_coords[i][1][0]))
    tetris_coords_3[i][1][1] = ((tetris_coords[i][0][1]) - (tetris_coords[i][1][1]))

    tetris_coords_3[i][2][0] = ((tetris_coords[i][2][0]) - (tetris_coords[i][1][0]))
    tetris_coords_3[i][2][1] = ((tetris_coords[i][2][1]) - (tetris_coords[i][1][1]))

tetris_coords_4 = np.zeros((19,3,2))
for i in range (len(tetris_coords)):
    tetris_coords_4[i][0][0] = (0 - tetris_coords[i][2][0])
    tetris_coords_4[i][0][1] = (0 - tetris_coords[i][2][1])

    tetris_coords_4[i][1][0] = ((tetris_coords[i][0][0]) - (tetris_coords[i][2][0]))
    tetris_coords_4[i][1][1] = ((tetris_coords[i][0][1]) - (tetris_coords[i][2][1]))

    tetris_coords_4[i][2][0] = ((tetris_coords[i][1][0]) - (tetris_coords[i][2][0]))
    tetris_coords_4[i][2][1] = ((tetris_coords[i][1][1]) - (tetris_coords[i][2][1]))



# ///Functions to calculate coordinates///
def calculate_coordinates (y_cord,x_cord,piece_id,set): 
    if (set ==1): tetrisSet = tetris_coords
    elif (set ==2): tetrisSet = tetris_coords_2
    elif (set ==3): tetrisSet = tetris_coords_3
    elif (set ==4): tetrisSet = tetris_coords_4

    cord_1 = (int(y_cord),int(x_cord))
    cord_2 = (int(y_cord+((tetrisSet[piece_id-1][0][0]))) , int(x_cord+((tetrisSet[piece_id-1][0][1]))))
    cord_3 = (int(y_cord+((tetrisSet[piece_id-1][1][0]))) , int(x_cord+((tetrisSet[piece_id-1][1][1]))))
    cord_4 = (int(y_cord+((tetrisSet[piece_id-1][2][0]))) , int(x_cord+((tetrisSet[piece_id-1][2][1]))))
    coordsSet = (cord_1,cord_2,cord_3,cord_4)#A tuple of the coordinates of each point of the tetris piece

    return coordsSet

def get_tetris_coordinates(y_cord,x_cord,piece_id,wrt): #wrt is with respect to and it says at which point the origin is
    #coordsSet1
    if wrt == 1:
        return calculate_coordinates(y_cord,x_cord,piece_id,1)
    elif wrt == 2:
        return calculate_coordinates(y_cord,x_cord,piece_id,2)
    elif wrt == 3:
        return calculate_coordinates(y_cord,x_cord,piece_id,3)
    elif wrt == 4:
        return calculate_coordinates(y_cord,x_cord,piece_id,4)





# ///Functions to generate grids///
def convertTarget(targetInput): #Turns the lists of lists given ny utils into a numpy array with a border a 3 around the edge made up of zeros
    outputTarget = np.asarray(targetInput) #Converts to numpy array
    
    width = outputTarget.shape[1]
    addonTop = (np.zeros((3,width),dtype = 'int'))
    outputTarget = np.vstack((outputTarget,addonTop))
    outputTarget = np.vstack((addonTop,outputTarget))

    height = outputTarget.shape[0]
    addonSide = (np.zeros((height,3),dtype = 'int'))
    outputTarget = np.hstack((outputTarget,addonSide))
    outputTarget = np.hstack((addonSide,outputTarget))

    return(outputTarget)

def convertTargetBooster(targetInput): #Turns the lists of lists given ny utils into a numpy array with a border a 3 around the edge made up of 2s, used for the booster
    outputTarget = np.asarray(targetInput) #Converts to numpy array
    
    width = outputTarget.shape[1]
    addonTop = (np.full((3,width),2,dtype = 'int'))
    outputTarget = np.vstack((outputTarget,addonTop))
    outputTarget = np.vstack((addonTop,outputTarget))

    height = outputTarget.shape[0]
    addonSide = (np.full((height,3),2,dtype = 'int'))
    outputTarget = np.hstack((outputTarget,addonSide))
    outputTarget = np.hstack((addonSide,outputTarget))

    return(outputTarget)

def generate_empty_solution(dimension):#Making solution np array in the same size as the target grid (This is the final ouput)
    size = dimension
    size = list(size)
    size.append(2)
    size = tuple(size)
    grid_solution = np.zeros(size)
    return grid_solution

def make_rect_list(height,width): #Generates list with certain width and certain height
    list_output = []
    for i in range(height):
        list_output.append([])
        for j in range (width):
            list_output[i].append([])
    return list_output





# ///Scanning Functions///

#Neigbours
def calcNeighbours(yCord,xCord,grid_target):
    numberOfNeighbours = 0
    if grid_target[yCord-1][xCord] == 1: numberOfNeighbours+=1
    if grid_target[yCord][xCord-1] == 1: numberOfNeighbours+=1
    if grid_target[yCord+1][xCord] == 1: numberOfNeighbours+=1
    if grid_target[yCord][xCord+1] == 1: numberOfNeighbours+=1
            
    return(numberOfNeighbours)  

def getNeigbours(tilesToCheckY,tilesToCheckX,grid_target,neighboursGrid):
    for i in tilesToCheckY: #i is the y coordinate, numbered from 0
        for j in tilesToCheckX: #j is the x coordinate, numbered from 0
            neighboursGrid [i][j] = (calcNeighbours(i,j,grid_target))
    return(neighboursGrid)

def updateNeighbours(yCord,xCord,grid_target,grid_solution):
    numberOfNeighbours = 0
    if grid_target[yCord-1][xCord]==1 and grid_solution[yCord-1][xCord][0] == 0: numberOfNeighbours+=1
    if grid_target[yCord][xCord-1] == 1 and grid_solution[yCord][xCord-1][0] == 0: numberOfNeighbours+=1
    if grid_target[yCord+1][xCord] == 1 and grid_solution[yCord+1][xCord][0] == 0: numberOfNeighbours+=1
    if grid_target[yCord][xCord+1] == 1 and grid_solution[yCord][xCord+1][0] == 0: numberOfNeighbours+=1
            
    return(numberOfNeighbours) 




#piece fit scanning
def tilePieceRecursion(yCord,xCord,targetGrid,remaining = None,pieces = None):#This function gets given the coordinates in a grid and returns a list of pieces that will fit
    if pieces is None:
        pieces = []
        remaining = pieceTree
    if  isinstance(remaining, int):
        pieces.append(remaining)
    else:
        for mini in remaining:
            cords = mini[0]
            if targetGrid[yCord+cords[0]][xCord+cords[1]] == 1:
                pieces = tilePieceRecursion(yCord,xCord,targetGrid,mini[1],pieces)
    return(pieces)

def scanGrid(height,width,list_pieces_fit,targetGrid):#For each square store all the serial numbers of each part of each piece that can fit there 
    serial_counter = 1 #Start at 1 because 0 means nothing 
    for i in (height): #i is the y coordinate, numbered from 0
            for j in (width): #j is the x coordinate, numbered from 0
                pieces = tilePieceRecursion(i,j,targetGrid) #Calls the recursive function to find which pieces will fit
                for pieceid in pieces:
                    piece_cords = get_tetris_coordinates (i,j,pieceid,1)#Only needs to try one set of the pieces as it goes through every tile anyway
                    piece_segment_1_cord = piece_cords[0] #Getting the cordinate for each segment
                    piece_segment_2_cord = piece_cords[1]
                    piece_segment_3_cord = piece_cords[2]
                    piece_segment_4_cord = piece_cords[3] 
                    list_pieces_fit[piece_segment_1_cord[0]][piece_segment_1_cord[1]].append ([pieceid,serial_counter,1])#0
                    list_pieces_fit[piece_segment_2_cord[0]][piece_segment_2_cord[1]].append ([pieceid,serial_counter,2])
                    list_pieces_fit[piece_segment_3_cord[0]][piece_segment_3_cord[1]].append ([pieceid,serial_counter,3])
                    list_pieces_fit[piece_segment_4_cord[0]][piece_segment_4_cord[1]].append ([pieceid,serial_counter,4])
                    serial_counter += 1

    return(list_pieces_fit)

#Ranking
def rankTile(yCord,xCord,list_pieces_fit,neighboursGrid): #For a given coordinate this returns the ranking if that square
    node1 = len(list_pieces_fit[yCord][xCord])-1 #This is what working on need to extend rank list as each tile can have more than 19 possibilities
    node2 = (neighboursGrid[yCord][xCord])-1
    return(rankOrderTree[node1][node2])

def rankGrid(tilesToCheckY,tilesToCheckX,rankOrderArray,list_pieces_fit,neighboursGrid):
    for i in tilesToCheckY: #i is the y coordinate, numbered from 0
        for j in tilesToCheckX: #j is the x coordinate, numbered from 0
            rankOrderArray[rankTile(i,j,list_pieces_fit,neighboursGrid)].append([i,j])
    return(rankOrderArray)

def rankIndividual(yCord,xCord,rankOrderArray,list_pieces_fit,neighboursGrid):
    rankOrderArray[rankTile(yCord,xCord,list_pieces_fit,neighboursGrid)].append([yCord,xCord])
    return(rankOrderArray)





# ///List of pieces manipulation///
def get_intersecting (yCord,xCord,list_pieces_fit): #Returns list of all the pieces in each point in list_pieces_fit 
    SIDsPids = []
    for x in (list_pieces_fit[yCord][xCord]):
        SIDsPids.append(x)
    return SIDsPids

def delete_intersecting (yCord,xCord,SIDs,pieceID,originID,list_pieces_fit,rankOrderArray,neighboursGrid):
    coordinates_to_check = get_tetris_coordinates(yCord,xCord,pieceID,originID)
    for cord in coordinates_to_check:
        #print (list_pieces_fit[cord[0]][cord[1]])
        for y in (list_pieces_fit[cord[0]][cord[1]]):
            if y[1] == SIDs:
                list_pieces_fit[cord[0]][cord[1]].remove(y)
                rankOrderArray = rankIndividual(cord[0],cord[1],rankOrderArray,list_pieces_fit,neighboursGrid)




# ///Iteration Functions///

def getCoordsOfLowestProduct(rankOrderArray,list_pieces_fit): #Returns the the coordinates tile which has the highest rank (top left of array)
    for i in range (len(rankOrderArray)):
        row = rankOrderArray[i]
        if len(row)>= 1:
            for index in range (len(row)):
                coords = row[index]
                if len(list_pieces_fit[coords[0]][coords[1]]) != 0:
                    del row[0:index+1]
                    return (coords)#Returns 1D list of coordinates
        rankOrderArray[i] = []

def calcSumOfNeigbours(y_cord,x_cord,piece,neighboursGrid):
    piece_id = piece[0]
    origin_id = piece[2]
    coords = calculate_coordinates(y_cord,x_cord,piece_id,origin_id)
    total = 0
    for coord in coords:
        total += neighboursGrid[coord[0]][coord[1]]

    return(total)#Returns the total of all the product fo a certian piece




# ///Booster Functions

def booster(tilesToCheckY,tilesToCheckX,grid_booster,dictionary_pieces,grid_solution,serialNo):
    for y in tilesToCheckY:
        for x in tilesToCheckX:
            if grid_booster[y][x] == 1:
                pieces = tilePieceBoosterRecursion(grid_booster,y,x)
                for piece in pieces:
                    if dictionary_pieces[piece] >= 1:
                        cords = get_tetris_coordinates(y,x,piece,1)
                        counter = 0
                        for cord in cords:
                            if grid_booster[cord[0]][cord[1]] ==0:
                                counter+=1
                        if counter <=1:
                            for cord in cords:
                                grid_solution[cord[0]][cord[1]] = [piece,serialNo]
                                grid_booster[cord[0]][cord[1]] = 2                    
                            serialNo += 1
                            dictionary_pieces[piece] -= 1
                            break

def tilePieceBoosterRecursion(grid_booster,yCord,xCord,remaining = None,pieces = None):#This function gets given the coordinates in a grid and returns a list of pieces that will fit
    if pieces is None:
        pieces = []
        remaining = pieceTree
    if  isinstance(remaining, int):
        pieces.append(remaining)
    else:
        for mini in remaining:
            cords = mini[0]
            if grid_booster[yCord+cords[0]][xCord+cords[1]] <= 1:
                pieces = tilePieceBoosterRecursion(grid_booster,yCord,xCord,mini[1],pieces)
    return(pieces)



# ///Do Super Slow Function
def checkNoGaps(grid_booster,tilesToCheckY,tilesToCheckX,area):
    counter = 0
    for i in tilesToCheckY:
        for j in tilesToCheckX:
            if grid_booster[i][j] == 1:
                counter += 1
    if area <= 100:
        if counter<=4:
            return True
    elif area <= 400:
        if counter <=8:
            return True
    elif area == 2500:
        if counter <=20:
            return True
    elif counter <=20:
            return True
    else:
        return(False)


# ///Main Function///

def Tetris(target, limit_tetris):

    print('setting up')
    #Initialisation
    targetActualHeight = len(target)
    targetActualWidth = len(target[0])
    grid_target = convertTarget(target)
    grid_booster = convertTargetBooster(target)
    dictionary_pieces = deepcopy(limit_tetris) #This is the dictionary list of the number of each piece
    grid_solution = generate_empty_solution((targetActualHeight+6,targetActualWidth+6)) #This is the final output grid
    list_pieces_fit = make_rect_list(targetActualHeight+6,targetActualWidth+6) #Makes a rectangular list of lists ready to store list of the piece ids, it has an additional border of 3
    tilesToCheckY = np.arange(3,targetActualHeight+3,1,dtype=int) #Since we have addedan additional border of three around the edge
    tilesToCheckX = np.arange(3,targetActualWidth+3,1,dtype=int)
    neighboursGrid = np.zeros((targetActualHeight+6,targetActualWidth+6),dtype=int) 
    rankOrderArray = []
    serialNo = 1
    for q in range(504): #Initialising the rank order array, Each row represents a rank
        rankOrderArray.append([])
    if (targetActualHeight * targetActualWidth) <= 2500:
        doSuperSlow = True
    else:
        doSuperSlow = False

    whatdraw = 0
    whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))

    #Initial Scanning
    print('startes initial scaning')
    t1 = time.time()
    list_pieces_fit = scanGrid(tilesToCheckY,tilesToCheckX,list_pieces_fit,grid_target) #Carries out initial scanning of grid
    neighboursGrid = getNeigbours(tilesToCheckY,tilesToCheckX,grid_target,neighboursGrid)
    rankOrderArray = rankGrid(tilesToCheckY,tilesToCheckX,rankOrderArray,list_pieces_fit,neighboursGrid)
    t2 = time.time()
    timeInitialScanning = (t2-t1)
    print(timeInitialScanning)

    whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
    counter = 0
    h=1

    timeGettingCordinates = 0
    arraytimeGettingCordinates =[]
    timeCounter = 0
    timeFindingBestPiece = 0

    if doSuperSlow == False:
        #Main Iteration Loop
        while(True):
            try: #This is an arbitrary number, will change it to a condition that there is nothing left in rank order
                whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
                
                t1=time.time()
                cordinates = getCoordsOfLowestProduct(rankOrderArray,list_pieces_fit)
                t2=time.time()
                timeGettingCordinates += (t2-t1)
            
                if timeCounter >= 100:
                    arraytimeGettingCordinates.append(timeGettingCordinates)
                    timeGettingCordinates = 0
                    timeCounter = 0
                    #print(rankOrderArray)
                    #print()
                    #print()
                timeCounter+=1

                t1=time.time()
                indexOfChosen = 0
                minSumNeighbours = calcSumOfNeigbours(cordinates[0],cordinates[1],list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen],neighboursGrid)
                numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                for index in range (len(list_pieces_fit[cordinates[0]][cordinates[1]])):
                    piece = list_pieces_fit[cordinates[0]][cordinates[1]][index]
                    if dictionary_pieces[piece[0]] >=1:
                        tempSum = calcSumOfNeigbours(cordinates[0],cordinates[1],list_pieces_fit[cordinates[0]][cordinates[1]][index],neighboursGrid)
                        if tempSum == minSumNeighbours:
                            tempnumberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][index][0]]
                            if tempnumberAvailable > numberAvailable:
                                indexOfChosen = index
                                minSumNeighbours = tempSum
                                numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                                numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                        elif tempSum < minSumNeighbours:
                            indexOfChosen = index
                            minSumNeighbours = tempSum
                            numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                t2=time.time()
                timeFindingBestPiece += (t2-t1) 
                #print(list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen])
                

                if (indexOfChosen == 0) and (dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]<=0):
                    list_pieces_fit[cordinates[0]][cordinates[1]].remove(list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen])
                    #print(list_pieces_fit[cordinates[0]][cordinates[1]])
                    #print('sdfaf')
                    

                else:
                    dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]] -= 1

                    serialID = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][1]
                    piece_id = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]
                    origin_id = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][2] #Could be 1,2,3,4 says which coordinate of the piece has been found             
                    coordinates_to_check = get_tetris_coordinates(cordinates[0],cordinates[1],piece_id,origin_id)
                    for x in coordinates_to_check:
                        grid_solution[int(x[0])][int(x[1])] = [piece_id,serialNo]
                        grid_booster[int(x[0])][int(x[1])] = 2
                    serialNo += 1    
            
                    for z in coordinates_to_check:
                        neighboursGrid[z[0]+1][z[1]] = updateNeighbours(z[0]+1,z[1],grid_target,grid_solution)
                        neighboursGrid[z[0]-1][z[1]] = updateNeighbours(z[0]-1,z[1],grid_target,grid_solution)
                        neighboursGrid[z[0]][z[1]+1] = updateNeighbours(z[0]-1,z[1]+1,grid_target,grid_solution)
                        neighboursGrid[z[0]][z[1]-1] = updateNeighbours(z[0],z[1]-1,grid_target,grid_solution)

                    
                    for z in coordinates_to_check:  
                        intersections = get_intersecting(int(z[0]),int(z[1]),list_pieces_fit)        
                        for q in intersections:
                            delete_intersecting (int(z[0]),int(z[1]),int(q[1]),int(q[0]),int(q[2]),list_pieces_fit,rankOrderArray,neighboursGrid)
                    #print(h)
                    h+=1


                
            except:
                counter += 1
                #print(grid_booster)
                booster(tilesToCheckY,tilesToCheckX,grid_booster,dictionary_pieces,grid_solution,serialNo)
                #print('Time getting cordinates' + str(timeGettingCordinates))
                #print(arraytimeGettingCordinates)
                #print('Time finding best piece' + str(timeFindingBestPiece))
                #print(h)
                #print(counter)
                whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
                
                if True:
                    output = []
                    for y in tilesToCheckY:
                        output.append([])
                        for x in tilesToCheckX:
                            output[y-3].append((int(grid_solution[y][x][0]),int(grid_solution[y][x][1])))
                    return (output)



    else:
        list_pieces_fit2 = deepcopy(list_pieces_fit) #The 2 version stay the same always
        grid_target2 = deepcopy(grid_target)
        grid_booster2 = deepcopy(grid_booster)
        dictionary_pieces2 = deepcopy(dictionary_pieces)
        grid_solution2 = deepcopy(grid_solution)
        neighboursGrid2 = deepcopy(neighboursGrid)
        rankOrderArray2 = deepcopy(rankOrderArray)
        serialNo2 = deepcopy(serialNo)

        area = targetActualHeight*targetActualWidth

        print('Doing Slow Way')
        for m in tilesToCheckY:
            print (tilesToCheckY)
            for f in tilesToCheckX:
                if (len(list_pieces_fit2[m][f])>=1):
                    for k in range (len(list_pieces_fit2[m][f])):
                        print(len(list_pieces_fit2[m][f]))
                        print ('the index is' + str(k))
                        if (dictionary_pieces2[list_pieces_fit2[m][f][k][0]] >=1):
                            startIndex = k
                        
                            startCoordinates = [m,f]
                            print(startCoordinates)

                            #Set starting values
                            list_pieces_fit = deepcopy(list_pieces_fit2)
                            grid_target = deepcopy(grid_target2)
                            grid_booster = deepcopy(grid_booster2)
                            dictionary_pieces = deepcopy(dictionary_pieces2)
                            grid_solution = deepcopy(grid_solution2)
                            neighboursGrid = deepcopy(neighboursGrid2)
                            rankOrderArray = deepcopy(rankOrderArray2)
                            serialNo1 = deepcopy(serialNo2)

                            #Main Iteration Loop
                            needToBreak = False
                            while(needToBreak == False):
                                try: #This is an arbitrary number, will change it to a condition that there is nothing left in rank order
                                    whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
                                    
                                    if startCoordinates:
                                        cordinates = startCoordinates
                                        startCoordinates = False
                                        print('start')
                                    else:
                                        cordinates = getCoordsOfLowestProduct(rankOrderArray,list_pieces_fit)
                                        print('update')
                                
                                    if timeCounter >= 100:
                                        arraytimeGettingCordinates.append(timeGettingCordinates)
                                        timeGettingCordinates = 0
                                        timeCounter = 0
                                        #print(rankOrderArray)
                                        #print()
                                        #print()
                                    timeCounter+=1

                                    if startIndex:
                                        indexOfChosen = startIndex
                                        startIndex = False
                                    else:
                                        t1=time.time()
                                        indexOfChosen = 0
                                        minSumNeighbours = calcSumOfNeigbours(cordinates[0],cordinates[1],list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen],neighboursGrid)
                                        numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                                        for index in range (len(list_pieces_fit[cordinates[0]][cordinates[1]])):
                                            piece = list_pieces_fit[cordinates[0]][cordinates[1]][index]
                                            if dictionary_pieces[piece[0]] >=1:
                                                tempSum = calcSumOfNeigbours(cordinates[0],cordinates[1],list_pieces_fit[cordinates[0]][cordinates[1]][index],neighboursGrid)
                                                if tempSum == minSumNeighbours:
                                                    tempnumberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][index][0]]
                                                    if tempnumberAvailable > numberAvailable:
                                                        indexOfChosen = index
                                                        minSumNeighbours = tempSum
                                                        numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                                                        numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                                                elif tempSum < minSumNeighbours:
                                                    indexOfChosen = index
                                                    minSumNeighbours = tempSum
                                                    numberAvailable = dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]
                                        t2=time.time()
                                        timeFindingBestPiece += (t2-t1) 
                                        #print(list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen])
                                    

                                    if (indexOfChosen == 0) and (dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]]<=0):
                                        list_pieces_fit[cordinates[0]][cordinates[1]].remove(list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen])
                                        #print(list_pieces_fit[cordinates[0]][cordinates[1]])
                                        #print('sdfaf')
                                        

                                    else:
                                        dictionary_pieces[list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]] -= 1

                                        serialID = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][1]
                                        piece_id = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][0]
                                        origin_id = list_pieces_fit[cordinates[0]][cordinates[1]][indexOfChosen][2] #Could be 1,2,3,4 says which coordinate of the piece has been found             
                                        coordinates_to_check = get_tetris_coordinates(cordinates[0],cordinates[1],piece_id,origin_id)
                                        for x in coordinates_to_check:
                                            grid_solution[int(x[0])][int(x[1])] = [piece_id,serialNo]
                                            grid_booster[int(x[0])][int(x[1])] = 2
                                        serialNo += 1    
                                
                                        for z in coordinates_to_check:
                                            neighboursGrid[z[0]+1][z[1]] = updateNeighbours(z[0]+1,z[1],grid_target,grid_solution)
                                            neighboursGrid[z[0]-1][z[1]] = updateNeighbours(z[0]-1,z[1],grid_target,grid_solution)
                                            neighboursGrid[z[0]][z[1]+1] = updateNeighbours(z[0]-1,z[1]+1,grid_target,grid_solution)
                                            neighboursGrid[z[0]][z[1]-1] = updateNeighbours(z[0],z[1]-1,grid_target,grid_solution)

                                        
                                        for z in coordinates_to_check:  
                                            intersections = get_intersecting(int(z[0]),int(z[1]),list_pieces_fit)        
                                            for q in intersections:
                                                delete_intersecting (int(z[0]),int(z[1]),int(q[1]),int(q[0]),int(q[2]),list_pieces_fit,rankOrderArray,neighboursGrid)
                                        #print(h)
                                        h+=1


                                    
                                except:
                                    whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
                                
                                        #print(grid_booster)
                                    booster(tilesToCheckY,tilesToCheckX,grid_booster,dictionary_pieces,grid_solution,serialNo)
                                    if checkNoGaps(grid_booster,tilesToCheckY,tilesToCheckX,area) == True:
                                        #print('Time getting cordinates' + str(timeGettingCordinates))
                                        #print(arraytimeGettingCordinates)
                                        #print('Time finding best piece' + str(timeFindingBestPiece))
                                        #print(h)
                                        #print(counter)
                                        whatdraw = (draw(whatdraw,grid_target,grid_solution,colours,list_pieces_fit,tilesToCheckY,tilesToCheckX))
                                        
                                        if True:
                                            output = []
                                            for y in tilesToCheckY:
                                                output.append([])
                                                for x in tilesToCheckX:
                                                    output[y-3].append((int(grid_solution[y][x][0]),int(grid_solution[y][x][1])))
                                            print('Exporting')
                                            return (output)
                                    else:
                                        print('Passed')
                                        needToBreak = True
                                        
                                    
                                print('shit')