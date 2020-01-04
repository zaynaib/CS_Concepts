from author import Author


def test_author_constructor():
    jill = Author("Jill","fairytail@gmail.com","Female")
    assert jill.email == "fairytail@gmail.com"