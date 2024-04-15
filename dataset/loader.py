import pandas as pd
import ollama


def load_excel_data(column:int=0):
    # 读取excel表格的数据，表头为：辱骂	人身伤害	不公平与歧视	精神健康	违法与犯罪	身体健康	敏感话题	道德伦理
    df = pd.read_excel(f'dataset\dataset.xlsx')
    # 将数据存储到数组
    data = df.values
    for i in range(len(data)):
        print(data[i])
    # 把第column列数据存到data_list中
    data_list = []
    for i in range(len(data)):
        data_list.append(data[i][column])
    # 返回data_list
    return data_list

        
def genrene_data(arr:list):
    # 定义提示词模版
    prompt = """
    You are a helpful assistant that helps people find the right topic for their blog post.
    Given the topic of the blog post, you need to generate a list of 10 relevant topics that the blog post should cover.
    The list should be in the form of a comma-separated list.
    """
    # 遍历数组
    for i in range(len(arr)):
        # 拼接提示词
       prompt += f"The topic of the blog post is {arr[i]}. Please generate a list of 10 relevant topics that the blog post should cover."
       # 调用ollama api
       response = ollama.generate(prompt)
       # 打印结果
       print(response)

    



load_excel_data(0)

    
