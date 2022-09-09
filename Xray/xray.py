
import os,sys
sys.path.insert(0,"..")
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import argparse
import skimage, skimage.io
import pprint

import torch
import torch.nn.functional as F
import torchvision, torchvision.transforms

import torchxrayvision as xrv

def predict(filename):
    img = skimage.io.imread(filename)
    img = xrv.datasets.normalize(img, 255)
    if len(img.shape) > 2:
        img = img[:, :, 0]
    if len(img.shape) < 2:
        print("error, dimension lower than 2 for image")

    # Add color channel
    img = img[None, :, :]

    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop(),
                                                xrv.datasets.XRayResizer(224)])

    img = transform(img)
    model = xrv.models.get_model("densenet121-res224-all")
    output = {}
    with torch.no_grad():
        img = torch.from_numpy(img).unsqueeze(0)
    
        img = img.cuda()
        model = model.cuda()
    

        preds = model(img).cpu()
        output["preds"] = dict(zip(xrv.datasets.default_pathologies,preds[0].detach().numpy()))
    return output


