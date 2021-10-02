import numpy as np

#Calculates the log diagnostic odds ratio of a model
#with high_ls landslides predicted with high risk (total or pct)
#with high_area area labeled as high risk (total or pct)
#and weighting moderate risk alerts with certain weight compared
#to high risk alerts
def log_dor(high_ls,
            moderate_ls, 
            low_ls, 
            high_area, 
            moderate_area, 
            low_area, 
            moderate_weight):
    return ((np.log(high_ls) + 
            moderate_weight*np.log(moderate_ls) - 
            (1+moderate_weight)*np.log(low_ls))
    - (np.log(high_area) + 
       moderate_weight*np.log(moderate_area) - 
       (1+moderate_weight)*np.log(low_area)))

class Model_eval:

    #initilizes model evaluation. Moderate_weight is a number in [0,1] which
    #specifies the weight of a "moderate" prediction compared to a "high" 
    #predicition. The larger the prior the slower the evaluation changes
    def __init__(self,moderate_weight,prior):
        self.high_ls = 0.008*prior
        self.moderate_ls = 0.001*prior
        self.low_ls = 0.991*prior
        self.high_area = 0.008*prior
        self.moderate_area = 0.001*prior
        self.low_area = 0.991*prior
        self.moderate_weight = moderate_weight 

    #returns the log diagnostic odds ratio for the test
    def get_score(self):
        return(log_dor(self.high_ls, 
                       self.moderate_ls, 
                       self.low_ls, 
                       self.high_area, 
                       self.moderate_area, 
                       self.low_area, 
                       self.moderate_weight))

    #adds a new historical datapoint. Classification is the model predicition
    #for this landslide, and high_area modertae_area and low_area are
    #the areas classified as high moderate or low risk by the model at the 
    #time of the landslide (total or pct)
    def add_slide(self, 
                  classification, 
                  high_area, 
                  moderate_area, 
                  low_area):
        total_area = high_area + moderate_area + low_area
        high_area /= total_area
        moderate_area /= total_area
        low_area /= total_area
        if classification == "High":
            self.high_ls += 1
        elif classification == "moderate":
            self.moderate_ls += 1
        elif classification == "Low":
            self.low_ls += 1
        else:
            raise Exception("Risk prediction must be High, Moderate or Low")
        self.high_area += high_area
        self.moderate_area += moderate_area
        self.low_area += low_area
        
if __name__ == "__main__":
    print("Running example")
    m1 = Model_eval(moderate_weight = 0.5, prior = 10)
    print("Initial score")
    print(m1.get_score())
    m1.add_slide(classification = "High",
                 high_area = 0.008,
                 moderate_area = 0.001,
                 low_area = 0.991)
    m1.add_slide(classification = "Low",
                 high_area = 0.008,
                 moderate_area = 0.001,
                 low_area = 0.991)
    m1.add_slide(classification = "High",
                 high_area = 0.008,
                 moderate_area = 0.001,
                 low_area = 0.991)
    print("Score after some obeservations")
    print(m1.get_score())
