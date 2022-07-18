## UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
## INSTITUTO DE INFORMÁTICA
## INF01124 - CLASSIFICAÇÃO E PESQUISA DE DADOS 
## LABORATÓRIO 1

## LEONARDO AZZI MARTINS, 00323721
## 2022/1

# -----------------------------------------------
#   SHELL, potências de 2
# -----------------------------------------------
def shell_pot(nElem, vec_pot, fw):
    
    h = (int(nElem)//2)

    print(*vec_pot, "    SEQ=SHELL")


    for el in vec_pot:
        fw.write("%s " % el)
        
    fw.write("SEQ=SHELL\n")

    while h > 0:
        
        for i in range(h, nElem):
            t = vec_pot[i]
            j = i

            while j >= h and vec_pot[j-h] > t:
                vec_pot[j] = vec_pot[j-h]
                j -= h
            vec_pot[j] = t

        print(*vec_pot,"    INCR="+str(h))

        for el in vec_pot:
            fw.write("%s " % el)
        fw.write("INCR=%s\n" % str(h))

        h = h//2

# -----------------------------------------------
#   KNUTH, h < N/3 
# -----------------------------------------------
def shell_knuth(nElem, vec_knuth, fw):
    
    N = int(nElem)
    h = 1

    print(*vec_knuth, "    SEQ=KNUTH")

    for el in vec_knuth:
        fw.write("%s " % el)
    fw.write("SEQ=KNUTH\n")

    while h < N/3:
        h = 3 * h + 1;
    while h >= 1:
        for i in range(h, nElem):
            t = vec_knuth[i]
            j = i

            while j >= h and vec_knuth[j-h] > t:
                vec_knuth[j] = vec_knuth[j-h]
                j -= h
            vec_knuth[j] = t

        print(*vec_knuth,"    INCR="+str(h))

        for el in vec_knuth:
            fw.write("%s " % el)
        fw.write("INCR=%s\n" % str(h))
            
        h = h//3

# -----------------------------------------------
#   CIURA 
# -----------------------------------------------
def shell_ciura(nElem, vec_ciura, fw):

    print(*vec_ciura, "    SEQ=CIURA")

    for el in vec_ciura:
        fw.write("%s " % el)
    fw.write("SEQ=CIURA\n")
    

    # CIURA (espelhada)
    ciuraSeq = [1750, 701, 301, 132, 57, 23, 10, 4, 1]

    for seq in ciuraSeq:
        while seq <= nElem:
            h = seq
        
            for i in range(h, nElem):
                t = vec_ciura[i]
                j = i

                while j >= h and vec_ciura[j-h] > t:
                    vec_ciura[j] = vec_ciura[j-h]
                    j -= h
                vec_ciura[j] = t


            print(*vec_ciura,"    INCR="+str(h))

            for el in vec_ciura:
                fw.write("%s " % el)
            fw.write("INCR=%s\n" % str(h))

            break

# -----------------------------------------------
#   Execução do SHELLSORT
# -----------------------------------------------
def shellsort(v, num_elem):
    with open('saida1.txt', 'w') as file:

        for vec, quantElem in zip(v, num_elem): # Itera em paralelo a lista de vetores e lista de quantidades de elementos em cada vetor
            
            vec_p = vec[:]
            shell_pot(quantElem, vec_p, file)

            vec_k = vec[:]
            shell_knuth(quantElem, vec_k, file)
            
            vec_c = vec[:]
            shell_ciura(quantElem, vec_c, file)

# -----------------------------------------------
#   main
# -----------------------------------------------
def main():
        
    with open('entrada1.txt') as f:
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
    
    shellsort(vecs, numElem)

if __name__ == "__main__":
    main()
