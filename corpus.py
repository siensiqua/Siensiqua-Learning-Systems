# module corpus
from util import MultipleRecordsError as MRE
from util import NoneValueError as NVE
#from nltk.corpus import
from os import path

# unique corpora id : {corpora_info>> item:entry}
corp_dirlib = defaultdict(lambda:f'no corpora assigned to {str(key)}}')
corpora_info = dict()



def __init__(self):
  self.crpra_id : int = 0
  self.crpra_name : str = None
  self.author : str = None
  self.year_pub : int = 0
  self.tags : list = None
  self.process : str = None
  self.subject : list = []
  self.source_url : str = None
  self.encoding : str = None
  self.license : str = None
  regex_processes = []
  
    # runs re functions on text

#data_class
class Instance:
  instance = {}
  def __init__(self,
              components,):

    self.components = components

  def _
class CorpusLoader:
  def __init__(self,
               crpra_id,
               crpra_name,
               encoding,
               
               
               
               
               ):
    self.crpra_id = crpra_id
    self.name = name
    self.encoding = encoding
    self.current_instance
    
  def instantiate_(self,
                  file): #puts self in function and it becomes bigger self #transcendence of sub-self
    # pulls from repository
    key_list = [self.crpra_id,self.crpra_name]
    if file:
      
    elif self.crpra_id:
      load_process = 
    elif self.crpra_name:
      crp_list_mtc = [crpra_dirlib.keys()[i] for i,c_name in enumerate(crpra_dirlib.values()) if self.crpra_name in c_name]
      if crp_list_mtc > 1:
        raise MRE(crp_list_mtc,self.crpra_name) #f"{len(param_1)} records found including {param_2}
      elif crp_list_mtc==1:
        #crp_mtc is crpra id
        #pulls from repos.ry
    elif 
    else:
      raise NVE(self) #'I can't do anything with nothing...'

  
        
      
    
    

  def preprocess_(self,text):
