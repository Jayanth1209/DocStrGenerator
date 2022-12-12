import os
import openai

def write_function_as_string(text_file: str,python_version:str) -> str:
    with open(text_file,'r') as file:
        content = file.read()
    with open(text_file,'w') as file:
        file.seek(0,0)
        file.write(f"# Python {python_version}".rstrip('\r\n')+'\n'+\
        content+'\n'+'# An elaborate, high quality docstring for the above function:'.rstrip('\r\n')+\
        '\n'+'"""'.rstrip('\r\n'))
    with open(text_file,'r') as file:
        return file.read().replace('\n','\n')

def create_docstring(function_as_string: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
    model="code-davinci-002",
    prompt=function_as_string,
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", "\"\"\""]
    )
    with open('docstring.txt','w') as file:
        file.write(response['choices'][0]['text'])


if __name__=='__main__':
    function_as_string = write_function_as_string('simple.txt','3.7')
    create_docstring(function_as_string)