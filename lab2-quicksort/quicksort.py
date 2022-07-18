## UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
## INSTITUTO DE INFORMÁTICA
## INF01124 - CLASSIFICAÇÃO E PESQUISA DE DADOS 
## LABORATÓRIO 1

## LEONARDO AZZI MARTINS, 00323721
## 2022/1

# -----------------------------------------------
#   Particionador - Mediana
# -----------------------------------------------
def partitioner_median(C):

    for vec in C:
        # for j in i:
        #     print(j, end=" ")
        print("primeiro: ", vec[0])
        print("meio: ", vec[len(vec)//2])
        print("ultimo: ", vec[len(vec)-1])

        ini = 0
        mei = len(vec)//2
        fim = len(vec)-1

        a = vec[ini]
        b = vec[mei]
        c = vec[fim]

        if(a < b):
            if(b < c):
                medianIndex = mei
            else:
                if(a < c):
                    medianIndex = fim
                else:
                    medianIndex = ini


# -----------------------------------------------
#   Partição - LOMUTO
# -----------------------------------------------
def partition_lomuto(C, left, right):
    chave = C[left]
    storeindex = left + 1

    i = left + 1
    for i in right:
        if(C[i] < chave):
            C[i] = C[storeindex]
            storeindex = storeindex + 1

        C[left] = C[storeindex-1]

        if (i <= right):
            i = i + 1

# -----------------------------------------------
#   main
# -----------------------------------------------
def main():
        
    with open('entrada-quicksort.txt') as f:
        lines = f.readlines()

        vecs = []
        numElem = []

        for i in lines:
            elem = list(i.split(" "))
            
            if '\n' in elem:
                elem.remove('\n')

            elem = [eval(x) for x in elem]

            numElem.append(elem[0])
            elem.pop(0)
            vecs.append(elem)

        partitioner_median(vecs)

if __name__ == "__main__":
    main()