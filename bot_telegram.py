import os
import telebot
from telebot import types
from api_mercadopago import gerar_pix_pagamento

# Carrega a chave da API do Telegram a partir de uma variável de ambiente
CHAVE_API = os.getenv("6350617394:AAF1CTTjzmPpI823ohPQiGC1JV3ZSesJKu0")
bot = telebot.TeleBot(CHAVE_API)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "pagar_vip":
        try:
            # Gerar o QR Code do PIX
            pix_code = gerar_pix_pagamento()

            # Criar o botão de pagamento via PIX
            botao_pagamento = types.InlineKeyboardButton("ASSINAR VIP R$9,99 (PIX)", callback_data="pagar_vip")

            # Criar layout com o botão de pagamento
            layout_pagamento = types.InlineKeyboardMarkup()
            layout_pagamento.add(botao_pagamento)

            # Enviar a mensagem com a imagem, o código do PIX e o botão de pagamento
            with open('./imagem/vip.png', 'rb') as photo:
                message = bot.send_photo(call.message.chat.id, photo, caption=f"*♦️VIDEOS TODOS OS DIAS♦️*\n\n🔥+DE 99VIDEOS\n🔥SEXO\n🔥MASTURBAÇÃO\n🔥ANAL\n🔥SEXO A 3\n\nEstou esperando você bem molhadinha no meu VIP😍\n\n💠CLIQUE PARA PAGAR VIA PIX💠\n\n{pix_code}", parse_mode="Markdown", reply_markup=layout_pagamento)
        except Exception as e:
            bot.send_message(call.message.chat.id, "Desculpe, ocorreu um erro ao gerar o link de pagamento. Por favor, tente novamente mais tarde.")
            print(f"Erro ao gerar o link de pagamento: {e}")

@bot.message_handler(func=lambda message: True)
def mensagem_generica(message):
    # Criando o botão
    botao = types.InlineKeyboardButton("Plano VIP", callback_data="pagar_vip")

    # Criando o layout do botão
    layout = types.InlineKeyboardMarkup()
    layout.add(botao)

    # Responder a qualquer mensagem recebida
    bot.send_message(message.chat.id, "Oiee, para ter acesso aos meus *CONTEÚDOS*, *clique abaixo*!❤️", parse_mode="Markdown", reply_markup=layout)

if __name__ == "__main__":
    bot.polling()