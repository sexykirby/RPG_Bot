import secrets

# 卡片種類與機率（機率總和應為1）
card_pool = {
    "普通": 0.7,  # 70% 的機率抽到普通卡
    "罕見": 0.2,  # 20% 的機率抽到罕見卡
    "稀有": 0.08, # 8% 的機率抽到稀有卡
    "超稀有": 0.02 # 2% 的機率抽到超稀有卡
}

def draw_card():
    # 生成一個隨機數，從0到999（共1000個可能值）
    rand = secrets.randbelow(1000) / 1000
    cumulative_probability = 0.0

    # 決定卡片種類
    for rarity, probability in card_pool.items():
        cumulative_probability += probability
        if rand < cumulative_probability:
            return rarity

def simulate_draws(num_draws):
    results = []
    for _ in range(num_draws):
        results.append(draw_card())
    return results

# 模擬抽 10 張卡
draw_results = simulate_draws(10)
print(draw_results)