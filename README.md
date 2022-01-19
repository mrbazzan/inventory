
# SHOPIFY BACKEND INTERN CHALLENGE

## Aim
To build an inventory tracking web application for a logistics company.

## How to use application

- Install **Python** from [this url](https://python.org/downloads)

- Download **Pycharm Community Edition** from [this url](https://www.jetbrains.com/pycharm/download/)

- Follow the [*Get started*](https://www.jetbrains.com/help/pycharm/quick-start-guide.html#create) guide for Pycharm.

- Clone this repository from Pycharm **terminal**
```shell
git clone https://github.com/mrbazzan/inventory.git
```

- Change to the inventory directory
```shell
cd inventory
```

- Create a virtual environment, activate it and install the requirements
    ```shell
    python3 -m venv venv/
    ```
    
    For Linux/Max OS
    ```shell
    source venv/bin/activate
    ```
    For Windows
    ```shell
    cd venv/Scripts && activate
    ```
    Then;
    ```shell
    pip install -r requirements.txt
    ```

- Make and Run migrations
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

- Run server and proceed to the 127.0.0.1:8000
```shell
python3 manage.py runserver
```