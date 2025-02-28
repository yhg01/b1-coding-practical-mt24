"""
This module implements the UUV controller
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Controller:
    """
    A proportional-derivative controller
    """
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0

    def update(self, current_value,setpoint,dt):
        """
        Update the controller with the current value and return the control signal

        :param current_value: the current position of the system
        :return: the control signal
        """
        error = setpoint - current_value
        derivative = (error - self.previous_error)/dt
        self.previous_error = error
        return self.kp * error + self.kd * derivative


