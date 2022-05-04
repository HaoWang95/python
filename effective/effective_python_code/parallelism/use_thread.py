import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(f'execution: {i} is a factor of {number}')
            yield i  # got one factor


if __name__ == '__main__':
    numbers: list = [2461957, 40365436, 103556034]

    # This is single-threaded calculation example
    start_single_thread = time.time()
    factor_single_thread_result = []
    for n in numbers:
        temp = list(factorize(n))
        factor_single_thread_result.append(temp)

    print(f'result of factors: {factor_single_thread_result}')
    end_single_thread = time.time()
    single_thread_time_taken = end_single_thread - start_single_thread
    # time took is about 15.5s
    print(f'Single thread time taken: {single_thread_time_taken:.4f}')

    # consider using a multi-threading approach to achieve it