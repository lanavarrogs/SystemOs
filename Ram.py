#Simulacion de la ram
class Ram:

    def __init__(self,memory):
        self.memory = memory
        self.space = []

    #Establece el espacio definido de la memoria 
    def initialize(self):
        self.space = [ '*' for i in range(0,1024) ]
    
    
    def set_memory(self,size_memory):
        for i in range(0,self.memory):
            if self.space[i] == '*' and i < size_memory:
                self.space[i] = '.'
        self.memory -= size_memory

    def set_free_memory(self,size_memory):
        for i in range(0,self.memory):
            if self.space[i] == '.' and i < size_memory:
                self.space[i] = '*'
        self.memory += size_memory
        
    def status_ram(self):
        num = 0
        for i in range(0,1024):
             if self.space[i] == '.':
               num += 1 
        porcentage = (num * 100) / 1024
        for i in range(0,100): 
            if i <= num:
                print('#',end = '')
            else:
                print('/',end = '')
        print(f" %{porcentage} of use ")