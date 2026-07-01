---
type: protein-evaluation
gene: "B2RD40"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B2RD40 (Copine-2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B2RD40 |
| 蛋白全称 | Copine-2 |
| UniProt ID | B2RD40 |
| 蛋白大小 | 532 aa / 58.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 532 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR000008; InterPro:IPR035892; InterPro:IPR037768; InterPro:IPR045052; InterPro:IPR010734; InterPro:IPR002035 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Calcium-dependent phospholipid-binding protein that plays a role in calcium-mediated intracellular processes. Exhibits calcium-dependent cell membrane binding properties

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000008 |
| InterPro | IPR035892 |
| InterPro | IPR037768 |
| InterPro | IPR045052 |
| InterPro | IPR010734 |
| InterPro | IPR002035 |
| InterPro | IPR036465 |
| Pfam | PF00168 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B2RD40编码Copine-2（CPNE2）的TrEMBL变体，其结构域架构以Ca2+依赖性磷脂结合的双模块串联为特征：N端两枚C2结构域（IPR000008、IPR035892、Pfam PF00168）通过Ca2+离子桥与酸性磷脂头基（如磷脂酰丝氨酸、磷脂酰胆碱）结合，C端的VWA（von Willebrand factor A）结构域（IPR002035、IPR036465）形成经典Rossmann折叠，负责蛋白-蛋白互作表面。IPR037768（Copine特有）和IPR045052（Copine-2分类）进一步确认其特异性。

532 aa（58.5 kDa）的分子量在Copine家族中较为保守。AlphaFold预测结构可用，C2域的Ca2+结合环和VWA域的MIDAS基序预测可靠。PPI数据有限（TrEMBL条目，PubMed=0），但Copine家族的功能注释提示其核心互作伙伴包括膜靶向蛋白、肌动蛋白骨架组分和多种信号通路节点（如MEK1、JAB1/COPS5）。

TE调控相关性的机制推论较为间接：Copine-2的主要功能集中在Ca2+介导的膜运输和信号转导跨膜转位，但其在细胞应激条件下可能转位至核膜或核质。若其VWA域确实在核内存在结合伙伴（如染色质调节因子），则Ca2+信号可能通过Copine-2间接偶联胞外/胞内信号与核内基因表达调控。从这个角度，Copine-2可能作为Ca2+信号路径的"传送带"，将胞质事件传递给核内效应分子。极端应激（如UV损伤、热刺激）可同时触发TE激活和Ca2+内流，Copine-2可能在此交叉节点发挥桥接作用。

但GO-CC缺乏核定位注释（核定位特异性仅4/10），且当前无任何直接数据支持Ca2+-Copine2-TE通路的存在。归一化总分67.8/100，TE调控潜力极低，不建议作为优先靶标。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B2RD40

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B2RD40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2RD40
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B2RD40
