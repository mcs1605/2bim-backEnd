def process_order(user_id, product_id, payment_info):
    if not (user_id and product_id and payment_info):
        return "Dados inválidos!"
    print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
    return "Pedido confirmado com sucesso!"

compra = process_order(100, 4005, 'cartao_de_credito')
print(compra)

