import torch
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score

def train(model, optimizer, data, device):
    model.train()
    optimizer.zero_grad()
    z = model.encode(data.x.to(device), data.edge_index.to(device))
    pos_pred = model.decode(z, data.edge_index[:, data.y == 1].to(device))
    neg_pred = model.decode(z, data.edge_index[:, data.y == 0].to(device))
    loss = -torch.mean(F.logsigmoid(pos_pred) + F.logsigmoid(-neg_pred))
    loss.backward()
    optimizer.step()
    return loss.item()

def test(model, data, X_test, y_test, node_mapping, device):
    model.eval()
    with torch.no_grad():
        z = model.encode(data.x.to(device), data.edge_index.to(device))
        edge_index_test = torch.tensor([[node_mapping[u], node_mapping[v]] for u, v in X_test], dtype=torch.long).t().contiguous()
        pos_pred = model.decode(z, edge_index_test[:, y_test == 1].to(device))
        neg_pred = model.decode(z, edge_index_test[:, y_test == 0].to(device))

        preds = torch.cat([pos_pred, neg_pred])
        labels = torch.cat([torch.ones(pos_pred.size(0)), torch.zeros(neg_pred.size(0))])

        auc_roc = roc_auc_score(labels.cpu(), preds.cpu())
        precision = precision_score(labels.cpu(), (preds.cpu() > 0).float())
        recall = recall_score(labels.cpu(), (preds.cpu() > 0).float())
        f1 = f1_score(labels.cpu(), (preds.cpu() > 0).float())

        return auc_roc, precision, recall, f1
