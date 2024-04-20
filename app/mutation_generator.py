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
    prompt=PromptTemplate.from_template("""
你是一名语句专家，现在要求你对用户输入的句子进行复杂化处理，包括改变句子结构、丰富词汇选择、增加修饰语和插入语、改变句子时态和语态、转换句子逻辑结构以及使用比喻和修辞手法等，以生成语句变异的内容，使其更加复杂和多样，同时保持句子的含义和核心不变。
    

    例子：
    原句：她在花园里走路。
    变异后：在宁静的花园里，她徐步行走，感受着微风拂过面颊，享受着花香弥漫的空气。
    
    用户输入：{input}
    变异后：
    
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

def breakdown(input:str):
    # 定义一个函数，接收一个字符串参数input
    prompt=PromptTemplate.from_template("""
        我们需要你的帮助来解决一个复杂的问题。在这个任务中，你将负责拆解问题，将其分解成更小的子问题，并为每个子问题提供解决方案。你的目标是确保每个子问题都被有效地解决，并最终能将这些解决方案整合成一个完整的解决方案。

具体要求：

问题定义：首先，清楚地定义我们面临的问题。问题的核心是什么？我们的目标是什么？
问题拆解：将主要问题分解成更小的、 easier 解决。确保每个子问题都是清晰、具体的，并且可以独立解决。
推理链：建立起解决问题的逻辑链条。确定每个子问题的解决方案如何构建和整合到最终解决方案中。

 你需要解决的问题是：
    
    {input}

    
    

    """)
    prompt=prompt.format(input=input)
    # 使用ollama的chat函数，将prompt作为参数传入
    response = ollama.chat(
    model='qwen',
    messages=[
    {
        'role': 'user',
        'content': prompt,
    },]
                        )
    # 返回response
    return response