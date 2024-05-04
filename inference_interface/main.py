import gradio as gr

def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    sentence = '{"prediction": [0,1,1],"proba": [[0.6220932006835938,0.37790676951408386],[0.13481587171554565,0.8651841282844543],[0.4999037981033325,0.5000962018966675]]}'
    return sentence

def main():
    with gr.Blocks() as demo:
            with gr.Row():
            
                with gr.Column():
                    with gr.Tab("Model1"):
                        quantity = gr.Slider(2, 20, value=4, label="Count", info="Choose between 2 and 20")
                        animal = gr.Dropdown(["cat", "dog", "bird"], label="Animal", info="Will add more animals later!")
                        countries = gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries", info="Where are they from?")
                        place = gr.Radio(["park", "zoo", "road"], label="Location", info="Where did they go?")
                        activity_list = gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity", info="Select activities they engaged in.")
                        morning = gr.Checkbox(label="Morning", info="Did they do it in the morning?")
                    with gr.Tab("Model2"):
                        quantity = gr.Slider(2, 20, value=4, label="Count", info="Choose between 2 and 20")
                        animal = gr.Dropdown(["cat", "dog", "bird"], label="Animal", info="Will add more animals later!")
                        countries = gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries", info="Where are they from?")
                        place = gr.Radio(["park", "zoo", "road"], label="Location", info="Where did they go?")
                        activity_list = gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity", info="Select activities they engaged in.")
                        morning = gr.Checkbox(label="Morning", info="Did they do it in the morning?")
                
                
                with gr.Column():
                    output = gr.JSON(label="Model Output")

            submit_button = gr.Button("Build Sentence")

            submit_button.click(
                fn=sentence_builder,
                inputs=[quantity, animal, countries, place, activity_list, morning],
                outputs=output
            )

    demo.launch()

if __name__ == "__main__":
    main()
