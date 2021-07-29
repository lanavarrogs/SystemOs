import os
import Process 

#Definicion de todos los comandos basicos por usar
def run_commands(command,priority_Queue,ram):
    path = os.getcwd() 
    command_execute = command.split()
    if len(command_execute) > 3 : 
        print("Error con el comando")
    try:
        if command_execute[0] == "crear" and len(command_execute) == 2 :
            if not os.path.isdir(command_execute[1]):
                os.system("mkdir " + path + "/ "+ command_execute[1])
            else: 
                print(" \n El directorio ya existe ")
        elif command_execute[0] == "remover" and len(command_execute) == 2: 
            os.system("rm" + path + command_execute[1] )
        elif command_execute[0] == "cambiar" and len(command_execute) ==2:
            os.chdir(command_execute[1])
            path = os.getcwd()
        elif command_execute[0] == "regresar" and len(command_execute) ==2:
            os.chdir('../')
        elif command_execute[0] == "mostrar" and len(command_execute) == 1:
            directorios = os.listdir(path)
            print(directorios)
        elif command_execute[0] == "matar" and len(command_execute) == 2:
            try: 
                priority = int(command_execute[1])
                process = priority_Queue.queue[priority]
                ram.set_free_memory(process.memory)
            except Exception as e:
                    print(e)
        elif command_execute[0] == "status" and len(command_execute) == 1:
             ram.status_ram()
        else:
            print("El comando introducido no existe")
    except Exception as e:
        pass
