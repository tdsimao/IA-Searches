# -*- coding: latin-1 -*-

import itertools

from heapq import heappop,heappush,heapify
from heapq import merge as heapmerge

DEBUG = False

class Node:
    def __init__(self,parent = None, cost = 0, action = None, estado = None):
        self.cost = cost
        self.parent = parent
        self.action = action
        self.estado = estado
        #self.hash = hash(str(self.estado))
        if parent != None:
            self.depth = parent.depth+1
        else:
            self.depth = 0
    
    
    def getPath(self):
        '''
            Retorna os filhos lista de nós desde a raiz ate a folha atual
        '''
        node = self
        path = []
        while node != None:
            path.append(node)
            node = node.parent
        return path[::-1]
    
    def __eq__(self, other):
        #return self.hash == other.hash
        return self.estado == other.estado
        
    def __lt__(self, other):
        #return self.hash == other.hash
        return self.cost < other.cost

    def __hash__(self):
        return hash(str(self.estado))
    
#    def __str__(self):
#        return str(self.estado)
    
    def __repr__(self):
        return str(self.estado)




def diff(listA, listB):
    """
        Recebe uma lista a e um conjunto (set) b
        retorna a-b, isto é os elementos de a que não estão em b
        
    
    """
    #b = set(b
    c= []
    #return a for a in listA if a not in listB]
    for a in listA:
        if a not in listB:
            c.append(a)
        else:
            for b in listB:
                if a == b and a.cost < b.cost:
                    #print a, a.cost, a.f, a.h
                    #print a.parent
                    #print b, b.cost, b.f, b.h
                    #print b.parent
                    #print
                    #c.append(a) 
                    break            
    return c
            
            
class Search():
    def __init__(self,p):
        self.p  = p

    def nextNode(self,node):
        """
            Deve retornar próximo nó a ser expandido
            
        """
        raise NotImplementedError

    def run(self):
        """
            Método principal que realiza a busca
            Deve retornar Nó objetivo ou None em caso de falha
            
        """
        raise NotImplementedError
    
    def addEdge():
        """
            Método para adicionar nós a borda
            
        """
        raise NotImplementedError




        
class SearchUnformed(Search):
    """
        Classe para busca sem informação
    """
    def __init__(self,p):
        Search.__init__(self,p)
        

    
class BuscaLargura(SearchUnformed):
    """
        Classe de busca em Largura
    """
    
    def __init__(self,p):
        SearchUnformed.__init__(self,p)
        self.edge = []
        self.explored = set()
        
        
    def nextNode(self,node):
        """
            Retornar próximo nó a ser expandido
        """
        return self.edge.pop(0)
    
    def pushEdge(self,node):
        """
            Adiciona node na borda
        """
        return self.edge.pop(0)
    
    
    
    def run(self):
        """
            Método principal que realiza a busca
            Deve retornar Nó objetivo ou None em caso de falha
        """
        return buscaLargura(self.p)
    
        self.pushEdge(self.p.rootNode)
        if self.p.isSolution(p.rootNode):
            return self.p.rootNode,1,0
        
        
        while True:
        
            
            #se edge (borda) vazia não há resposta
            if not self.edge:
                return None,len(self.explored),len(self.explored)+len(self.edge)
            #
            
            node = self.nextNode() #remove e retorna o primeiro no da borda
            
            
            explored.add(node)
            successors = p.successors(node)
            
            print(node)
            if DEBUG:
                print 'Nó'
                print(node)
            
            #remove de sucessores os nós ja explorados
            successors = diff(successors,explored)
            
            #remove de sucessores os nós da borda
            successors = diff(successors,edge) 
            
                
            #verifica se algum dos nós gerados é solução
            for s in successors:
                if p.isSolution(s):
                    return s,len(explored),len(explored)+len(edge)
            
            # implementação da FILA
            # insere novos sucessores no final caracterizando a busca em largura
            edge += successors
            
            if DEBUG:
                print 'Explorados'
                for s in explored:
                    print(s)
                print
                print 'Edge'
                for s in edge:
                    print(s)
                print
        




    
        

    
def buscaLargura(p):
    '''retorna solução ou falha(None)'''
    edge = []
    edge.append(p.rootNode)
    explored = set()
    if p.isSolution(p.rootNode):
        return p.rootNode,1,0
    while True:
        #se edge (borda) vazia não há resposta
        if not edge:
            return None,len(explored),len(explored)+len(edge)
        #
        node = edge.pop(0) #remove e retorna o primeiro no da borda
        explored.add(node)
        successors = p.successors(node)
        
        if DEBUG:
            print 'Nó'
            print(node)
        
        #remove de sucessores os nós ja explorados
        successors = diff(successors,explored)
        
        #remove de sucessores os nós da borda
        successors = diff(successors,edge) 
        
            
        #verifica se algum dos nós gerados é solução
        for s in successors:
            if p.isSolution(s):
                return s,len(explored),len(explored)+len(edge)
        
        # implementação da FILA
        # insere novos sucessores no final caracterizando a busca em largura
        edge += successors
        
        if DEBUG:
            print 'Explorados'
            for s in explored:
                print(s)
            print
            print 'Edge'
            for s in edge:
                print(s)
            print
        
    
def buscaProfundidade(p):
    '''retorna solução ou falha(None)'''
    edge = []
    edge.append(p.rootNode)
    explored = set()
    if p.isSolution(p.rootNode):
        return p.rootNode,1,1
    while True:
        #se edge vazia não há resposta
        if not edge:
            return None,len(explored),len(explored)+len(edge)
        #
        node = edge.pop(0) #remove e retorna o primeiro no da borda
        if DEBUG:
            print node
        explored.add(node)
        successors = p.successors(node)
        
        #remove de sucessores os nós ja explorados
        successors = diff(successors,explored) 
        #remove de sucessores os nós da borda
        successors = diff(successors,edge) 
        
        #verifica se algum dos nós gerados é solução
        for s in successors:
            if p.isSolution(s):
                return s,len(explored),len(explored)+len(edge)

        # implementação da FILA
        # insere novos sucessores no topo da pilha caracterizando a busca em profundidade
        edge = successors+edge
        
    
    
    
def buscaProfundidadeLimitada(p):
    limit = 13
    resultado, node,numNosExplorados,numNosGerados = bplRecursiva(p.rootNode,p,limit)
    return node,numNosExplorados,numNosGerados

def buscaProfundidadeIterativa(p):
    limit = 0
    resultado = 'FALHA'
    while resultado != 'Sucesso':
        if DEBUG:
            print 'limite = ',limit
        resultado, node,numNosExplorados,numNosGerados = bplRecursiva(p.rootNode,p,limit)
        numNosGerados+=1 #para contabilizar o nó raiz
        limit += 1
    return node,numNosExplorados,numNosGerados



def bplRecursiva(node,p,limit):
    
    numNosExplorados = 1
    numNosGerados = 0
    #TODO verificar tamanho a serem retornados
    if p.isSolution(node):
        if DEBUG:
            print 'solução encontrada', node
        return 'Sucesso',node,numNosExplorados,numNosGerados
    elif limit == 0:
        if DEBUG:
            print 'limite atingido'
        return 'CORTE',None,numNosExplorados,numNosGerados
    else:
        corteOcorreu = False
        successors = p.successors(node)
        #print 'Sucessores'
        #for s in successors:
        #    print s,
        #print
        #recursivamente procura pela solução em cada um dos sucessores 
        numNosGerados+=len(successors)
        for s in successors:
            #print 's = ',s
            if DEBUG:
                print s
            resultado,n1,numNosExploradosFilho,numNosGeradosFilho = bplRecursiva(s,p,limit-1)
            numNosExplorados += numNosExploradosFilho
            numNosGerados += numNosGeradosFilho
            if resultado == 'CORTE':
                corteOcorreu = True
            elif resultado == 'Sucesso':
                return 'Sucesso',n1,numNosExplorados,numNosGerados
        if corteOcorreu:
            return 'CORTE',None,numNosExplorados,numNosGerados
        else:
            return 'FALHA',None,numNosExplorados,numNosGerados
            
        
        
def addABorda(successors,edge,explored):
    """
        adiciona nos a borda
    """
    for s in successors:
        if s not in edge:
            if s not in explored:
                edge.append(s)
        else:
            aux = set()
            aux.add(s)
            b = aux.intersection(edge).pop() 
            if s.cost < b.cost:
                #print s, s.cost
                #print b, b.cost
                #print 
                edge.remove(b)
                edge.append(s)
            
            #if s.cost < (list(explored)+edge).getitem(s):
                #print 'Teste'
                


    
    
def buscaCustoUniforme(p):
    '''retorna solução ou falha(None)'''
    edge = []
    edge.append(p.rootNode)
    explored = set()
    if p.isSolution(p.rootNode):
        return p.rootNode,1,1
    while True:
        #se edge (borda) vazia não há resposta
        if not edge:
            return None,len(explored),len(explored)+len(edge)
        #
        node = edge.pop(0) #remove e retorna o primeiro no da borda
        if DEBUG:
            print node
        explored.add(node)
        successors = p.successors(node)
        addABorda(successors,edge,explored)
        
        
        #verifica se algum dos nós gerados é solução
        for s in successors:
            if p.isSolution(s):
                return s,len(explored),len(explored)+len(edge)
        
        # implementação da ordem de prioridade
        # insere novos sucessores de forma ordenada segundo custo em edge
        
        if DEBUG:
            print 'Edge Anterior:'
            for s in edge:
                print s,s.cost
            print
            
            print 'Sucessores não ordenados:'
            for s in successors:
                print s,s.cost
            print
        
        #reordena borda
        edge = sorted(edge, key=lambda n: n.cost)
        
        if DEBUG:
            print 'Sucessores ordenados:'
            for s in successors:
                print s,s.cost
            print 'Edge posterior:'
            for s in edge:
                print s,s.cost
            print
            print 20*'-_'
            print
        
        
        #expandir o nó escolhido, adicionando os nós resultantes a borda
        #apenas se não estiver na borda ou no conjunto explorado
    
           
        
    
def buscaAStar(p):
    '''retorna solução ou falha(None)'''
    edge = []
    edge.append(p.rootNode)
    explored = set()
    if p.isSolution(p.rootNode):
        return p.rootNode,1,1
    while True:
        #se edge (borda) vazia não há resposta
        if not edge:
            return None,len(explored),len(explored)+len(edge)
        #
        node = edge.pop(0) #remove e retorna o primeiro no da borda
        
        
        if DEBUG:
            print node
        
        
        explored.add(node)
        
        
        if p.isSolution(node):
            return node,len(explored),len(explored)+len(edge)
        
        #print
        #print node.cost, node.f, node
        
        successors = p.successors(node)
        
        addABorda(successors,edge,explored)
                
        edge = sorted(edge, key=lambda n: n.f)
        
        #edge += successors
        if DEBUG:
            print 'Edge posterior:'
            for s in edge:
                print s,s.h
            print
            print 20*'-_'
            print
            
        
        #expandir o nó escolhido, adicionando os nós resultantes a borda
        #apenas se não estiver na borda ou no conjunto explorado
    
           
    
    
def buscaGulosa(p):
    '''retorna solução ou falha(None)'''
    edge = []
    edge.append(p.rootNode)
    explored = set()
    if p.isSolution(p.rootNode):
        return p.rootNode,1,1
    while True:
        #se edge (borda) vazia não há resposta
        if not edge:
            return None,len(explored),len(explored)+len(edge)
        #
        node = edge.pop(0) #remove e retorna o primeiro no da borda
        if DEBUG:
            print node,'\t',node.h,'\t',node.f
        explored.add(node)
        successors = p.successors(node)
        
        
        addABorda(successors,edge,explored)
        
        ##remove de sucessores os nós ja explorados
        #successors = diff(successors,explored) 
        ##remove de sucessores os nós da borda
        #successors = diff(successors,edge) 
        
        
        #verifica se algum dos nós gerados é solução
        for s in successors:
            if p.isSolution(s):
                return s,len(explored),len(explored)+len(edge)
        
        # implementação da ordem de prioridade
        # insere novos sucessores de forma ordenada segundo custo em edge
        
        successors = sorted(successors, key=lambda s: s.h)
        
        edge = sorted(itertools.chain(edge,successors), key=lambda n: n.h)
        
        #print 'Edge posterior:'
        #for s in edge:
            #print s,s.h
        #print
        #print 20*'-_'
        #print
        
        
        #expandir o nó escolhido, adicionando os nós resultantes a borda
        #apenas se não estiver na borda ou no conjunto explorado
    
    
# variaveis globais utilizadas pelo método buscaIDAStar
    
infinito = float('inf')
nextLimit = infinito

def buscaIDAStar(p):
    global nextLimit 
    nextLimit = infinito
    """    
    Função IDA* (problema) devolve a sequência da solução
        Entradas:
            problema
            f-limite (limite atual de f)
            raiz (um nó)
        raiz = Faça-nó (Estado-Inicial(problema))
        f-limite = f(raiz)
        laço faça
            solução, f-limite = DFS-contorno(raiz, f-limite)
            Se solução não nula então devolve solução
            Se f-limite = infinito então devolve falha
    """
    
    numNosExplorados,numNosGerados = 0,1
    limit = p.rootNode.f
    node = p.rootNode
    
    def DFSContorno(node,p,limit):
        global nextLimit 
        numNosExplorados,numNosGerados = 1,0
        
        #se nó esta fora do contorno
        if node.f > limit:
            #print limit, node.f
            return None,numNosExplorados,numNosGerados,node.f
        #se node é solução
        if p.isSolution(node):
            return node,numNosExplorados,numNosGerados,limit
        for sucessor in p.successors(node):
            numNosGerados += 1
            solucao, numNosExploradosFilho, numNosGeradosFilho, newLimit = DFSContorno(sucessor,p,limit)
            numNosExplorados += numNosExploradosFilho
            numNosGerados += numNosGeradosFilho
        
            if solucao != None:
                #return solucao,numNosExplorados,numNosGerados,newLimit
                return solucao,numNosExplorados,numNosGerados,limit
            else:
                #print nextLimit
                #if newLimit<nextLimit:
                    #print nextLimit, newLimit
                    #nextLimit = newLimit
                if newLimit < nextLimit:
                    print nextLimit,newLimit
                    
                    nextLimit = newLimit
                #nextLimit = min(nextLimit,newLimit)
                
        #return solucao,numNosExplorados,numNosGerados,newLimit
        return solucao,numNosExplorados,numNosGerados,nextLimit
    
    while True:
        print 10*'-=-='
        nextLimit = infinito
        solucao,numNosExploradosFilho,numNosGeradosFilho,limit = DFSContorno(p.rootNode,p,limit)
        #return
        numNosExplorados += numNosExploradosFilho
        numNosGerados += numNosGeradosFilho
        if solucao != None:
            return solucao,numNosExplorados,numNosGerados
        

    
def buscaRBFS(p):
    raise NotImplementedError
        
        
        

def busca(p,tipo):
    '''retorna:
            nó solução ou None em caso de falha;
            numero de nós explorados;
            numero de nos gerados.
    '''
    
    #tipos = ['BL', 'BP', 'BPL', 'BPI', 'BCU', 'A*', 'IDA*','RBFS']
    
    
    if tipo == 'BL':
        b = BuscaLargura(p)
        return b.run()
        #return buscaLargura(p)
    elif tipo == 'BP':
        return buscaProfundidade(p)
    elif tipo == 'BPL':
        return buscaProfundidadeLimitada(p)
    elif tipo == 'BCU':
        return buscaCustoUniforme(p)
    elif tipo == 'BPI':
        return buscaProfundidadeIterativa(p)
    elif tipo == 'A*':
        return buscaAStar(p)
    elif tipo == 'BG':
        return buscaGulosa(p)
    elif tipo == 'IDA*':
        return buscaIDAStar(p)
    elif tipo == 'RBFS':
        return buscaRBFS(p)

