from schematics import types
from schematics.models import Model


class MongoModel(Model):
    _id = types.BaseType(serialize_when_none=False)

    def to_snake_case(self):
        return ''.join([
            f"{'_'+i.lower() if i.isupper() else i}"
            for i in self.__class__.__name__
        ]).lstrip('_')

class GuildSettings(MongoModel):
    guild_id = types.IntType(required=True)
    disabled_cogs = types.ListType(types.StringType)
    disabled_commands = types.ListType(types.StringType)


class MutedMember(MongoModel):
    guild_id = types.IntType(required=True)
    user_id = types.IntType(required=True)
    start_time = types.DateTimeType()
    end_time = types.DateTimeType(required=True)
    duration = types.IntType()
