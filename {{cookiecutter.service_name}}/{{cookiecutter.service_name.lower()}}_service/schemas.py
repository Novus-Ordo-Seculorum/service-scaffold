from axial.schema import Schema
from axial.schema import fields


class StatusSchema(Schema):
    name = fields.Str(1, required=True)
    status = fields.Str(2, required=True)
