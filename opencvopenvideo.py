import cv2

# 打开视频文件
video = cv2.VideoCapture('src.mp4')

# 检查视频是否成功打开
if not video.isOpened():
    print("无法打开视频文件")
    exit()

frame_count = 0  # 帧计数器

while True:
    # 读取视频帧
    ret, frame = video.read()

    # 如果视频帧读取失败，退出循环
    if not ret:
        break

    # 在这里对视频帧进行处理，如预处理、保存等

    # 显示当前帧
    cv2.imshow("Frame", frame)
    cv2.imwrite("gir"+ str(frame_count) + ".jpg", frame)
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frame_count += 1

# 释放视频对象和关闭窗口
video.release()
cv2.destroyAllWindows()