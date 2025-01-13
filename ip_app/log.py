from .models import Logs

def log_create(action_performed, product_name, product_id, description):
    Logs.objects.create(
        action_performed = action_performed, 
        product_name = product_name,
        description = description
    )
