def generate_report(analysis_list):
    results = 0  # 初始化结果计数器

    # 遍历分析列表，计算类型为'True'的项的数量
    for item in analysis_list:
        if(item.get('type')=='True'):  # 如果项的类型为'True'
           results=results+1  # 增加结果计数器的值
    results=results/len(analysis_list)  # 计算比例
    return results  # 返回结果

