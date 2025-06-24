def linear_search(mevalar,target):

    for meva in range(len(mevalar)):
        if mevalar[meva] == target:
            return meva
        
    return -1


print(linear_search([3,2,1],1))