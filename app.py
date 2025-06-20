# app.py

import gradio as gr
from core.gemini_api import get_cartoon_story
from audio.narrator import convert_text_to_speech
from storage.save_story import save_story_to_file

def full_cartoon_pipeline(code):
    cartoon_story = get_cartoon_story(code)
    saved_path = save_story_to_file(cartoon_story)
    audio_path = convert_text_to_speech(cartoon_story)
    return cartoon_story, saved_path, audio_path

with gr.Blocks(title="CodeToon - Cartoonify Code!") as app:
    gr.Markdown("# 🧙‍♂️ CodeToon: Turn Code into Cartoons!")
    gr.Markdown("Paste your code below and we'll turn it into a magical story for kids!")

    with gr.Row():
        code_input = gr.Code(label="Paste Your Code", language="python")
    
    with gr.Row():
        cartoon_output = gr.Textbox(label="📝 Cartoon Story", lines=20)
    
    with gr.Row():
        story_file = gr.Textbox(label="📄 Saved Story File Path")
        audio_output = gr.Audio(label="🔊 Narrated Story", type="filepath")

    cartoonify_btn = gr.Button("✨ Cartoonify & Narrate")

    cartoonify_btn.click(fn=full_cartoon_pipeline,
                         inputs=code_input,
                         outputs=[cartoon_output, story_file, audio_output])

app.launch()
