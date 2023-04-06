import sqlite3

from flask import Flask
from flask_restx import Resource, fields, Api


app: Flask = Flask(__name__)

api = Api(app, version='1.0', title='Market Data API',
          description='API pour récupérer les données de marché')

ns = api.namespace('marketdata',
                   description='Endpoints pour les données de marché')

market_data_model = api.model('MarketData', {
    'symbol': fields.String(required=True,
                            description="Le symbole de l'entreprise"),
    'price': fields.Float(required=True,
                          description="Le prix actuel de l'action"),
    'volume': fields.Integer(required=True,
                             description="Le volume d'actions échangées")
})


@ns.route('/<string:symbol>')
class MarketData(Resource):
    name = 'Market Data'

    @classmethod
    def get_market_data(cls, symbol):
        conn = sqlite3.connect('market_data.db')
        try:
            c = conn.cursor()
            c.execute(f"SELECT * FROM market_data WHERE symbol = '{symbol}' "
                      "ORDER BY timestamp DESC LIMIT 1")
            data = c.fetchone()
        finally:
            conn.close()
        if not data:
            return None
        return {'symbol': data[0], 'price': data[1], 'volume': data[2]}

    @api.doc(responses={
        200: 'Success',
        404: 'Data not found'
    })
    @ns.marshal_with(market_data_model)
    def get(self, symbol):
        print(self.name)
        data = self.get_market_data(symbol)
        if not data:
            api.abort(404, f"Aucune donnée pour le symbole {symbol}")
        return data, 200


if __name__ == '__main__':
    app.run(debug=True)
