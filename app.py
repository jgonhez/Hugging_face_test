from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt : str):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox( placeholder = "Introduzca texto a resumir" ,lines = 4)
    gr.Interface(fn = predict , inputs = textbox , outputs = "text")

demo.launch()