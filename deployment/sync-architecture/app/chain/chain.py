from langchain_community.llms import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate


SYSTEM =""" - You are an assistant for a medical company
            - Your objective is to analyse and diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements.
            - You should format you output in a form of a lengthy report analysing and exmplaining the significanse of each measurments and how the measurments might affect you final jugment.
            """

PROMPT = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM),
            ("human", "{user_input}"),
        ]
    )

llm = LlamaCpp(
    model_path="../../models/phi/snapshots/c80d904a71b99a3eaeb8d3dbf164166384c09dc3/Phi-3-mini-4k-instruct-q4.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    verbose=False,  # Verbose is required to pass to the callback manager
)


llm_chain = PROMPT | llm