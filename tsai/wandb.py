# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/201_wandb.ipynb (unless otherwise specified).

__all__ = ['get_wandb_agent', 'run_wandb_agent']

# Cell
from fastcore.script import *
from .imports import *
from .export import *

# Cell
def get_wandb_agent(script_path, sweep, entity=None, project=None, count=None):
    try: import wandb
    except ImportError: raise ImportError('You need to install wandb to run sweeps!')
    if 'program' not in sweep.keys(): sweep["program"] = script_path
    sweep_id = wandb.sweep(sweep, entity=entity, project=project)
    entity = ifnone(entity, os.environ['WANDB_ENTITY'])
    project = ifnone(project, os.environ['WANDB_PROJECT'])
    print(f"\nwandb agent {entity}/{project}/{sweep_id}\n")

def run_wandb_agent(script_path, sweep, entity=None, project=None, count=None):
    try: import wandb
    except ImportError: raise ImportError('You need to install wandb to run sweeps!')
    if 'program' not in sweep.keys(): sweep["program"] = script_path
    sweep_id = wandb.sweep(sweep, entity=entity, project=project)
    entity = ifnone(entity, os.environ['WANDB_ENTITY'])
    project = ifnone(project, os.environ['WANDB_PROJECT'])
    print(f"\nwandb agent {entity}/{project}/{sweep_id}\n")
    wandb.agent(sweep_id, function=None, count=count)