import os
import sys

if 'google.colab' in sys.modules:
    
    # Clone GitHub repository
    !git clone https://github.com/miykael/amld20_classification.git
        
    # Copy files required to run the code
    !cp -r 'amld20_classification/downloads' 'amld20_classification/utils.py' .
    
    # Install packages via pip
    !pip install -r "amld20_classification/colab-requirements.txt"
    
    # Restart Runtime
    os.kill(os.getpid(), 9)