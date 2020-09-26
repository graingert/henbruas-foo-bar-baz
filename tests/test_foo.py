from foo import bar

reveal_type(bar)
reveal_type(bar.baz)
reveal_type(bar.foo.bar.baz)
reveal_type(bar.foo.bar.baz.x)
reveal_type(bar.baz.x)
