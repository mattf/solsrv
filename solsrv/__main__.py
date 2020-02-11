import os

import connexion

import solsrv.api as api

app = connexion.FlaskApp(__name__)

# setup operationIds
solsrv = api.Solsrv()
api.getDocument = solsrv.getDocument
api.addDocument = solsrv.addDocument
api.addDocuments = solsrv.addDocuments
api.status = solsrv.status

app.add_api('solsrv.yaml')

app.run(port=os.getenv('PORT'))
