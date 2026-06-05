---
type: protein-evaluation
gene: "PBXIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PBXIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PBXIP1 / HPIP |
| 蛋白名称 | Pre-B-cell leukemia transcription factor-interacting protein 1 |
| 蛋白大小 | 731 aa / 80.6 kDa |
| UniProt ID | Q96AQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 731 aa / 80.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051990 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HPIP |

**关键文献**:
1. Single-cell and multi-omics analysis identifies TRIM9 as a key ubiquitination regulator in pancreatic cancer.. *Frontiers in immunology*. PMID: 41050689
2. Two decades of a protooncogene HPIP/PBXIP1: Uncovering the tale from germ cell to cancer.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 34090932
3. HPIP and RUFY3 are noncanonical guanine nucleotide exchange factors of Rab5 to regulate endocytosis-coupled focal adhesion turnover.. *The Journal of biological chemistry*. PMID: 37797694
4. Profiling of embryonic stem cell differentiation.. *The review of diabetic studies : RDS*. PMID: 25148369
5. PBXIP1 - An indicator for poor outcome and metastatic spread in colorectal cancer.. *Pathology, research and practice*. PMID: 35785747

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 54.3% |
| 有序区域 (pLDDT>70) 占比 | 34.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.5），有序残基占 34.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051990 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.650 | 0.302 | — |
| PBX1 | 0.624 | 0.000 | — |
| PMVK | 0.519 | 0.000 | — |
| DCST2 | 0.488 | 0.000 | — |
| MDFI | 0.486 | 0.486 | — |
| GMCL1 | 0.451 | 0.451 | — |
| GJC3 | 0.429 | 0.000 | — |
| WASHC3 | 0.426 | 0.422 | — |
| RSPH1 | 0.417 | 0.000 | — |
| APOE | 0.414 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Chuk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DPPA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSNAX | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WASHC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| ZMYND8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| capR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000357448.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.5 + PDB: 无 | pLDDT=57.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PBXIP1 — Pre-B-cell leukemia transcription factor-interacting protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小731 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163346-PBXIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PBXIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163346-PBXIP1/subcellular

![](https://images.proteinatlas.org/73481/1829_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/73481/1829_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/73481/1861_F7_17_cr5aeb5dae8390a_red_green.jpg)
![](https://images.proteinatlas.org/73481/1861_F7_8_cr5aeb5dae8237f_red_green.jpg)
![](https://images.proteinatlas.org/73481/2088_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/73481/2088_C7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AQ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
