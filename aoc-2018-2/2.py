#!/usr/bin/python

def readfile():

    sn = []
    occurences = []
    i=0
    j=0
    with open("2-input.txt") as f:

        for line in f.readlines():
            j=j+1
            sn = []
            for char in line:
                i=0
                for val in sn:
                    if (val==char):
                        i=i+1
                if(i == 0):
                    sn.append(char)
                        

            for char in sn:
                if ( line.count(char) != 1):
                    value = j,line.count(char)
                    occurences.append(value)
            
    occurences = list( dict.fromkeys(occurences) )
    print (occurences)
   
    x2=0
    x3=0
    for line in occurences:
        if line[1] == 2:
            x2=x2+1
        elif line[1] == 3:
            x3=x3+1

    print("x2:",x2)
    print("x3:",x3)
    print("Wynik:",x2*x3)

def main():
    readfile()

if __name__ == "__main__":
    main()