import cv2
import numpy as np

# 加载OpenPose模型
net = cv2.dnn.readNetFromTensorflow('path/to/openpose/model.pb')

# 加载输入图像
image = cv2.imread('path/to/input/image.jpg')

# 执行前向传递
blob = cv2.dnn.blobFromImage(image, 1.0, (368, 368), (127.5, 127.5, 127.5), swapRB=True, crop=False)
net.setInput(blob)
output = net.forward()

# 定义关键点连接
POSE_PAIRS = [
    [1, 2], [1, 5], [2, 3], [3, 4], [5, 6], [6, 7], [1, 8], [8, 9], [9, 10],
    [1, 11], [11, 12], [12, 13], [1, 0], [0, 14], [14, 16], [0, 15], [15, 17]
]

# 提取关节位置
points = []
for i in range(18):  # 18个关键点
    heatMap = output[0, i, :, :]
    _, conf, _, point = cv2.minMaxLoc(heatMap)
    x = (image.shape[1] * point[0]) / output.shape[3]
    y = (image.shape[0] * point[1]) / output.shape[2]
    points.append((int(x), int(y)))

# 在图像上绘制关节位置和连接线
for i, point in enumerate(points):
    cv2.circle(image, point, 5, (0, 255, 0), -1)
    cv2.putText(image, str(i), point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]
    if points[partA] and points[partB]:
        cv2.line(image, points[partA], points[partB], (255, 0, 0), 2)

# 显示结果图像
cv2.imshow('Joints', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
