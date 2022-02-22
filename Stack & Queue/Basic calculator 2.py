
def calculate(s): 
        last_number = 0
        current_num = 0
        output = 0
        operation = "+"
        s += "+0"
        
        for char in s:
            if char.isdigit():
                current_num = (current_num * 10) + (ord(char) - ord('0'))
                continue
            if char == " ":
                continue
            if operation in ['+', '-']:
                output += last_number
                if operation == '+':
                    last_number = current_num
                else:
                    last_number = -current_num
            elif operation == '*':
                last_number *= current_num
            elif operation == '/':
                if last_number < 0:
                    temp = -last_number
                    last_number = -(temp/current_num)
                else:
                    last_number /= current_num
            
            operation = char
            current_num = 0
        
        output += last_number
        return output
                
                
                
        
