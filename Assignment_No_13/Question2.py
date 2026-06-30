# WAP which accepts radius of circle 
# and print area of circle

def AreaofCircle(radi):
    Area = 3.14*radi*radi 
    return Area

def main():
    rad = int(input("Enter Radius of circle :"))
    result = AreaofCircle(rad)
    print("Area of circle is :",result,"cm²")

if __name__ == "__main__":
    main()