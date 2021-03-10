from PIL import Image
import PySimpleGUI as gui
import shutil
import time
import ai

gui.ChangeLookAndFeel('Black')
layout = [

    [
        gui.Text('', key="bos", font=(None, 30),
                 justification='center', size=(50, 1))
    ],

    [
        gui.Text('Handwritten Text Recognition by Group HYLT',
                 font=("hacked", 70), text_color= "deep pink", justification="center")
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Image(key='img')
    ],
    
    [
        gui.Graph(
            canvas_size=(1500, 200),
            graph_bottom_left=(0, 0),
            graph_top_right=(1500, 200),

            key="graph"

        )
    ],
    [
        gui.Image('loading.gif', key='loading',visible=False)
    ],
    [
        gui.Text('', key="result", text_color= "yellow2",font=("digital dream skew", 30),
                 justification='center', size=(50, 1))
    ],
 
       [
        gui.Text('',key = "probability", font=("digital dream skew", 30),text_color= "yellow2", justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],

    [
        gui.FileBrowse(button_color=(
            'white', 'deep pink')),
        gui.Submit('Run', key="OK", button_color=(
            'white', 'deep pink'),size=(5, 1)),
        gui.CloseButton('Quit', button_color=(
            'white', 'red'), key="Quit", size=(5, 1))
    ]
]

window = gui.Window('HYLT', layout, element_justification='c',
                    font=(None, 15)).Finalize()
window.Maximize()
graph = window.Element("graph")
while True:

    event, values = window.read()

    print('Event:', event, values)
    if event in (None, 'Quit'):
        break
        
    path = values['Browse']
    workingPath = '../data/test.png'
    shutil.copyfile(path, workingPath)
    image = Image.open(path)
    image.save(workingPath)
    
    graph.DrawText("Handwritten Text Image Input",
                   (730, 150), font=("hacked", 40), color='yellow2') 
    graph.DrawImage(filename=path, location=(575, 100))
    window.finalize()

    result = ai.main()
    startSecond = time.time()
    while True:
        second = time.time()
        if second - startSecond > 10:
            break
        event, values = window.read(timeout=25)
        window.Element('loading').Update(visible=True)
        window.Element('loading').UpdateAnimation(
            'loading.gif',  time_between_frames=0)
        window.finalize()
    window.Element('loading').Update(visible=False)  
    window.finalize()
    name = "Recognized Text: \" " + result[0] + " \""
    probability = "Probability: " + str(result[1])
   
    window["result"].Update(name)
    window["probability"].Update(probability)
   
