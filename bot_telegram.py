import telebot
from telebot import types
from api_mercadopago import gerar_link_de_pagamento

CHAVE_API = "6350617394:AAF1CTTjzmPpI823ohPQiGC1JV3ZSesJKu0"
bot = telebot.TeleBot(CHAVE_API)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "mensagem_nova":
        # Gerar o link de pagamento
        link_pagamento = gerar_link_de_pagamento()

        # Criar botão de pagamento
        botao_pagamento = types.InlineKeyboardButton("ASSINAR VIP R$9,99", url=link_pagamento)

        # Criar layout com o botão de pagamento
        layout_pagamento = types.InlineKeyboardMarkup()
        layout_pagamento.add(botao_pagamento)

        # Enviar a mensagem com a imagem e o botão de pagamento
        with open('./imagem/vip.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption="*♦️VIDEOS TODOS OS DIAS♦️*\n\n+DE 99VIDEOS\nSEXO\nMASTURBAÇÃO\nANAL\nSEXO A 3\n\nEstou esperando você bem molhadinha no meu VIP😍\n\n💠CLIQUE PRA VIRAR VIP💠", parse_mode="Markdown", reply_markup=layout_pagamento)

@bot.message_handler(func=lambda message: True)
def mensagem_genérica(mensagem):
    # Criando o botão
    botao = types.InlineKeyboardButton("Plano VIP", callback_data="mensagem_nova")

    # Criando o layout do botão
    layout = types.InlineKeyboardMarkup()
    layout.add(botao)

    # Responder a qualquer mensagem recebida
    bot.send_message(mensagem.chat.id, "Oiee, para ter acesso aos meus *CONTEÚDOS*, *clique abaixo*!", reply_markup=layout)

bot.polling()