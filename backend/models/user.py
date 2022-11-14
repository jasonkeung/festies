USER_SCHEMA = {
    "age": int,
    "name": str,
}


class User:
    def __init__(self, kwargs):
        # check kwargs
        if kwargs.keys() != USER_SCHEMA.keys():
            raise TypeError(
                f"Unexpected arg(s): {(kwargs.keys() - USER_SCHEMA.keys()) or (USER_SCHEMA.keys() - kwargs.keys())}"
            )
        kwargs_schema = {key: type(val) for key, val in kwargs.items()}
        if kwargs_schema != USER_SCHEMA:
            raise TypeError(
                f"Given schema {kwargs_schema} does not match expected schema {USER_SCHEMA}"
            )

        self.__dict__.update(kwargs)
