# Deep Q Neural Network to solve OpenAI Cart Pole challenge

# Top 5 in leaderboard - https://github.com/openai/gym/wiki/Leaderboard#cartpole-v0

OpenAI Gym's Cartpole problem is an environment where the goal is to train an agent to balance a pole on a moving cart with limitations as below:

    Observation: 
        Type: Box(4,)
        Num	Observation                 Min         Max
        0	Cart Position             -4.8            4.8
        1	Cart Velocity             -Inf            Inf
        2	Pole Angle                 -24°           24°
        3	Pole Velocity At Tip      -Inf            Inf
        
    Action:
        Type: Discrete(2)
        Num	Action
        0	Push cart to the left
        1	Push cart to the right
        
Keras with a TensorFlow backend has been applied to the problem with multiple iterations and permutations of Deep Q Neural Networks, including differing node counts, layers, activation functions, and optimisation.

Ultimately, the best solution found has been through applying a Sequential model as outlined below. The ReLU activation function is applied to hidden layers, while a linear activation function is applied to the output layer.

<p align="center"><img src="/modelExport/modelSpec.png" /></p>

The OpenAI Cart Pole Challenge is to deliver a model that as quickly as possible delivers an average score of over 195. This requires an aggressive initial learning stage and as such, in the real world/commercial environment it would be better to have a longer learning period which would likely deliver better overall long term performance.

Below is a scores output of my Deep Q Neural Network, you can see that within 12 Runs, it delivers a 100 run average of over 195. **This places it 5th in the challenge leaderboard.**

Photo of scores through life of model till solved
<p align="center"><img src="outputs/scores.png" /></p>

Below is the first 5 learning iterations, you can see where it fails on pole angle. (If the GIF stops, refresh the page)
<p align="center"><img src="GIFs/FirstFiveIterations.gif" /></p>

Below is one of the final iterations, you can see the substantial improvement from the above. (If the GIF stops, refresh the page)
<p align="center"><img src="GIFs/RunningModelExample.gif" /></p>

# Dependencies

    matplotlib
    deque
    os
    csv
    numpy
    sys
    seaborn
    random
    gym
    keras
    PIL   

# How to run
The model is simple to run. Ensure you have the above packages installed in your environment and download:

    kerasPoleBalance.py
    loggingFunctionality.py

Run kerasPoleBalance.py and you're done. Any outputs requested will be generated within that directory.
