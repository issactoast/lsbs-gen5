import numpy as np

np.random.seed(258261505)
np.random.randint(1, 9) # 발표조
# np.random.randint(1, 4)  # 발표자
# np.random.permutation(9)+1


import numpy as np
np.random.seed(250707)

# 0~35까지 숫자 섞기
x=np.arange(1, 6)
numbers = np.random.permutation(x)
numbers[0:5]

# 앞에서 35개만 추출해서 7x5 형태로 reshape
teams = numbers.reshape(5, -1)

# 출력
print("팀 구성 (0이 있는 팀은 4명):\n")
for i, team in enumerate(teams, 1):
    count = 5 - (1 if 0 in team else 0)
    print(f"Team {i}: {team.tolist()} (인원 수: {count}명)")
