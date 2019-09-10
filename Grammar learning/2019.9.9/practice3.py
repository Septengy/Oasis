"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
题目作者: 骆昊
程序作者: Sep
"""
score = float(input("请输入百分制成绩："))
if score > 100:
    print("无效成绩")
elif score >= 90 and score <= 100:
    print("您的等级制成绩为A")
elif score >= 80:
    print("您的等级制成绩为B")
elif score >= 70:
    print("您的等级制成绩为C")
elif score >= 60:
    print("您的等级制成绩为D")
elif score <= 60 and score >= 0:
    print("您的等级制成绩为C")
else:
    print("无效成绩")