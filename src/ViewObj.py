from typing import ClassVar, Generic, TypeVar, Type, no_type_check, Any
import weakref
import copy
import types

class MixinLogicalOperatorView:
    _obj: Any

    def __and__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj & value

    def __or__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj | value

    def __xor__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj ^ value

    def __bool__(self):
        return bool(self._obj)


class MixinComparisonOperatorView:
    _obj: Any

    def __lt__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj < value

    def __le__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj <= value

    def __eq__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj == value

    def __ne__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj != value

    def __gt__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj > value

    def __ge__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj >= value

class MixinBinaryOperatorView:
    _obj: Any

    def __add__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj + value

    def __sub__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj - value

    def __mul__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj * value

    def __truediv__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj / value

    def __floordiv__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj // value

    def __mod__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj % value

    def __pow__(self, value):
        value = value.__obj if isinstance(value, View) else value
        return self._obj ** value

    def __lshift__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj << value

    def __rshift__(self, value):
        value = value._obj if isinstance(value, View) else value
        return self._obj >> value

class MixinAttrOperatorView:
    _obj: Any

    def __getattr__(self, item):
        attr = getattr(self._obj, item)
        print("get attr", attr, type(attr))
        if isinstance(attr, types.MethodType):
            method = type(self._obj).__dict__[item]
            return types.MethodType(method, self)
        elif isinstance(attr, types.BuiltinFunctionType):
            match attr.__name__:
                case "append" | "extend" | "insert" | "remove" | "pop" | "clear" | "reverse" | "sort":
                    raise AttributeError("View object is immutable")
            return attr
        return View(getattr(self._obj, item))

    def __setattr__(self, name: str, value, /) -> None:
        raise AttributeError("View object is immutable")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("View object is immutable")

class MixinItemOperatorView:
    _obj: Any

    def __getitem__(self, key):
        return View(self._obj[key])

    def __setitem__(self, key, value):
        raise AttributeError("View object is immutable")

    def __delitem__(self, key):
        raise AttributeError("View object is immutable")

    def __contains__(self, item):
        return item in self._obj

    def __iter__(self):
        return iter(self._obj)

    def __len__(self):
        return len(self._obj)

class MixinCastingOperatorView:
    _obj: Any

    def __int__(self):
        return int(self._obj)

    def __float__(self):
        return float(self._obj)

    def __str__(self):
        return str(self._obj)

    def __repr__(self):
        return repr(self._obj)

    def __hash__(self):
        return hash(self._obj)

class View[T](MixinCastingOperatorView,
              MixinAttrOperatorView,
              MixinItemOperatorView,
              MixinBinaryOperatorView,
              MixinComparisonOperatorView,
              MixinLogicalOperatorView):
    __cached__: ClassVar[weakref.WeakValueDictionary] = weakref.WeakValueDictionary()
    __obj: T

    def copy(self)->T:
        return copy.deepcopy(self.__obj)

    def __new__(cls, obj: T)->'View[T]':
        if id(obj) in cls.__cached__:
            return cls.__cached__[id(obj)]
        if isinstance(obj, View):
            return obj
        ins = super().__new__(cls)
        cls.__cached__[id(obj)] = ins
        return ins

    def __init__(self, obj: T):
        object.__setattr__(self, '_View__obj', obj)

    @property
    def get(self)->T:
        return self #type: ignore

    @property
    def _obj(self)->T:
        return self.__obj #type: ignore
