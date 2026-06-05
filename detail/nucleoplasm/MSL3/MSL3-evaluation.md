---
type: protein-evaluation
gene: "MSL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MSL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSL3 / MSL3L1 |
| 蛋白名称 | MSL complex subunit 3 |
| 蛋白大小 | 521 aa / 59.8 kDa |
| UniProt ID | Q8N5Y2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 521 aa / 59.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.5; PDB: 2Y0N, 3OA6, 3OB9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016197, IPR000953, IPR008676, IPR038217, IPR026 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- MSL complex (GO:0072487)
- NuA4 histone acetyltransferase complex (GO:0035267)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 103 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MSL3L1 |

**关键文献**:
1. MSL2 variants lead to a neurodevelopmental syndrome with lack of coordination, epilepsy, specific dysmorphisms, and a distinct episignature.. *American journal of human genetics*. PMID: 38815585
2. Loss of function of male-specific lethal 3 (Msl3) does not affect spermatogenesis in rodents.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 37847071
3. Msl3 promotes germline stem cell differentiation in female Drosophila.. *Development (Cambridge, England)*. PMID: 34878097
4. Loss Of Chromodomain of Male-Specific Lethal 3 (MSL3) Does Not Affect Spermatogenesis In Rodents.. *bioRxiv : the preprint server for biology*. PMID: 36993289
5. Evidence of activity-specific, radial organization of mitotic chromosomes in Drosophila.. *PLoS biology*. PMID: 21264350

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.5 |
| 高置信度残基 (pLDDT>90) 占比 | 37.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 39.3% |
| 有序区域 (pLDDT>70) 占比 | 54.3% |
| 可用 PDB 条目 | 2Y0N, 3OA6, 3OB9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.5），有序残基占 54.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR008676, IPR038217, IPR026541; Pfam: PF05712, PF22732 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MSL1 | 0.999 | 0.985 | — |
| MSL2 | 0.999 | 0.930 | — |
| KAT8 | 0.997 | 0.841 | — |
| H4C6 | 0.992 | 0.950 | — |
| KAT5 | 0.958 | 0.301 | — |
| DMAP1 | 0.950 | 0.310 | — |
| EPC1 | 0.950 | 0.376 | — |
| MEAF6 | 0.946 | 0.303 | — |
| TRRAP | 0.945 | 0.313 | — |
| ING3 | 0.940 | 0.181 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000312244.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| Kat8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| UBC32 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| UBC34 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| IQD6 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| EMB3135 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| PAP3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |
| PAM74 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.5 + PDB: 2Y0N, 3OA6, 3OB9 | pLDDT=68.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MSL3 — MSL complex subunit 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小521 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5Y2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005302-MSL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5Y2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000005302-MSL3/subcellular

![](https://images.proteinatlas.org/34536/376_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/34536/376_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/34536/378_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/34536/378_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/34536/383_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/34536/383_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N5Y2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
