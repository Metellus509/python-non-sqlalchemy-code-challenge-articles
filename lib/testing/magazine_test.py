import pytest
from classes.many_to_many import Magazine

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        # Changing name is allowed
        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # Invalid assignment raises ValueError
        with pytest.raises(ValueError):
            magazine_2.name = 2  # not a string

        with pytest.raises(ValueError):
            magazine_2.name = "A"  # too short

        with pytest.raises(ValueError):
            magazine_2.name = "ThisMagazineNameIsWayTooLong"  # too long

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.category, str)

        # Changing category is allowed
        magazine.category = "Style"
        assert magazine.category == "Style"

        # Invalid assignment raises ValueError
        with pytest.raises(ValueError):
            magazine.category = ""  # empty string

        with pytest.raises(ValueError):
            magazine.category = 123  # not a string
