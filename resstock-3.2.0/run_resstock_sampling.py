import os
import subprocess
from os.path import join
import pandas as pd
import numpy as np
from shutil import copyfile

building_unit_type_to_resstock_category = {"2": 'Multi-Family with 2 - 4 Units', "3_4": 'Multi-Family with 2 - 4 Units', "5_9": 'Multi-Family with 5+ Units', "10_19": 'Multi-Family with 5+ Units', "20_49": 'Multi-Family with 5+ Units', "50_plus": 'Multi-Family with 5+ Units', "SFA": 'Single-Family Attached', "SFD": 'Single-Family Detached' }

parallel_resstock_processes = []
for (unit_type, resstock_category) in building_unit_type_to_resstock_category.items():
    source_ACS_file = join('project_columbus','housing_characteristics',f'Geometry Building Type ACS {unit_type}.tsv')
    dest_ACS_file = join('project_columbus','housing_characteristics',f'Geometry Building Type ACS.tsv')
    copyfile(source_ACS_file, dest_ACS_file)
    parallel_resstock_processes.append(subprocess.Popen([f"ruby", f"{join('resources','run_sampling.rb')}", f"-p", f"project_columbus", f"-n", f"1", f"-o", f"{join('columbus', f'single_{unit_type}_unit_buildstock.csv')}"]))

for p in parallel_resstock_processes:
    p.wait()

# for p in parallel_resstock_processes:
#     print("Output:\n", p.stdout)
#     print("Error:\n", p.stderr)
#     print("\n")