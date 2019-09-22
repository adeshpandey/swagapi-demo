import connexion
def get():
    """Fetch a list of users from DB"""
    return [{"fname":"Adesh","lname":"Pandey","email":"adesh.pandey10@gmail.com","address":{"houseno":"129","locality":"Lajpat Nagar","city":"New Delhi"}}]
def post():
    return connexion.request.json