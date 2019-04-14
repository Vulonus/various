def solution(N):
    binaryGap = 0
    found = False
    gapLen = 0
    while N > 0:
        N //= 2
        if N % 2 == 0:
            gapLen += 1
            found = True
        elif gapLen > binaryGap or found:
            binaryGap = gapLen
            gapLen = 0

    print(binaryGap)


if __name__ == "__main__":
    print('Print longest binary gap for number: ')
    solution(int(input()))