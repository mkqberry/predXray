import os
from cv2 import cv2
from tensorflow.keras.models import load_model
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class DeepLearning:
    def __init__(self, filePath:str):
        self.filePath = filePath
        self.mainPath = os.getcwd()
    
    def imagePreprocessing(self):
        fpath = self.filePath[::-1]
        fname = fpath.split("/")[0]
        fname = fname[::-1]
        fpath = fpath[::-1]
        fpath = fpath.replace("/"+fname, "")
        os.chdir(fpath)
        img_array = cv2.imread(fname, cv2.IMREAD_COLOR)
        img = cv2.resize(img_array, (224, 224))
        img = img.reshape(1, 224, 224, 3)
        os.chdir(self.mainPath)
        return img
    
    def loadSavedModel(self):
        #path = os.getcwd()
        modelpath = os.path.join(self.mainPath, "model")
        modelpath = os.path.join(modelpath, "resnet_50.h5")
        model = load_model(modelpath)
        return model
    
    def getClass(self):
        model = self.loadSavedModel()
        x = self.imagePreprocessing()
        result = model.predict(x)
        result = np.argmax(result, axis=1)
        result = str(result[0])
        return result
