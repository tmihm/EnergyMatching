#!/bin/bash 

for file in N*; do cd $file && head -n 1000 fort.59 > left && grep "* E(2) is" Output > right && paste left right > line_up_mp2_twist.out && cd ../; done
