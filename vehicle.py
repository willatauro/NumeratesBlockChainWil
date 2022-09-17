class Vehicle:
            ### Below is an class variable/attribute and not instance variable , all instances will share the same attribute
    # top_speed = 100
    # warnings = []

#We use constructor so that we can use instance variables instead of class variables 
### __ (double underscore) is called dunder , below is special method and there are many other
    def __init__(self, starting_top_speed = 100):
        self.top_speed = starting_top_speed
        #self.warnings =[]
        # this is convention to make it private but its not stopping anyone from accessing it,python will yell, here you can access from inside the class methods and not outside

        self.__warnings=[]

    def add_warning(self, warning_text):

        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    ## special method to print object

    def __repr__(self):
        print('Printing')

        ## it has to return something
        return 'Top Speed : {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def drive(self):
        print('I am driving but certainlyy not faster than {}'.format(self.top_speed))

    def get_warnings(self):
        return self.__warnings