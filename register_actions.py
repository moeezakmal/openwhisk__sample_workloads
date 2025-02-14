import os
import sys
import subprocess
from pathlib import Path

top_dir = Path.cwd() / 'functions'

os.chdir(str(top_dir / 'chameleon'))
cmd = 'wsk action create chameleon faas_chameleon.py --docker sailresearch/chameleon_openwhisk --web raw -i --memory 256'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'float_operation'))
cmd = 'wsk action create float_op float_operation.py -i --memory 256'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'image_processing'))
cmd = 'wsk action create image_process image_process.py --docker sailresearch/python3_openwhisk --web raw -i --memory 512'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'linpack'))
cmd = 'wsk action create linpack linpack.py --docker sailresearch/python3_openwhisk --web raw --memory 512 -i'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'matmult'))
cmd = 'wsk action create matmult matmult.py --docker sailresearch/python3_openwhisk --web raw --memory 512 -i'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'pyaes'))
cmd = 'wsk action create pyaes faas_pyaes.py --docker sailresearch/pyaes_openwhisk --web raw -i --memory 256'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'video_processing'))
cmd = 'wsk action create video_process video_process.py --docker sailresearch/video_process_openwhisk --web raw -i --memory 512'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'ml_inference' / 'logistic_regression_review'))
cmd = 'wsk action create lr_review lr_review.py --docker sailresearch/lr_review_openwhisk --web raw -i --memory 256'
subprocess.call(cmd, shell=True)

os.chdir(str(top_dir / 'ml_inference' / 'mobilenet'))
cmd = 'wsk action create mobilenet mobilenet.py --docker sailresearch/mobilenet_openwhisk --web raw -i --memory 1024'
subprocess.call(cmd, shell=True)