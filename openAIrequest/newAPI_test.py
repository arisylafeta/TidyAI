import os
import openai
openai.api_key = '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'
model_engine = "text-davinci-003"

'''
def completionQuery():
  prompt = ('Write me a bio (a text introduction about myself) using multiple inputs:/n The tone of voice to use./n Some personal information:/n - My full name/n - My education level/n - My gender/n Some examples of other bio./n Informations I want to emphasize./n Then, only after my answer, generate the bio./n')

  text_input = ('Tone of voice: professional/n Full name: Manuel Cecere Palazzo/n Education level: Ms student/n Gender: Male/n Bio examples:/n -Creative and Technical ML and Web Development Professional. Effectively provides end-to-end service, collaborates in projects that involve database and building user-facing websites. Proficient working with front and back ends of a website or application. Positive and adaptable, works cooperatively with team members and strives towards achieving a common goal. Demonstrates great interest and passion in learning new programming languages./n Specific information:/n - Passionate for AI for social good/n - Binge reader/n - Extrovert/n')

  prompt += "/n" + text_input

  completion = openai.Completion.create(
                                    engine = model_engine,
                                    prompt = prompt,
                                    max_tokens = 1024,
                                    n = 1,
                                    temperature = 0.1,
                                        )

  print(completion.choices[0].text)
'''

def chatQuery():
  messages = [
 {"role": "system", "content" : "You're a kind helpful assistant"}
]
  content = ('Write me a bio (a text introduction about myself) using multiple inputs:/n The tone of voice to use./n Some personal information:/n - My full name/n - My education level/n - My gender/n Some examples of other bio./n Informations I want to emphasize./n Then, only after my answer, generate the bio./n')
  text_input = ("Tone of voice: professional/n Full name: Manuel Cecere Palazzo/n Education level: Ms student/n Gender: Male/n Bio examples:/n -Creative and Technical ML and Web Development Professional. Effectively provides end-to-end service, collaborates in projects that involve database and building user-facing websites. Proficient working with front and back ends of a website or application. Positive and adaptable, works cooperatively with team members and strives towards achieving a common goal. Demonstrates great interest and passion in learning new programming languages./n Specific information:/n - Passionate for AI for social good/n - Binge reader/n - Extrovert/n")

  content += text_input
  messages.append({"role": "user", "content": content})

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

  chat_response = completion.choices[0].message.content
  print(f'ChatGPT: {chat_response}')
  print('AOO!')