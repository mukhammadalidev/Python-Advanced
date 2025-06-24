mevalar = [1,4,5,15]
target = 15

def linear_search(mevalar,target):
    for x in mevalar:
        if x == target:
            return x #topildi
    return -1 #topilmadi


print(linear_search([23,12,43,78],79))