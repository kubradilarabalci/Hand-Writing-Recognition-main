from PIL import Image
import PySimpleGUI as gui

import shutil
import ai

gui.ChangeLookAndFeel('DarkTeal')
layout = [

    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],

    [
        gui.Text('Handwritten Text Recognition by Group HYLT',font=(None, 50), justification = "center"  )
    ],
    [
        gui.Image(key='img')
    ],
    #[
    #   gui.Text('',key = "Handwritten Text Image", justification='center', font = (None,25), size = (50,1))
    #],

    [
        gui.Graph(
            canvas_size=(1500, 500),
            graph_bottom_left=(0, 0),
            graph_top_right=(1500, 500),
            
            key="graph"
            
        )
    ],

    [
        gui.Text('',key = "result", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "probability", font=(None, 30), justification='center', size = (50,1))
    ],
        [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],
    [
        gui.Text('',key = "bos", font=(None, 30), justification='center', size = (50,1))
    ],


    [
        gui.FileBrowse(),
        gui.Submit('Run', key="OK", size=(5, 1)),
        gui.CloseButton('Quit', button_color=(
            'white', 'red'), key="Quit", size=(5, 1))
    ]
]

window = gui.Window('HYLT', layout, no_titlebar=True, element_justification = 'c', font=(None, 15)).Finalize()
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
    image = Image.open(workingPath)

    #image.thumbnail((1000, 1000))
    #image.save(workingPath)
    graph.DrawText("Handwritten Text Image Input", (760,300),font=(None, 40), color = 'red')
    graph.DrawImage(filename="../data/test.png", location=(600, 250))
    #window['img'].Update(workingPath)
    window.finalize()
    result = ai.main()
    name = "Recognized text: \" " + result[0] + " \""
    probability = "Probability: " + str(result[1])
    #graph.DrawText(name, (760,150),font=(None, 30), color = 'white')
    #graph.DrawText(probability, (720,70),font=(None, 30), color = 'white')
    window["result"].Update(name)
    window["probability"].Update(probability)
    #window["Handwritten Text Image"].Update("Handwritten Text Image Input")
    
    #window["graph"].Update('')

    #print(ai.main())
