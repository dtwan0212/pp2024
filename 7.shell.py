import subprocess


def shell():
    while True:
        command = input("$ ")  
        if command.lower() == 'exit':
            break
        
        
        redirect_input = None
        redirect_output = None
        
        if '<' in command:
            parts = command.split('<')
            command = parts[0].strip()
            redirect_input = parts[1].strip()
        
        if '>' in command:
            parts = command.split('>')
            command = parts[0].strip()
            redirect_output = parts[1].strip()
        
        
        try:
            if redirect_input:
                with open(redirect_input, 'r') as f:
                    if command.strip() == 'bc':  
                        data = f.read()
                        output = str(eval(data))  
                    else:
                        output = subprocess.check_output(command, stdin=f, shell=True, text=True)
            else:
                if command.strip() == 'bc':  
                    data = input("Enter expression: ")
                    output = str(eval(data))  
                else:
                    output = subprocess.check_output(command, shell=True, text=True)
            
            if redirect_output:
                with open(redirect_output, 'w') as f:
                    f.write(output)
            else:
                print(output)
        
        except subprocess.CalledProcessError as e:
            print("Error:", e)
        except FileNotFoundError:
            print("Command not found:", command)
        except IndexError:
            print("Invalid input/output redirection")

if __name__ == "__main__":
    shell()
