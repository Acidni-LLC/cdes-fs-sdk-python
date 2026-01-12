# CDES-FS: Cannabis Data Exchange Standard - Food Service Extension

Food service SDK for cannabis-infused culinary applications. Part of the [CDES](https://cdes.dev) ecosystem.

## Features

- **COA Integration** - Link recipes to lab test data
- **Terpene Pairing** - Flavor suggestions based on terpene profiles
- **Dosage Calculation** - Precise THC/CBD per serving
- **Recipe Management** - Cannabis-infused recipe database
- **Compliance** - Food safety and lot tracking

## Use Cases

- Cannabis-infused restaurants and cafes
- Edible manufacturers
- Catering services with cannabis offerings
- Recipe development with precise dosing
- Flavor pairing based on terpene science

## Installation

```bash
pip install cdes-fs
```

## Quick Start

```python
from cdes_fs import (
    CannabisIngredient, Recipe, TerpeneProfile,
    IngredientType, RecipeCategory
)
from decimal import Decimal

# Create a cannabis ingredient with COA reference
butter = CannabisIngredient(
    name="Cannabis-Infused Butter",
    ingredient_type=IngredientType.BUTTER,
    thc_mg_per_gram=Decimal("10.0"),
    coa_reference=CannabisCOAReference(
        coa_id="COA-2026-001",
        batch_number="BATCH-001",
        strain_name="Blue Dream"
    )
)

# Get terpene-based food pairing suggestions
profile = TerpeneProfile(
    coa_reference=butter.coa_reference,
    limonene=Decimal("0.8"),
    myrcene=Decimal("0.5")
)
pairings = profile.suggest_pairings()
# ["citrus desserts", "seafood", "mangoes", "tropical fruits"]

# Create a recipe with automatic dosage calculation
recipe = Recipe(
    name="Cannabis Lemon Bars",
    category=RecipeCategory.DESSERT,
    servings=12,
    cannabis_ingredients=[(butter, Decimal("50.0"))]  # 50g of butter
)
dosage = recipe.calculate_total_dosage()
# 500mg total THC / 12 servings = ~42mg per serving (high_dose_warning=True)
```

## Documentation

- [Full Documentation](https://cdes.dev/docs/food-service)
- [Dosage Calculator](https://cdes.dev/tools/dosage)
- [Terpene Pairing Guide](https://cdes.dev/guides/terpene-pairing)

## License

MIT License - see [LICENSE](LICENSE) for details.
