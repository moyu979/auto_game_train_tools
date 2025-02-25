from pynput.keyboard import Listener as kb_listener
from pynput.mouse import Listener as mouse_listener
from datetime import datetime
import os
import time
# 获取当前的日期和时间
current_time = datetime.now()
date=current_time.strftime("%Y_%m_%d_%H_%M_%S")
# 保存按键记录的文件路径
log_file = "data"
if not os.path.exists(log_file):
    os.mkdir(log_file)
log=open(os.path.join(log_file,f"{date}.txt"),"w")
log.write("movement,time,paras\n")
# 创建一个函数来处理按键按下事件
def on_press(key):
    timestamp=datetime.now().timestamp()
    log.write(f"'kb_p',{timestamp},{key}\n")
    # try:
    #     file.write(f"{key.char}\n")  # 记录按下的字符
    # except AttributeError:
    #     with open(log_file, "a") as file:
    #         file.write(f"{key}\n")  # 记录特殊按键，如 shift、enter 等

# 创建一个函数来处理按键释放事件
def on_release(key):
    timestamp=datetime.now().timestamp()
    log.write(f"'kb_r',{timestamp},{key}\n")
    if key == 'esc':  # 按下 escape 键退出监听
        return False

def on_move(x, y):
    timestamp=datetime.now().timestamp()
    log.write(f"'ms_m',{timestamp},{x},{y}\n")
    
def on_click(x, y, button, pressed):
    if pressed:
        timestamp=datetime.now().timestamp()
        log.write(f"'ms_p',{timestamp},{x},{y},{button}\n")
    else:
        timestamp=datetime.now().timestamp()
        log.write(f"'ms_r',{timestamp},{x},{y},{button}\n")
        #print(f"鼠标释放，位置：({x}, {y}), 按钮：{button}")

def on_scroll(x, y, dx, dy):
    timestamp=datetime.now().timestamp()
    log.write(f"'ms_sc',{timestamp},{x},{y},{dx},{dy}\n")
    #print(f"鼠标滚动，位置：({x}, {y}), 滚动：{dx}, {dy}")

# 启动键盘监听
kb=kb_listener(on_press=on_press, on_release=on_release)
kb.start()
ms=mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
ms.start()

# kb.join()
# ms.join()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("监听器停止")
    # 停止监听器
    kb.stop()
    ms.stop()