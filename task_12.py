from task_11 import Any, NoneValue


Void = NoneValue()


def assignment_attempt(target, source):
    global Void

    if issubclass(source, Any) and issubclass(target, Any):
        target = source
        return

    target = Void
