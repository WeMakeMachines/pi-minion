# Installing Python Dependencies on Linux servers

## Installing Python 3.9.5

On debian and derivatives, the python3 package only installs Python up to version 3.7, which doesn't include support for the typings used in this project

It might therefore be necessary to manually compile Python 3.9.5

1. Run the following command to setup the build tools

    ```shell
   sudo apt install wget software-properties-common build-essential libnss3-dev zlib1g-dev libgdbm-dev libncurses5-dev libssl-dev libffi-dev libreadline-dev libsqlite3-dev libbz2-dev 
   ```
   
2. Download Python 3.9.5

    ```shell
    wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
   ```
   
3. Extract the contents of the compressed file, and move into the folder

    ```shell
    tar xvf Python-3.9.5.tgz
    cd Python-3.9.5/
    ```

4. Configure

    ```shell
    ./configure –enable-optimizations
    ```
   
5. Install

    ```shell
    sudo make altinstall
    ```
   
6. Verify with the following command
    
    ```shell
    python3.9 -V
    ```
   
### Aliasing to python3

Additionally, you might want to remove any old references to python3, and alias this to the new installation

```shell
sudo apt remove python3
```

Once this is complete, add the following line to the end of `~/.bashrc`

```bash
alias python3='python3.9'
```

## Other dependencies

```text
sudo apt install python-pip python3-venv
```