import csv

def main():
    products = [
        {"id": 1, "name": "Bàn phím", "price": 250, "quantity": 10},
        {"id": 2, "name": "Chuột", "price": 80, "quantity": 25},
        {"id": 3, "name": "Màn hình", "price": 1500, "quantity": 4},
        {"id": 4, "name": "Tai nghe", "price": 120, "quantity": 12},
        {"id": 5, "name": "Webcam", "price": 95, "quantity": 7},
    ]
    with open("products.csv", mode="w", encoding="utf-8") as file:
        file.write("id,name,price,quantity\n")
        for product in products:
            file.write(f"{product['id']},{product['name']},{product['price']},{product['quantity']}\n")
    products = []
    with open("products.csv", mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = {
                "id": int(row["id"]),
                "name": row["name"],
                "price": float(row["price"]),
                "quantity": int(row["quantity"]),
            }
            products.append(product)
    print("--- Tất cả sản phẩm ---")
    for product in products:
        print(f"{product['id']} - {product['name']} - {product['price']} - {product['quantity']}")
    print("\n--- Sản phẩm có giá > 100 ---")
    for product in products:
        if product["price"] > 100:
            print(f"{product['id']} - {product['name']} - {product['price']} - {product['quantity']}")
    total_value = 0
    for product in products:
        product["total"] = product["price"] * product["quantity"]
        total_value += product["total"]
    print("\n--- Thêm cột total ---")
    for product in products:
        print(
            f"{product['id']} - {product['name']} - {product['price']} - {product['quantity']} - {product['total']}")
    print(f"\nTổng giá trị tồn kho: {total_value}")

if __name__ == '__main__':
    main()