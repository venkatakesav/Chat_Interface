import numpy as np
import gradio as gr
import google.generativeai as genai
from PIL import Image
import os
import io

api_key = "AIzaSyBtMmUSa0eOLjCKpf7yDlNHw-g92W-5d5c"

def sepia(text, input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return "hello World"

def gemini_model(text, input_img):
    genai.configure(api_key=api_key)

    img = Image.fromarray(input_img)

    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([text, img])
    return response.text

demo = gr.Interface(
    fn=gemini_model,
    inputs=["text", gr.Image()],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch()
