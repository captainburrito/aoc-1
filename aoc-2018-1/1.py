#!/usr/bin/python

import time
import sys

def readfile():
    
    sum=0
    sumarray = []
    duplicate=False

    while (duplicate==False):
        with open("1-input.txt") as f:
            
            for line in f.readlines():
                
                operator = line[0]
                value = line[1:]

                if operator == "+":
                    sum=sum+int(value)

                elif operator == "-":
                    sum=sum-int(value)

                for val in sumarray:
                    if val==sum:
                        duplicate = True
                        print(val,"to duplikat !")
                        break

                if(duplicate == False):
                    sumarray.append(sum)
                else:
                    break

                
                if(len(sumarray)==0):
                    sumarray.append(sum)

def main():
    readfile()

if __name__ == "__main__":
    main()
