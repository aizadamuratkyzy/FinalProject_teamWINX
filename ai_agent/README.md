# AI Agent — Cluster Monitor

This module monitors the health of the Mini-GFS cluster and gives recommendations.

## What it does

- Checks if Master server is online
- Checks if all 3 Chunkservers are online
- Generates an AI recommendation based on cluster status

## How to run
python ai_agent/agent.py
## Example output
===== MINI-GFS AI CLUSTER REPORT =====
Generated at: 2026-05-20 12:00:00
Master Server: ONLINE
Chunkserver 1: ONLINE
Chunkserver 2: ONLINE
Chunkserver 3: OFFLINE
AI Analysis:
Warning: One chunkserver is offline. Restart the failed node to restore full replication.
## Owner

Nesibeli