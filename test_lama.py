from simple_lama_inpainting import SimpleLama
from PIL import Image
import numpy as np

def test_lama():
    print("Initializing LaMa...")
    lama = SimpleLama()
    print("LaMa initialized.")
    
    # Create a dummy image (100x100 white)
    img = Image.new('RGB', (100, 100), color='white')
    # Create a mask (100x100 black)
    mask = Image.new('L', (100, 100), color=0)
    
    print("Running inference on dummy image...")
    res = lama(img, mask)
    print("Inference complete.")
    res.save("test_lama_out.png")

if __name__ == "__main__":
    test_lama()
