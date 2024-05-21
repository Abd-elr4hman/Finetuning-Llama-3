from llama_cpp import Llama



if __name__ =="__main__":
    llm = Llama.from_pretrained(
        repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF",
        filename="*q8_0.gguf",
        verbose=False
    )
    SYSTEM ="""
            - You are an assistant for a medical company
            - Your objective is to analyse and diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements.
            - You should format you output in a form of a lengthy report analysing and exmplaining the significanse of each measurments and how the measurments might affect you final jugment.
            """

    example ="\n1. Number of times pregnant is 1.0.\n2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test is 85.0.\n3. Diastolic blood pressure (mm Hg) is 66.0.\n4. Triceps skin fold thickness (mm) is 29.0.\n5. 2-Hour serum insulin (mu U/ml) is 0.0.\n6. Body mass index (weight in kg/(height in m)^2) is 26.6.\n7. Diabetes pedigree function is 0.351.\n8. Age (years) is 31.0.\n"
        
    response = llm.create_chat_completion(
        messages = [
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": "Give me a report of the patient status given theses mesurments: {}".format(example)
            }
        ]
    )
    print(response)
