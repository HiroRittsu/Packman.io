import nidaqmx
import sys
import numpy as np
from matplotlib import pyplot as plt
from threading import Thread
from Controller import Controller
import os

system = nidaqmx.system.System.local()

class EMG(Controller):
    fps = 30
    nb_samples_per_frame = 50
    nb_samples_per_seconds = fps * nb_samples_per_frame

    graph_nb_seconds = 2
    nb_samples_in_graph = nb_samples_per_seconds * graph_nb_seconds
    nb_frames_in_graph = fps * graph_nb_seconds

    def __init__(self, threshold_left=0.6, threshold_right=0.6, frequency=50 * 30):
        Controller.__init__(self);

        self.threshold_left = threshold_left
        self.threshold_right = threshold_right
        self.frequency = frequency

        # Add a nidaqmx task to retrieve sample from the two sensors
        
        self.task = nidaqmx.Task()
        for device in system.devices:
            device_name = device.name
        self.task.ai_channels.add_ai_voltage_chan(device_name+'/ai0')
        self.task.ai_channels.add_ai_voltage_chan(device_name+'/ai1')
        #self.task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
        #self.task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai1")
        #self.task.ai_channels.add_ai_voltage_chan("cDAQ2Mod1/ai0")
        #self.task.ai_channels.add_ai_voltage_chan("cDAQ2Mod1/ai1")
        self.task.timing.cfg_samp_clk_timing(self.frequency, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
        self.task.start()
        

        # Prepare data for the graph
        self.data_left = [0 for i in range(EMG.nb_samples_in_graph)]
        self.data_right = [0 for i in range(EMG.nb_samples_in_graph)]

        self.averages_left = [0 for i in range(EMG.nb_frames_in_graph)]
        self.averages_right = [0 for i in range(EMG.nb_frames_in_graph)]

        # Start a thread to display the graph
        self.thread = Thread(target=self.run_graph)
        self.thread.setDaemon(True)
        self.thread.start()

    def get_input(self):
        # Get all the data available in the buffer (so all data since the previous frame)
        
        data = self.task.read(number_of_samples_per_channel=nidaqmx.constants.READ_ALL_AVAILABLE)
        data_left = data[0]
        data_right = data[1]

        if len(data_left) != 0:
            average_left = sum(data_left) / len(data_left)
        else:
            average_left = 0
        if len(data_right) != 0:     
            average_right = sum(data_right) / len(data_right)
        else:
            average_right = 0

        # Update data for the graph
        self.averages_left = self.averages_left[1:] + [average_left]
        self.averages_right = self.averages_right[1:] + [average_right]

        self.data_left = self.data_left[len(data_left):] + data_left
        self.data_right = self.data_right[len(data_right):] + data_right

        # Check which direction the player wants to go
        left = average_left >= self.threshold_left
        right = average_right >= self.threshold_right

        if left and right:
           return Controller.Input.Launch
       
        if left:
            return Controller.Input.Left

        if right:
            return Controller.Input.Right
        
        return Controller.Input.Null

    def run_graph(self):
        def generate_x(count):
            return np.linspace(-EMG.graph_nb_seconds, 0, count)
        
        fig = plt.figure()

        ax_left = fig.add_subplot(211)
        ax_left.set_title("Left controller")
        ax_left.set_autoscale_on(True)

        graph_samples_left, = ax_left.plot(generate_x(EMG.nb_samples_in_graph), self.data_left)
        graph_averages_left, = ax_left.plot(generate_x(EMG.nb_frames_in_graph), self.averages_left, 'g')
        ax_left.plot(generate_x(EMG.nb_samples_in_graph), [self.threshold_left for i in range(EMG.nb_samples_in_graph)], 'r--')

        ax_right = fig.add_subplot(212)
        ax_right.set_title("Right controller")
        ax_right.set_autoscale_on(True)

        graph_samples_right, = ax_right.plot(generate_x(EMG.nb_samples_in_graph), self.data_right)
        graph_averages_right, = ax_right.plot(generate_x(EMG.nb_frames_in_graph), self.averages_right, 'g')
        ax_right.plot(generate_x(EMG.nb_samples_in_graph), [self.threshold_right for i in range(EMG.nb_samples_in_graph)], 'r--')

        while True:
            graph_samples_left.set_ydata(self.data_left)
            graph_averages_left.set_ydata(self.averages_left)

            ax_left.relim()
            ax_left.autoscale_view(True,True,True)

            graph_samples_right.set_ydata(self.data_right)
            graph_averages_right.set_ydata(self.averages_right)

            ax_right.relim()
            ax_right.autoscale_view(True,True,True)

            plt.draw()
            plt.pause(0.01)


    def close(self):
        os._exit(0)

