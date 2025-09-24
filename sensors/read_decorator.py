

# common/actions.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Optional, Type, get_origin, get_args
from enum import Enum
import inspect
import functools
import typing

@dataclass(frozen=True)
class ReadParam:
    name: str
    type_: Type[Any]                         # e.g. int, float, str, bool, Enum subclass
    required: bool = True
    default: Any = None
    choices: Optional[Iterable[Any]] = None  # for enums or fixed options
    help: str = ""

@dataclass
class ReadAction:
    key: str
    label: str
    func: Callable[..., Any]
    params: list[ReadParam] = field(default_factory=list)
    description: str = ""

def read(
    key: str | None = None,
    *,
    label: str | None = None,
    description: str = "",
    # Optional manual param descriptors (otherwise derived from annotations)
    params: list[ReadParam] | None = None
):
    """Marks an instance method as a menu action."""
    def decorator(fn: Callable[..., Any]):
        meta = {
            "key": key or fn.__name__,
            "label": label or fn.__name__.replace("_", " ").title(),
            "description": description,
            "params": params,  # may be None -> auto-derive
        }
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        setattr(wrapper, "_is_menu_action", True)
        setattr(wrapper, "_menu_action_meta", meta)
        return wrapper
    return decorator

# --- Helpers used by UI param prompting ---
def coerce_input(raw: str, type_: Type[Any]) -> Any:
    origin = get_origin(type_)
    if origin is Optional:
        inner = get_args(type_)[0] if get_args(type_) else str
        return coerce_input(raw, inner) if raw != "" else None

    if isinstance(type_, type) and issubclass(type_, Enum):
        # accept name, value string, or 1-based index
        for i, m in enumerate(type_):
            if raw.lower() == m.name.lower() or raw == str(m.value) or raw == str(i+1):
                return m
        raise ValueError(f"Invalid option. Expected one of {[m.name for m in type_]}")
    if type_ is bool:
        return raw.strip().lower() in {"1","y","yes","true","t"}
    if type_ is int:
        return int(raw.strip())
    if type_ is float:
        return float(raw.strip())
    return raw  # str or fallback

def derive_params_from_signature(fn: Callable[..., Any]) -> list[ReadParam]:
    sig = inspect.signature(fn)
    hints = typing.get_type_hints(fn, include_extras=False)
    params: list[ReadParam] = []
    for name, p in sig.parameters.items():
        if name == "self":
            continue
        ann = hints.get(name, str)
        required = (p.default is inspect._empty)
        default = None if required else p.default
        choices = None
        if isinstance(ann, type) and issubclass(ann, Enum):
            choices = list(ann)
        params.append(ReadParam(name=name, type_=ann, required=required, default=default, choices=choices))
    return params
