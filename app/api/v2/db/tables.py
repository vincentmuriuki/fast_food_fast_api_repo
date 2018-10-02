
users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY, 
    username VARCHAR(55) NOT NULL,
    email VARCHAR(55) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(25) NOT NULL,
    user_type boolean DEFAULT false
)
"""

category_table = """
CREATE TABLE IF NOT EXISTS categories (
 category_id serial PRIMARY KEY,
 category_name VARCHAR(25) NOT NULL
)
"""

meals_table = """
CREATE TABLE IF NOT EXISTS meals (
    name VARCHAR(25) NOT NULL,
    description VARCHAR(25) NOT NULL,
    price INT NOT NULL,
    meal_id serial PRIMARY KEY,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
)
"""

orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id serial PRIMARY KEY,
    user_id INT NOT NULL,
    ordered_date VARCHAR(250) NOT NULL,
    price INT NOT NULL,
    status VARCHAR (25) NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
"""

blacklist = """
CREATE TABLE IF NOT EXISTS blacklist (
    user_tokens character varying(200) NOT NULL
) 
"""

queries = [category_table, users_table, meals_table, orders_table]
