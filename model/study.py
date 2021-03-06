from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_version import *
from .code import *
from .study_design import *
from uuid import UUID

class Study(ApiBaseModel):
  uuid: Union[UUID, None]
  studyTitle: str
  studyVersion: str
  studyType: Union[Code, UUID, None]
  studyPhase: Union[Code, UUID, None]
  studyIdentifiers: Union[List[StudyIdentifier], List[UUID], None] = []
  studyProtocolVersions: Union[List[StudyProtocolVersion], List[UUID], None] = []
  studyDesigns: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False
  
  @classmethod
  def search(cls, store, identifier):
    identifiers = store.get_by_klass("StudyIdentifier")
    for item in identifiers:
      result = store.get("", item['uuid'])
      if result['studyIdentifier'] == identifier:
        studies = store.get_by_klass("Study")
        for study in studies:
          if result['uuid'] in study['studyIdentifiers']:
            return study['uuid']
    return None