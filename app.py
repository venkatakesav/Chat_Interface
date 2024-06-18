import numpy as np
import gradio as gr
import google.generativeai as genai
from PIL import Image
import os
import io
import json

api_key = "AIzaSyBtMmUSa0eOLjCKpf7yDlNHw-g92W-5d5c"

with open("database.json", "r") as fp:
    data = json.load(fp)

def gemini_model(text, input_img):
    input_img = Image.open(input_img)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([text, input_img])
    return response.text

def echo(message, history):
    file_path = message["files"][0]
    output = ""
    for entry in data:
        if file_path.split("/")[-1] == entry["image"].split('/')[-1]:
            output = entry["conversation"][0]["a"]
    print("Message", message)
    return output

demo = gr.ChatInterface(
    fn=echo,
    examples=[{"text": "Describe the Image:", "files": ["images/bahubali.png"]}, \
              {"text": "Biryani", "files": ["images/biryani.png"]}, \
              {"text": "Kali", "files": ["images/kali.png"]}, \
              {"text": "Narasimha", "files": ["images/narasimha.png"]}, \
              {"text": "Salman Khan", "files": ["images/Salkhan.png"]}, \
              {"text": "Siva", "files": ["images/siva.png"]}, \
              {"text": "Statue Of Unity", "files": ["images/statueunity.png"]}, \
              ],
    title="Chat Interface Demo",
    multimodal=True,
)

if __name__ == "__main__":
    demo.launch()
