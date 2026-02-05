import gradio as gr 



def f():
    return x+y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            xbox = gr.Dropdown(choices = [playerID], label = "Player")
            ybox = gr.Number(label = "Type in value of Y")
        with gr.Column():
            sumbox = gr.Number(label = "Sum of X and Y")
    
        
    
    xbox.change(fn = f, inputs = [xbox, ybox], outputs = [sumbox])
    ybox.change(fn = f, inputs = [xbox, ybox], outputs = [sumbox])

iface.launch()