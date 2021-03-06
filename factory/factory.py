import yaml
from uuid import uuid4

# def soa(df):
#   encounters = []
#   activities = []
#   # data = {'activity_1': ["x", "", "", ""], 'activity_2': ["", '', 'X', '']}
#   # pd.DataFrame.from_dict(data, orient='index', columns=['Visit 1', 'Visit 2', 'Visit 3', 'Visit 4'])
#   columns = df.columns.values.tolist()
#   rows = list(df.index)
#   for column in columns:
#     encounters.append(encounter_data(column, "The %s visit" % (column), None, None, None))
#   for row in rows:
#     activities.append(activity_data(row))
#   for index, row in df.iterrows():
#     for column in df:
#       if row[column].upper() == "X":
#         workflow_item_data("WFI %s,%s)", None, None, encounters[column], activities[row])

def double_link(items, prev, next):
  for item in items:
    item['uuid'] = str(uuid4())
  for idx, item in enumerate(items):
    if idx == 0:
      item[prev] = None
    else:
      item[prev] = items[idx-1]['uuid']
    if idx == len(items)-1:  
      item[next] = None
    else:
      item[next] = items[idx+1]['uuid']
    
def code_data(code, system, version, decode):
  return {
    "code": code,
    "codeSystem": system,
    "codeSystemVersion": version,
    "decode": decode
  }

def code_for(klass, attribute, **kwargs):
  if 'c_code' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'conceptId', kwargs['c_code'])
    return code_data(entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  elif 'submission_value' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'submissionValue', kwargs['submission_value'])
    return code_data(entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  else:
    raise Exception("Need to specify either a C Code or Submission value when selecting a CT value.")

def workflow_data(description, start, end, items):
  return {
    "workflow_desc": description,
    "workflow_start_point": start,
    "workflow_end_point": end,
    "workflow_item": items
  }

def workflow_item_data(description, from_pit, to_pit, previous, encounter, activity):
  return {
    "description": description,
    "from_point_in_time": from_pit,
    "to_point_in_time": to_pit,
    "previous_workflow_item": previous,
    "encounter": encounter,
    "activity": activity
  }

def activity_data(name, description, sequence, procedures, study_data):
  return {
    "activityName": name,
    "activityDesc": description,
    "previousActivityId": None,
    "nextActivityId": None,
    "definedProcedures": procedures,
    "studyDataCollection": study_data
  }

def procedure_data(the_type, the_code):
  return {
    "procedureType": the_type,
    "procedureCode": the_code
  }

def study_data_data(name, description, link):
  return {
    "studyDataName": name,
    "studyDataDesc": description,
    "crfLink": link
  }

def encounter_data(name, description, sequence, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None):
  return {
    "encounterName": name,
    "encounterDesc": description,
    "previousEncounterId": None,
    "nextEncounterId": None,
    "encounterType": encounter_type,
    "encounterEnvironmentalSetting": env_setting,
    "encounterContactMode": contact_mode,
    "transitionStartRule": start_rule,
    "transitionEndRule": end_rule
  }

def point_in_time_data(start, end, pit_type):
  return {
    "start_date": start,
    "end_date": end,
    "point_in_time_type": pit_type
  }

def investigational_intervention_data(description, codes):
  return {
    "codes": codes,
    "interventionDesc": description,
  }

def endpoint_data(description, purpose, level):
  return {
    "endpointDesc": description,
    "endpointPurposeDesc": purpose,
    "endpointLevel": level
  }

def objective_data(description, level, endpoints):
  return {
    "objectiveDesc": description,
    "objectiveLevel": level,
    "objectiveEndpoints": endpoints
  }

def estimand_data(measure, population, treatment, variable, events):
  return { "summaryMeasure": measure, "analysisPopulation": population, "treatment": treatment, "variableOfInterest": variable, "intercurrentEvents": events }

def intercurrent_event_data(name, description, strategy):
  return { "intercurrentEventName": name, 
           "intercurrentEventDesc": description,
           "intercurrentEventStrategy": strategy
  }

def study_identifier_data(identifier, organisation):
  return {
    "studyIdentifier": identifier,
    "studyIdentifierScope": organisation
  }

def organization_data(identifier_scheme, org_identifier, org_name, organisation_type):
  return {
    "organisationIdentifierScheme": identifier_scheme,
    "organisationIdentifier": org_identifier,
    "organisationName": org_name,
    "organisationType": organisation_type
  }

def analysis_population_data(description):
  return {
    "populationDesc": description
  }

def study_design_population_data(description):
  return {
    "populationDesc": description
  }
  
def study_arm_data(name, description, arm_type, origin_description, origin_type):
  return {
    "studyArmName": name,
    "studyArmDesc": description,
    "studyArmType": arm_type,
    "studyArmDataOriginDesc": origin_description,
    "studyArmDataOriginType": origin_type,
  }

def study_epoch_data(name, description, epoch_type, encounters):
  return {
    "studyEpochName": name,
    "studyEpochDesc": description,
    "previousEpochId": None,
    "nextEpochId": None,
    "studyEpochType": epoch_type,
    "encounters": encounters
  }

def study_cell_data(arm, epoch, elements):
  return {
    "studyArm": arm,
    "studyEpoch": epoch,
    "studyElements": elements
  }

def study_element_data(name, description, start=None, end=None):
  return {
    "studyElementName": name,
    "studyElementDesc": description,
    "transitionStartRule": start,
    "transitionEndRule": end
  }

def transition_rule_data(description):
  return {
    "transitionRuleDesc": description
  }

def study_indication_data(description, indications):
  return {
    "codes": indications,
    "indicationDesc": description
  }

def study_data(title, version, type, phase, identifiers, protocol_versions, designs):
  return {
    "studyTitle": title,
    "studyVersion": version,
    "studyType":  type,
    "studyPhase":  phase,
    "studyIdentifiers": identifiers,
    "studyProtocolVersions": protocol_versions,
    "studyDesigns": designs
  }

def study_design_data(intent, type, model, cells, indications, objectives, populations, interventions, workflows, estimands):
  return {
    "trialIntentTypes": intent,
    "trialType": type,
    "interventionModel": model,
    "studyCells": cells,
    "studyIndications": indications,
    "studyObjectives": objectives,
    "studyPopulations": populations,
    "studyInvestigationalInterventions": interventions,
    "studyWorkflows": workflows,
    "studyEstimands": estimands
  }

def study_protocol_version_data(brief_title, official_title, public_title, scientific_title, version, amendment, effective_date, status):
  return {
    "briefTitle": brief_title,
    "officialTitle": official_title,
    "publicTitle": public_title,
    "scientificTitle": scientific_title,
    "protocolVersion": version,
    "protocolAmendment": amendment,
    "protocolEffectiveDate": effective_date,
    "protocolStatus": status
  }

def workflow_item_data(description, encounter, activity):
  return {
    'workflowItemDesc': description,
    'workflowItemEncounter': encounter,
    'workflowItemActivity': activity,
  }

def workflow_data(description, items):
  return {
    'workflowDesc': description,
    'workflowItems': items
  }

# Internal methods
def _find_ct_entry(klass, attribute, name, value):
  with open("data/ct.yaml") as file:
    ct = yaml.load(file, Loader=yaml.FullLoader)
    for entry in ct[klass][attribute]['terms']:
      if entry[name] == value:
        return entry
    raise Exception("Could not find CT match for (%s, %s, %s, %s)." % (klass, attribute, name, value))        

