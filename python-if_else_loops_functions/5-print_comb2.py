#!/usr/bin/bash
for i in range(99):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
