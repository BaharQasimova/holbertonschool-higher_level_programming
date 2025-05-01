#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    with open('/tmp/hidden_4.pyc', 'rb') as f:
        f.seek(16)
        code = marshal.load(f)

    module = types.ModuleType('hidden_4')
    exec(code, module.__dict__)

    names = dir(module)

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
