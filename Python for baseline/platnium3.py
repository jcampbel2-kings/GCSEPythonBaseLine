#Area Calculator (with menu)
#March 2022
#James Campbell

def AreaTriangle():
    print('Enter base of triangle')
    base=input('>')
    #convert to float number
    base=float(base)
    print('Enter height of triangle')
    height=input('>')
    #convert to float number
    height=float(height)
    area = base * height / 2
    print('The area of a triangle of base',base,'and height', height,'is',area)
    return
##end AreaTriangle

def AreaSquare():
    print('Enter length of square')
    length=input('>')
    #convert to float number
    length=float(length)

    area = length ** 2
    print('The area of a square of length',length,'is',area)
    return
##end AreaSquare

def AreaRectangle():
    print('Enter length of Rectangle')
    length=input('>')
    #convert to float number
    length=float(length)
    print('Enter width of Rectangle')
    width=input('>')
    #convert to float number
    width=float(width)
    area = length * width
    print('The area of a rectangle of length',length,'and width', width,'is',area)
    return
##end AreaRectangle

def AreaCircle():
    print('Enter radius of circle')
    radius=input('>')
    #convert to float number
    radius=float(radius)

    area = PI * (radius ** 2)
    print('The area of a circle of radius',radius,'is',area)
    return
##end AreaCircle

#display menu and process option
#loop until exit request
def menu():
    print('Welcome to Area Calculator')
    choice=''
    #loop until exit requested
    while choice != 'q':
        print()
        print('------------')
        print('Menu Options')
        print('------------')
        print()
        print('1) Area Triangle')
        print('2) Area Square')
        print('3) Area Rectangle')
        print('4) Area Circle')
        print('Q) Quit')

        #get choice and force convert to lowercase
        choice=input('>').lower()
        #process options
        if choice=='1':
            AreaTriangle()
        elif choice=='2':
            AreaSquare()
        elif choice=='3':
            AreaRectangle()
        elif choice=='4':
            AreaCircle()
        elif choice=='q':
            print("Exit requested")
        else:
            print("Invalid option,  try again")
    #end of while loop
    return
##end menu

 
##main program
PI = 3.1416
print('Welcome to my Area Calculator')
menu()
print('Goodbye')
