from saleapp import app
import json
import os


def read_product(keyword=None, from_price=None, to_price=None):
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        products = json.load(f)
    if keyword:
        return [product for product in read_product() if product["name"].find(keyword) >= 0]
    if from_price and to_price:
        return [product for product in read_product() if from_price <= product["price"] <= to_price]
    return products


def read_products_by_cate_id(cate_id):
    return [product for product in read_product() if product["category_id"] == cate_id]


if __name__ == "__main__":
    print(read_product())
