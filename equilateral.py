def is_equilateral (a,b,c):
    if a == b and b == c and c == a:
        return "Yes"
    else:
        return "No"
    
def main():
    a = int(input("Please enter the value you want to compare"))
    b = int(input("Please enter the value you want to compare"))
    c = int(input("Please enter the value you want to compare"))

    print(is_equilateral(a,b,c))

main()