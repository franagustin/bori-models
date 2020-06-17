from typing import Dict, Tuple

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
    exclude_fields = ('_id', 'guild_id')

    guild_id = types.IntType(required=True)
    disabled_cogs = types.ListType(types.StringType)
    disabled_commands = types.ListType(types.StringType)
    muted_role = types.IntType()
    prefixes = types.ListType(types.StringType)

    @classmethod
    def valid_settings(cls) -> Tuple[Dict[str, bool], Dict[str, str]]:
        valid_settings, aliases = {}, {}
        for field, field_type in cls._fields.items():  # pylint: disable=no-member
            if field in cls.exclude_fields:
                continue
            is_multiple = field_type.native_type is list
            valid_settings[field] = is_multiple
            if is_multiple and field.endswith('s'):
                finish = -2 if field.endswith('es') else -1
                alias = field[:finish]
                aliases[alias] = field
                valid_settings[alias] = is_multiple
        return valid_settings, aliases


class MutedMember(MongoModel):
    guild_id = types.IntType(required=True)
    user_id = types.IntType(required=True)
    start_time = types.DateTimeType()
    end_time = types.DateTimeType(required=True)
    duration = types.IntType()
