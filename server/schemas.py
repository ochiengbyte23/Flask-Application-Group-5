from marshmallow import Schema, fields, validate
from models import User, Role

class UserSchema(Schema): 
    id = fields.Integer(dump_only=True) 
    name = fields.String(required=True, validate=validate.Range(min=4)) 
    email = fields.String(required=True, error_messages={"required": "Email is required."}) 
    password = fields.String(validate=validate.Range(min=6, max=15))
    
class RoleSchema(Schema): 
    role_id = fields.Integer(dump_only=True) 
    role = fields.String(required=True)