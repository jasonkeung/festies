EVENT_SCHEMA = {
    "title": str,
    "city": str,
    "date": str,
    "time": str,
}


class Event:
    def __init__(self, kwargs):
        # check kwargs
        if kwargs.keys() != EVENT_SCHEMA.keys():
            raise TypeError(
                f"Unexpected arg(s): {(kwargs.keys() - EVENT_SCHEMA.keys()) or (EVENT_SCHEMA.keys() - kwargs.keys())}"
            )
        kwargs_schema = {key: type(val) for key, val in kwargs.items()}
        if kwargs_schema != EVENT_SCHEMA:
            raise TypeError(
                f"Given schema {kwargs_schema} does not match expected schema {EVENT_SCHEMA}"
            )

        self.__dict__.update(kwargs)
