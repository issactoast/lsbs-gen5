import numpy as np
import pandas as pd

# 1) 데이터 로드 (palmerpenguins 패키지 권장, 없으면 seaborn 대체)
try:
    from palmerpenguins import load_penguins
    penguins = load_penguins()
except Exception:
    import seaborn as sns
    penguins = sns.load_dataset("penguins")

# 2) 사용 변수 선택 & 결측 제거
feature_cols = ["bill_length_mm", "bill_depth_mm"]
target_col = "body_mass_g"

df = penguins[feature_cols + [target_col]].dropna().reset_index(drop=True)

X = df[feature_cols].to_numpy(dtype=float)
y = df[target_col].to_numpy(dtype=float)

# 3) 학습/검증 분할 + 표준화
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_t = scaler.fit_transform(X_train)
X_test_t  = scaler.transform(X_test)

# 4) 모델 구성 (질문에 준 구조, 입력 차원=2)
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(542, activation='relu', input_shape=[X_train_t.shape[1]]),
    layers.Dense(542, activation='relu'),
    layers.Dense(542, activation='relu'),
    layers.Dense(542, activation='relu'),
    layers.Dense(542, activation='relu'),
    layers.Dense(1)  # 회귀 출력
])

model.compile(
    optimizer="adam",
    loss="mae"
)

# 5) 학습 
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    min_delta=0.001, # 개선으로 간주할 최소 손실 변화량
    patience=20,     # 개선이 없을 때 기다릴 에폭 수
    restore_best_weights=True, # 최소 손실 시점의 가중치 복원
)

history = model.fit(
    X_train_t, y_train,
    validation_split=0.2,
    epochs=500,
    batch_size=32,
    callbacks=[early_stopping],
    verbose=1
)


model.weights

# 6) 예측 프리뷰
y_pred = model.predict(X_test_t[:5]).flatten()
preview = pd.DataFrame({
    "bill_length_mm": X_test[:5, 0],
    "bill_depth_mm" : X_test[:5, 1],
    "y_true_body_mass_g": y_test[:5],
    "y_pred_body_mass_g": np.round(y_pred, 1),
})
print("\n예측 미리보기(5개):")
print(preview.to_string(index=False))
