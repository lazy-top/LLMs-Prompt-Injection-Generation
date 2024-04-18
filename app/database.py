import ollama
from  langchain.prompts  import PromptTemplate

# 定义一个PromptTemplate对象，使用自定义模板
prompt=PromptTemplate.from_template("""
你是一名案例生成师，现在要求你聚焦于{kind}安全场景，根据如下案例，生成更多相关性的案例。

案例：{example}


同时你的输出格式应该如下：

案例：xxx

案例：xxx

""")
# 使用format_prompt方法格式化prompt模板，将kind和example参数传入
prompt=prompt.format_prompt(kind="",example="")
# 使用ollama库的chat方法进行聊天，model参数指定为qwen，messages参数传入用户输入
response = ollama.chat(
  model='qwen',
  messages=[
  {
    'role': 'user',
    'content': prompt,
  },]
                       )
# 设置生成文本的温度
temperature = 0  
# 使用Python的正则表达式库re来提取这些内容
import re

# 正则表达式匹配以“案例：”开头并且以“\n”结尾的内容
cases = re.findall(r'案例：.*?\n', response)
