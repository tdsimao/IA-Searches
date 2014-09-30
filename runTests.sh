#!/bin/bash
# declare STRING variable
nameFile=out/RPHeuristica3.csv
#print variable on a screen
mkdir out/
echo saida salva em $nameFile
# bash for loop
tipos=(BL BP BPL BPI BCU A* IDA* RBFS)
tipos=(A* IDA* RBFS)
#echo "Array size: ${#array[*]}"
echo "Tipo de Busca, Achou, Profundidade, Custo, Nós Explorados, Nós Gerados, Fator de Ramificação, Tempo (s), Entrada" > $nameFile 
for problem in $( ls tests/ ); 
do
    for instancia in $(ls tests/$problem);
    do
        for tipoBusca in ${tipos[*]};
        do
            echo "./main.py tests/$problem/$instancia $tipoBusca $problem "
            ./main.py tests/$problem/$instancia $tipoBusca $problem >> $nameFile &
        done
    done
done
