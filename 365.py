import time

def focus_clock(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        time.sleep(1)
        print(f"倒计时剩余时间: {i} 秒", end='\r')

    print("专注时间结束！")

# 设置专注时长为25分钟
focus_clock(25)
