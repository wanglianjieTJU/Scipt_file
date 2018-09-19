import sys
sys.path.append('/home/code/wanglianjie/fcn666/caffe/python/')
import caffe
import surgery,score
import numpy as np
import os
weights = ''
solver = caffe.SGDSolver('solver.prototxt')
solver.net.copy_from(weights)
#interp_layers=[k for k in solver.net.params.keys() if 'up' in k]
#surgery.interp(solver.net,interp_layers)
val=np.load('',dtype=str)
score.seg_tests(solver,False,val,layer='score')