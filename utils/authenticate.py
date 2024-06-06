from flask import session, jsonify, request

protected_routes = ['pets']

class authenticate():
  def check_authentication():
    if 'user_id' not in session and request.endpoint in protected_routes:
      return jsonify({"Error":"Unauthorized"}), 401