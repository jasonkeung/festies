GROUP_SCHEMA = {
    "events": list,
    "group_bio": str,
    "members": list,
    "names": str,
}


class Group:
    def __init__(self, kwargs):
        # concat sorted usernames to make unique group identifier
        kwargs["names"] = "+".join(sorted(kwargs["members"]))

        # check kwargs
        if kwargs.keys() != GROUP_SCHEMA.keys():
            raise TypeError(f"Unexpected arg(s): {kwargs.keys() - GROUP_SCHEMA.keys()}")
        kwargs_schema = {key: type(val) for key, val in kwargs.items()}
        if kwargs_schema != GROUP_SCHEMA:
            raise TypeError(
                f"Given schema {kwargs_schema} does not match expected schema {GROUP_SCHEMA}"
            )

        self.__dict__.update(kwargs)
