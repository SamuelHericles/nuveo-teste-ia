class SpamDetector:
    def __init__(self, model):
        """
            This class is to get if mensage is spam and your probability.

            @param model - object uploade model.
        """
        if f"{type(model)}" == "<class 'sklearn.pipeline.Pipeline'>":
            self.model = model
        else:
            raise TypeError('This is not a model uploaded from pickle framework')

    def is_spam(self, treated_mensage): 
        """
            This function return a boolean if mensage is spam or not

            @param treated_mensage - mensage string

            @return boolean, true for spam, flase for ham
        """
        return round(self.prob_spam(treated_mensage),0) == 1 

    def prob_spam(self, treated_mensage):
        """
            This function return a probability if mensage is spam

            @param treated_mensage - mensage string

            @return spam probobility's in float
        """        
        return self.model.predict_proba([treated_mensage])[0,1]