import os
import pandas as pd
import requests
from io import StringIO

# 1️⃣ 下载数据集并保存
def import_data(url, team_member=1):
    """
    下载数据集并保存到 data/ 目录，并以列表返回每行数据
    :param url: 数据集的 URL
    :param team_member: 团队成员编号 (1-4)
    :return: 字符串列表，每个字符串是一行数据
    """
    # 确保 data 目录存在
    os.makedirs("data", exist_ok=True)

    # 下载数据
    response = requests.get(url)
    response.raise_for_status()  # 确保下载成功

    # 确定文件路径
    file_path = f"data/dataset_M{team_member}.txt"
    
    # 保存文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)

    # 以列表返回每一行数据
    return response.text.splitlines()

# 2️⃣ 规范化日期格式
def standardize_dates(lines):
    """
    规范化数据集中的日期格式
    :param lines: 数据集的每行数据（字符串列表）
    :return: 处理后的 pandas DataFrame
    """
    # 使用 StringIO 将文本数据转换为 Pandas 可读格式
    data = pd.read_csv(StringIO("\n".join(lines)))

    # 找到包含日期的列（假设列名包含 'date' 或 'time'）
    date_columns = [col for col in data.columns if 'date' in col.lower() or 'time' in col.lower()]
    
    for col in date_columns:
        # 统一转换为 YYYY-MM-DD HH:MM:SS
        data[col] = pd.to_datetime(data[col], errors='coerce', infer_datetime_format=True)

    return data

# 示例用法：
url = "https://example.com/dataset.txt"  # 替换为实际数据集 URL
lines = import_data(url, team_member=1)  # 下载数据
df_cleaned = standardize_dates(lines)  # 处理日期格式
print(df_cleaned.head())  # 查看前几行
