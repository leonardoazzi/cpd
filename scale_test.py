## UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
## INSTITUTO DE INFORMÁTICA
## INF01124 - CLASSIFICAÇÃO E PESQUISA DE DADOS 
## LABORATÓRIO 1

## LEONARDO AZZI MARTINS, 00323721
## 2022/1

# -----------------------------------------------
#   main
# -----------------------------------------------
def main():
        
    with open('entrada2.txt') as f:
        lines = f.readlines()

        vecs = []
        numElem = []

        for i in lines:
            elem = list(i.split(" "))
            elem.remove('\n')

            elem = [eval(x) for x in elem]

            numElem.append(elem[0])
            elem.pop(0)
            vecs.append(elem)
    
    # shellsort(vecs, numElem)

if __name__ == "__main__":
    main()
