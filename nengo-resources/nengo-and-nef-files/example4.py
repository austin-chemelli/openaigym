import nengo

model = nengo.Network()
with model:
    
    stim_a = nengo.Node(0)
    stim_b = nengo.Node(0)
    
    a = nengo.Ensemble(n_neurons=100, dimensions=1) 
    b = nengo.Ensemble(n_neurons=100, dimensions=1) 
    c = nengo.Ensemble(n_neurons=100, dimensions=2, radius=2) 
    
    nengo.Connection(stim_a, a) 
    nengo.Connection(stim_b, b) 
    
    
    # this shows how the dimensions of c represent a and b
    # c is constant at 0 
    
    # def func_a(x): 
    #     return x, 0 
        
    # def func_b(x): 
    #     return 0, x

    # nengo.Connection(a, c, function=func_a) 
    # nengo.Connection(b, c, function=func_b)
    
    # but you don't always need to use functions - use this syntax to simplify your life
    nengo.Connection(a, c[0])
    nengo.Connection(b, c[1])
    
    
    
    
    
    
    