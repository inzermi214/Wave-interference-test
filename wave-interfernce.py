import numpy as np
import tkinter as tk
from tkinter import Canvas

def draw_grid():
    # 격자 그리기
    for i in range(0, 501, 50):  # X축 격자S
        canvas.create_line(i, 0, i, 400, fill='lightgray')
    for i in range(0, 401, 50):  # Y축 격자
        canvas.create_line(0, i, 500, i, fill='lightgray')

def plot_waves():
    # Canvas 초기화ZS
    canvas.delete("all")
    draw_grid()  # 격자 그리기
    freq = np.linspace(0, 10, 1000)  # 주파수 범위

    # 기본 주파수와 진폭 설정
    try:
        freq1 = float(freq1_var.get())
        freq2 = float(freq2_var.get())
        amp1 = float(amplitude1_var.get())
        amp2 = float(amplitude2_var.get())
    except ValueError:
        return  # 입력값이 올바르지 않으면 아무것도 하지 않음

    # 두 개의 파동 생성
    wave1 = amp1 * np.sin(2 * np.pi * freq1 * freq)
    wave2 = amp2 * np.sin(2 * np.pi * freq2 * freq)

    # 그래프 그리기
    for i in range(len(freq) - 1):
        # X축을 주파수로, Y축을 진폭으로 설정
        canvas.create_line(freq[i] * 50, 200 - wave1[i] * 50, freq[i + 1] * 50, 200 - wave1[i + 1] * 50, fill='red')
        canvas.create_line(freq[i] * 50, 200 - wave2[i] * 50, freq[i + 1] * 50, 200 - wave2[i + 1] * 50, fill='blue')

    # X축과 Y축 라벨 그리기
    canvas.create_text(250, 380, text="주파수 (Frequency)", font=("Arial", 12))
    canvas.create_text(20, 200, text="진폭 (Amplitude)", font=("Arial", 12), angle=90)

def start_animation():
    global running
    if not running:
        running = True
        update()

def stop_animation():
    global running
    running = False

def update():
    global frame
    if not running:
        return  # 애니메이션이 멈춘 경우 종료

    canvas.delete("all")
    draw_grid()  # 격자 그리기
    freq = np.linspace(0, 10, 1000)  # 주파수 범위

    # 사용자 입력값으로 파동 생성
    try:
        freq1 = float(freq1_var.get())
        freq2 = float(freq2_var.get())
        amp1 = float(amplitude1_var.get())
        amp2 = float(amplitude2_var.get())
    except ValueError:
        return  # 입력값이 올바르지 않으면 아무것도 하지 않음

    # 두 개의 파동 생성 (파동이 움직이는 효과)
    wave1 = amp1 * np.sin(2 * np.pi * freq1 * (freq - speed * frame / 10))
    wave2 = amp2 * np.sin(2 * np.pi * freq2 * (freq + speed * frame / 10))

    # 간섭 결과
    interference = wave1 + wave2

    # 그래프 그리기
    for i in range(len(freq) - 1):
        # X축을 주파수로, Y축을 진폭으로 설정
        canvas.create_line(freq[i] * 50, 200 - wave1[i] * 50, freq[i + 1] * 50, 200 - wave1[i + 1] * 50, fill='blue')
        canvas.create_line(freq[i] * 50, 200 - wave2[i] * 50, freq[i + 1] * 50, 200 - wave2[i + 1] * 50, fill='red')
        # 간섭 결과
        canvas.create_line(freq[i] * 50, 200 - interference[i] * 50, freq[i + 1] * 50, 200 - interference[i + 1] * 50, fill='green', width=2)

    frame += 1
    canvas.after(50, update)  # 다음 프레임을 요청

# tkinter GUI 설정
root = tk.Tk()
root.title("Wave Interference Simulator")

# 주파수와 진폭 초기값
freq1_var = tk.StringVar(value="1")
freq2_var = tk.StringVar(value="1")
amplitude1_var = tk.StringVar(value="1")
amplitude2_var = tk.StringVar(value="1")
speed = 0.15  # 파동 속도
frame = 0  # 애니메이션 프레임
running = False  # 애니메이션 상태

# GUI 구성
tk.Label(root, text="파동 1 주파수:").grid(row=0, column=0)
tk.Entry(root, textvariable=freq1_var).grid(row=0, column=1)

tk.Label(root, text="파동 1 진폭:").grid(row=1, column=0)
tk.Entry(root, textvariable=amplitude1_var).grid(row=1, column=1)

tk.Label(root, text="파동 2 주파수:").grid(row=2, column=0)
tk.Entry(root, textvariable=freq2_var).grid(row=2, column=1)

tk.Label(root, text="파동 2 진폭:").grid(row=3, column=0)
tk.Entry(root, textvariable=amplitude2_var).grid(row=3, column=1)

tk.Button(root, text="파동 표시", command=plot_waves).grid(row=4, columnspan=2)
tk.Button(root, text="시작", command=start_animation).grid(row=5, column=0)
tk.Button(root, text="정지", command=stop_animation).grid(row=5, column=1)

# Canvas 설정
canvas = Canvas(root, width=500, height=400)
canvas.grid(row=6, columnspan=2)

# 기본 파동 그리기
plot_waves()  # 초기 상태에서 기본 파동 그리기

root.mainloop()
