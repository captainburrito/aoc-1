def readfile():
    
    sum=0
    
    with open("1-input.txt") as f:
        
        for line in f.readlines():
            
            operator = line[0]
            value = line[1:]
            
            if operator == "+":
                sum=sum+int(value)
            elif operator == "-":
                sum=sum-int(value)
        
        print(sum)

def main():
    readfile()

if __name__ == "__main__":
    main()
