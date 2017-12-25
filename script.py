# js is single thread,if there is a mistaken,it will affect many place.
# MetaProgramming
# golang append
# django method of using database

def he():
    print("hello world")

#
def test_format():
    a = "{h}"
    h = "12"
    print(a.format())

def test_2():
    a = "{}"
    print(a.format("hello _________"))

def test_items():
    a = {"a":1}
    for k,v in a.items():
        print(k,v)

test_items()

# create class
def class_with_methd(func):
    klass = "abc"
    w = type(klass,(),{'bar':True})
    setattr(w,func.__name__,func)
    return w

def say_foo(self):
    print('hello')



# generate new class model
# def generate(class_name,attr:dict)->'class':
#     new_class = type(class_name,(models.Model))
#     for k,v in attr.items():
#         setattr(new_class,k,v)
#     return new_class

# def make_new_model(loaded:dict):
#     class_name = ""
#     for n in loaded:
#         class_name = n

Foo = class_with_methd(say_foo)
foo = Foo()
foo.say_foo()

class A:
    def foo(self,x):
        print('executing foo({})'.format(x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo({})'.format(x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo{}'.format(x))


if __name__ == '__main__':
    a = A()
    a.foo('666')
    A.class_foo('666')
    A.static_foo('666')
    a.static_foo('777')