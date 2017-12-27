import numpy as np
import individual as id
import function as fn
import sys
import os
import csv
from config import Config as cf


"""for make result file (results.csv)"""
if os.path.exists("results"):
    pass
else:
    os.mkdir("results")

results = open("results" + os.sep + "results.csv", "w")
results_writer = csv.writer(results, lineterminator="\n")


def main():
    for trial in range(cf.get_trial()):
        np.random.seed(trial)
        results_list = [] # fitness list
        pso_list = [] # firefly list
        """Generate Initial Population"""
        for p in range(cf.get_population_size()):
            pso_list.append(id.Individual())

        """Sort Array"""
        pso_list =  sorted(pso_list, key=lambda ID : ID.get_fitness())

        """Find Initial Best"""
        BestPosition = pso_list[0].get_position() # Best Solution
        BestFitness = fn.calculation(BestPosition,0)

        """↓↓↓Main Loop↓↓↓"""
        for iteration in range(cf.get_iteration()):

            """Generate New Solutions"""
            for i in range(len(pso_list)):

                """Update Position"""
                pso_list[i].update_position()

                """Calculate Fitness"""
                pso_list[i].set_fitness(fn.calculation(pso_list[i].get_position(), t=iteration))

                """if f_x < f_(p_best) # for minimize optimization"""
                if(pso_list[i].get_fitness() < pso_list[i].get_p_best_fitness()):
                    pso_list[i].set_p_best_fitness(pso_list[i].get_fitness())
                    pso_list[i].set_p_best_position(pso_list[i].get_position())

                """if f_x < f_(g_best) # for minimize optimization"""
                if(pso_list[i].get_fitness() < BestFitness):
                    BestFitness = pso_list[i].get_fitness()
                    BestPosition = pso_list[i].get_position()

                """Reload Velocity"""
                pso_list[i].update_velocity(BestPosition)

            """Sort Array"""
            pso_list = sorted(pso_list, key=lambda ID: ID.get_fitness())

            """Rank and Find the Current Best"""
            if pso_list[0].get_fitness() < BestFitness:
                BestPosition = pso_list[0].get_position()
                BestFitness = fn.calculation(BestPosition,iteration)

            sys.stdout.write("\r Trial:%3d , Iteration:%7d, BestFitness:%.4f" % (trial , iteration, BestFitness))
            results_list.append(str(BestFitness))

        results_writer.writerow(results_list)

if __name__ == '__main__':
    main()
    results.close()
