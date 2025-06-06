import json

from raypyng.rml import RMLFile

rml = RMLFile('rml/sotexs.rml')


beamline_dict = {}
for i, oe in enumerate(rml.beamline.children()):
    print(i, oe.resolvable_name())
    name = oe.resolvable_name()
    beamline_dict[name]={'x':None, 'y':None, 'z':None}
    for w_pos in oe.worldPosition.children():
        beamline_dict[name][w_pos.name()] = w_pos.cdata



with open("sotexs.json", "w") as f:
    json.dump(beamline_dict, f, indent=4, sort_keys=False)
