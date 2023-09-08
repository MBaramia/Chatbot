import openai
import gradio

openai.api_key = "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"
messages = [{"role": "system", "content": "You are a banking analyst who advises clients on optimal trading ideas for their investments."}]

def CustomChatGPT(AskMeAnything):
    messages.append({"role": "user", "content":AskMeAnything})
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=messages)
    ChatGPT_reply = response["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs="text" , title = "Mo's Chatbot")
demo.launch(share=True)