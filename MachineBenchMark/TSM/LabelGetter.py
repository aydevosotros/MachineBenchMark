'''
Created on Dec 31, 2013

@author: antonio
'''

class LabelGetter(object):
    '''
    For getting the label based on the training set
    '''


    def __init__(self, selfparams):
        '''
        Constructor
        '''
        
    def gainingBased(self, initValue, endValue, margin):
        '''
        Se trata de que determine si gana o pierde en un un margen de tiempo definido
        por los valores de initValue y endValue. Así se supone que se debería poder entrenar
        para determinar si la ganacia será al menos la especificada en el margen
        '''
        print("Obteniendo etiquetas en base a la ganancia")
        
    
    def trendingBased(self, data):
        '''
        Se trata de que determine la tendencia para una fecha dada en base al entrenamiento.
        Tiene que encontrar los máximos y los mínimos que vemos en la gráfica de velas para
        determinar si la tendencia es alcista o bajista
        '''
        print("Obteniendo etiquetas en base a la tendencia")
        
        