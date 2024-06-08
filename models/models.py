#Association tables need to be imported before the 2 table that association table is using 
from .speciesclassification import SpeciesClassification
from .symptomsclassifications import SymptomClassification
from .species import Species
from .classification import Classification
from .symptom import Symptom
from .user import User
from .pet import Pet
from .petsymptom import PetSymptom
from .illnesses import Illness