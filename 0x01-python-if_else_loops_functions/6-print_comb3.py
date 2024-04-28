#!/usr/bin/python3
num_comb = ''
for i in range(10):
    for j in range(i+1, 10):
        num_comb += "{}{}, ".format(i,j) 

print(num_comb[:-2])
