---
type: protein-evaluation
gene: "TIPARP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TIPARP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TIPARP / PARP7 |
| 蛋白名称 | Protein mono-ADP-ribosyltransferase TIPARP |
| 蛋白大小 | 657 aa / 76.2 kDa |
| UniProt ID | Q7Z3E1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 657 aa / 76.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051712, IPR012317, IPR004170, IPR037197, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PARP7 |

**关键文献**:
1. The association between TIPARP gene polymorphisms rs2665390 and ovarian cancer susceptibility.. *Gynecologic oncology reports*. PMID: 37091214
2. Identification and characterization of human TIPARP gene within the CCNL amplicon at human chromosome 3q25.31.. *International journal of oncology*. PMID: 12851707
3. Glucocorticoids, genes and brain function.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 29180230
4. Impairment of aryl hydrocarbon receptor signalling promotes hepatic disorders in cancer cachexia.. *Journal of cachexia, sarcopenia and muscle*. PMID: 37127348
5. TiPARP forms nuclear condensates to degrade HIF-1α and suppress tumorigenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 32482854

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 57.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 57.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051712, IPR012317, IPR004170, IPR037197, IPR000571; Pfam: PF00644 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARP1 | 0.862 | 0.000 | — |
| PARP16 | 0.735 | 0.000 | — |
| CYP1A1 | 0.594 | 0.000 | — |
| PARP6 | 0.582 | 0.000 | — |
| CYP1B1 | 0.577 | 0.000 | — |
| AHRR | 0.575 | 0.000 | — |
| PARP4 | 0.549 | 0.000 | — |
| TNKS2 | 0.543 | 0.066 | — |
| PARP3 | 0.532 | 0.000 | — |
| PARP2 | 0.532 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| RPL11 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LAD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLPP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RNF166 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RNF114 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 无 | pLDDT=68.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. TIPARP — Protein mono-ADP-ribosyltransferase TIPARP，研究基础较多，新颖性有限。
2. 蛋白大小657 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3E1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163659-TIPARP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TIPARP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3E1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TIPARP/IF_images/TIPARP_IF_blue_green.jpg]]



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z3E1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
