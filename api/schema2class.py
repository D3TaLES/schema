from pybliometrics.scopus import AbstractRetrieval
import python_jsonschema_objects as pjs
from urllib import request
import json, time
import jsonschema

class Schema2Class():
    def __init__(self,schema_name=None, named_only=False):

        # fetch schema_frontend
        self.schema_name = schema_name
        schema_url = "https://raw.githubusercontent.com/D3TaLES/schema/main/schema/{}.schema_frontend.json".format(self.schema_name)
        response = request.urlopen(schema_url)
        self.schema = json.loads(response.read().decode())

        # generating classes
        builder = pjs.ObjectBuilder(self.schema)
        ns = builder.build_classes(named_only=named_only)

        # get all name space
        for name_space in dir(ns):
            setattr(self,name_space,getattr(ns,name_space))

        # highest-level name space for validation
        # self.high_level = getattr(ns,schema_name.title())

        # required values
        if self.schema.get("required",):
            self.required = self.schema.get("required")
        else:
            self.required = None













































from monty.json import MSONable


# class Solvent_DFT(MSONable):
#     def __init__(self, name=None, dielectric_constant=None, model=None, dropna=True):
#         self.dropna = dropna
#         self.model = model or ''
#         self.dielectric_constant = dielectric_constant or 0.0
#         self.name = name or ''
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#
#         del d["@module"]
#         del d["@class"]
#         del d["@version"]
#
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#         del d["dropna"]
#
#         return d
#
#
# class DFT_parameters(MSONable):
#     def __init__(self, functional=None, basis_set=None, tuning_parameter=None, solvent=None,
#                  dropna=True):
#         self.dropna = dropna
#         self.functional = functional or ''
#         self.basis_set = basis_set or ''
#         self.tuning_parameter = tuning_parameter or 0.0
#         self.solvent = solvent or Solvent_DFT(dropna=self.dropna).to_dict()
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#
#         del d["@module"]
#         del d["@class"]
#         del d["@version"]
#
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#         del d["dropna"]
#
#         return d
#
#
# class Data(MSONable):
#     def __init__(self, dft_parameters=None, value=None, unit=None, order=None, name=None, dropna=True):
#         self.dropna = dropna
#         self.name = name or ''
#         self.dft_parameters = dft_parameters or DFT_parameters(dropna=self.dropna).to_dict()
#         self.value = value or 0.0
#         self.unit = unit or ''
#         self.order = order or 0
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#         del d["@module"]
#         del d["@class"]
#         del d["@version"]
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#
#         del d["dropna"]
#
#         return d
#
#
# class Molecular_structure(MSONable):
#     def __init__(self, optimzed=None, charge=None, multiplicity=None, dft_parameters=None, sites=None,
#                  electronic_descriptors=None, geometry_descriptors=None, chemical_descriptors=None, dropna=True):
#         self.dropna = dropna
#         self.optimzed = optimzed or False
#         self.charge = charge or 0
#         self.multiplicity = multiplicity or 0
#         self.dft_parameters = dft_parameters or DFT_parameters(dropna=self.dropna).to_dict()
#         self.sites = sites
#         self.electronic_descriptors = electronic_descriptors or [Data(dropna=self.dropna).to_dict()]
#         self.geometry_descriptors = geometry_descriptors or [Data(dropna=self.dropna).to_dict()]
#         self.chemical_descriptors = chemical_descriptors or [Data(dropna=self.dropna).to_dict()]
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#
#         del d["@module"]
#         del d["@class"]
#         del d["@version"]
#
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#
#         del d["dropna"]
#
#         return d
#
#
# class Computation(MSONable):
#     def __init__(self, _id=None, smiles=None, selfies=None, inchi=None, inchi_key=None, geometry=None, iupac_name=None,
#                  synonyms=None, number_of_atoms=None, molecular_weight=None, reorganization_energy=None,
#                  vertical_ionization_energy=None, vertical_electron_affinity=None, adiabatic_ionization_energy=None,
#                  adiabatic_electron_affinity=None, redox_potential=None, dropna=True):
#         self.dropna = dropna
#         self._id = _id or ''
#         self.smiles = smiles or ''
#         self.selfies = selfies or ''
#         self.inchi = inchi or ''
#         self.inchi_key = inchi_key or ''
#         self.geometry = geometry or [Molecular_structure(dropna=self.dropna).to_dict()]
#         self.iupac_name = iupac_name or ''
#         self.synonyms = synonyms or ['']
#         self.number_of_atoms = number_of_atoms or 0
#         self.molecular_weight = molecular_weight or 0.0
#         self.reorganization_energy = reorganization_energy or [Data().to_dict()]
#         self.vertical_electron_affinity = vertical_electron_affinity or [Data(dropna=self.dropna).to_dict()]
#         self.vertical_ionization_energy = vertical_ionization_energy or [Data(dropna=self.dropna).to_dict()]
#         self.adiabatic_electron_affinity = adiabatic_electron_affinity or [Data(dropna=self.dropna).to_dict()]
#         self.adiabatic_ionization_energy = adiabatic_ionization_energy or [Data(dropna=self.dropna).to_dict()]
#         self.redox_potential = redox_potential or [Data(dropna=self.dropna).to_dict()]
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#
#         del d["@module"]
#         del d["@class"]
#         del d["@version"]
#
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#         del d["dropna"]
#
#         return d
#
#
# class RootSchema(MSONable):
#     def __init__(self, _id=None, computational_data=None, ml_data=None, characterization_data=None,
#                  related_literature=None, dropna=True):
#         self.dropna = dropna
#         self.computational_data = computational_data or Computation(dropna=self.dropna).to_dict()
#         self.ml_data = ml_data
#         self.characterization_data = characterization_data
#         self.related_literature = related_literature
#
#     def to_dict(self) -> dict:
#         d = self.as_dict()
#
#         if self.dropna:
#             for key in list(d.keys()):
#                 if not d[key]:
#                     del d[key]
#                 elif isinstance(d[key], list):
#                     if not d[key][0]:
#                         del d[key]
#
#         del d["dropna"]
#
#         return d
