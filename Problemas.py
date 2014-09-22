# -*- coding: latin-1 -*-

from Buscas import Node

from itertools import combinations

class Problem:
    def __init__(self):
        self.rootNode  = Node()

    def isSolution(self,node):
        raise NotImplementedError

    def successors(self,node):
        '''
            Retornar os possíveis filhos do nó
        '''
        successors = []
        for a in self.actions(node):
            s = self.child(node,a)
            if s:
                if s not in successors:
                    successors.append(s)
            
        return successors
        
        
    def actions(self,node):
        '''
            Deve retornar as possíveis ações aplicáveis a um nó
        '''
        raise NotImplementedError
    
    def value(self,node):
        '''
            Deve retornar uma estimativa da distância do nó para um estado meta
        '''
        raise NotImplementedError
    
    def child(self,node,action):
        '''
            Deve retornar um filho aplicando a ação no estado atual do nó
        '''
        raise NotImplementedError
        
    def printPath(self,path):
        for node in path:
            self.printNode(node)
            
            
        
    

    
    

class ReguaPuzzle(Problem):
    
    def __init__(self, size, input):
        '''
            Recebe a entrada na forma de texto e quebra a mesma
        '''
        Problem.__init__(self)
        self.size = size
        
        if len(input) != 2*size+1:
            raise ValueError('Entrada inválida: '+str(size)+' '+input)
        aux = input.split('-')
        
        
        self.rootNode.estado = {'left':aux[0],'right':aux[1]}
        self.value(self.rootNode)
        
        
        
    def isSolution(self,node):
        return self.size*'B'+self.size*'A' == node.estado['left'] + node.estado['right']
        
        
    def actions(self,node):
        '''
            Retorna as  possíveis ações aplicando a um nó na ordem:
                1. Blocos à esquerda mais próximos até os mais distantes
                2. Blocos à direita mais próximos até os mais distantes
                
            cada ação tem o formato    
            ação = (lado,tamanho)
        '''
        actions = []
        leftSize = len(node.estado['left'])
        for i in range(1,min(self.size,leftSize)+1):
            actions.append(('left',i))
        rightSize = len(node.estado['right'])
        for i in range(1,min(self.size,rightSize)+1):
            actions.append(('right',i))
        return actions
    
    
    
    def child(self,node,action):
        '''
            Deve retornar um filho aplicando a ação no estado atual do nó
            ação = (lado,tamanho)
        '''
        i = action[1]
        estadoFilho = {}
        if action[0] == 'right':
            rightSize = len(node.estado['right'])
            estadoFilho['right'] = node.estado['right'][0:i-1]+node.estado['right'][i::]
            estadoFilho['left']  = node.estado['left']+node.estado['right'][i-1]
        elif action[0] == 'left':
            leftSize = len(node.estado['left'])
            estadoFilho['left'] = node.estado['left'][0:-i]+node.estado['left'][leftSize-i+1::]
            estadoFilho['right'] = node.estado['left'][-i]+node.estado['right']
        son = Node(parent = node, cost = node.cost+i, action = 'L'+str(i), estado = estadoFilho)
        self.value(son)
        #print 'Avaliação filho:',son.f
        return son
    
    
    def printNode(self,node):
        print node.estado['left']+'-'+node.estado['right'],node.h,node.cost,node.h+node.cost
        
    def value(self,node):
        '''
            Calcula uma estimativa da distância do nó para um estado meta h
            Adiciona os seguites atributos ao nó:
                h: função heurisitca que estima a distancia para o nó Objetivo
                f = h+cost
        '''
        
        estado = node.estado['left']+node.estado['right']
        
        #h1: numero de python
        #node.h = estado[0:self.size].count('A')
        
        #h2: As a esquerda do branco
        #node.h = node.estado['left'].count('A') + node.estado['right'].count('B') 
        
        #h3: somatori num As a esquerda de cada B
        
        s = self.size
        h = 0
        for c in estado:
            if c == 'B':
                s-=1
            else:
                h += s
        node.h =  h
        node.f = h+node.cost
    
        
        

    
    

class TravessiaPonte(Problem):
    
    def __init__(self, maxCost, input):
        Problem.__init__(self)
        self.maxCost = int(maxCost)
        intInput = []
        for i in input:
            intInput.append(int(i))
        self.rootNode.estado = {'west':intInput,'east':[],'flashLight':'west'}
        self.value(self.rootNode)
        
    def value(self,node):
        '''
            Calcula uma estimativa da distância do nó para um estado meta h
            Adiciona os seguites atributos ao nó:
                h: função heurisitca que estima a distancia para o nó Objetivo
                f = h+cost
        '''
        
        #h1
        #if node.estado['west']:
            #h = min(node.estado['west'])
        #else:
            #h = 0
        
        
        #h2
        #if node.estado['west']:
            #h = max(node.estado['west'])
        #else:
            #h = 0
        
        #h3
        
        h = 0
        
                
                
        if node.estado['west']:
            l = list(node.estado['west'])
            l2 = sorted(list(node.estado['east']+l))
            h = 0
            menor = l2[0]
            segMenor = l2[1]
                
            #soma o valores de ida de cada dupla somandp os maiores duplas
            for i in range(0,len(l),2):
                h+= l[-(i+1)]
            
            
            #if segMenor not in l:
                
                
            
            if len(l)>2:
                idaEVoltaMenorDupla = menor+2*segMenor
                tempoIdaMenorDupla = segMenor
                if len(l) % 2 == 0:
                    ##   (numDuplas - 1)* tempoIdaEVoltaMenorDupla + tempoIdaMenorDupla
            #        print 'caso Par'
                    h+=(len(l)/2 - 1 )*idaEVoltaMenorDupla 
                else:
                    if len(l)> 3:
                        
                        # (numDuplas - 1) * tempoIdaEVoltaMenorDupla + segundoMenor
                        numDuplas = ((len(l)-1)/2)
                        h += (numDuplas-2) * idaEVoltaMenorDupla + tempoIdaMenorDupla
                    else:
                        h += tempoIdaMenorDupla
        
        
        node.h =  h
        node.f = h + node.cost
        
        
        #print node,h,node.f

        
    def actions(self,node):
        '''
            Retorna as  possíveis ações aplicando a um nó 
                
            cada ação tem o formato:
                ação = (individuos,partida)
            onde:
                individuos é um set
                partida é o lado de onde os individuos saem
            
            
        '''
        partida = node.estado['flashLight']
        actions = []
        for numIndividuos in range(1,3,1):
            for individuos in combinations(node.estado[partida],numIndividuos):
                actions += [(individuos,partida)]
        
        return actions

    
    
    def child(self,node,action):
        '''
            Deve retornar um filho aplicando a ação no estado atual do nó
            ação = (lado,tamanho)
        '''
        partida = action[1]
        individuos = action[0]
        if partida == 'west':
            destino = 'east'
        else:
            destino = 'west'
        estadoFilho = {}
        
        estadoFilho['west'] = list(node.estado['west'])
        estadoFilho['east'] = list(node.estado['east']) 
        
        estadoFilho[destino].extend(individuos)
        estadoFilho[destino].sort()
        for i in individuos:
            estadoFilho[partida].remove(i)
        
        estadoFilho['flashLight'] = destino
        
        son = Node(parent = node, cost = node.cost+max(individuos), action = action, estado = estadoFilho)
        self.value(son)
        #print 'Avaliação filho:',son.f
        
        return son
    
    def printNode(self,node):
        if node.action != None:
            for i in node.action[0]:
                print i,
            if node.action[1] == 'west':
                print '>>'
            else:
                print '<<'
        else:
            print node.estado['west']
    
    def isSolution(self,node):
#        return (len(node.estado['west']) == 0) and node.cost <= self.maxCost
        return (len(node.estado['west']) == 0)

