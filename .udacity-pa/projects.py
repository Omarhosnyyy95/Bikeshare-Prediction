import argparse
import subprocess as sp
from udacity_pa import udacity

nanodegree = 'nd101'
projects = ['Predicting_bike_sharing_data']
filenames = ['my_answers.py', 'Predicting_bike_sharing_data.ipynb']

def submit(args):

  # Do we prefer ipynb, html or both?
  # sp.call(['jupyter', 'nbconvert', '--to', 'html', 'dlnd_image_classification.ipynb'])
  jwt_path = "D:\Projects\data_analysis\Projects\deep learning\deep-learning-v2-pytorch\project-bikesharing\.udacity-pa\jwt"
  udacity.submit(nanodegree, projects[0], filenames, 
                 environment = args.environment,
                #  jwt_path = args.jwt_path)
                 jwt_path = jwt_path)
