import pandas as pd

class TreaterMensage():
    """
        This class is for treat path file, if csv or txt.
        
        @param path - path file where csv or txt file there is.
    """
    def __init__(self, path):
        self.path = path
        self.type = path.split('.')[-1]
        
    def get_mensage(self):
        """
            This funciton upload file correct.

            @return read a string if txt file or upload dataframe type is csv file.        
        """
        if self.type == 'csv':
            try:
                df_mensages = pd.read_csv(self.path, sep='\t', names=['mensages'])            
            except:
                df_mensages = pd.read_csv(self.path, sep='\t')            
            return df_mensages, self.type
            
        elif self.type == 'txt':
            f = open(self.path, "r")
            return f.read(), self.type

        else: 
            print('You not pass corret type')
            return
        