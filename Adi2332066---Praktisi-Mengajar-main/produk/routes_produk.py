from flask import blueprints, request, jsonify
from produk.controller.produkcontroller import ProdukController

produk_routes = blueprints('produk_routes', __name__)
produk_controller = ProdukController()

@produk_routes.route('/produk', methods=['GET'])
def lihat_produk():
    return jsonify(produk_controller.lihat_produk())