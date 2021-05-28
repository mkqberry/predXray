import os
import cv2
from tensorflow.keras.models import load_model
import numpy as np

class DeepLearning:
    def __init__(self, filePath:str, fileName:str):
        self.filePath = filePath
        self.fileName = fileName
        self.mainPath = os.getcwd()
   
    def imagePreprocessing(self):
        fpath = self.filePath.replace("/"+self.fileName, "")
        os.chdir(fpath)
        img_array = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        img = cv2.resize(img_array, (224, 224))
        img = img.reshape(1, 224, 224, 3)
        os.chdir(self.mainPath)
        return img
    
    def loadSavedModel(self):
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
