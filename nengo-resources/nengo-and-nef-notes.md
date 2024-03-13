# [Nengo and the Neural Engineering Framework](https://www.youtube.com/playlist?list=PLX-XEf1yTMrnjFt30RQ7X6k-dfhL1fIGq) - Notes

## Lecture 1A 
### Goals
- building mechanistic models of the mind - internal components that map onto the real system 
- we need a computational model that goes beyond pages of math and will help us make it analytically tractable 

### Cognitive Modeling 
- choose a phenomenon, build a program, and compare the behaviors of the program and humans 
- many domains - memory, mental arithmetic, and reward learning 
- problem arises: how do we know if we're right? 

### Cognitive Architectures 
- provide a more constrained approach with basic modules 
  - declarative memory 
  - visual recognition 
  - hand movement 
  - procedural memory 
- use these modules to do many tasks - we don't suddenly get new brain areas when new tasks arise 
- ACT-R 
  - declarative memory 
  - procedural memory: IF-THEN rules (IF I'm counting and I'm at THREE, THEN go to FOUR) 
  - parameter values: `d = 0.5`, `50 ms` per rule (found by looking at human data across conditions) 
- variety of tasks: 
  - mental arithmetic, estimating time, visual search, ATC, etc. 
- adding more constraints is helpful, because the same components do many different tasks 
- parameter values shouldn't change (or, theory can say when they do change) 
- predicting many aspects of behavior with this limited set of components 

### Brain-Based Model
- predicts more than just overt behavior (can be used to apply towards biological behaviors) 
  - connectivity, firing patterns, results of lesions, timing, effects of drugs 
- different algorithms: 
  - instead of implementing algorithms, we determine the types of algorithms that neurons would be good at implementing 
  - then, we make software tools to make those types of algorithms easy to program 

### Connectionism 
- neural networks -> many components -> many connections 
- components add their inputs and perform some non-linearity to produce outputs 
- deciding what the components can do -> sigmoid neuron (because it's easy to program) 
- connection weights -> start random, apply a learning rule (gets better at task, maybe, but requires lots of computing) 

### Neural Engineering 
- Neuron activity is a distributed representation of a vector x 
- connections from neurons decode functions of x 

