"""
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，
鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""
for male_sum in range (1, 21):
    for female_sum in range (1, 34):
        chick_sum = 100 - male_sum - female_sum
        if male_sum * 5 + female_sum * 3 + chick_sum / 3 == 100:
            print("可买%d只公鸡，加%d只母鸡和%d只小鸡" % (male_sum, female_sum, chick_sum))