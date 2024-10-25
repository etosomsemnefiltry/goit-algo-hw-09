import timeit

def change_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin  # Сколько монет данного номинала
            result[coin] = num_coins
            amount -= num_coins * coin  # Уменьшаем сумму на использованные монеты

    return result

def change_coins_dynamic(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 монет для суммы 0

    # Для каждой суммы от 1 до amount находим мин количество монет
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Восстанавливаем набор монет
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break

    return result

amount = 8323

greedy_time = timeit.timeit(lambda: change_coins_greedy(amount), number=100)
dp_time = timeit.timeit(lambda: change_coins_dynamic(amount), number=100)


print(f"\nЖадный алгоритм - {greedy_time}:", change_coins_greedy(amount))
print(f"Динамическое программирование - {dp_time}:", change_coins_dynamic(amount))

