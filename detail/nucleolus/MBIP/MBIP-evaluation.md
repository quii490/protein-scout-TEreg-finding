---
type: protein-evaluation
gene: "MBIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MBIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MBIP |
| 蛋白名称 | MAP3K12-binding inhibitory protein 1 |
| 蛋白大小 | 344 aa / 39.3 kDa |
| UniProt ID | Q9NS73 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 344 aa / 39.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.4; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ATAC complex (GO:0140672)
- cytosol (GO:0005829)
- mitotic spindle (GO:0072686)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MBIP promotes ESCC metastasis by activating MAPK pathway.. *Cellular signalling*. PMID: 38199596
2. MBIP (MAP3K12 binding inhibitory protein) drives NSCLC metastasis by JNK-dependent activation of MMPs.. *Oncogene*. PMID: 32963352
3. Systemic gene transfer of binding immunoglobulin protein (BiP) prevents disease progression in murine collagen-induced arthritis.. *Clinical and experimental immunology*. PMID: 25228326
4. Molecular specification and patterning of progenitor cells in the lateral and medial ganglionic eminences.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 18799682
5. Fathers' preconception smoking and offspring DNA methylation.. *Clinical epigenetics*. PMID: 37649101

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.4 |
| 高置信度残基 (pLDDT>90) 占比 | 8.4% |
| 置信残基 (pLDDT 70-90) 占比 | 48.3% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.4），有序残基占 56.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DR1 | 0.994 | 0.831 | — |
| YEATS2 | 0.994 | 0.828 | — |
| ZZZ3 | 0.991 | 0.828 | — |
| WDR5 | 0.989 | 0.836 | — |
| TADA2A | 0.988 | 0.837 | — |
| SGF29 | 0.985 | 0.812 | — |
| TADA3 | 0.982 | 0.815 | — |
| KAT14 | 0.980 | 0.839 | — |
| KAT2A | 0.974 | 0.834 | — |
| KAT2B | 0.974 | 0.834 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000399718.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLEKHF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COPS4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KAT14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FXR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RAP1GDS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WDR5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DGCR6L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NDEL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VTA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.4 + PDB: 无 | pLDDT=68.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. MBIP — MAP3K12-binding inhibitory protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小344 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS73
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151332-MBIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MBIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS73
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000151332-MBIP/subcellular

![](https://images.proteinatlas.org/3388/17_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3388/17_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3388/18_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3388/18_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3388/19_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3388/19_G4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NS73-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
