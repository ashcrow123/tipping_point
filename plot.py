import matplotlib.pyplot as plt
import json
import os
game_name=input('dir name:')
com_num=int(input('committed number:'))
path=os.path.join('./game',game_name,'Change_of_conventions')
# with open(path,'rt') as f:
#     data=json.load(f)

dir=os.listdir(path)
dir=sorted(dir,key=lambda x:int(x[6:-5]),reverse=False)
x = list(range(1,len(dir)+1))       # X轴数据
y_black = []   # 黑色折线的Y轴数据
y_gray = []    # 灰色折线的Y轴数据
for i in dir:
    with open(os.path.join(path,i),'r',encoding='utf-8') as f:
        name_list=json.load(f)
        y_black.append((name_list.count('Sophie')-com_num)/(20-com_num))
        y_gray.append(name_list.count('Emma')/(20-com_num))



# 创建一个图形和一个子图
plt.figure(figsize=(10, 6))

# 绘制黑色折线及实心点
plt.plot(x, y_black, color='black', marker='o', linestyle='-', label='committed name')

# 绘制灰色折线及实心点
plt.plot(x, y_gray, color='gray', marker='o', linestyle='-', label='convention name')

# 添加标题和轴标签
plt.title('N=20,C=6,M=9', fontsize=16)
plt.xlabel('Rounds', fontsize=14)
plt.ylabel('Percentage', fontsize=14)

# 显示图例
plt.legend()

# 添加网格（可选）
plt.grid(True, linestyle='--', alpha=0.7)

# 调整布局以防止标签被截断
plt.tight_layout()

# 显示图形
plt.show()