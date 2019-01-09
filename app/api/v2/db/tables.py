
users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY, 
    username VARCHAR(55) NOT NULL,
    email VARCHAR(55) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(25) NOT NULL,
    user_type boolean DEFAULT True)
    """


meals_table = """
CREATE TABLE IF NOT EXISTS meals (
    name VARCHAR(25) NOT NULL,
    description VARCHAR(25) NOT NULL,
    price INT NOT NULL,
    meal_id serial PRIMARY KEY)
"""

orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id serial PRIMARY KEY,
    user_id INT,
    -- ordered_date TIMESTAMP WITH TIME ZONE DEFAULT ('now'::text)::date not null,
    name VARCHAR(250) NOT NULL,
    price INT NOT NULL,
    status VARCHAR (25) DEFAULT 'Pending',
    description VARCHAR(255))"""

blacklist = """
CREATE TABLE IF NOT EXISTS blacklist (
    user_tokens character varying(200) NOT NULL
) 
"""

queries = [users_table, meals_table, orders_table]
