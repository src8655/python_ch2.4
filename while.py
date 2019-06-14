# else 는 while 조건에 의해 정상적으로 끝났을 때 실행함
# break로 했을 때 안함
count = 1
while count < 11:
    print(count, end=' ')
    # if count == 5:
    #     break
    count += 1
else:
    print('ok')


# break, continue, else문 적용
i = 0
while i < 10:
    i += 1
    if i < 5:
        continue

    if i >= 10:
        break

    print(i, end=' ')
else:
    # break : 실행안함
    # continue : 실행함(정상적인 종료)
    print('ok')
print()


# 무한루프
i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break

    i += 1
else:
    print('else block')
