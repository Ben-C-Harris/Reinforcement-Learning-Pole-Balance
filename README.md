# Deep Q Neural Network to solve OpenAI Cart Pole challenge


# Top 5 in leaderboard - https://github.com/openai/gym/wiki/Leaderboard#cartpole-v0

# Summary:
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

Ultimately, the best solution found has been through applying a Sequention model as outlined below. The ReLU activation function is applied to hidden layers, while a linear activation function is applied to the output layer.

<p align="center"><img src="/modelExport/modelSpec.png" /></p>



Photo of scores through life of model till solved
<p align="center"><img src="outputs/scores.png" /></p>

GIF of first five iterations to show starting point
<p align="center"><img src="GIFs/FirstFiveIterations.gif" /></p>

GIF of final iteration to show end point
<p align="center"><img src="GIFs/RunningModelExample.gif" /></p>
