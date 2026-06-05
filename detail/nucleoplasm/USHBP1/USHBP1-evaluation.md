---
type: protein-evaluation
gene: "USHBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## USHBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | USHBP1 / AIEBP, MCC2 |
| 蛋白名称 | Harmonin-binding protein USHBP1 |
| 蛋白大小 | 703 aa / 76.1 kDa |
| UniProt ID | Q8N6Y0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 703 aa / 76.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040171, IPR019536; Pfam: PF10506 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AIEBP, MCC2 |

**关键文献**:
1. Weighted correlation gene network analysis reveals a new stemness index-related survival model for prognostic prediction in hepatocellular carcinoma.. *Aging*. PMID: 32644941
2. A Genome-Wide Association Study Suggests Novel Loci Associated with a Schizophrenia-Related Brain-Based Phenotype.. *PloS one*. PMID: 23805179
3. Cannabinoid Receptor 1 associates to different molecular complexes during GABAergic neuron maturation.. *Journal of neurochemistry*. PMID: 33942314

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.0 |
| 高置信度残基 (pLDDT>90) 占比 | 34.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 37.8% |
| 有序区域 (pLDDT>70) 占比 | 51.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.0），有序残基占 51.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040171, IPR019536; Pfam: PF10506 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCCC2 | 0.960 | 0.000 | — |
| USH1C | 0.926 | 0.233 | — |
| BTD | 0.812 | 0.056 | — |
| MMRN2 | 0.754 | 0.000 | — |
| MCCC1 | 0.603 | 0.000 | — |
| SERTAD3 | 0.539 | 0.539 | — |
| ZMAT4 | 0.534 | 0.000 | — |
| GMCL1 | 0.520 | 0.062 | — |
| ZBTB25 | 0.503 | 0.000 | — |
| ADGRF5 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000252597.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXOC8 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| TUBGCP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NOC4L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NDC80 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KANSL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FANCG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXOC7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COPS4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IL16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.0 + PDB: 无 | pLDDT=68.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. USHBP1 — Harmonin-binding protein USHBP1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小703 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6Y0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130307-USHBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=USHBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6Y0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000130307-USHBP1/subcellular

![](https://images.proteinatlas.org/52471/1405_G1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52471/1405_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52471/1408_G1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/52471/1408_G1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/52471/2178_G3_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/52471/2178_G3_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N6Y0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
