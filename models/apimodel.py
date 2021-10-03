from mongoengine import Document, StringField, ListField, FloatField, ReferenceField
from models.prediction import Prediction
import numpy as np

class ApiModel(Document):
    name = StringField(required=True)
    url = StringField(required=True)
    predictions = ListField(ReferenceField(Prediction))

    high_ls = FloatField(default=0.008*10)
    moderate_ls = FloatField(default=0.001*10)
    low_ls = FloatField(default=0.991*10)
    high_area = FloatField(default=0.008*10)
    moderate_area = FloatField(default=0.001*10)
    low_area = FloatField(default=0.991*10)
    moderate_weight = FloatField(default=1) 

    #Calculates the log diagnostic odds ratio of a model
    #with high_ls landslides predicted with high risk (total or pct)
    #with high_area area labeled as high risk (total or pct)
    #and weighting moderate risk alerts with certain weight compared
    #to high risk alerts
    def log_dor(self,high_ls,
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

    #returns the log diagnostic odds ratio for the test
    def get_score(self):
        return(self.log_dor(self.high_ls, 
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
    #weight is weight of event. If only interested in some area, set 0 for all slides
    #in other areas and 1 for all slides in area of interest. Should be number
    #between 0 and 1 to keep model prior meaningful
    def add_slide(self, 
                  classification, 
                  high_area, 
                  moderate_area, 
                  low_area,
                  weight):
        total_area = high_area + moderate_area + low_area
        high_area /= total_area
        moderate_area /= total_area
        low_area /= total_area
        if classification == "High":
            self.high_ls += 1*weight
        elif classification == "moderate":
            self.moderate_ls += 1*weight
        elif classification == "Low":
            self.low_ls += 1*weight
        self.high_area += high_area*weight
        self.moderate_area += moderate_area*weight
        self.low_area += low_area*weight
    
