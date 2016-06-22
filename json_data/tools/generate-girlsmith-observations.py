from __future__ import print_function
import json
import os
from collections import OrderedDict
from fhirclient.models import fhirdate, observation, patient, familymemberhistory, quantity
from observation_commons import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

#TODO set up the patient and verify these connections
patient_id = "TBD"
patient_id_ref = "Patient/"+patient_id
patient_name = "Lois Kent"
patient_dob = datetime(2014,5,1)

# data for generation (provided by Aly)
# Girl Smith 0-2 yr
# Visit    Age(mos)  Age(wks)   Wt(lbs)  Ht(in)
observation_list = [
    ["MD",  0, 2, 7., 20.],
    ["WIC", 1, 0, 7.5, 20.],
    ["WIC", 3, 0, 11., 22.75],
    ["WIC", 6, 0, 15., 25.5],
    ["MD",  8, 0, 18., 27.],
    ["WIC", 12, 0, 21., 29.5],
    ["WIC", 15, 0, 23.5, 31.],
    ["MD", 18, 0, 25., 32.],
    ["WIC", 21, 0, 28.5, 33.5],
    ["MD", 24, 0, 29., 34.5],
]

def lbs_to_kg(lbs):
    return round(lbs*0.453592,1)
def in_to_cm(ins):
    return round(ins*2.54,1)

if __name__ == '__main__':
    # set up observation structure from model
    for i in range(len(observation_list)):
        # performer, age_mos, wt_lbs, ht_in, bmi = observation_list[i]
        performer, age_mos, age_wks, wt_lbs, ht_in= observation_list[i]
        o = observation.Observation()
        o.status = 'final'
        o.subject = {"reference":patient_id_ref, "display":patient_name}
        o.encounter = [{"display":performer}]
        o.performer = [{"display":performer}]
        date_seen = patient_dob + relativedelta(months=age_mos) + relativedelta(weeks=age_wks)
        o.effectiveDateTime = date_seen.isoformat()

        o.code = coding_weight
        o.valueQuantity = {"value":lbs_to_kg(wt_lbs),"unit":"kg"}
        with open(os.path.join('ob-lois','ob-lois-wt-'+str(i)+'.json'),'w') as f:
            print(json.dumps(OrderedDict(o.as_json()), indent=4, separators=(',', ': ')), file=f)

        o.code = coding_height
        o.valueQuantity = {"value":in_to_cm(ht_in),"unit":"cm"}
        with open(os.path.join('ob-lois', 'ob-lois-ht-' + str(i) + '.json'), 'w') as f:
            print(json.dumps(OrderedDict(o.as_json()), indent=4, separators=(',', ': ')), file=f)

        # o.code = coding_bmi
        # o.valueQuantity = {"value": bmi, "unit": "kg/m2"}
        # with open(os.path.join('ob-lois', 'ob-lois-bmi-' + str(i) + '.json'), 'w') as f:
        #     print(json.dumps(OrderedDict(o.as_json()), indent=4, separators=(',', ': ')), file=f)

    h = familymemberhistory.FamilyMemberHistory()
    h.patient = {"reference":patient_id_ref, "display":patient_name}
    h.status = 'completed'
    h.relationship = {"coding":[{"code":"MTH","system":"http://hl7.org/fhir/familial-relationship"}]}
    measurement = quantity.Quantity()
    measurement.unit = "cm"
    measurement.value = 162
    h.extension = [{"url": "http://fhir-registry.smarthealthit.org/StructureDefinition/family-history#height", "valueQuantity": {"unit": "cm", "value": 162}}]
    with open(os.path.join('ob-lois', 'ob-lois-mth.json'), 'w') as f:
        print(json.dumps(OrderedDict(h.as_json()), indent=4, separators=(',', ': ')), file=f)

    h = familymemberhistory.FamilyMemberHistory()
    h.patient = {"reference":patient_id_ref, "display":patient_name}
    h.status = 'completed'
    h.relationship = {"coding":[{"code":"FTH","system":"http://hl7.org/fhir/familial-relationship"}]}
    measurement = quantity.Quantity()
    measurement.unit = "cm"
    measurement.value = 177
    h.extension = [{"url": "http://fhir-registry.smarthealthit.org/StructureDefinition/family-history#height", "valueQuantity": {"unit": "cm", "value": 177}}]
    with open(os.path.join('ob-lois', 'ob-lois-fth.json'), 'w') as f:
        print(json.dumps(OrderedDict(h.as_json()), indent=4, separators=(',', ': ')), file=f)
