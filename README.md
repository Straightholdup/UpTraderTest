# UpTrader test project

## Usage

1. Clone this repository to your local machine.

2. Create a `.env` file inside the `src` directory with the following content:

    ```
    DEBUG=1
    SECRET_KEY=foo
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=up_trader_db
    SQL_USER=up_trader
    SQL_PASSWORD=up_trader
    SQL_HOST=db
    SQL_PORT=5432
    ```

   Make sure to replace the values with your desired settings.

3. Run the following command in the root directory of the cloned repository to start the containers:

    ```
    docker-compose up --build
    ```

   This command will build the Docker images and start the containers for the Django web application and PostgreSQL
   database.

4. Access the Django application by navigating to `http://localhost:8000` in your web browser.