from factory.factory import *

class SimpleStudy():

  def json():
    procedure_code = code_data("767002", "SNOMED-CT", "2022-05-31", "White blood cell count")           
    procedure_1 = procedure_data("Specimen Collection", procedure_code)
    study_data_1 = study_data_data("Study Data 1", "Something", "Link 1")
    activity_1 = activity_data("A1", "Activity_1", 1, [procedure_1], [])
    activity_2 = activity_data("A2", "Activity_2",  2, [], [study_data_1])
    activities = [activity_1, activity_2]
    double_link(activities, 'previousActivityId', 'nextActivityId')

    encounter_type = code_data("C7652x", "http://www.cdisc.org", "1", "SITE VISIT")
    env_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')    
    env_contact_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    encounter_1 = encounter_data("Encounter 1", "desc", 1, encounter_type, env_setting, env_contact_mode)
    encounter_2 = encounter_data("Encounter 2", "desc", 2, encounter_type, env_setting, env_contact_mode)
    encounters = [encounter_1, encounter_2]
    double_link(encounters, 'previousEncounterId', 'nextEncounterId')

    wfi_links = [
      [encounter_1, activity_1],
      [encounter_2, activity_2]
    ]
    wfis = []
    for item in wfi_links:
      wfis.append(workflow_item_data("", item[0], item[1]))
    workflow = workflow_data("Schedule of Activities", wfis)
    double_link(wfis, 'previousWorkflowItemId', 'nextWorkflowItemId')  

    ii_1 = investigational_intervention_data(
      "Intervention 1", 
      [ 
        code_data("C7639x", "http://www.cdisc.org", "1", "MODEL 1"), 
        code_data("C7639y", "http://www.cdisc.org", "1", "MODEL 2")
      ]
    )

    population_1 = study_design_population_data("Population 1")

    endpoint_1 = endpoint_data(
      "Endpoint 1", 
      "level description",
      code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE")
      )
    endpoint_2 = endpoint_data(
      "Endpoint 2",
      "level description",
      code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE"),
      )
    objective_1 = objective_data(
      "Objective Level 1", 
      code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
      [endpoint_1, endpoint_2]
    )

    phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase IIa Trial")
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    registry_type = code_data("C2365x", "http://www.cdisc.org", "1", "REGISTRY_STUDY_IDENTIFIER")
    sponsor_type = code_data("C2365y", "http://www.cdisc.org", "1", "SPONSOR_STUDY_IDENTIFIER")
    organisation_1 = organization_data("DUNS", "123456789", "ACME Pharma", sponsor_type)
    organisation_2 = organization_data("FDA", "CT-GOV", "ClinicalTrials.gov", registry_type)
    organisation_3 = organization_data("EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database", registry_type)
    identifier_1 = study_identifier_data("CT-GOV-1234", organisation_2)
    identifier_2 = study_identifier_data("EU-5678", organisation_3)
    identifier_3 = study_identifier_data("ACME-5678", organisation_1)
    identifiers = [identifier_1, identifier_2, identifier_3]

    indication_1 = study_indication_data("Something bad", [code_data("C6666x", "http://www.cdisc.org", "1", "BAD STUFF")])
    indication_2 = study_indication_data("Something similarly bad", [code_data("C6666y", "http://www.cdisc.org", "1", "BAD SIMILAR STUFF")])
    origin_type = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    study_arm_1 = study_arm_data("Placebo", "The Placebo Arm", placebo, "Captured subject data", origin_type)
    study_arm_2 = study_arm_data("Active", "Super Drug Arm", treatment, "Captured subject data", origin_type)

    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    study_epoch_1 = study_epoch_data("Run In", "The run in", run_in, [encounter_1, encounter_2])
    study_epoch_2 = study_epoch_data("Treatment", "The drug!", treatment, [])
    study_epoch_3 = study_epoch_data("Follow Up", "Go away", follow_up, [])
    epochs = [study_epoch_1, study_epoch_2, study_epoch_3]
    double_link(epochs, 'previousEpochId', 'nextEpochId')
    print(epochs)

    start_rule = transition_rule_data("Start Rule")
    end_rule = transition_rule_data("End Rule")
    study_element_1 = study_element_data("Element 1", "First element", start_rule, end_rule)
    study_element_2 = study_element_data("Element 2", "Second element")
    study_element_3 = study_element_data("Element 3", "Third element")
    study_element_4 = study_element_data("Element 4", "Fourth element")

    study_cells = []
    study_cells.append(study_cell_data(study_arm_1, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_2, [study_element_2]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_3, [study_element_4]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_2, [study_element_3]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_3, [study_element_4]))

    intent = code_for('StudyDesign', 'trialIntentType', c_code='C15714')
    design_1_type = code_for('StudyDesign', 'trialType', submission_value='BIOSIMILARITY')
    design_2_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='PARALLEL')

    design_1 = study_design_data([intent], design_1_type, int_model, study_cells, [indication_1], [objective_1], [population_1], [ii_1], [workflow], [])
    design_2 = study_design_data([intent], design_2_type, int_model, study_cells, [indication_1, indication_2], [objective_1], [population_1], [ii_1], [], [])
    designs = [design_1, design_2]
    final = code_data("C1113x", "http://www.cdisc.org", "1", "FINAL")
    protocol_version_1 = study_protocol_version_data("Short", "Very Official", "Public Voice", "Incomprehensible", "1", None, "2022-01-01", final)
    protocol_version_2 = study_protocol_version_data("Shorter", "Very Official", "Public Voice", "Incomprehensible", "1", "Amendment 1", "2022-02-01", final)
    protocol_versions = [protocol_version_1, protocol_version_2]

    return study_data("New Title", "1", study_type, phase, identifiers, protocol_versions, designs)
