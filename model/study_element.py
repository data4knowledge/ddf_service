from typing import Union
from .api_base_model import ApiBaseModel
from .transition_rule import TransitionRule
from uuid import UUID

class StudyElement(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyElementName: str
  studyElementDesc: str
  transitionStartRule: Union[TransitionRule, UUID, None] = None
  transitionEndRule: Union[TransitionRule, UUID, None] = None
