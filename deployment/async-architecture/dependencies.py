
def generate_report(llm_chain, question):
    response = llm_chain.invoke({"user_input": question})

    #write response to db
    with open("log.txt", mode="w") as report_file:
        content = f"{response}"
        report_file.write(content)