health = int(input("Hp : "))
amountWeapon = input("무기의 개수 : ")

weapon = []
for i in range(int(amountWeapon)):
    infoWeapon = input("%d번째 무기 : " % (i+1))
    spInfoWeapon = infoWeapon.split(' ')

    weapon.append({'strength': spInfoWeapon[0], 'durability': spInfoWeapon[1]})

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j]['strength'] > arr[j + 1]['strength']:
                arr[j]['strength'], arr[j + 1]['strength'] = arr[j + 1]['strength'], arr[j]['strength']

bubble_sort(weapon)

count = 0
for i in weapon:
    for j in range(int(i['durability'])):
        if health <= 0:
            break
        else:
            health -= int(i['strength'])
            count += 1

print(count)
