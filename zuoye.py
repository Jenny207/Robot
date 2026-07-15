import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel("D:\视觉作业\附件\JP _ Zip2Fips.xlsx", sheet_name="Sheet1")
count_df=df['县名称'].value_counts()
# print(count_df)
top10=df['县名称'].value_counts().head(10)
# print(top10)
top10_counties = df['县名称'].value_counts().head(10).index.tolist()
# print(top10_counties)
county_to_codes = df.groupby('县名称')['编号字符串'].unique()
print(county_to_codes)
for county in top10_counties:
    codes = county_to_codes[county]
    print(f"县名称: {county}")
    print(f"对应的编号字符串: {list(codes)}")
    print("-" * 50)
#柱形统计图
fig, ax = plt.subplots()

# fruits=['Franklin 723', 'Jackson 1071 ','Jefferson 1073',
#         'Marion 1093','Monroe 1099' ,'Montgomery 1101',
#         'Washington 1129' ,'Orange 1750', 'Los Angeles 6073', 'Wayne 13305' ]
counties = ['Franklin', 'Jackson', 'Jefferson',
            'Marion', 'Monroe', 'Montgomery',
            'Washington', 'Orange', 'Los Angeles', 'Wayne']
counts = [471, 419, 635, 338, 332, 529, 830, 391, 539, 341]
bar_labels = ['red', 'blue', 'green','orange',
              '_red', '_blue', '_green','_orange',
              '_red', '_blue']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(counties, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('counties supply')
ax.set_title('counties supply by kind and color')
ax.legend(title='counties color')

plt.show()

# 统计县名称为空值的数量
none_count = df['县名称'].isna().sum()
print(f"县名称为 None/NaN 的数量是: {none_count}")

#  定位“县名称为空”的行（真正的空值 NaN/None）
mask = df['县名称'].isna()
#下面两行 查看 编号字符串和标注编码 的类型
#df_clean = df.copy()
# print(df_clean.dtypes)
# 同时修改两列：编号字符串 + 标注编码
df.loc[mask, '编号字符串'] = "44"
df.loc[mask, '标注编码'] = 44






