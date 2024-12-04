import numpy as np
import pandas as pd
import statsmodels.formula.api as smf



class regression_discontinuity(object):
    
    def __init__(self, data, treatment_col, outcome_col, cutoff):
        self.data = data
        self.treatment_col = treatment_col
        self.outcome_col = outcome_col
        self.cutoff = cutoff
        self.data['treatment'] = self.data[treatment_col] > self.cutoff



    

class linear_rd(regression_discontinuity):
        
    def __init__(self, data, treatment_col, outcome_col, cutoff):
        super().__init__(data, treatment_col, outcome_col, cutoff)
        
    def fit(self, bandwidth=0.1, kernel='triangular'):
        self.data['treatment'] = self.data[self.treatment_col] > self.cutoff

        model = smf.wls(f'{self.outcome_col} ~ treatment + {self.treatment_col}', self.data)

        self.results = model.fit()

        return self.results
    
    def summary(self):
            return self.results.summary()
        
class linear_interaction_rd(regression_discontinuity):
    pass
