import sqlite3


def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()


def add_products():
    products = [
        ("Продукт 1", 50.0, 10),
        ("Продукт 2", 70.0, 15),
        ("Продукт 3", 90.0, 20),
        ("Продукт 4", 30.0, 5),
        ("Продукт 5", 60.0, 25),
        ("Продукт 6", 20.0, 8),
        ("Продукт 7", 100.0, 3),
        ("Продукт 8", 10.0, 7),
        ("Продукт 9", 45.0, 12),
        ("Продукт 10", 35.0, 18),
        ("Продукт 11", 55.0, 22),
        ("Продукт 12", 65.0, 17),
        ("Продукт 13", 75.0, 13),
        ("Продукт 14", 85.0, 9),
        ("Продукт 15", 95.0, 4)
    ]

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()


def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def select_products_by_limit(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def main():
    create_database()

    add_products()

    update_quantity(1, 50)

    update_price(1, 75.5)

    delete_product(15)

    print("Все товары:")
    select_all_products()

    print("\nТовары дешевле 100 сом и больше 5 шт:")
    select_products_by_limit(100, 5)

    print("\nПоиск товаров по названию 'Продукт':")
    search_products_by_title("Продукт")


if __name__ == "__main__":
    main()
