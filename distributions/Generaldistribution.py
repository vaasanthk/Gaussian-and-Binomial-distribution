class Distribution:

    def __init__(self, mu=0, sigma=1):
        """ Generic distribution class for calculation and 
        visualizing a probability distribution. 

        Attributes:
         mean (float) representing the mean value of the 
         distribution 
         stdev (float) representing the standard deviation of
         the distribution 
         data list (list of floats) a list of floats extracted
         from the data file """

        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """ Function to read the data from a txt file. The txt
        file should have one number (float) per line. 

        The numbers are stored in the data attribute.

        Args:
             file_name (string): name of a file to read from

        Returns:
                None  
        """

        with open(file_name) as f:
            data_list = []
            line = f.readline()
            while line:
                data_list.append(int(line))
                line = f.readline()
        f.close()

        self.data = data_list
