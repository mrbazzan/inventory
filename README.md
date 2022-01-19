
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

- Load some default data
```shell
python3 manage.py loaddata user.json
python3 manage.py loaddata product.json
```

- Create superuser
```shell
python3 manage.py createsuperuser
```
After that, the [admin page](http://127.0.0.1/admin) can be
accessed using the username and password from the `createsuperuser` above.


- Run server 
```shell
python3 manage.py runserver
```
and proceed to the 127.0.0.1:8000

NB: Because the web app models a logistic company, it is assumed that the company
has agents(driver) that ensure items in the inventory gets delivered to the exact
location. This is why there is a need to populate some data initially(data migration).

You can also opt not to load default data, but there is a need to create superuser.

## ADDITIONAL TASK
- Push a button export product data to CSV.