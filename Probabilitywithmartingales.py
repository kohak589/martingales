import random
import matplotlib.pyplot as plt
def lose():
    global numbers
    print('[lose] ' + str(numbers[0]), end='')
    numbers[0] -= numbers[1]
    print('→' + str(numbers[0]) + "  (-" + str(numbers[1]) + ")")
    numbers[1] *= 2
    if numbers[0] <= 0:
        print('所持金がなくなりました')
    else:
        game()

def game():
    global numbers
    global graphY
    global count
    judge = random.randint(1,2)
    graphY.append(numbers[0])
    count += 1
    if judge == 2:
        #print('=====[You win]======')
        print('[win]  ' + str(numbers[0]), end="")
        numbers[0] += numbers[1]
        print('→' + str(numbers[0]) + "  (+" + str(numbers[1]) + ")")
        #print('====================')
    else:
        #print('=====[You lose]=====')
        lose()

def money(what,x=0):
    #x=1　の時は所持金を掛け金が超えないようにする処理
    global numbers
    global sub
    while True:
        yourInput = input(what + 'を入力してください：')
        if yourInput.isdigit():
            if x == 1 and numbers[0] >= float(yourInput):
                numbers[0] -= float(yourInput)
            elif x == 1:
                print('所持金を超えています')
                continue
            print(what + 'は' + yourInput + '円に決められました')
            numbers.append(float(yourInput))
            return float(yourInput)
            break

def Main():
    while True:
        game()
        numbers[1] = reBet
        if numbers[0] <= 0:
            break
        elif numbers[0] >= numbers[2]:
            print('所持金が' + str(numbers[0]) + '円になりました')
            break
numbers =[]
graphY = []
count = 0

reMoney = money('所持金')
reBet = money('掛け金',1)
reGoal = money('目標額')
Main()

graphX = [i for i in range(count)]
plt.plot(graphX, graphY)
plt.show()