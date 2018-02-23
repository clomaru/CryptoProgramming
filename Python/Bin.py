def bin(q):
    '''
    自然数mに対し、その2進数表示を求める
    :pram m: <int> 整数
    :return: <int> mの2進数表示
    '''
    ans = []
    while True:
        q, mod = divmod(q, 2)
        ans.insert(0, mod)
        if q == 0:
            break
    return ans

if __name__ == '__main__':
    num = int(input())
    print(bin(num))
