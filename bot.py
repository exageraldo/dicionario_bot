from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import itertools
import logging
import pydicts
import utils

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text(
        'Seja bem vind@ ao DicioBot'
    )


def help(bot, update):
    update.message.reply_text(
        'Os comandos são bem simples:\n'
        '/significado <palavra>\n'
        '/sinonimo <palavra>\n'
        '/antonimo <palavra>\n'
    )


def significados(bot, update, args):
    args = utils.get_args(args)
    significados = pydicts.Dicio.meanings(args['palavra'])
    for significado in itertools.islice(significados, args['max']):
        update.message.reply_text(significado)


def sinonimos(bot, update, args):
    args = utils.get_args(args)
    sinonimos = pydicts.Dicio.synonyms(args['palavra'])
    for sinonimo in itertools.islice(sinonimos, args['max']):
        update.message.reply_text(sinonimo)


def antonimos(bot, update, args):
    args = utils.get_args(args)
    antonimos = pydicts.Dicio.antonyms(args['palavra'])
    for antonimo in itertools.islice(antonimos, args['max']):
        update.message.reply_text(antonimo)


def error(bot, update, error):
    logger.warning('Update {update} caused error {error}')


def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("significado", significados, pass_args=True))
    dp.add_handler(CommandHandler("sinonimo", sinonimos, pass_args=True))
    dp.add_handler(CommandHandler("antonimo", antonimos, pass_args=True))
    dp.add_handler(CommandHandler("informal", informal, pass_args=True))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
