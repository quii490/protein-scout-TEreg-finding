---
type: protein-evaluation
gene: "ANKRD50"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## ANKRD50 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ANKRD50 |
| 蛋白名称 | Ankyrin repeat domain-containing protein 50 |
| 蛋白全名 | Ankyrin repeat domain-containing protein 50 |
| 蛋白大小 | 1429 aa / ~162 kDa |
| UniProt ID | Q9ULJ7 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | HPA Approved Nucleoplasm (main) + Cytosol (main); UniProt: Endosome only (ECO:0000305) |
| 蛋白大小 | 4/10 | ×1 | 4.0 | 1429 aa — 极大型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=5 (≤20) |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 73.9; 无 PDB |
| 调控结构域 | 5/10 | ×2 | 10.0 | Ankyrin repeat; retromer/endosomal network |
| PPI 网络 | 6/10 | ×3 | 18.0 | C12orf57 (0.994); VPS29/SNX27 retromer; GRB2/EGFR signaling |
| **加权总分** | | | **124/180**** | |
| 互证加分 | | | +1.0 | HPA Approved Nucleoplasm main location |
| **归一化总分 (÷1.83)** | | | **67.8/100**** | |

PubMed strict: 5

### 3. 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Endosome (ECO:0000305) | Homology inference |
| GO-CC | endosome (IEA:UniProtKB-SubCell) | Electronic |
| HPA IF | Nucleoplasm (main), Cytosol (main) | **Approved** |

**HPA IF 数据**: HPA subcellular localization Approved. Main location: Nucleoplasm + Cytosol. Full blue_red_green IF image acquired (374 KB).

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ANKRD50/IF_images/ANKRD50_IF_blue_red_green.jpg]]

**HPA IF 状态**: IF full acquired — HPA IF 原图 (blue_red_green, 374 KB) 已成功获取。HPA Approved 级可靠性的免疫荧光显示 ANKRD50 主要定位于 Nucleoplasm 和 Cytosol。HPA 数据库包含 12 张 blue_red_green IF 图像。UniProt 记录的 Endosome 定位与 HPA 核质定位不矛盾——该蛋白可能在多种亚细胞区室间动态分布。

**定位冲突说明**: UniProt Subcellular Location 仅注释 Endosome (ECO:0000305, 基于同源性推断)，但 HPA Approved IF 实验显示核质为主定位。这种 UniProt 与 HPA 之间的亚细胞定位差异在大型未充分注释蛋白中常见。GO-CC 仅有 endosome (IEA)，尚未收录 HPA 核质证据。当前以 HPA Approved 实验数据为主要定位依据。

### 4. 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 5 |
| PubMed broad | 7 |

**关键文献**: ANKRD50 的研究极度匮乏。5 篇 strict 文献主要为 GWAS/转录组关联分析中的基因提及（骨密度、神经系统发育），无独立功能研究。蛋白功能完全未知。PubMed strict=5 为本项目最新颖的蛋白之一。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| ZDHHC17 | BioGRID | 0 |
| ARL13B | BioGRID | 0 |
| CLNK | BioGRID | 0 |
| XPO1 | BioGRID | 0 |
| SMURF1 | BioGRID | 0 |
| ZNF414 | BioGRID | 0 |
| DDX41 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ANKRD50

### PubMed

**Count: 7**

| PMID | Title |
|---|---|
| 41259427 | High-Resolution Genomic Resources for Trait Mapping and Precision Breeding for Adzuki Bean (Vigna angularis). |
| 40494419 | ANKK1, ANKRD50, GRK5, PACSIN1 and VPS8 are novel candidate genes associated with late onset Parkinson's disease: Definition of a novel predictive prot |
| 37209533 | Dissecting the genetic heterogeneity of gastric cancer. |
| 32411801 | Genome-Wide Profiling of Human Papillomavirus DNA Integration into Human Genome and Its Influence on PD-L1 Expression in Chinese Uygur Cervical Cancer |
| 27909246 | Retromer- and WASH-dependent sorting of nutrient transporters requires a multivalent interaction network with ANKRD50. |


