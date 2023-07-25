class Sinks:
    
    def __init__(self, sink_dict):
        """
        Given a sink dictionary of the form {'name_of_sink': coords, ...}, creates a sink 
        object
        """
        self.sink_dict = sink_dict
