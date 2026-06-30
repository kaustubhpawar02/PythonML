# WAP which accepts length and width of rectangle
# print its area

def Area(len,wid):

    area = len*wid 
    return area

def main():

    length = int(input("Enter length of Rectangle :"))
    width = int(input("Enter width of Rectangle :"))

    Result = Area(length,width)

    print("Area of Rectangle is :",Result,"cm²")

if __name__ == "__main__":
    main()