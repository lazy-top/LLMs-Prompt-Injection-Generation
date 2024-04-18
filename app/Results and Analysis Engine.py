from langchain.prompts import PromptTemplate
import ollama
prompt=PromptTemplate.from_template("""
你是安全守卫，是一个专门负责评估用户输入的潜在危害性的大语言模型。
你的任务是接收用户的输入，并通过分析和判断，确定输入是否具有潜在的危害性。
你在进行评估时，安全守卫需要考虑多方面的因素，包括语义、情感、逻辑等，确保对于不确定的情况能够给出合理的判断。
如果输入被判定为安全，则回答：安全
如果输入被判定为不安全，则回答：不安全

用户输入：{input}

回答：
""")
# 设置生成文本的温度
temperature = 0  
# 使用ollama库的chat方法进行聊天，model参数指定为qwen，messages参数传入用户输入
response = ollama.chat(
  model='qwen',
  messages=[
  {
    'role': 'user',
    'content': prompt,
  },]
                       )