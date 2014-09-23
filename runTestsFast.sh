#!/bin/bash
# declare STRING variable
    nameFile=out/$(date +%y-%m-%d_%H:%M).csv
#print variable on a screen
echo saida salva em $nameFile
# bash for loop
#tipos=(BL BP BPL BPI BCU A* IDA* RBFS)
tipos=(BL BP BPL BPI BCU A* IDA*)

#echo "Array size: ${#array[*]}"
echo "Tipo de Busca, Achou, Profundidade, Custo, Nós Explorados, Nós Gerados,Fator de Ramificação, Tempo (s), Entrada"
for problem in $( ls tests/ ); 
do
    for instancia in $(ls tests/$problem);
    do
        for tipoBusca in ${tipos[*]};
        do
            echo "./main.py tests/$problem/$instancia $tipoBusca $problem "
            ./main.py tests/$problem/$instancia $tipoBusca $problem 
        done
        # garante a execução de apenas uma instancia de cada problema
        # e um tipo de busca para cada instancia
        break
    done
done
