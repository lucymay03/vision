from brainscore_vision import model_registry
from brainscore_vision.model_helpers.brain_transformation import ModelCommitment
from .model import get_model, get_layers

model_registry['TAESD'] = lambda: ModelCommitment(identifier='TAESD', activations_model=get_model('TAESD'), layers=get_layers('TAESD'))
