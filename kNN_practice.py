#농구 선수들의 데이터로 kNN (K-fold: K 교차검증) 을 사용하여 포지션을 예측하는 알고리즘 연습. (이진분류)

#데이터 수집
import pandas as pd

df = pd.read_csv("..\git\machine_learning_study")
#수집된 데이터 샘플을 확인
df.head()

