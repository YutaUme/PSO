import numpy as np
from config import Config as cf
import function as fn

class Individual:
    def __init__(self):
        self.__position = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()
        self.__velocity = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()
        self.__fitness = fn.calculation(self.__position,0) # iteration = 0
        self.__p_best_position = self.__position
        self.__p_best_fitness = self.__fitness

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = velocity

    def get_fitness(self):
        return self.__fitness

    def set_fitness(self,fitness):
        self.__fitness = fitness

    def get_p_best_position(self):
        return self.__p_best_position

    def set_p_best_position(self,p_best_position):
        self.__p_best_position = p_best_position

    def get_p_best_fitness(self):
        return self.__p_best_fitness

    def set_p_best_fitness(self,p_best_fitness):
        self.__p_best_fitness = p_best_fitness

    def update_position(self):
        self.__position = self.__position + self.__velocity

        """Simple Boundary Rule (#if over boundary, set zero velocity)"""
        for i in range(len(self.__position)):
            if (self.__position[i] > cf.get_max_domain()):
                self.__position[i] = cf.get_max_domain()
                # self.__velocity = np.zeros(len(self.__velocity))
            if (self.__position[i] < cf.get_min_domain()):
                self.__position[i] = cf.get_min_domain()
                # self.__velocity = np.zeros(len(self.__velocity))

    def update_velocity(self, best_position):
        r_1 = np.random.rand(cf.get_dimension())
        r_2 = np.random.rand(cf.get_dimension())

        """
        [Reload Equation] (x indicate position vector)
        v = wv + c_1 * r_1 (x_pbest - x) + c_2 * r_2 (x_gbest - x)
        """
        self.__velocity = cf.get_W() * self.__velocity \
                          + cf.get_C1() * r_1 * (self.__p_best_position - self.__position) \
                          + cf.get_C2() * r_2 * (best_position - self.__position)

    def print_info(self,i):
        print("id:","{0:3d}".format(i),
              "|| fitness:",str(self.__fitness).rjust(14," "),
              "|| position:",np.round(self.__position,decimals=4))

if __name__ == '__main__':
    pass
