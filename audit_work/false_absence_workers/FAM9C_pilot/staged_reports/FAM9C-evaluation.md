---
type: protein-evaluation
gene: "FAM9C"
date: 2026-06-04
tags: [protein-scout, scored, false-absence-repair, pilot]
status: scored
---

## FAM9C — SCORED (False-Absence Recovery)

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| UniProt | Q8IZT9 |
| 蛋白 | Protein FAM9C |
| 大小 | 166 aa |
| AlphaFold pLDDT | ? |
| PubMed strict | 0 |
| PDB | 0 entries |

### 2. 核定位证据

| 来源 | 定位 | 证据 |
|---|---|---|
| UniProt | Nucleus | **ECO:0000269** (实验证据) |
| GO-CC | synaptonemal complex (IBA:GO_Central) | — |
| HPA | No subcellular data (ok=True) | — |

**HPA IF 状态**: HPA packet ok=True 但无 subcellular localization 数据。核定位基于 UniProt experimental evidence (ECO:0000269)。

### 3. False Absence Recheck

**原报告问题**: 原 49-line rejected 报告含有以下 harvest failure 迹象：
- UniProt `?` — 实际 accession 为 Q8IZT9，定位为 Nucleus ECO:0000269
- AlphaFold pLDDT `?` — 实际值为 ?
- GO-CC `No data` — 实际有 synaptonemal complex
- HPA `main=No data` — 实际 packet ok=True
- IF unavailable — 需独立检索 HPA

**修复**: 重新 harvest FAM9C，确认 UniProt 有实验级核定位证据。原 `核定位 0/10` 应修正为 `核定位 6/10`。

### 4. 功能背景

FAM9C 是 FAM9 家族蛋白，UniProt 实验证据定位为 Nucleus。GO-CC 注释为 synaptonemal complex（减数分裂染色体联会复合体），与染色质功能相关。

### 5. PubMed 证据

| Type | Count |
|---|---|
| Strict | 0 |
| Broad | 0 |

研究极少，极度新颖。

### 6. AlphaFold / PAE / PDB

- AlphaFold pLDDT: ?
- PAE: 暂无数据（未生成 PAE 图片）
- PDB: 0 entries

### 7. PPI 网络

| 来源 | 结果 |
|---|---|
| STRING | packet 返回 0 partners |
| IntAct | packet 返回 0 interactions |
| UniProt interactions | 11 |

PPI 网络数据有限，但不影响核定位判断。

### 8. TE-Regulator Relevance

FAM9C 定位于 nucleus + synaptonemal complex，与减数分裂染色体结构相关。与 TE 调控的直接关联较弱，但核定位 + 极度新颖使其适合 as exploratory candidate。

### 9. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | UniProt Nucleus ECO:0000269 |
| 蛋白大小 | 10/10 | ×1 | 10 | 166 aa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 |
| 三维结构 | 3/10 | ×3 | 9 | pLDDT=N/A (packet未采集) (packet未采集) |
| 调控结构域 | 5/10 | ×2 | 10 | FAM9 family |
| PPI 网络 | 3/10 | ×3 | 9 | Limited data |
| **加权总分** | | | **112/180** | |
| **归一化总分 (÷1.83)** | | | **61.2/100** | |

### 10. Final Decision

**SCORED** — rescued from false-absence rejection. UniProt experimental evidence (ECO:0000269) confirms nuclear localization. Original rejection was caused by harvest/network failure writing `?` for all data fields.

### 11. 人工复核建议

HPA subcellular data 缺失，建议独立检索 HPA 确认 IF 图像状态。STRING/IntAct/PDB 数据均为零，但不影响核定位核心证据。

### 12. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8IZT9
- HPA: 无 subcellular 数据 (ok=True)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZT9
- Packet: 2026-06-04 re-harvest
