import cv2
import pytesseract

# 读取图片
image = cv2.imread('C:\\Users\\wenjin\\Desktop\\pythontools\\123.jpg')

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化处理
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
#print(cv2.__version__)
# 设置Tesseract路径（如果必要）
# pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract>'
cv2.imshow('binary_image', binary_image)
cv2.waitKey(0)
# 执行OCR
text = pytesseract.image_to_string(binary_image, lang='chi_sim')

# 打印结果
print(text)