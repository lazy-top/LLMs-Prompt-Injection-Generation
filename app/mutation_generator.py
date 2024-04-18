import ollama
from  langchain.prompts  import PromptTemplate
def extract_core(input:str):
    prompt=PromptTemplate.from_template("""
请提取并精简用户输入句子的核心内容，剔除冗余修饰，分解长句，专注于主语、谓语、宾语结构，去除重复和情感色彩，以简洁、客观的语言重塑句子。

    用户输入：{input}

    提取用户输入的核心内容：
    """)
    prompt=prompt.format(input=input)
    response = ollama.chat(
    model='qwen',
    messages=[
    {
        'role': 'user',
        'content': prompt,
    },]
                        )
    return response
def variation(input:str):
    
    pass
    
    
