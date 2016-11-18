from rets.models.metadata.base import Base


class System(Base):
    elements = {
        'SystemID': None,
        'SystemDescription': None,
        'TimeZoneOffset': None,
        'Comments': None,
        'Version': None,
    }
