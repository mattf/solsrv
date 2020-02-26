import os

import connexion

import solsrv.api as api

app = connexion.FlaskApp(__name__)

# setup operationIds
solsrv = api.Solsrv()
api.getDocument = solsrv.get_document
api.addDocument = solsrv.add_document
api.addDocuments = solsrv.add_documents
api.status = solsrv.status

app.add_api('solsrv.yaml')

app.run(port=os.getenv('PORT'))
