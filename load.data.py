import pandas as pd  # 导入 pandas 库

# 读取数据集
file_path = "/Users/tyb/teat_w5m/formative task0227/formative-data-cleaning-task/query.csv"  # 你的数据文件路径

# 读取数据
df = pd.read_csv(file_path)  # 读取整个 CSV 文件

# 查看前 5 行，检查数据格式
print(df.head())

# 另存为新的 CSV 文件
df.to_csv("test.csv", index=False)  # 生成 test.csv，并去掉 Pandas 自动添加的索引列

