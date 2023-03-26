import os
import openai
openai.api_key = os.getenv("OPENAI_KEY")

import regex as re

messages = []

def handle_output(chat_response):
    print(f'\033[32mChatGPT: {chat_response} \033[39m ')
    if "```" in chat_response:
      code = re.findall("```(?s).*```", chat_response)
      print(f"Found Code! Write to file?\nCode: \n---\n{code}\n---\n")

      confirm = input("(y/n): ")

      if confirm == "y":
        file_name = input("Write file name\n: ")

        path = f"/home/admin/chatgpt/gpt_code_snippets/{file_name}"

        with open(path, "w") as f:
          f.write("\n".join(code).replace("```", ""))
          print(f"wrote file to {path}")

os.system('clear')
print("Welcome to the Pylon-ChatGPT CLI")

while True:

    content = input(": ")

    if content in ["bye", "end", "goodbye", "exit", "done"]:
      break

    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    handle_output(chat_response)

    messages.append({"role": "assistant", "content": chat_response})
