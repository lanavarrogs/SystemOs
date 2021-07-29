import Ram
import time
import commands
import filesystem
import Process
import os
import queue

virtual_ram = Ram.Ram(1024)
virtual_ram.initialize()
process_queue = queue.PriorityQueue()


#Inicia los recursos iniciales del sistema operativo
def start_operating_system():


    virtual_ram.set_memory(400)
    intialize_filesystem()
    initialize_process()

    print("""
                          .
                   %%%%%%%.
               %%%%%%.  %%%%%%.
          %%%%%%           *%%%%%%.
       %%%%%                   .%%%%%%
       %%%%%%%%               %%%%%%%%
       %%   %%%%%%%      .%%%%%%%  %%%
       %%       #%%%%%%%%%%%#      %%%    
       %%           %%%%#          %%%    Iniciando el sistema operativo......
       %%            %%%           %%%
       %%            %%%           %%%
       %%%%%         %%%          %%%%
         %%%%%%%     %%%     %%%%%%.
             #%%%%%%%%%%%%%%%%%
                  %%%%%%%%#
                      .
    """)


def intialize_filesystem():
    #Crear el sistema de archivos del os
    filesystem.initialize_filesystem()

def login():
    while True:
        username =  input('username: ')
        password = input('password: ')
        if username != "admin" or password != "password":
            print("Lo siento, intente de nuevo")
        else:
            break
           
#Interfaz del usuario command line
def interface():
    while True:
        command = input('admin'+'@sytemos:$')
        commands.run_commands(command,process_queue,virtual_ram)


#Simulacion de la prioridad de los procesadores y consumo de memoria virtual
def initialize_process():
   
    process1 = Process.Process(20,1)
    virtual_ram.set_memory(process1.memory)
    
    process2 = Process.Process(40,2)
    virtual_ram.set_memory(process2.memory)

    process_queue.put(process1)
    process_queue.put(process2)




if __name__ == "__main__":
    start_operating_system()
    time.sleep(5)
    login()
    os.system("clear")
    interface()
