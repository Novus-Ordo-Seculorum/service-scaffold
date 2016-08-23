from axial.schema import Schema
from axial.schema import fields


class ApiStatusSchema(Schema):
    name = fields.Str(1, required=True)
    when = fields.Str(2, required=True)
