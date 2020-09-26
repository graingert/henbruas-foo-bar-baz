import foo.bar.baz

__all__ = ["foo", "baz"]

reveal_type(foo)
reveal_type(foo.bar)
reveal_type(foo.bar.baz)
reveal_type(foo.bar.baz.x)
reveal_type(baz)
reveal_type(bar.baz)
