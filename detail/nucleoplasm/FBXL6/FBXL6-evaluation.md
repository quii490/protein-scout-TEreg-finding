---
type: protein-evaluation
gene: "FBXL6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXL6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL6 / FBL6 |
| 蛋白名称 | F-box/LRR-repeat protein 6 |
| 蛋白大小 | 539 aa / 58.6 kDa |
| UniProt ID | Q8N531 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 539 aa / 58.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR047922, IPR001611, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL6 |

**关键文献**:
1. Elevated FBXL6 activates both wild-type KRAS and mutant KRAS(G12D) and drives HCC tumorigenesis via the ERK/mTOR/PRELID2/ROS axis in mice.. *Military Medical Research*. PMID: 38124228
2. The E3 ubiquitin ligase FBXL6 controls the quality of newly synthesized mitochondrial ribosomal proteins.. *Cell reports*. PMID: 37267103
3. Elevated FBXL6 expression in hepatocytes activates VRK2-transketolase-ROS-mTOR-mediated immune evasion and liver cancer metastasis in mice.. *Experimental & molecular medicine*. PMID: 37653031
4. Elevated FBXL6 activates ATAD3A through K63-linked polyubiquitination and promotes the malignant progression of TNBC via metabolic reprogramming.. *International journal of biological macromolecules*. PMID: 40975350
5. Prognostic value and drug sensitivity of F‑box and leucine‑rich repeat protein 6 in glioma.. *Oncology letters*. PMID: 38807668

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 51.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 71.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.0，有序区 71.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR047922, IPR001611, IPR006553; Pfam: PF12937, PF13516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.944 | 0.816 | — |
| CUL1 | 0.940 | 0.797 | — |
| ADCK5 | 0.693 | 0.000 | — |
| SLC52A2 | 0.675 | 0.000 | — |
| HSP90AA1 | 0.640 | 0.626 | — |
| FBXL8 | 0.586 | 0.000 | — |
| E5RI56_HUMAN | 0.540 | 0.458 | — |
| FBXL16 | 0.532 | 0.000 | — |
| CPSF1 | 0.528 | 0.000 | — |
| FBXO16 | 0.521 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 无 | pLDDT=78.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXL6 — F-box/LRR-repeat protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小539 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N531
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182325-FBXL6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N531
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000182325-FBXL6/subcellular

![](https://images.proteinatlas.org/8867/100_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/8867/100_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/8867/1841_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/8867/1841_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/8867/82_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/8867/82_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N531-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
