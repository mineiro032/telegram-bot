import mercadopago


def gerar_link_de_pagamento():
    sdk = mercadopago.SDK("TEST-520820846840078-043012-f4b7251db15c5de9b54c9767eb25259a-336930514")

    payment_data = {
        "items": [
            {
                "id": "1",
                "title": "VIP",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 9.99,
            },
        ],
        "back_urls": {
            "success": "https://t.me/V1PVendas_bot/compracerta",
            "failure": "http://test.com/failure/compraerrada",
            "pending": "http://test.com/pending/compraerrada",
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento