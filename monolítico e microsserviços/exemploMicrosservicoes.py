class UserService:
    def validate_user(self, user_id):
        return user_id is not None # Simula validação de usuário
    
class OrderService:
    def confirm_order(self, user_id, product_id):
        if not user_service.validate_user(user_id):
            return "Usuário inválido!"
        print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
        return "Pedido confirmado com sucesso!"
