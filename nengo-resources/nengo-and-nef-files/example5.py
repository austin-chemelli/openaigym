import nengo

model = nengo.Network()
with model:
    
    # multiplying two numbers
    # answer stored in d, c is just an intermediary to combine them
    stim_a = nengo.Node(0)
    stim_b = nengo.Node(0)
    
    a = nengo.Ensemble(n_neurons=100, dimensions=1) 
    b = nengo.Ensemble(n_neurons=100, dimensions=1) 
    c = nengo.Ensemble(n_neurons=100, dimensions=2)
    d = nengo.Ensemble(n_neurons=100, dimensions=1) 
    
    nengo.Connection(stim_a, a) 
    nengo.Connection(stim_b, b) 
    
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1]) 
    
    def multiply(x): 
        return x[0] * x[1]
    nengo.Connection(c, d, function=multiply) 
    
    '''
    NEURAL COMPUTATION
    - with enough neurons, we can approximate any function to 
      any degree of accuracy 
    - mean squared error becomes inversely proportional to # of neurons
    - what functions are neurons good at approximating? do SVD on tuning curves. 
    
    BIOLOGICAL ALGORITHMS
    - what do neural algorithms look like?
        - each node (group of neurons) stores a vector 
        - each connection computes a function and applies a filter
        - set of functions and filter depends on neuron model 
    - Different from standard connectionism 
        - there, connections only do linear weights
        - some functions easier than others 
        - max(a, b) takes a large number of neurons
        - sin(a + b) * cos(b - a) is pretty easy 
    '''
    
    
    
    
    
    
    
    