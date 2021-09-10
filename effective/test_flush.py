import time
if __name__ == '__main__':
    print("hello ", end='', flush=True)
    print(" world", flush=True)
    print("hello\b\b\bHowdy")

    # for i in range(10000):
    #     print('{:s}\r'.format(''), end='', flush=True)
    #     time.sleep(0.001)
    #     print('Loading index: {:d}/10000'.format(i+1), end='', flush=True)
