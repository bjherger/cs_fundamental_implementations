# CS Fundamental Implementations

It's been ... a few years since I took an algorithms + data structures course. To keep things fresh, I've decided 
to implement a set of common data structures. 

My goal is to implement:

 - **Data Structures:** Linked Lists, Trees, Tries, Graphs, Stacks, Queues, Heaps, Vectors / ArrayLists, Hash Tables
 - **Algorithms:** Breadth-First Search, Depth-First Search, Binary Search, Merge Sort, Quick Sort

Each with appropriate testing. 

## Quick Start
```
# Create python virtual environment
conda env create -f environment.yml 

;z# Activate python virtual environment
source activate simple

# Run scrip

cd bin/
python main.py  
```

## Getting started

### Repo structure

 - `bin/main`: Code entry point

### Python Environment
Python code in this repo utilizes packages that are not part of the common library. To make sure you have all of the 
appropriate packages, please install [Anaconda](https://www.continuum.io/downloads), and install the environment 
described in environment.yml (Instructions [here](http://conda.pydata.org/docs/using/envs.html), under *Use 
environment from file*, and *Change environments (activate/deactivate)*). 

### To run code
  
To run the Python code, complete the following:
```bash
# Install anaconda environment
conda env create -f environment.yml 
# Make a note of the environent name (e.g. source activate environment_name)

# Activate environment
source activate environment_name

# Run script
cd bin/
python file_name.py
```


## Contact
Feel free to contact me at `13herger <at> gmail <dot> com`
