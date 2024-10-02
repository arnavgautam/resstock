import os
import subprocess
from os.path import join, exists
import pandas as pd
import numpy as np
from shutil import copyfile

building_unit_type_to_resstock_category = {"SFD": 'Single-Family Detached'} # {"2": 'Multi-Family with 2 - 4 Units', "3_4": 'Multi-Family with 2 - 4 Units', "5_9": 'Multi-Family with 5+ Units', "10_19": 'Multi-Family with 5+ Units', "20_49": 'Multi-Family with 5+ Units', "50_plus": 'Multi-Family with 5+ Units', "SFA": 'Single-Family Attached', "SFD": 'Single-Family Detached' }
NUM_RESIDENCES = 100
# parallel_resstock_processes = []
for (unit_type, resstock_category) in building_unit_type_to_resstock_category.items():
    output_filepath = join('columbus', f'{NUM_RESIDENCES}_{unit_type}_unit_buildstock.csv')
    if not exists(output_filepath):
        source_ACS_file = join('project_columbus','housing_characteristics',f'Geometry Building Type ACS {unit_type}.tsv')
        dest_ACS_file = join('project_columbus','housing_characteristics',f'Geometry Building Type ACS.tsv')
        copyfile(source_ACS_file, dest_ACS_file)
        subprocess.run(f"ruby {join('resources','run_sampling.rb')} -p project_columbus -n {NUM_RESIDENCES} -o {output_filepath}")
        # parallel_resstock_processes.append(subprocess.Popen

# for p in parallel_resstock_processes:
#     p.wait()

# for p in parallel_resstock_processes:
#     print("Output:\n", p.stdout)
#     print("Error:\n", p.stderr)
#     print("\n")