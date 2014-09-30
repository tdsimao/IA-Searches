#!/bin/bash
# declare STRING variable
nameFile=out/h3-017.csv
#print variable on a screen
mkdir out/
echo saida salva em $nameFile
# bash for loop
tipos=(A* IDA* RBFS)
problem=TP
instancia=017.txt
#echo "Array size: ${#array[*]}"
echo "Tipo de Busca, Achou, Profundidade, Custo, Nós Explorados, Nós Gerados, Fator de Ramificação, Tempo (s), Entrada" > $nameFile 
for tipoBusca in ${tipos[*]};
do
    echo "./main.py tests/$problem/$instancia $tipoBusca $problem "
    ./main.py tests/$problem/$instancia $tipoBusca $problem >> $nameFile &
done
