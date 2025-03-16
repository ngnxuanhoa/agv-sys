import cv2
import numpy as np

# Đọc hình ảnh bản đồ từ camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Chuyển ảnh sang grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Làm mờ ảnh để giảm nhiễu
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Nhận diện biên cạnh bằng Canny
edges = cv2.Canny(blurred, 50, 150)

# Hiển thị ảnh
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
