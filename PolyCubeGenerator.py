import maya.cmds as cmds
import random

#Function for UI
def uI():
    
    #If window already exists, delete it
    if(cmds.window('PolyCubeSpawner', exists=True)):
        cmds.deleteUI('PolyCubeSpawner')
    theWin = cmds.window('PolyCubeSpawner')
    cmds.columnLayout()
    cmds.text(label = 'Please enter the number of \nrandom polycubes you would \nlike to spawn', align = 'left', font = 'smallBoldLabelFont')
    cmds.intField('numOfCubes', width = 135)
    cmds.text(label = '\n')
    cmds.button(label = 'Spawn polycubes', command = 'spawnPolyCubes()', backgroundColor = [0,5,22], height = 66, width = 135, align = 'center')
    cmds.showWindow('PolyCubeSpawner') 
    
#Function to spawn polycubes       
def spawnPolyCubes():
    num = cmds.intField('numOfCubes', q = True, value = True)
    for i in range(0, num):
        cubeWidth = random.randint(1,6)
        cubeHeight = random.randint(1,6)
        cubeDepth = random.randint(1,6)
        xAxis = random.uniform(-179.25, 179.25)
        yAxis = random.uniform(-179.25, 179.25)
        zAxis = random.uniform(-179.25, 179.25)
        cmds.polyCube(w = cubeWidth, h = cubeHeight, d = cubeDepth, axis = [xAxis, yAxis, zAxis])
uI() 
  
