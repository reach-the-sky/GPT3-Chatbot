import openai as ai

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"Human: {question}\nAI: {answer}\n"
    return chat_log

if __name__ == "__main__":
    ai.api_key = ""

    completion = ai.Completion()

    start_chat_log = """Human: Hello, I am Human.
    AI: Hello, human I am openai gpt3.
    Human: How are you?
    AI: I am fine, thanks for asking. 
    """

    train = input("\nDo you want to train the openai chatbot (True/False): ")
    if(train == "True"):
        print("\n(To stop the training enter stop in the qestion)\n")
        while(True):
            question = input("Question: ")
            if question == "stop":
                break
            answer = input("Answer: ")
            start_chat_log = modify_start_message(start_chat_log,question,answer)
            print("\n")

    question = ""
    print("\nEnter the questions to openai (to quit type \"stop\")")
    while True:
        question = input("Question: ")
        if question == "stop":
            break
        print("AI: ",chat(question,start_chat_log))