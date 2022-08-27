# ----------------------------------------------------------------------------------------------------

# INFORMAÇÕES SOBRE O TRABALHO & OS INTEGRANTES ------------------------------------------------------

# ----------------------------------------------------------------------------------------------------

# INF01124: Classificação & Pesquisa de Dados
# Laboratório 4: Hash Table
# Erick Larratéa Knoblich 00324422
# Leonardo Azzi Martins 00323721

# ----------------------------------------------------------------------------------------------------

# IMPORTAÇÕES:

# ----------------------------------------------------------------------------------------------------

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ----------------------------------------------------------------------------------------------------

# CLASSES & SUAS FUNÇÕES -----------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------

class Element:

    def __init__(self, key):
        self.key = key
        self.next = None        

class Hash_Table:

    # Setup =========================================================================================
    def __init__(self, table_size):

        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.number_of_elements = 0

        for i in range(table_size):

            self.hash_table[i] = Element("Empty")

    # Hash Function =================================================================================
    def Hash_Function(self, key, hash_size):

        hashsum = 0

        for i in range(len(key)):

            hashsum = (hashsum * 31) + ord(key[i])
        
        return hashsum % hash_size

    def Auxiliary_Hash_Function(self):

        new_size = 2 * self.table_size + 1
        extended_hash_table  = [None] * new_size

        for i in range(new_size):

            extended_hash_table[i] = Element("Empty")

        for i in range(self.table_size):

            index = self.hash_table[i]

            while(index != None):
            
                auxiliary_index = index
                index = index.next
                bucket = extended_hash_table[self.Hash_Function(auxiliary_index.key, new_size)]
                auxiliary_index.next = bucket
                bucket = auxiliary_index

        return new_size

    # BUSCA ========================================================================================
    def Search_Item(self, key):

        index = self.Hash_Function(key, self.table_size)
        found_name = False
        searches = 0
        pointer = self.hash_table[index]

        while(pointer != None):

            searches += 1
            
            if(pointer.key == key):
            
                found_name = True
            
            pointer = pointer.next
        
        if(found_name == True):

            return searches

        else:

            return -1

    # INSERÇÃO ====================================================================================
    def Insert_Item(self, key, used, size):

        index = self.Hash_Function(key, self.table_size)

        if(self.hash_table[index].key == "Empty"):
        
            self.hash_table[index].key = key
            used += 1
            
        else:
        
            pointer = self.hash_table[index]
            index = Element(key)
            
            while(pointer.next != None):
            
                pointer = pointer.next
            
            pointer.next = index

        if(self.number_of_elements == int(0.5 * self.table_size)):
        
            size = self.Auxiliary_Hash_Function()
        
        self.number_of_elements += 1

        return used, size

# ARQUIVO =======================================================================================
def Write_Output_File(table_size): 
    
    Output_File = open("experimento" + str(table_size) + ".txt", "w")
    HashTable = Hash_Table(table_size)
    mean = 0
    total_searches = 0
    
    max_searches = 0
    min_searches = table_size

    size_table = 0

    with open(os.path.join(sys.path[0], "nomes_10000.txt"), "r") as file:
        
        used_entries = 0

        for line in file:

            used_entries, size_table = HashTable.Insert_Item(line.split('\n')[0], used_entries, size_table)

    Output_File = open("experimento" + str(table_size) + ".txt", "a", encoding = "utf-8")

    Output_File.write(
        
        "PARTE 1: ESTATÍSTICAS DA TABELA HASH"
        + "\n" +
        "NÚMERO DE ENTRADAS DA TABELA USADAS " + str(used_entries)
        + "\n" +
        "NÚMERO DE ENTRADAS DA TABELA VAZIAS " + str(HashTable.table_size - used_entries)
        + "\n" +
        "TAXA DE OCUPAÇÃO " + str(used_entries / HashTable.table_size)
        + "\n" +
        "MÍNIMO TAMANHO DE LISTA " + str(HashTable.table_size)
        + "\n" +
        "MÁXIMO TAMANHO DE LISTA " + str(size_table)
        + "\n" +
        "MÉDIO TAMANHO DE LISTA " + str((HashTable.table_size + size_table) / 2)
        + "\n\n" +
        "PARTE 2: ESTATÍSTICAS DAS CONSULTAS \n"

        )

    with open(os.path.join(sys.path[0], "consultas.txt"), "r") as file:
        
        for line in file:     

            searches = HashTable.Search_Item(line.split('\n')[0])

            if searches == -1:

                Output_File.write(line.split('\n')[0] + " MISS\n")

            else:

                if searches > max_searches:

                    max_searches = searches

                if searches < min_searches:

                    min_searches = searches
                
                Output_File.write(line.split('\n')[0] + " HIT " + str(searches) + "\n")

            mean += searches
            total_searches += 1

    Output_File.write(
        
        "MÍNIMO NÚMERO DE TESTES POR NOME ENCONTRADO " + str(min_searches)
        + "\n" +
        "MÁXIMO NÚMERO DE TESTES POR NOME ENCONTRADO " + str(max_searches)
        + "\n" +
        "MÉDIA NÚMERO DE TESTES POR NOME ENCONTRADO " + str(mean / total_searches)
        + "\n" +
        "MÉDIA DAS CONSULTAS " + str(searches/total_searches)

        )

    Output_File.close()

Write_Output_File(503)
Write_Output_File(2503)
Write_Output_File(5003)
Write_Output_File(7507)

print("Hi mom!")

