class Solsrv:
    def __init__(self):
        self.store = {}

    def addDocuments(self, body):
        accepted = []
        rejected = []
        for doc in body:
            if self.addDocument(doc['id'], doc['content']):
                rejected.append(doc['id'])
            else:
                accepted.append(doc['id'])
        return {"accepted": accepted, "rejected": rejected}

    def addDocument(self, id, body):
        if len(id) > 42:  # TODO: why 42?
            return 'Id too long', 400

        if id in self.store:
            return 'Document already exists', 409

        self.store[id] = body

    def getDocument(self, id):
        if id not in self.store:
            return 'Document not found', 404

        return self.store[id]

    def status(self):
        return {'len(store)': len(self.store)}
