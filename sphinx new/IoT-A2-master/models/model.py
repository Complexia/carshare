from flask import jsonify

class Model:
    # get the parameters of the model in a writable format
    def getWritable(self):
        return list(self.__dict__.values())