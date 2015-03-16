#!/usr/bin/env python
# -*- coding: latin-1 -*-
import time
import sys
from Problemas import *
from Buscas import busca

TIPOS_BUSCAS = ['BL', 'BP', 'BPL', 'BPI', 'BCU', 'A*', 'IDA*','RBFS']
TIPOS_PROBLEMAS = ['RP','TP','MC']
DEBUG = False

    

TEST = False
    
def main():
    try:
        fileName = sys.argv[1]
        tipoBusca = sys.argv[2]
    except:
        print 'Comando inválido'
        print 'Formato de chamada: \n\t./main.py <arquivoEntrda> <tipoDeBusca> <tipoProblema>'
        print 'Exemplo:\n\t./main.py entradaSimples.txt BL\t'
        print 'Tipos de Busca Válidos:\n\t',
        print TIPOS_BUSCAS
        print 'Tipos de Problemas Válidos:\n\t',
        print TIPOS_PROBLEMAS
        return
    try:
        tipoProblema = sys.argv[3]
    except:
        tipoProblema = 'RP'
    if tipoBusca not in TIPOS_BUSCAS+['BG']:
        print 'Busca inválida:',tipoBusca
        return
    
    problemas = []
    if tipoProblema == 'RP':
        content = [x.strip('\n') for x in open(fileName, 'r').readlines()] 
        #gambiarra para pegar dois elementos do iterador em cada loop
        inputIterator = content.__iter__()
        
        inputs = []
        for t in inputIterator:
            i = {}
            i['size'] = int(t)
            i['state'] = inputIterator.next()
            inputs.append(i)
            
        for i in inputs:
            try:
                p = ReguaPuzzle(i['size'],i['state'])
                #save input to be show in the out
                p.input = i
                problemas.append(p)
            except ValueError as e:
                print e
                continue
            
    elif tipoProblema == 'TP':
        #load file content removing \n

        content = [x.strip('\n') for x in open(fileName, 'r').readlines()] 
        i ={}
        i['maxSize'] = content[0].split(' ')[1]
        
        i['input'] = content[1::]
        
        try:
            p = TravessiaPonte(i['maxSize'],i['input'])
            #save input to be show in the out
            p.input = i
            problemas.append(p)
        except ValueError as e:
            print e
    elif tipoProblema == 'FP':
        
        
        j = 40
            
        i = FindPathProblem.createInstance(j)
        start = time.clock()
        p = FindPathProblem(i['worldmap'],i['intialPosition'],i['goalPosistion'])
        node,numNosExplorados,numNosGerados = busca(p,tipoBusca)
        end = time.clock()
        print j,end - start
            
        return
        #i = FindPathProblem.loadInstance(fileName)
        i = FindPathProblem.createInstance(30)

        
        
        try:
            p = FindPathProblem(i['worldmap'],i['intialPosition'],i['goalPosistion'])
            #save input to be show in the out
            p.input = i
            problemas.append(p)
        except ValueError as e:
            print e
    if tipoProblema == 'MC': 
        p = MissionariesCannibals(3,fileName)
        #save input to be show in the out
        #p.input = i
        problemas.append(p)
    
    #gambiarra para pegar dois elementos do iterador em cada loop
    #inputIterator = content.__iter__()
    
    
    for problema in problemas:
        start = time.clock()
        node,numNosExplorados,numNosGerados = busca(problema,tipoBusca)
        end = time.clock()

        if not TEST:
            if node != None:
                print 'solução encontrada'
                
                print 'caminho da solução:'
                problema.printPath(node.getPath())
                print 'profundidade da meta: ............................................',node.depth
                print 'custo da solução: ................................................',node.cost
            else:
                print 'solução não encontrada'
                print 'profundidade da meta: ............................................None'
                print 'custo da solução: ................................................None'
            print 'número de nós explorados: ........................................',numNosExplorados
            print 'número de nós gerados: ...........................................',numNosGerados
            print 'fator de ramificação médio: ......................................',float(numNosGerados) /numNosExplorados
        else:
            print tipoBusca,',',
            if node != None:
                print 1,',',
                print node.depth,',',
                print node.cost,',',
            else:
                print None,',',
                print None,',',
                print None,',',
            print numNosExplorados,',',
            print numNosGerados,',',
            print '%.4f' % (float(numNosGerados) /numNosExplorados),',',
            print "%.2g" % (end-start),
            for value in problema.input.values():
                #print ',"',str(value).replace(',',','),'"'
                print ',"',str(value),'"',
            #pula linha
            print
        print node.getPath()
            
        ##
        # SALVAR SOLUÇÕES DIRETÓRIO OUT
        # 
        ##
        
        
    #print r.successors()
    #print 'teste'.pop()

main()

#print 'Anotações: '
#print "\tTente usar heapq"

#print """\tManual for Package pgfplots
#\tGetting the Data Into TEX """
