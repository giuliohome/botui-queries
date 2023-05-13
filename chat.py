import openai
from my_secrets import SECRET_KEY
openai.api_key = SECRET_KEY

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]


# Front end web app
import gradio as gr
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    chat_history = []
    
    def user(user_message, history):
        # Get response from QA chain
        print(user_message)
        messages.append( {"role": "user", "content":user_message})
        response = openai.ChatCompletion.create(
        # {"answer": "chatgpt answer to this question: " + user_message}  # qa({"question": user_message, "chat_history": history})
              model="gpt-3.5-turbo",
              messages=messages
            )
        # print(response)
        gpt_msg = response["choices"][0]["message"]
        messages.append(gpt_msg) 
        # {"role": "assistant", "content":response})
        # Append user message and response to chat history
        history.append((user_message, gpt_msg["content"]))
        return gr.update(value=""), history
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(debug=True)
