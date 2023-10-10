## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.7: You can download and install Python from [python.org](https://www.python.org/downloads/).
- `pip`: The package manager for Python. It is usually included with Python installations.
- Pyfirmata: PyFirmata is a Python interface for the Firmata protocol.
- Ultralytics : YOLO is a family of compound-scaled object detection models trained on the COCO dataset
- Pandas : Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool
- Numpy : NumPy is a Python library used for working with arrays.

## Installation

### 1. Clone the Repository

Start by cloning the project repository from GitHub:

```bash
git clone https://github.com/suvanbanerjee/MiniProject.git
```

If you have GitHub CLI installed, you can also use the gh command to clone the repository

### 2. Install Dependencies
``` pip install -r requirements.txt  ```

## Usage


Before running the application, make sure you are in the project directory. Then, edit the signal_n.py (n=1,2,3...) in top section edit the ftp server details and port number, Username and password. 
Then run each signal.py file on n diffrnet computers.

In linker.py file edit the ('COM4') to desired port where arduino is connected.


