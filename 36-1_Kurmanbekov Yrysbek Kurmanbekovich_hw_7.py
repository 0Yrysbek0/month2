import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
        price NUMERIC(10,2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')


def add_products():
    products_data = [
        ("Product 1", 10.50, 20),
        ("Product 2", 5.99, 15),
        # Добавьте остальные товары
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products_data)
    conn.commit()


def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()


def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()


def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)


def select_filtered_products():
    limit_price = 100.0
    limit_quantity = 5
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (limit_price, limit_quantity))
    filtered_products = cursor.fetchall()
    for product in filtered_products:
        print(product)


def search_products_by_title(title):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + title + '%',))
    matching_products = cursor.fetchall()
    for product in matching_products:
        print(product)


add_products()
select_all_products()
update_quantity(1, 30)
update_price(2, 8.99)
select_filtered_products()
search_products_by_title("мыло")


conn.close()