import numpy as np
from typing import List, Union
from loguru import logger
from pydantic import BaseModel

class DPMetrics(BaseModel):
    epsilon: float
    sensitivity: float
    mechanism: str = "Laplace"

class DifferentialPrivacyEngine:
    def __init__(self, epsilon: float):
        self.epsilon = epsilon
        logger.info(f"DP Engine initialized with epsilon={self.epsilon}")

    def add_laplace_noise(self, value: Union[float, np.ndarray], sensitivity: float) -> Union[float, np.ndarray]:
        """Applies the Laplace Mechanism to a value or array."""
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale, size=np.shape(value))
        logger.debug(f"Applying Laplace noise with scale {scale:.4f}")
        return value + noise

    def generate_synthetic_data(self, original_data: np.ndarray, sensitivity: float) -> np.ndarray:
        """Generates a differentially private synthetic version of the input data."""
        logger.info("Generating DP synthetic dataset...")
        return self.add_laplace_noise(original_data, sensitivity)

if __name__ == "__main__":
    # Example Usage: Privacy-Preserving Analytics
    engine = DifferentialPrivacyEngine(epsilon=0.1) # Strong privacy
    
    # Sensitive dataset (e.g., ages, salaries)
    sensitive_data = np.array([25, 30, 45, 50, 60], dtype=float)
    
    # Sensitivity usually represents the max possible change by 1 individual
    # For a mean age, it might be (max_age - min_age) / N
    dp_data = engine.generate_synthetic_data(sensitive_data, sensitivity=1.0)
    
    print(f"Original Data: {sensitive_data}")
    print(f"DP Synthetic Data: {dp_data}")
    print(f"Privacy Loss (Epsilon): {engine.epsilon}")