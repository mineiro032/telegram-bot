import os
import telebot
from telebot import types
from api_mercadopago import gerar_pix_pagamento

CHAVE_API = os.getenv("6350617394:AAF1CTTjzmPpI823ohPQiGC1JV3ZSesJKu0")
bot = telebot.TeleBot(CHAVE_API)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "pagar_vip":
        try:
            # Gerar o QR Code do PIX
            pix_code = gerar_pix_pagamento()

            # Criar o botão de pagamento via PIX
            botao_pagamento = types.InlineKeyboardButton("PAGAR VIA PIX", callback_data="pagar_vip")

            # Criar layout com o botão de pagamento
            layout_pagamento = types.InlineKeyboardMarkup()
            layout_pagamento.add(botao_pagamento)

            # Enviar a mensagem com o código do PIX e o botão de pagamento
            message = bot.send_message(call.message.chat.id, f"Seu código PIX para pagamento é:\n\n{pix_code}", parse_mode="Markdown", reply_markup=layout_pagamento)
        except Exception as e:
            bot.send_message(call.message.chat.id, "Desculpe, ocorreu um erro ao gerar o código do PIX. Por favor, tente novamente mais tarde.")
            print(f"Erro ao gerar o código do PIX: {e}")