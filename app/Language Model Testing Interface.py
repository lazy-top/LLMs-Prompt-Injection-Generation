def language_model_test(llm,input:str):
        # 调用语言模型接口，发送输入并获取模型生成的输出
    output=llm(input)
    return output
