from saleapp import app, dao
from flask import Flask, render_template, request, url_for, redirect


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/products')
def products_list():
    keyword = request.args["keyword"] if request.args.get("keyword") else None
    from_price = float(request.args["from_price"]) if request.args.get("from_price") else None
    to_price = float(request.args["to_price"]) if request.args.get("to_price") else None
    return render_template("product-list.html",
                           products=dao.read_product(keyword=keyword, from_price=from_price, to_price=to_price))


@app.route('/products/<int:category_id>')
def product_list_by_cate(category_id):
    return render_template("product-list.html", products=dao.read_products_by_cate_id(cate_id=category_id))


@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    """

    add: /products/add
    update: /products/add?product_id
    :return: template
    """
    err_mgs = None
    if request.method.lower() == "post":
        if request.args.get("product_id"): #UPDATE
            d = request.form.copy()
            d["product_id"] = request.args["product_id"]
            if dao.update_product(**d):
                return redirect(url_for('products_list'))
            else:
                err_mgs = "some thing wrong !"
        else:#add
            if dao.add_products(**dict(request.form)):
                return redirect(url_for('products_list'))

            else:
                err_mgs = "some thing wrong !"

    categories = dao.read_categories()
    product = None
    if request.args.get("product_id"):
        product = dao.read_product_by_id(product_id=int(request.args["product_id"]))

    return render_template("product-add.html", categories=categories, product=product, err_mgs=err_mgs)


if __name__ == '__main__':
    app.run(debug=True)
