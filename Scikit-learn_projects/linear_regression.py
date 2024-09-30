import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# create sample data
X = np.array([100, 150, 200, 250, 300]).reshape(-1, 1)
y = np.array([500, 700, 1000, 1200, 1500])

# Create a linear model
model = LinearRegression()

# training model
model.fit(X, y)

# predict the price of house have 220m2
new_area = np.array([[200]])
predict_price = model.predict(new_area)

print("Giá nhà dự đoán cho căn nhà 220m2: ", predict_price[0])

# draw visualization
plt.scatter(X, y, color="blue", label="Dữ liệu thực tế")
plt.plot(X, model.predict(X), color="red", label="Đường hồi quy")
plt.xlabel("Diện tích (m2)")
plt.ylabel("Giá nhà (triệu đồng)")
plt.legend()
plt.show()