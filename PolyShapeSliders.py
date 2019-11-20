#Import
import maya.cmds as cmds
from functools import partial

#Function to translate polyshape
def translate(slider, *args, **kwargs):
    value = getSliderValue(slider)
    cmds.move(value, **kwargs)
    
#Function to rotate polyshape
def rotation(slider, *args, **kwargs):
    value = getSliderValue(slider)
    cmds.rotate(value, **kwargs)

#Function to scale 
def scaleShape(slider, *args, **kwargs):
    value = getSliderValue(slider)
    cmds.scale(value, **kwargs)  

#Function for slider value
def getSliderValue(ctrlName):
    value = cmds.floatSlider(ctrlName, q=True, value=True)
    return value
 
#Function to reset location and sliders    
def reset():
    cmds.move(0.00, 0.00, 0.00) 
    cmds.rotate(0.00, 0.00, 0.00)
    cmds.scale(1.00, 1.00, 1.00)
    windowUI()  

#Window
def windowUI():
    
    #If window exists, delete it
    if(cmds.window('TranslatePolyShape', exists=True)):
        cmds.deleteUI('TranslatePolyShape')
    theWin = cmds.window('TranslatePolyShape')    
    cmds.columnLayout(adjustableColumn=True, columnAlign='center', rowSpacing=20, height =400)  
                                              
    #For Translation
    cmds.text('\n', height=2)
    cmds.text('Translate:', font='boldLabelFont')
    cmds.text('X Axis', font='obliqueLabelFont', height=10)
    xSlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.text('Y Axis', font='obliqueLabelFont')
    ySlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.text('Z Axis', font='obliqueLabelFont')
    zSlider = cmds.floatSlider(min=-100.00, max=100.00, value=0.00, step=1, dc='empty')
    cmds.floatSlider(xSlider, e=True, dc = partial(translate, xSlider, x=0.5))
    cmds.floatSlider(ySlider, e=True, dc = partial(translate, ySlider, y=0.5))
    cmds.floatSlider(zSlider, e=True, dc = partial(translate, zSlider, z=0.5))
    
    #For Rotation
    cmds.text('Rotate:', font='boldLabelFont')
    cmds.text('Rotate X', font='obliqueLabelFont', height=10)
    xRotate = cmds.floatSlider(min = -360.00, max = 360.00, value = 0.00, step = 1, dc = 'empty')
    cmds.text('Rotate Y', font='obliqueLabelFont', height=10)
    yRotate = cmds.floatSlider(min = -360.00, max = 360.00, value = 0.00, step = 1, dc = 'empty')
    cmds.text('Rotate Z', font='obliqueLabelFont', height=10)
    zRotate = cmds.floatSlider(min = -360.00, max = 360.00, value = 0.00, step = 1, dc = 'empty')
    cmds.floatSlider(xRotate, e=True, dc = partial(rotation, xRotate, x=0.5))
    cmds.floatSlider(yRotate, e=True, dc = partial(rotation, yRotate, y=0.5))
    cmds.floatSlider(zRotate, e=True, dc = partial(rotation, zRotate, z=0.5))
    
    #For Scale
    cmds.text('Scale:', font='boldLabelFont')
    cmds.text('Scale X', font='obliqueLabelFont', height=10)
    xScale = cmds.floatSlider(min = 0.10, max = 100.00, value = 1.00, step = 1, dc = 'empty')
    cmds.text('Scale Y', font='obliqueLabelFont', height=10)
    yScale = cmds.floatSlider(min = 0.10, max = 100.00, value = 1.00, step = 1, dc = 'empty')
    cmds.text('Scale Z', font='obliqueLabelFont', height=10)
    zScale = cmds.floatSlider(min = 0.10, max = 100.00, value = 1.00, step = 1, dc = 'empty')
    cmds.floatSlider(xScale, e=True, dc = partial(scaleShape, xScale, x=0.5))
    cmds.floatSlider(yScale, e=True, dc = partial(scaleShape, yScale, y=0.5))
    cmds.floatSlider(zScale, e=True, dc = partial(scaleShape, zScale, z=0.5))
    
    #Reset button
    cmds.button(label='Reset All', command='reset()')
    cmds.showWindow()  
windowUI()