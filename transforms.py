"""Small cleaning functions from AK_silver_transformation.

These mirror the Spark logic in the notebook, in plain Python,
so pytest can test them without a Spark cluster:
- initcap + trim  -> strip + title
- lower + trim    -> strip + lower
"""


def clean_name(name):
    if name is None:
        return None
    return name.strip().title()


def clean_email(email):
    if email is None:
        return None
    return email.strip().lower()


def clean_status(status):
    if status is None:
        return None
    return status.strip().title()


def clean_event_type(event_type):
    if event_type is None:
        return None
    return event_type.strip().lower()