# Try the Seshat API in Jupyter

You can explore the Seshat data in an interactive Jupyter notebook. This folder contains examples of how to use it. First, follow these steps:

1. Ensure you have a working installation of Python 3 and Conda. If not, [download Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html), which should give you both
    - Note: you can use a different tool for creating a Python virtual environment than conda (e.g. venv) if you prefer

2. Set up a virtual environment, install packages into it and create a jupyter kernel.

    ```
        conda create --name seshat_api python=3.11
        conda activate seshat_api
        python -m ipykernel install --user --name=seshat_api --display-name="Python (seshat_api)"
    ```

3. Install the *seshat_api* package into the venv.

    ```     
        git clone https://github.com/Seshat-Global-History-Databank/seshat_api
        cd seshat_api
        pip install .
    ```

4. You can then open the notebook with Jupyter (or another application that can run notebooks such as VSCode). First go to this examples dir and open the Jupyter notebook application:
    ```
        cd examples
        jupyter notebook
    ```
    - Note: if Jupyter wants to to set a password, use `Ctrl-C` to escape and run `jupyter notebook --generate-config` before running `jupyter notebook` again and entering a blank password.

4. From the Jupyter notebook interface in your browser, choose an `.ipynb` file to open, then choose the Kernel that you created called `Python (seshat_api)` in the top right.

5. Follow the instructions in the notebook.