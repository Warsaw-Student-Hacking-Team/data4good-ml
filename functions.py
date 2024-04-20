import torch
import numpy as np
#import means absolute error
from sklearn.metrics import mean_absolute_error


def model_test(torch_model, test_loader, device, round_treshold):

    torch_model.eval()
    preds_list = []
    outs_list = []
    input_size = test_loader.dataset.tensors[0].shape[-1]


    with torch.no_grad():
        for i, (x, y) in enumerate(test_loader):
            x = x.reshape(-1,input_size).to(device)
            preds = torch_model(x)
        
        
    preds = preds.to(device).cpu().numpy()
    y = y.float().numpy()
    outs_list.append(y)
    preds_list.append(preds)

    preds_list = np.concatenate(preds_list, axis=0)
    outs_list = np.concatenate(outs_list, axis=0)

    return mean_absolute_error(outs_list, preds_list)
