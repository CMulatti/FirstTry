while True:
    MAINMENU=(input("Seleccione un opción.\n1.Operadores matemáticos\n2.Operadores Relacionales\n3.Validador de tipos de datos\n"))
    
    if MAINMENU.isdigit():
        MAINMENU=int(MAINMENU)
    
        if MAINMENU==1:
            menu1=int(input("Seleccione la operación deseada.\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Módulo(Resto)\n6.Potencia\n"))
            if menu1==1:
                numbers=(input("ingrese sus dos numeros separados por un espacio: "))
                number1, number2=map(int,numbers.split()) #numbers.split()  This part takes the string numbers and splits it into a list of substrings wherever it finds whitespace.
                print("la suma de los numeros es: ",number1+number2) #map(int, ...): This part applies the int function to each element of the list returned by numbers.split(). number1, number2 = ...: This part unpacks the list of integers [10, 20] into the variables number1 and number2. So, number1 will be assigned the first element of the list (10), and number2 will be assigned the second element of the list (20).
            elif menu1==2:
                    numbers=(input("ingrese los números separados en coma: "))
                    number1, number2=map(int, numbers.split(","))
                    print("la resta de los numeros es: ",number1-number2)
            elif menu1==3:
                number1=int(input("ingrese el primer numero a multiplicar: "))
                number2=int(input("ingrese el segundo numero a multiplicar: "))
                print("la multiplicación de los numeros es: ",number1*number2)
            elif menu1==4:
                number1=int(input("ingrese el primer numero a dividir: "))
                number2=int(input("ingrese el segundo numero a dividir: "))
                print("la división de los numeros es: ",number1/number2)    
            elif menu1==5:
                number1=int(input("ingrese el primer numero: "))
                number2=int(input("ingrese el segundo numero: "))
                mod=number1%number2
                print(f"el resto al dividir los números es: {mod}")     
            elif menu1==6:
                basenumber=int(input("ingrese el numero base: "))
                power=int(input("ingrese la potencia a que desea elevarlo: "))
                result= basenumber**power
                print(f"{basenumber} elevado a {power} es: {result}") 


        elif MAINMENU==2:
            num1= int(input("Para determinar el mayor de dos numeros, digite su primer número: "))
            num2= int(input("Para determinar el mayor de dos numeros, digite su segundo número: "))
            if num1>num2:
                print(f"el número mayor es {num1}")
            elif num1==num2:
                print("los números deben ser diferentes")
            else:
                print(f"el número mayor es: {num2}")


        elif MAINMENU==3:
            dato=input("ingrese su dato: ")
            if dato.isalpha():
                print ("su dato ingresado es de tipo caracter")
            elif dato.isdigit():
                if int(dato)>=0:
                    print ("su valor ingresado es un número entero positivo")
                else:
                    print ("su valor ingresado es un número entero negativo")
            elif "." in dato:
                float_value=float(dato) # If dato can be successfully converted to a float, the result is assigned to the variable float_value and the print executes.
                print ("su valor ingresado es un número decimal")
            else:   #OR elif dato.isalnum():
                print ("su dato ingresado es de tipo alfanumérico") 

    elif str(MAINMENU).lower()== "back":     # If the user types "back", break out of the loop to go back to the main menu
        break

    else:
        print("menú inválido")




"""The long string r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$" is a regular expression pattern used for validating passwords. Let's break it down:

r at the beginning: The r is a prefix indicating that the string is a "raw" string literal in Python. In raw string literals, backslashes are treated as literal characters and not as escape characters. This is useful in regular expressions because backslashes are commonly used and can be misinterpreted as escape characters in normal string literals.
"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$": This is the regular expression pattern itself.
^: Asserts the start of the string.
(?=.*[a-z]): Positive lookahead assertion. This ensures that the string contains at least one lowercase letter ([a-z]).
(?=.*[A-Z]): Positive lookahead assertion. This ensures that the string contains at least one uppercase letter ([A-Z]).
(?=.*\d): Positive lookahead assertion. This ensures that the string contains at least one digit (\d).
(?=.*[@$!%*?&]): Positive lookahead assertion. This ensures that the string contains at least one special character from the set @$!%*?&.
[A-Za-z\d@$!%*?&]{8,}: Matches any combination of letters (both uppercase and lowercase), digits, and the specified special characters, with a minimum length of 8 characters.
$: Asserts the end of the string."""

"""import re

def validate_password(password):
    # Regular expression pattern for password validation
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False

# Example usage
password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please ensure it contains at least 8 characters including uppercase and lowercase letters, numbers, and special characters.")"""