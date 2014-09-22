#!/bin/bash
# declare STRING variable
nameFile=out/$(date +%y-%m-%d_%H:%M).csv
#print variable on a screen
echo saida salva em $nameFile
# bash for loop
tiposBusca=(BL BP BPL BPI BCU A* IDA* RBFS)



echo "Array size: ${#array[*]}"

echo "Array items:"
for item in ${tiposBusca=[*]}
do
    printf "   %s\n" $item
done

for tipoBusca in ${tiposBusca[*]} do
	for problem in $( ls tests/ ); do
		for instancia in $(ls tests/$problem);do
#		./main.py tests/$problem/$instancia $tipoBusca $problem
			./main.py tests/$problem/$instancia $tipoBusca $problem  >> $nameFile 
			$tipoBusca \n>> $nameFile
		done
	done
done
