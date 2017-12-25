import numpy as np

"""Describe the Parameters"""
class Config:
    __PopulationSize = 100 # Population Size (default = 15)
    __MaxDomain = 500 # variable upper limit
    __MinDomain = -500 # variable lower limit
    __Dimension = 2 # The number of dimension
    __W = 0.9 # inertia weight
    __C1 = 2.0 # weight for personal best
    __C2 = 2.0 # weight for global best
    __Trial = 31
    __Iteration = 3000

    @classmethod
    def get_population_size(cls):
        return cls.__PopulationSize

    @classmethod
    def get_W(cls):
        return cls.__W

    @classmethod
    def get_C1(cls):
        return cls.__C1

    @classmethod
    def get_C2(cls):
        return cls.__C2

    @classmethod
    def get_iteration(cls):
        return cls.__Iteration

    @classmethod
    def get_trial(cls):
        return cls.__Trial

    @classmethod
    def get_dimension(cls):
        return cls.__Dimension

    @classmethod
    def get_max_domain(cls):
        return cls.__MaxDomain

    @classmethod
    def set_max_domain(cls, _max_domain):
        cls.__MaxDomain = _max_domain

    @classmethod
    def get_min_domain(cls):
        return cls.__MinDomain

    @classmethod
    def set_min_domain(cls, _min_domain):
        cls.__MinDomain = _min_domain







