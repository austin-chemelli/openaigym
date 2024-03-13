import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    
    
    # we can change the number of neurons, firing rate, to examine accuracy
    a = nengo.Ensemble(n_neurons=10, dimensions=1)
    
    b = nengo.Ensemble(n_neurons=10, dimensions=1) 


    # by default, nengo finds the best value to pass the identity function from a to b 
    
    nengo.Connection(stim, a) 
    nengo.Connection(a, b) 
    
    # def square(x): 
    #     return x**2
        
    # def func(x): 
    #     return -1 if x < 0 else 1 
    
    # this function now defines the calculation to find the connection weights that best approximate this function
    # nengo.Connection(a, b, function=square) 
    
    # this function isn't represented well when x is close to 0, because a smooth version is represented 
    # we see a much smoother transition because neurons are trying to approximate the function 
    # showcases the brain limitation 
    # with more neurons, it'll do a better job 
    # nengo.Connection(a, b, function=func) 
    
    '''
    - computing y = x^2 takes as much work as computing y = x
    '''
    
    
    
    
    
    
    