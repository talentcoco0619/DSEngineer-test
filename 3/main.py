from abc import ABC, abstractmethod
import numpy as np

class DigitClassificationInterface(ABC):
    @abstractmethod
    def predict(self, image: np.ndarray) -> int:
        pass

class ConvolutionalNeuralNetwork(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Assume image is a 28x28x1 tensor
        # ... CNN prediction logic ...
        raise NotImplementedError

class RandomForestClassifier(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Flatten the image to a 1D array of 784 elements
        image = image.flatten()
        # ... Random Forest prediction logic ...
        raise NotImplementedError

class RandomModel(DigitClassificationInterface):
    def predict(self, image: np.ndarray) -> int:
        # Assume image is a 10x10 center crop
        # ... Random value prediction logic ...
        return np.random.randint(0, 10)
    
class DigitClassifier:
    def __init__(self, algorithm: str):
        self.model = self._select_model(algorithm)

    def _select_model(self, algorithm: str) -> DigitClassificationInterface:
        if algorithm == 'cnn':
            return ConvolutionalNeuralNetwork()
        elif algorithm == 'rf':
            return RandomForestClassifier()
        elif algorithm == 'rand':
            return RandomModel()
        else:
            raise ValueError("Unsupported algorithm")

    def predict(self, image: np.ndarray) -> int:
        # Ensure image is 28x28x1
        if image.shape != (28, 28, 1):
            raise ValueError("Image must be 28x28x1")
        # Crop the center 10x10 for the RandomModel
        if isinstance(self.model, RandomModel):
            center_crop = image[9:19, 9:19, 0]
            return self.model.predict(center_crop)
        else:
            return self.model.predict(image)
        

# Example usage of DigitClassifier
if __name__ == "__main__":
    classifier = DigitClassifier(algorithm='rand')  #rand, cnn or rf 

    # Create a dummy 28x28x1 numpy array to represent an image
    dummy_image = np.random.rand(28, 28, 1)

    # Make a prediction
    prediction = classifier.predict(dummy_image)
    print(f"The predicted digit is: {prediction}")