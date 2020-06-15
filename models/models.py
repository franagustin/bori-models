from schematics import types
from schematics.models import Model


class GuildSettings(Model):
    guild_id = types.IntType(required=True)
    disabled_cogs = types.ListType(types.StringType)
    disabled_commands = types.ListType(types.StringType)


class MutedMember(Model):
    guild_id = types.IntType(required=True)
    user_id = types.IntType(required=True)
    start_time = types.DateTimeType()
    end_time = types.DateTimeType(required=True)
    duration = types.IntType()
