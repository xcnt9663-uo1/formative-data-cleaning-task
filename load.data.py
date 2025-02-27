import pandas as pd  # 导入 pandas 库

# 读取数据集（假设是 CSV 文件）
file_path = "query.csv"  # 替换为你的数据文件路径
df = pd.read_csv(file_path)  # 读取数据

# 查看前 5 行
print(df.head())
