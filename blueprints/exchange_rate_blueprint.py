import logging
import traceback
from flask import jsonify, Blueprint
from settings import BASE_ROUTE
from services.exchange_rate_service import ExchangeRateService

exchange_rate_blueprint = Blueprint('exchange_rate_blueprint', 'exchange_rate_blueprint')

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

exchange_rate_service = ExchangeRateService()


@exchange_rate_blueprint.route(f'/{BASE_ROUTE}/usd-rates', methods=['GET'])
def get_exchange_rate():
    try:
        res = exchange_rate_service.get_usd_rates()
        return jsonify(res), 200
    except Exception as error:
        logging.error(f'Error while getting exchange rate {str(error)}')
        logging.error(traceback.format_exc())

        return jsonify({'message': str(error)}), 500
