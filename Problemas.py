# -*- coding: latin-1 -*-

from Buscas import Node

from itertools import combinations
import pickle

class Problem(object):
    def __init__(self):
        self.rootNode  = Node()
        self.goalNode = Node()

    def isSolution(self,node):
        
        return node == self.goalNode

    
    def successorsGenerator(self,node):
        for a in self.actions(node):
            s = self.child(node,a)
            if s:
                yield s
        
        

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
            Must calculate 
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
            
    @staticmethod
    def loadInstance(f):
        '''
            return an instance of the problem from f

            f is the path to the problem
        '''
        raise NotImplementedError
    
    def createInstance(self, option = None):
        '''
            return an random instance of the problem
            maybe use some options
        '''
        raise NotImplementedError
        
    

    
    

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
        #h = estado[0:self.size].count('A')
        
        #h2: As a esquerda do branco
        #h = node.estado['left'].count('A') + node.estado['right'].count('B') 
        
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




class FindPathProblem(Problem):

    def __init__(self, worldmap, intialPosition, goalPosistion):
        Problem.__init__(self)
        self.worldmap = worldmap
        self.rootNode.estado = intialPosition
        self.goalNode.estado = goalPosistion
        self.value(self.rootNode)
        self.max_x = len(worldmap)
        self.max_y = len(worldmap[0])
    
    def actions(self,node):
        '''
            Deve retornar as possíveis ações aplicáveis a um nó
        '''
        (x,y) = node.estado
        
        actions = []
        possible_actions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for (aX,aY) in possible_actions:
            if not ( x+aX <  0 or x+aX >=self.max_x or  y+aY <  0 or y+aY >=self.max_y):
                if not self.worldmap[x+aX][y+aY]:
                    actions.append((aX,aY))
                
        return actions
    
    def value(self,node):
        '''
            Deve retornar uma estimativa da distância do nó para um estado meta
        '''
        (x,y) = node.estado
        (gX,gY) = self.goalNode.estado
        h = ((x - gX)**2 + (y - gY)**2)**0.5
        
        node.h =  h
        node.f = h + node.cost
        
    def child(self,node,action):
        '''
            Retornar um filho aplicando a ação no estado atual do nó
        '''
        (x,y) = action
        estadoFilho = (node.estado[0] + x,node.estado[1] + y)
        c = (x**2 + y**2)**0.5
        #print c
        son = Node(parent = node, cost = node.cost+c, action = action, estado = estadoFilho)
        self.value(son)
        return son
        
    
    @staticmethod
    def loadInstance(f):
        '''
            return an instance of the problem from f

            f is the path to the problem
        '''
        
        content = [x.strip('\n') for x in open(f, 'r').readlines()] 
        i ={}
        
        aux = content[0].split(' ')
        i['intialPosition'] = tuple([int(e) for e in aux])
        aux = content[1].split(' ')
        i['goalPosistion'] = tuple([int(e) for e in aux])

        i['worldmap'] = []
        for l in content[2::]:
            aux = l.split(' ')
            i['worldmap'].append([int(e) for e in aux])
        return i
    
    
    @staticmethod
    def createInstance(size ):
        '''
            return an random instance of the problem
            maybe use some options
        '''
        worldmap = []
        for i in xrange(size):
            l = []
            for j in xrange(size):
                l.append(0)
            worldmap.append(l)
        
        for i in xrange(1, size-1):
            worldmap[i][size/2] = 1
        i = {}
        i['intialPosition'] = [size/2,0]
        i['goalPosistion'] =  (size/2,size-1)
        i['worldmap'] = worldmap
        return i






    

class MissionariesCannibals(Problem):
    
    def __init__(self, size, input):
        '''
            Recebe a entrada na forma de texto e quebra a mesma
            input = None
        '''
        Problem.__init__(self)
        self.size = size
        self.rootNode.estado = {'left':{'M':3,'C':3}
                               ,'right':{'M':0,'C':0}
                               , 'boat' : 'left'}
        self.input = self.rootNode.estado
        
        self.value(self.rootNode)
        
    def isSolution(self,node):
        return node.estado == {'left':{'M':0,'C':0}
                               ,'right':{'M':3,'C':3}
                               , 'boat' : 'right'}
        
        
    def actions(self,node):
        '''
            Retorna as  possíveis ações aplicando a um nó na ordem:
        '''
        actions = []
        boat = node.estado['boat']
        for i in range(node.estado[boat]['C']+1):
            for j in range(node.estado[boat]['M']+1):
                if (i + j > 0) and (i + j < 3):
                    actions.append({'C':i,'M':j})
        return actions
        
    
    
    def child(self,node,action):
        '''
            Deve retornar um filho aplicando a ação no estado atual do nó
            ação = (lado,tamanho)
        '''
        estadoFilho = {}
        side1 = node.estado['boat']
        if node.estado['boat'] == 'left':
            estadoFilho['boat'] = 'right'
            side2 = 'right'
        else:
            estadoFilho['boat'] = 'left'
            side2 = 'left'
            
            
        
        estadoFilho[side1] =  { 'M' : node.estado[side1]['M'] - action['M'], 'C' : node.estado[side1]['C'] - action['C'] }
        estadoFilho[side2] = { 'M' : node.estado[side2]['M'] + action['M'], 'C' : node.estado[side2]['C'] + action['C'] }
        
        
        
        if (estadoFilho[side1]['M'] >= estadoFilho[side1]['C'] or estadoFilho[side1]['M'] == 0) and (estadoFilho[side2]['M'] >= estadoFilho[side2]['C'] or estadoFilho[side2]['M'] == 0 ):
            son = Node(parent = node, cost = node.cost+1, action = action, estado = estadoFilho)
            self.value(son)
            return son
        else:
            return None
    
    
    def printNode(self,node):
        print str(node.estado),node.h,node.cost,node.h+node.cost
        
    def value(self,node):
        '''
            Calcula uma estimativa da distância do nó para um estado meta h
            Adiciona os seguites atributos ao nó:
                h: função heurisitca que estima a distancia para o nó Objetivo
                f = h+cost
        '''
        
        h = node.estado['left']['M']+node.estado['left']['C']
        h = float(h)/2
        
        node.h =  h
        node.f = h+node.cost
    
        
        