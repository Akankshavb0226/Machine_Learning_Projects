# GNN Fault Detection for Automotive Sensor Networks

I built a proof-of-concept using a **two-layer Graph Convolutional Network (GCN)** to classify **sensor health** and infer **ECU-level faults** in a car-style sensor network. Sensors are nodes, links are edges, so the model learns from both readings and relationships.

**My role:** graph + features design, GCN implementation (PyTorch Geometric), training/evaluation, plots, and documentation.

> **Impact (POC):** clear separation of healthy vs. faulty sensors; ECU aggregation flags affected ECUs.  
> _Add a metric if you can, e.g., “~92% node-level accuracy on synthetic data.”_

## Overview
- **Graph:** nodes = sensors; edges = wiring/functional links  
- **Features:** synthetic readings (voltage/temperature) with healthy vs. faulty distributions  
- **Model:** 2× `GCNConv` → ReLU → log-softmax (node classification)  
- **ECU health:** aggregate sensor predictions per ECU  
- **Evaluation:** loss curve, node-label visualization, ECU summaries

## Files
- `Node_classification_GNN_Code.ipynb` — end-to-end notebook (data → model → evaluation)  
- `Paper Presentation.pdf` — brief write-up/slides  
- `README.md` — this summary

## Tech
Python · PyTorch · PyTorch Geometric (runs smoothly in Colab or locally)

## Next
Swap synthetic data for real logs; try GAT/GIN or temporal graphs; add a tiny `/predict` API and tests/CI.
