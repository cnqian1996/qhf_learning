import random

# 生成不重复的红球号码
def get_red_ball():
    red_balls = []
    while(len(red_balls) < 6):
        ball = random.randint(1, 33)
        if ball not in red_balls:
            red_balls.append(ball)
    return sorted(red_balls)

# 生成蓝球号码
def get_blue_ball():
    return random.randint(1,16)

# 输出选号结果
def print_result(red_balls, blue_ball):
    print("本期选号结果为：")
    print("红球号码：", end='')
    for ball in red_balls:
        print("{:02d}".format(ball), end=' ')
    print("蓝球号码：{:02d}".format(blue_ball))

# 运行程序
if __name__ == '__main__':
    red_balls = get_red_ball()
    blue_ball = get_blue_ball()
    print_result(red_balls, blue_ball)