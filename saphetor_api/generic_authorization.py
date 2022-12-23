
PREDIFINED_TOKEN="A_PREDIFINED_TOKEN"

def generic_auth(request=None):

    key = request.headers["Authorization"]
    return "Unauthorized"  if key != PREDIFINED_TOKEN else "Authorized"

