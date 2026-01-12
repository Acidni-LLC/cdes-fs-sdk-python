"""CDES-FS Core Models - Food service data models for cannabis-infused culinary applications."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

class IngredientType(str, Enum):
    """Type of cannabis ingredient."""
    FLOWER = "flower"
    CONCENTRATE = "concentrate"
    DISTILLATE = "distillate"
    ISOLATE = "isolate"
    TINCTURE = "tincture"
    BUTTER = "butter"           # Cannabis-infused butter
    OIL = "oil"                 # Cannabis-infused oil
    RSO = "rso"                 # Rick Simpson Oil
    KIEF = "kief"
    HASH = "hash"
    ROSIN = "rosin"
    SAUCE = "sauce"

class IngredientForm(str, Enum):
    """Physical form of ingredient."""
    SOLID = "solid"
    LIQUID = "liquid"
    POWDER = "powder"
    PASTE = "paste"
    CRYSTAL = "crystal"

class DosageUnit(str, Enum):
    """Units for cannabis dosage."""
    MG_THC = "mg_thc"
    MG_CBD = "mg_cbd"
    MG_TOTAL = "mg_total"
    GRAMS = "grams"
    ML = "ml"

class RecipeCategory(str, Enum):
    """Recipe categories."""
    APPETIZER = "appetizer"
    MAIN_COURSE = "main_course"
    DESSERT = "dessert"
    BEVERAGE = "beverage"
    SNACK = "snack"
    SAUCE = "sauce"
    BAKED_GOOD = "baked_good"
    CONFECTION = "confection"
    SAVORY = "savory"

class DietaryRestriction(str, Enum):
    """Dietary restrictions/labels."""
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"
    GLUTEN_FREE = "gluten_free"
    DAIRY_FREE = "dairy_free"
    NUT_FREE = "nut_free"
    SOY_FREE = "soy_free"
    KETO = "keto"
    PALEO = "paleo"
    LOW_SUGAR = "low_sugar"
    ORGANIC = "organic"

class AllergenType(str, Enum):
    """Common allergens."""
    MILK = "milk"
    EGGS = "eggs"
    FISH = "fish"
    SHELLFISH = "shellfish"
    TREE_NUTS = "tree_nuts"
    PEANUTS = "peanuts"
    WHEAT = "wheat"
    SOY = "soy"
    SESAME = "sesame"

class ComplianceStatus(str, Enum):
    """Food safety compliance status."""
    COMPLIANT = "compliant"
    PENDING_REVIEW = "pending_review"
    NON_COMPLIANT = "non_compliant"
    EXPIRED = "expired"

# =============================================================================
# COA REFERENCE - Links to Lab Data
# =============================================================================

@dataclass
class CannabisCOAReference:
    """Reference to Certificate of Analysis from CDES Core."""
    coa_id: str                          # CDES COA identifier
    batch_number: str
    strain_name: str
    lab_name: Optional[str] = None
    test_date: Optional[date] = None
    coa_url: Optional[str] = None        # Link to full COA
    
    # Key potency data (from COA)
    thc_percentage: Decimal = Decimal("0.00")
    cbd_percentage: Decimal = Decimal("0.00")
    total_cannabinoids: Decimal = Decimal("0.00")
    
    # Safety testing results
    passed_microbial: bool = True
    passed_pesticides: bool = True
    passed_heavy_metals: bool = True
    passed_residual_solvents: bool = True
    
    # Harvest/production info
    harvest_date: Optional[date] = None
    expiration_date: Optional[date] = None

@dataclass
class TerpeneProfile:
    """Terpene profile from COA - for flavor pairing."""
    coa_reference: CannabisCOAReference
    
    # Primary terpenes (percentage)
    myrcene: Decimal = Decimal("0.00")
    limonene: Decimal = Decimal("0.00")
    caryophyllene: Decimal = Decimal("0.00")
    pinene: Decimal = Decimal("0.00")
    linalool: Decimal = Decimal("0.00")
    humulene: Decimal = Decimal("0.00")
    terpinolene: Decimal = Decimal("0.00")
    ocimene: Decimal = Decimal("0.00")
    
    # Flavor notes (derived from terpenes)
    primary_flavors: list[str] = field(default_factory=list)  # citrus, pine, earthy, etc.
    aroma_notes: list[str] = field(default_factory=list)
    
    # Culinary pairing suggestions
    pairs_well_with: list[str] = field(default_factory=list)  # chocolate, citrus, herbs
    cuisine_types: list[str] = field(default_factory=list)    # Italian, Asian, desserts
    
    def suggest_pairings(self) -> list[str]:
        """Suggest food pairings based on terpene profile."""
        pairings = []
        if self.limonene > Decimal("0.5"):
            pairings.extend(["citrus desserts", "seafood", "light salads"])
        if self.myrcene > Decimal("0.5"):
            pairings.extend(["mangoes", "tropical fruits", "herbal dishes"])
        if self.caryophyllene > Decimal("0.3"):
            pairings.extend(["black pepper", "spicy foods", "dark chocolate"])
        if self.pinene > Decimal("0.3"):
            pairings.extend(["rosemary", "pine nuts", "Mediterranean"])
        if self.linalool > Decimal("0.2"):
            pairings.extend(["lavender", "honey", "floral desserts"])
        return pairings

# =============================================================================
# INGREDIENT MODELS
# =============================================================================

@dataclass
class CannabisIngredient:
    """Cannabis-based ingredient with COA reference."""
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    ingredient_type: IngredientType = IngredientType.DISTILLATE
    form: IngredientForm = IngredientForm.LIQUID
    
    # COA/Lab reference
    coa_reference: Optional[CannabisCOAReference] = None
    terpene_profile: Optional[TerpeneProfile] = None
    
    # Potency per gram/ml
    thc_mg_per_gram: Decimal = Decimal("0.00")
    cbd_mg_per_gram: Decimal = Decimal("0.00")
    
    # Activation/decarboxylation
    is_decarboxylated: bool = True
    decarb_temp_f: Optional[int] = None
    decarb_time_minutes: Optional[int] = None
    
    # Storage
    storage_temp_min_f: int = 60
    storage_temp_max_f: int = 70
    shelf_life_days: int = 365
    light_sensitive: bool = True
    
    # Sourcing
    supplier_id: Optional[str] = None
    supplier_name: Optional[str] = None
    lot_number: Optional[str] = None
    received_date: Optional[date] = None
    
    def calculate_thc_dose(self, grams: Decimal) -> Decimal:
        """Calculate THC dose for given amount."""
        return self.thc_mg_per_gram * grams
    
    def calculate_cbd_dose(self, grams: Decimal) -> Decimal:
        """Calculate CBD dose for given amount."""
        return self.cbd_mg_per_gram * grams

@dataclass
class Ingredient:
    """Non-cannabis ingredient."""
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    category: str = ""  # dairy, produce, dry goods, etc.
    unit: str = ""      # cups, grams, oz, etc.
    allergens: list[AllergenType] = field(default_factory=list)
    dietary_info: list[DietaryRestriction] = field(default_factory=list)
    supplier_id: Optional[str] = None

# =============================================================================
# RECIPE MODELS
# =============================================================================

@dataclass
class RecipeStep:
    """Step in a recipe."""
    step_number: int
    instruction: str
    duration_minutes: Optional[int] = None
    temperature_f: Optional[int] = None
    tips: Optional[str] = None
    
    # Cannabis-specific warnings
    max_temp_warning: bool = False  # Warn if temp too high for cannabinoids
    decarb_step: bool = False

@dataclass
class NutritionInfo:
    """Nutritional information per serving."""
    calories: int = 0
    fat_grams: Decimal = Decimal("0.00")
    carbs_grams: Decimal = Decimal("0.00")
    protein_grams: Decimal = Decimal("0.00")
    fiber_grams: Decimal = Decimal("0.00")
    sugar_grams: Decimal = Decimal("0.00")
    sodium_mg: int = 0

@dataclass
class DosageInfo:
    """Cannabis dosage information for recipe/serving."""
    thc_mg_per_serving: Decimal = Decimal("0.00")
    cbd_mg_per_serving: Decimal = Decimal("0.00")
    total_thc_mg: Decimal = Decimal("0.00")
    total_cbd_mg: Decimal = Decimal("0.00")
    servings: int = 1
    
    # Dosage guidance
    onset_time_minutes: int = 60      # Edibles typically 30-90 min
    duration_hours: int = 6           # Effects can last 4-8 hours
    recommended_for: str = ""         # "beginners", "experienced", etc.
    
    # Warnings
    high_dose_warning: bool = False   # True if > 10mg THC per serving
    
    def calculate_per_serving(self) -> dict:
        """Calculate per-serving dosage."""
        return {
            "thc_mg": self.total_thc_mg / self.servings if self.servings else Decimal("0"),
            "cbd_mg": self.total_cbd_mg / self.servings if self.servings else Decimal("0"),
        }

@dataclass
class Recipe:
    """Cannabis-infused recipe."""
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: Optional[str] = None
    category: RecipeCategory = RecipeCategory.DESSERT
    
    # Cannabis ingredients
    cannabis_ingredients: list[tuple[CannabisIngredient, Decimal]] = field(default_factory=list)  # (ingredient, amount)
    
    # Regular ingredients
    ingredients: list[tuple[Ingredient, str]] = field(default_factory=list)  # (ingredient, amount_string)
    
    # Instructions
    steps: list[RecipeStep] = field(default_factory=list)
    prep_time_minutes: int = 0
    cook_time_minutes: int = 0
    total_time_minutes: int = 0
    
    # Servings and dosage
    servings: int = 1
    dosage_info: DosageInfo = field(default_factory=DosageInfo)
    
    # Dietary info
    dietary_labels: list[DietaryRestriction] = field(default_factory=list)
    allergens: list[AllergenType] = field(default_factory=list)
    nutrition: Optional[NutritionInfo] = None
    
    # Culinary notes
    difficulty: str = "medium"  # easy, medium, hard
    chef_notes: Optional[str] = None
    terpene_pairing_notes: Optional[str] = None
    
    # Metadata
    author: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def calculate_total_dosage(self) -> DosageInfo:
        """Calculate total dosage from cannabis ingredients."""
        total_thc = Decimal("0.00")
        total_cbd = Decimal("0.00")
        
        for ingredient, amount in self.cannabis_ingredients:
            total_thc += ingredient.calculate_thc_dose(amount)
            total_cbd += ingredient.calculate_cbd_dose(amount)
        
        return DosageInfo(
            thc_mg_per_serving=total_thc / self.servings if self.servings else Decimal("0"),
            cbd_mg_per_serving=total_cbd / self.servings if self.servings else Decimal("0"),
            total_thc_mg=total_thc,
            total_cbd_mg=total_cbd,
            servings=self.servings,
            high_dose_warning=(total_thc / self.servings) > Decimal("10") if self.servings else False,
        )

# =============================================================================
# MENU MODELS
# =============================================================================

@dataclass
class MenuItem:
    """Menu item for cannabis-infused food service."""
    id: UUID = field(default_factory=uuid4)
    recipe_id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: Optional[str] = None
    price: Decimal = Decimal("0.00")
    
    # Dosage display
    thc_mg: Decimal = Decimal("0.00")
    cbd_mg: Decimal = Decimal("0.00")
    dosage_display: str = ""  # "10mg THC | 5mg CBD"
    
    # Availability
    is_available: bool = True
    available_from: Optional[datetime] = None
    available_until: Optional[datetime] = None
    quantity_available: Optional[int] = None
    
    # Display
    image_url: Optional[str] = None
    dietary_labels: list[DietaryRestriction] = field(default_factory=list)
    featured: bool = False

@dataclass
class Menu:
    """Cannabis-infused menu."""
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    description: Optional[str] = None
    items: list[MenuItem] = field(default_factory=list)
    
    # Venue info
    venue_name: Optional[str] = None
    venue_license: Optional[str] = None
    
    # Menu type
    menu_type: str = "standard"  # standard, tasting, special_event
    
    # Legal disclaimers
    disclaimers: list[str] = field(default_factory=list)
    age_requirement: int = 21
    
    is_active: bool = True
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

# =============================================================================
# COMPLIANCE MODELS
# =============================================================================

@dataclass
class FoodSafetyRecord:
    """Food safety compliance record."""
    id: UUID = field(default_factory=uuid4)
    venue_id: str = ""
    inspection_date: date = field(default_factory=date.today)
    inspector_name: Optional[str] = None
    score: Optional[int] = None
    status: ComplianceStatus = ComplianceStatus.COMPLIANT
    
    # Cannabis-specific compliance
    cannabis_license_verified: bool = False
    dosage_labeling_compliant: bool = False
    coa_records_available: bool = False
    staff_training_current: bool = False
    
    notes: Optional[str] = None
    next_inspection_date: Optional[date] = None
    
    # Violations
    violations: list[str] = field(default_factory=list)
    corrective_actions: list[str] = field(default_factory=list)

@dataclass
class LotTracking:
    """Lot tracking for cannabis ingredients."""
    id: UUID = field(default_factory=uuid4)
    cannabis_ingredient_id: UUID = field(default_factory=uuid4)
    lot_number: str = ""
    
    # Traceability
    coa_reference: Optional[CannabisCOAReference] = None
    received_date: date = field(default_factory=date.today)
    received_quantity: Decimal = Decimal("0.00")
    current_quantity: Decimal = Decimal("0.00")
    unit: str = "grams"
    
    # Usage tracking
    recipes_used_in: list[UUID] = field(default_factory=list)
    total_used: Decimal = Decimal("0.00")
    
    # Status
    is_active: bool = True
    quarantined: bool = False
    quarantine_reason: Optional[str] = None
    expiration_date: Optional[date] = None
    disposed_date: Optional[date] = None
    disposal_reason: Optional[str] = None

__all__ = [
    "IngredientType", "IngredientForm", "DosageUnit", "RecipeCategory",
    "DietaryRestriction", "AllergenType", "ComplianceStatus",
    "CannabisCOAReference", "TerpeneProfile", "CannabisIngredient", "Ingredient",
    "RecipeStep", "NutritionInfo", "DosageInfo", "Recipe",
    "MenuItem", "Menu", "FoodSafetyRecord", "LotTracking",
]
