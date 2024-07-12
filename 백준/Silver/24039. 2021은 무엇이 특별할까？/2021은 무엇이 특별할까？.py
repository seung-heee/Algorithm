prime_list = [2, 3]  # 소수 리스트

def find_next_prime(current_prime):
    while True:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:
            return current_prime

num = int(input())

index = 2
while True:
    product = prime_list[index - 1] * prime_list[index - 2]
    if product <= num:
        prime_list.append(find_next_prime(prime_list[-1]))
        index += 1
    else:
        print(product)
        break
