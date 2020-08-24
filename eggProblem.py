
def eggProblem(num_egg, num_floor):
    valueTable = [[j + 1 if i==0 else 0 for i in range(num_egg)] for j in range(num_floor)]
    for i in range(num_egg):
        valueTable[0][i] = 1
    
    for i in range(1, num_egg):
        for j in range(1, num_floor):
            k = range(1, j + 1)
            best_val = min([max(valueTable[try_floor - 1][i - 1], valueTable[j - try_floor - 1][i]) + 1 for try_floor in k])
            valueTable[j][i] = best_val
    return best_val
            

if __name__ == "__main__":
    num_egg = 2
    num_floor = 100
    print(eggProblem(num_egg, num_floor))