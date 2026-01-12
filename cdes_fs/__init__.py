"""
CDES-FS: Cannabis Data Exchange Standard - Food Service Extension

Food service SDK for cannabis-infused culinary applications.
Links to COA/lab data for ingredient sourcing, dosing calculations,
and compliance with food safety regulations.

Use Cases:
- Cannabis-infused restaurants and cafes
- Edible manufacturers
- Catering services
- Recipe development with precise dosing
- Flavor pairing based on terpene profiles
"""

__version__ = "0.1.0"
__author__ = "Acidni LLC"

from cdes_fs.models import (
    # Enums
    IngredientType,
    IngredientForm,
    DosageUnit,
    RecipeCategory,
    DietaryRestriction,
    AllergenType,
    ComplianceStatus,
    # Ingredient Models
    CannabisCOAReference,
    TerpeneProfile,
    CannabisIngredient,
    Ingredient,
    # Recipe Models
    RecipeStep,
    NutritionInfo,
    DosageInfo,
    Recipe,
    # Menu Models
    MenuItem,
    Menu,
    # Compliance Models
    FoodSafetyRecord,
    LotTracking,
)

__all__ = [
    "__version__",
    # Enums
    "IngredientType",
    "IngredientForm",
    "DosageUnit",
    "RecipeCategory",
    "DietaryRestriction",
    "AllergenType",
    "ComplianceStatus",
    # Ingredient Models
    "CannabisCOAReference",
    "TerpeneProfile",
    "CannabisIngredient",
    "Ingredient",
    # Recipe Models
    "RecipeStep",
    "NutritionInfo",
    "DosageInfo",
    "Recipe",
    # Menu Models
    "MenuItem",
    "Menu",
    # Compliance Models
    "FoodSafetyRecord",
    "LotTracking",
]
