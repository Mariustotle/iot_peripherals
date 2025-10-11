from typing import Any, List, Type, TypeVar, Set, Optional

T = TypeVar("T")

class ObjectScanner:
    """Recursively scans arbitrary nested structures for instances of a target type."""

    # ----------------------------------------------------------------------
    @staticmethod
    def _scan(obj: Any, target_type: Type[T], seen: Optional[Set[int]] = None) -> List[T]:
        if seen is None:
            seen = set()

        obj_id = id(obj)
        if obj_id in seen:
            return []
        seen.add(obj_id)

        matches: List[T] = []

        # Direct match (including subclasses)
        if isinstance(obj, target_type):
            matches.append(obj)

        # Handle collections
        elif isinstance(obj, (list, tuple, set)):
            for item in obj:
                matches.extend(ObjectScanner._scan(item, target_type, seen))
        elif isinstance(obj, dict):
            for value in obj.values():
                matches.extend(ObjectScanner._scan(value, target_type, seen))
        # Handle objects with attributes (__dict__)
        elif hasattr(obj, "__dict__"):
            for value in vars(obj).values():
                matches.extend(ObjectScanner._scan(value, target_type, seen))

        return matches

    # ----------------------------------------------------------------------
    @staticmethod
    def find_all(obj: Any, target_type: Type[T]) -> List[T]:
        """Return all instances of target_type (including subclasses) found recursively."""
        return ObjectScanner._scan(obj, target_type)

    # ----------------------------------------------------------------------
    @staticmethod
    def find_first(obj: Any, target_type: Type[T]) -> T:
        """Return the first instance of target_type found, or raise if not found."""
        matches = ObjectScanner._scan(obj, target_type)
        if not matches:
            raise ValueError(f"No instances of {target_type.__name__} found.")
        return matches[0]

    @staticmethod
    def find_first_or_default(obj: Any, target_type: Type[T]) -> Optional[T]:
        """Return the first instance of target_type found, or None if not found."""
        matches = ObjectScanner._scan(obj, target_type)
        return matches[0] if matches else None

    # ----------------------------------------------------------------------
    @staticmethod
    def find_single(obj: Any, target_type: Type[T]) -> T:
        """
        Return exactly one instance of target_type.
        Raises:
            ValueError: if no instances or more than one instance are found.
        """
        matches = ObjectScanner._scan(obj, target_type)
        if not matches:
            raise ValueError(f"No instances of {target_type.__name__} found.")
        if len(matches) > 1:
            raise ValueError(
                f"Expected a single {target_type.__name__}, found {len(matches)} instances."
            )
        return matches[0]

    @staticmethod
    def find_single_or_default(obj: Any, target_type: Type[T]) -> Optional[T]:
        """
        Return exactly one instance of target_type if present,
        or None if no matches are found.
        Raises:
            ValueError: if more than one instance is found.
        """
        matches = ObjectScanner._scan(obj, target_type)
        if len(matches) > 1:
            raise ValueError(
                f"Expected at most one {target_type.__name__}, found {len(matches)} instances."
            )
        return matches[0] if matches else None
