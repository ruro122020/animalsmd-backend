from flask import session, jsonify, request
#this file authenticates users before accessing protected routes.
#add route's endpoint to this array
protected_routes = ['pets']

class authenticate():
  def check_authentication():
    if 'user_id' not in session and request.endpoint in protected_routes:
      return jsonify({"Error":"Unauthorized"}), 401