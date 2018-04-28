class User(db.Model):
    userID = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    assetsCollected = db.Column(db.String(), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<UserID: {}\n assetsCollected: {}>".format(self.userID, self.assetsCollected)
