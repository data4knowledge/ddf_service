from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class Indication(ApiBaseModel):
  uuid: Union[str, None] = None
  indication_desc: str
  indication: Union[List[Code], List[str], None]