import gradio as gr
import requests
import json

# IP do servidor de predição da sua solução:
my_server_ip = "40.76.63.60"
# Porta do servidor de predição da sua solução, se nada foi alterado, deve ser 443:
my_server_port = "443"

def call_model_manager(model,loan_amount,term,property_value,income,Credit_Score,LTV,dtir1,loan_type,loan_limit,approv_in_adv,loan_purpose,Neg_ammortization,age,submission_of_application,Credit_Worthiness,open_credit,business_or_commercial,interest_only,lump_sum_payment,occupancy_type,total_units,credit_type,co_applicant_credit_type,Region):

    url = "http://{}:{}/predict".format(my_server_ip, my_server_port)
        
    data = [
        {
            "loan_amount": loan_amount,
            "term": term,
            "property_value": property_value,
            "income": income,
            "Credit_Score": Credit_Score,
            "LTV": LTV,
            "dtir1": dtir1,
            "loan_type": loan_type,
            "loan_limit": loan_limit,
            "approv_in_adv": approv_in_adv,
            "loan_purpose": loan_purpose,
            "Neg_ammortization": Neg_ammortization,
            "age": age,
            "submission_of_application": submission_of_application,
            "Credit_Worthiness": Credit_Worthiness,
            "open_credit": open_credit,
            "business_or_commercial": business_or_commercial,
            "interest_only": interest_only,
            "lump_sum_payment": lump_sum_payment,
            "occupancy_type": occupancy_type,
            "total_units": total_units,
            "credit_type": credit_type,
            "co_applicant_credit_type": co_applicant_credit_type,
            "Region": Region
        }
    ]
    
    if model == "Propensão à inadimplência":
        model = "modelo01"
    else:
        model = "modelo02"

    params={
        "model":model,
        "aluno": "Interface"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url,json=data,params=params,headers=headers,)
    resposta = json.loads(response.text.encode('utf8').decode())


    # response01 = requests.request("POST", url + f"?model=modelo01&aluno=a", headers=headers, data=conteudo)
    # respostas01 = json.loads(response01.text.encode('utf8').decode())
    # respostas01
    
    return resposta

def load_preset_fn():
    return [246500,300,238000,3060,712,103.57,60,"type3","cf","nopre","p3","neg_amm","65-74","to_inst","l1","nopc","nob/c","not_int","not_lpsm","pr","1U","CIB","EXP","south"]
def load_preset_fn2():
    return [676500,360,1098000,6600,534,61.61,54,"type3","cf","nopre","p1","neg_amm","55-64","not_inst","l1","nopc","nob/c","not_int","not_lpsm","pr","1U","CIB","EXP","south"]


def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                with gr.Tab("Inputs"):   
                    with gr.Row():
                        modelo = gr.Dropdown(["Propensão à inadimplência", "Clusterização e Classificação"], value='Propensão à inadimplência', label="Model", interactive=True)
                        with gr.Row():
                            load_preset1 = gr.Button("Load Preset 1 Cliente com risco inadimplência")
                            
                            load_preset2 = gr.Button("Load Preset 2 Cliente sem risco inadimplência")
                            
                    loan_amount = gr.Slider(16500, 3576500, value=16500, label="loan_amount", info="Choose between 2 and 20", interactive=True)
                    term = gr.Slider(96, 360, value=96, label="term", info="Choose between 2 and 20", interactive=True)
                    property_value = gr.Slider(8000, 16508000, value=8000, label="property_value", info="Choose between 2 and 20", interactive=True)
                    income = gr.Slider(0, 578580, value=0, label="income", info="Choose between 2 and 20", interactive=True)
                    Credit_Score = gr.Slider(500, 900, value=500, label="Credit_Score", info="Choose between 2 and 20", interactive=True)
                    LTV = gr.Slider(0.97, 7831.25, value=0.97, step=0.01, label="LTV", info="Choose between 2 and 20", interactive=True)
                    dtir1 = gr.Slider(5, 61, value=5, step=1, label="dtir1", info="Choose between 2 and 20", interactive=True)
                    
                    loan_type = gr.Dropdown(["type1", "type2", "type3"], label="loan_type", info="Will add more animals later!", interactive=True)
                    loan_limit = gr.Dropdown(["cf", "ncf"], label="loan_limit", info="Will add more animals later!", interactive=True)
                    approv_in_adv = gr.Dropdown(["nopre", "pre"], label="approv_in_adv", info="Will add more animals later!", interactive=True)
                    loan_purpose = gr.Dropdown(["p1", "p2", "p3","p4"], label="loan_purpose", info="Will add more animals later!", interactive=True)
                    Neg_ammortization = gr.Dropdown(["not_neg", "neg_amm"], label="Neg_ammortization", info="Will add more animals later!", interactive=True)
                    age = gr.Dropdown(["<25", "25-34", "35-44", "45-54", "55-64", "65-74",">74"], label="age", info="Will add more animals later!", interactive=True)
                    submission_of_application = gr.Dropdown(["to_inst", "not_inst"], label="submission_of_application", info="Will add more animals later!", interactive=True)
                    Credit_Worthiness = gr.Dropdown(["l1", "l2"], label="Credit_Worthiness", info="Will add more animals later!", interactive=True)
                    open_credit = gr.Dropdown(["nopc", "opc"], label="open_credit", info="Will add more animals later!", interactive=True)
                    business_or_commercial = gr.Dropdown(["nob/c", "b/c"], label="business_or_commercial", info="Will add more animals later!", interactive=True)
                    interest_only = gr.Dropdown(["not_int", "int_only"], label="interest_only", info="Will add more animals later!", interactive=True)
                    lump_sum_payment = gr.Dropdown(["not_lpsm", "lpsm"], label="lump_sum_payment", info="Will add more animals later!", interactive=True)
                    occupancy_type = gr.Dropdown(["ir", "pr", "sr"], label="occupancy_type", info="Will add more animals later!", interactive=True)
                    total_units = gr.Dropdown(["1U", "2U", "3U", "4U"], label="total_units", info="Will add more animals later!", interactive=True)
                    credit_type = gr.Dropdown(["CIB", "CRIF", "EXP", "EQUI"], label="credit_type", info="Will add more animals later!", interactive=True)
                    co_applicant_credit_type = gr.Dropdown(["CIB", "EXP"], label="co_applicant_credit_type", info="Will add more animals later!", interactive=True)
                    Region = gr.Dropdown(["North", "south", "central","North-East"], label="Region", info="Will add more animals later!", interactive=True)

            
            with gr.Column():
                with gr.Tab("Output"):   
                    submit_button = gr.Button("Send to Model")
                    output = gr.JSON(label="Model Output")


        load_preset1.click(
            fn=load_preset_fn,
            inputs=[],
            outputs=[loan_amount,term,property_value,income,Credit_Score,LTV,dtir1,loan_type,loan_limit,approv_in_adv,loan_purpose,Neg_ammortization,age,submission_of_application,Credit_Worthiness,open_credit,business_or_commercial,interest_only,lump_sum_payment,occupancy_type,total_units,credit_type,co_applicant_credit_type,Region]
        )

        load_preset2.click(
            fn=load_preset_fn2,
            inputs=[],
            outputs=[loan_amount,term,property_value,income,Credit_Score,LTV,dtir1,loan_type,loan_limit,approv_in_adv,loan_purpose,Neg_ammortization,age,submission_of_application,Credit_Worthiness,open_credit,business_or_commercial,interest_only,lump_sum_payment,occupancy_type,total_units,credit_type,co_applicant_credit_type,Region]
        )

        submit_button.click(
            fn=call_model_manager,
            inputs=[modelo,loan_amount,term,property_value,income,Credit_Score,LTV,dtir1,loan_type,loan_limit,approv_in_adv,loan_purpose,Neg_ammortization,age,submission_of_application,Credit_Worthiness,open_credit,business_or_commercial,interest_only,lump_sum_payment,occupancy_type,total_units,credit_type,co_applicant_credit_type,Region],
            outputs=[output]
        )

    demo.launch()

if __name__ == "__main__":
    main()
