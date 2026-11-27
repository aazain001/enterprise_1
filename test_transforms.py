from transforms import clean_email, clean_event_type, clean_name, clean_status


def test_clean_name():
    assert clean_name("  aazain khan ") == "Aazain Khan"


def test_clean_name_none():
    assert clean_name(None) is None


def test_clean_email():
    assert clean_email("  AAZAIN@EXAMPLE.COM ") == "aazain@example.com"


def test_clean_email_none():
    assert clean_email(None) is None


def test_clean_status():
    assert clean_status("  delivered ") == "Delivered"


def test_clean_event_type():
    assert clean_event_type("  PAGE_VIEW ") == "page_view"