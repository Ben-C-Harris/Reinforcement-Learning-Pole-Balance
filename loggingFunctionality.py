from statistics import mean
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import deque
import os
import csv
import numpy as np
import sys
import seaborn as sns
sns.set()

SCORES_CSV_PATH = "./scores/scores.csv"
SCORES_PNG_PATH = "./scores/scores.png"
SOLVED_CSV_PATH = "./scores/solved.csv"
SOLVED_PNG_PATH = "./scores/solved.png"

# Requirements for Solution (ref: https://github.com/openai/gym/wiki/CartPole-v0)
AVERAGE_SCORE_TO_SOLVE = 195
CONSECUTIVE_RUNS_TO_SOLVE = 100

class LoggerOutputs:
    
    '''
    Class initialization and check file paths
    '''
    def __init__(self, env_name):
        self.scores = deque(maxlen = CONSECUTIVE_RUNS_TO_SOLVE)
        self.env_name = env_name

        # Check if paths exhist, if they do then delete old data and start afresh
        if os.path.exists(SCORES_PNG_PATH):
            os.remove(SCORES_PNG_PATH)
        if os.path.exists(SCORES_CSV_PATH):
            os.remove(SCORES_CSV_PATH)

    '''
    Method called from main calculation class in kerasPoleBalance.py
    This method is called at the end of each simulation run and appends 
    the score for graphing and finding the min, max, and avg scores.
    Each time it is called, it saves a CSV of the scores to date and
    picture of its graph. Upon solution found it does this again.
    
    '''
    def addScore(self, score, run):
        self.saveCSV(SCORES_CSV_PATH, score)
        self.savePNG(input_path = SCORES_CSV_PATH,
                       output_path = SCORES_PNG_PATH,
                       title = "OpenAI Gym env: " + self.env_name,
                       x_label = "Simulation Run",
                       y_label = "Score",
                       averageLabel = 0,                       
                       nAverageRuns = CONSECUTIVE_RUNS_TO_SOLVE,
                       show_goal = True,
                       show_trend = True,
                       show_legend = True)
        
        self.scores.append(score)
        mean_score = mean(self.scores)
        
        # Console logging
        print("Scores: (min: " + str(min(self.scores)) + ", avg: " + str(mean_score) + ", max: " + str(max(self.scores)) + ")\n")
        
        # You have attained the average score required and completed the minimum number of simulations specified
        if mean_score >= AVERAGE_SCORE_TO_SOLVE and len(self.scores) >= CONSECUTIVE_RUNS_TO_SOLVE: # Solution Found
            solve_score = run-CONSECUTIVE_RUNS_TO_SOLVE
            print( "Solved in " + str(solve_score) + " runs, " + str(run) + " total runs.")
            self.saveCSV(SOLVED_CSV_PATH, solve_score)
            self.savePNG(input_path = SOLVED_CSV_PATH,
                           output_path = SOLVED_PNG_PATH,
                           title = "OpenAI Gym env: " + self.env_name + " number of iterations to solve run",
                           x_label="Sucessfully Solved Runs",
                           y_label="Step iterations before solution is solved",
                           averageLabel = 1,
                           nAverageRuns = None,
                           show_goal = False,
                           show_trend = False,
                           show_legend = True)
            sys.exit() # Terminate simulations - adaquate solution found

    '''
    Save plot picture showing have scores have evolved over training life,
    including trend since start, local average, and target score   
    '''
    def savePNG(self, input_path, output_path, title, x_label, y_label, averageLabel, nAverageRuns, show_goal, show_trend, show_legend):
        x = []
        y = []
        with open(input_path, "r") as scores:
            reader = csv.reader(scores)
            data = list(reader)
            for i in range(0, len(data)):
                x.append(int(i))
                y.append(int(data[i][0]))

        plt.subplots()
        plt.plot(x, y, label = "Run score")

        averageRange = nAverageRuns if nAverageRuns is not None else len(x)
               
        if averageLabel == 0: # Graph type 0 - iterative graph
            labelAvg = "Final " + str(averageRange) + " runs score average"
        elif averageLabel == 1: # Graph type 1 - final output graph
            labelAvg = "Average number of steps required to converge on solution"
        
        plt.plot(x[-averageRange:], [np.mean(y[-averageRange:])] * len(y[-averageRange:]), linestyle = "--", label = labelAvg)

        if show_goal:
            plt.plot(x, [AVERAGE_SCORE_TO_SOLVE] * len(x), linestyle = ":", label = "Average score goal of: " + str(AVERAGE_SCORE_TO_SOLVE))

        if show_trend and len(x) > 1:
            trend_x = x[1:]
            
            # Be aware that polyfit will give RankWarning in first couple iterations due to polyfit'ing on only a couple points
            z = np.polyfit(np.array(trend_x), np.array(y[1:]), 1)
            p = np.poly1d(z)
            plt.plot(trend_x, p(trend_x), linestyle = "-.",  label="Lifetime trend")

        plt.title(title)        
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        if show_legend:
            plt.legend(loc="upper left")

        plt.savefig(output_path, bbox_inches="tight")
        plt.close()

    '''
    Save CSV of each runs score to date with predesignated path.
    If path does not exist then create the file
    '''
    def saveCSV(self, path, score):
        if not os.path.exists(path):
            with open(path, "w", newline=""):
                pass
        scores_file = open(path, "a", newline="")
        with scores_file:
            writer = csv.writer(scores_file)
            writer.writerow([score])
            
            
            
            
            
