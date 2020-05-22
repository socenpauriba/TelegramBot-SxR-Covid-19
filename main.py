#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BOT DE TELEGRAM PER A SxR CREAT PER PAU RIBA QUEIJAS -> HTTPS://PRIBAQ.NET
# RECORDEU CANVIAR "CODI DE GRUP/CANAL/USUARI DE TELEGRAM" I "BOT-SECRET-KEY"
# NECESSITA EL MÒDUL "Python-Telegram-Bot" I PYTHON3

import time, random, sys, os, logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from datetime import datetime,timedelta

logging.basicConfig()

#DECLARACIÓ DE VARIABLES

NOM, TELEFON, CENTRE, ADRECA, MASCARETES, GORROS, BATES, GEL, PANTALLES, GUANTS  = range(10)
NOMCC, TELEFONCC, CEDIR = range(3)

canal = "CODI DE GRUP/CANAL/USUARI DE TELEGRAM" # Allà s'enviaran les respostes dels formularis
admin = "CODI DE GRUP/CANAL/USUARI DE TELEGRAM" # Allà s'enviaran les alertes (Inici del bot)
enter = """
"""
nomc = ""
telefonc = ""
cedirx = ""
nomx = ""
telefonx = ""
centrex = ""
mascaretesx = ""
gorrosx = ""
batesx = ""
adrecax = ""
guantsx = ""
pantallesx = ""
gelx = ""

#DEFINICIÓ DE FUNCIONS

def start(update, context):
    update.message.reply_text("Hola, sóc el bot de SxR!")
    update.message.reply_text("💬 Envia /faltamaterial per a sol·licitar material sanirati per a un centre de salut!")
    update.message.reply_text("💬 Envia /cedirmaterial per a cedir material sanirati per a un centre de salut!")
    print(update.message.chat_id)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def faltamaterial(update, context):
    update.message.reply_text("Per completar la sol·licitud has de respondre a unes preguntes:")
    update.message.reply_text("Com et dius? 🏷")
    return NOM

def cedirmaterial(update, context):
    update.message.reply_text("Per completar la sol·licitud has de respondre a unes preguntes:")
    update.message.reply_text("Com et dius? 🏷")
    return NOMCC

def received_nom(update, context):
    global nomx
    nomx = update.message.text
    update.message.reply_text("Quin és el teu telèfon? 📞")
    return TELEFON

def received_nomc(update, context):
    global nomx
    nomx = update.message.text
    update.message.reply_text("Quin és el teu telèfon? 📞")
    return TELEFONCC

def received_telefon(update, context):
    global telefonx
    telefonx = update.message.text
    update.message.reply_text("Quin centre de salut necessita material? 🏥")
    return CENTRE

def received_telefonc(update, context):
    global telefonx
    telefonx = update.message.text
    update.message.reply_text("Quin material vols cedir? (guants, bates, barrets, pantalles, gel hidroalcohòlic, mascaretes...) (especifica unitats)")
    return CEDIR

def received_centre(update, context):
    global centrex
    centrex = update.message.text
    update.message.reply_text("Adreça del centre? 📍")
    return ADRECA

def received_adreca(update, context):
    global adrecax
    adrecax = update.message.text
    update.message.reply_text("Necessiteu mascaretes? Quina quantitat? 😷")
    return MASCARETES

def received_mascaretes(update, context):
    global mascaretesx
    mascaretesx = update.message.text
    update.message.reply_text("Necessiteu barrets? Quina quantitat? 🎓")
    return GORROS

def received_gorros(update, context):
    global gorrosx
    gorrosx = update.message.text
    update.message.reply_text("Necessiteu guants? Quina quantitat? 🧤")
    return GUANTS

def received_guants(update, context):
    global guantsx
    guantsx = update.message.text
    update.message.reply_text("Necessiteu Gel hidroalcohòlic? Quina quantitat? 💦")
    return GEL

def received_gel(update, context):
    global gelx
    gelx = update.message.text
    update.message.reply_text("Necessiteu pantalles? Quina quantitat? 🥽")
    return PANTALLES

def received_pantalles(update, context):
    global pantallesx
    pantallesx = update.message.text
    update.message.reply_text("Necessiteu bates? Quina quantitat? 🥼")
    return BATES

def received_bates(update, context):
    global batesx
    batesx = update.message.text
    print("S'ha rebut una nova sol·licitut")
    if update.effective_chat.username:
        usuariname = update.effective_chat.username
    else:
        usuariname = "nousername"

    linia1 = "*NOVA SOL·LICITUT DE MATERIAL DE* @" + usuariname + ": 📥"
    linia5 = "🏷 *Nom:* " + nomx
    linia6 = "📞 *Telefon:* " + telefonx
    linia2 = "🏥 *Centre:* " + centrex
    linia3 = "😷 *Mascaretes:* " + mascaretesx
    linia7 = "🎓 *Barrets:* " + gorrosx
    linia4 = "🥼 *Bates:* " + batesx
    linia8 = "🧤 *Guants:* " + guantsx
    linia9 = "🥽 *Pantalles:* " + pantallesx
    linia10 = "📍 *Adreça:* " + adrecax
    linia11 = "💦 *Gel:* " + gelx

    context.bot.send_message(chat_id=canal, text=linia1+enter+linia5+enter+linia6+enter+linia2+enter+linia10+enter+linia3+enter+linia7+enter+linia4+enter+linia8+enter+linia11+enter+linia9, parse_mode='MARKDOWN')

    update.message.reply_text("El teu missatge ha estat enviat! 📤")
    return ConversationHandler.END

def received_cedir(update, context):
    global cedirx
    cedirx = update.message.text

    if update.effective_chat.username:
        usuariname = update.effective_chat.username
    else:
        usuariname = "nousername"

    linia1c = "*NOVA APORTACIÓ DE MATERIAL DE* @" + usuariname + ": 📥"
    linia2c = "🏷 *Nom:* " + nomx
    linia3c = "📞 *Telefon:* " + telefonx
    linia4c = "✍️ *Missatge:* " + cedirx

    context.bot.send_message(chat_id=canal, text=linia1c+enter+linia2c+enter+linia3c+enter+linia4c, parse_mode='MARKDOWN')

    update.message.reply_text("El teu missatge ha estat enviat! 📤")
    return ConversationHandler.END

def main():
    updater = Updater("BOT-SECRET-KEY", use_context=True)
    dp = updater.dispatcher
    
    # /START

    dp.add_handler(CommandHandler("start", start))

    # /FALTAMATERIAL
    
    conv_afc_handler = ConversationHandler(
        entry_points=[CommandHandler('faltamaterial', faltamaterial)],

        states={
            NOM: [MessageHandler(Filters.text,
                                          received_nom),
                           ],
            TELEFON: [MessageHandler(Filters.text,
                                          received_telefon),
                           ],
            CENTRE: [MessageHandler(Filters.text,
                                          received_centre),
                           ],

            ADRECA: [MessageHandler(Filters.text,
                                          received_adreca),
                           ],

            MASCARETES: [MessageHandler(Filters.text,
                                          received_mascaretes),
                           ],

            GORROS: [MessageHandler(Filters.text,
                                          received_gorros),
                           ],

            GUANTS: [MessageHandler(Filters.text,
                                          received_guants),
                           ],
            GEL: [MessageHandler(Filters.text,
                                          received_gel),
                           ],
            PANTALLES: [MessageHandler(Filters.text,
                                          received_pantalles),
                           ],

            BATES: [MessageHandler(Filters.text,
                                          received_bates),
                           ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), error)]
    )

    dp.add_handler(conv_afc_handler)

    
    # /CEDIRMATERIAL
    
    conv_cedir_handler = ConversationHandler(
        entry_points=[CommandHandler('cedirmaterial', cedirmaterial)],

        states={
            NOMCC: [MessageHandler(Filters.text,
                                          received_nomc),
                           ],
            TELEFONCC: [MessageHandler(Filters.text,
                                          received_telefonc),
                           ],

            CEDIR: [MessageHandler(Filters.text,
                                          received_cedir),
                           ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), error)]
    )

    dp.add_handler(conv_cedir_handler)
    updater.start_polling()
    updater.idle()

    context.bot.send_message(chat_id=admin, text="⚙️ El bot s'ha iniciat correctament!", parse_mode='MARKDOWN')

`#LOOP

if __name__ == '__main__':
    main()
