import nengo

model = nengo.Network()
with model:
    
    # group of neurons
    # a = nengo.Ensemble(n_neurons=100, dimensions=1) 
    # a = nengo.Ensemble(n_neurons=100, dimensions=2, radius=1) 
    a = nengo.Ensemble(n_neurons=100, dimensions=2, radius=2) 
    
    # Node = input, output, anything that isn't a neuron 
    # just arbitrary code 
    # simplest node gives a constant output 
    # if you have multiple dimensions, the stimulus is a 
    # list of that size
    stim = nengo.Node([0,0]) 
    
    nengo.Connection(stim, a) 
    
    '''
    - each neuron has a preferred direction (not just -1 or +1) 
    - different weightings decode different values
    - brain has neurons that are sensitive to more than one thing 
    - they have a preferred stimulus and this is randomly generated 
      by nengo to represent this 
    - multi-dimensional stimuli represent how some stimuli will cause
      neurons to be more sensitive
    - one set of weights will do a good job decoding some of those values, 
      other weights will do a good job decoding other sets of those values
    - moving both stimuli values shows how the neurons are not entirely 
      represented by one or the other - there is some sort of interaction
      
    - the radius is a limiting factor on the accuracy for the values that 
      it is trying to decode
      - if we have a radius of 1 with 2 stimuli, moving one will slightly 
        influence the other
      - increasing the radius solves this 
    '''
    
    '''
    - Neural Engineering -> connecting groups of neurons 
    - x -> group of neurons -> decode into y -> feed into another group of neurons -> decode into another output, z 
    - but this isn't exactly what happens within the brain 
    - we can postulate this intermediary weight y -> because neurons are more connected, and multiplying the factors to get a weight matrix is more biologically accurate
    '''
    
    
    
    