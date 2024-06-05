import mercadopago

def gerar_pix_pagamento():
    sdk = mercadopago.SDK("APP_USR-520820846840078-043012-94bb70878cdd1c3a495338af368ccaeb-336930514")

    payment_data = {
        "transaction_amount": 9.99,
        "description": "Assinatura VIP",
        "payment_method_id": "pix",
        "payer": {
            "email": "user@example.com"
        },
        "back_urls": {
            "success": "https://t.me/+33V5tRO6NwU1ZGUx",
            "failure": "http://test.com/failure/compraerrada",
            "pending": "http://test.com/pending/compraerrada"
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento