a = 1
b = 2
z = 444

print("locals", locals())
print("locals", "globals(")


def foo():
    c = 3
    d = 4
    print('a=', a)
    print(z)
    print("local in foo", locals())
    print("globals in foo", globals())

    def bar():
        g = 7



foo()
print 'a global '

