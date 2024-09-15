import os
import subprocess
from os.path import join
import pandas as pd
import numpy as np

building_unit_type_to_resstock_category = {"2": 'Multi-Family with 2 - 4 Units', "3_4": 'Multi-Family with 2 - 4 Units', "5_9": 'Multi-Family with 5+ Units', "10_19": 'Multi-Family with 5+ Units', "20_49": 'Multi-Family with 5+ Units', "50_plus": 'Multi-Family with 5+ Units', "SFA": 'Single-Family Attached', "SFD": 'Single-Family Detached' }

parallel_resstock_processes = [subprocess.Popen(f"openstudio {join('workflow','run_analysis.rb')} -y {join('project_columbus','columbus_baseline.yml')} -t {unit_type} -n 1 -k", capture_output=True, text=True) for (unit_type, resstock_category) in building_unit_type_to_resstock_category.items()]

for p in parallel_resstock_processes:
    p.wait()

for p in parallel_resstock_processes:
    print("Output:\n", p.stdout)
    print("Error:\n", p.stderr)
    print("\n")


# for (unit_type, resstock_category) in building_unit_type_to_resstock_category.items():
#     print(unit_type)
#     # os.system(f"openstudio workflow/run_analysis.rb -y project_minneapolis/minneapolis_upgrades.yml -t {unit_type} -n 1 -k")
#     result = subprocess.run(f"openstudio {join('workflow','run_analysis.rb')} -y {join('project_minneapolis','minneapolis_baseline.yml')} -t {unit_type} -n 1 -k", shell=True, capture_output=True, text=True)

#     # Print the output and error messages
#     print("Output:\n", result.stdout)
#     print("Error:\n", result.stderr)
#     print("\n")