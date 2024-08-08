CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM products WHERE name = 'POC') THEN
        INSERT INTO products (name, description, price)
        VALUES ('POC', 'Product of Concept', 99.99);
    END IF;
END $$;