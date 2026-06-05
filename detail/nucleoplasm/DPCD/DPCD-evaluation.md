---
type: protein-evaluation
gene: "DPCD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPCD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPCD |
| 蛋白名称 | Protein DPCD |
| 蛋白大小 | 203 aa / 23.2 kDa |
| UniProt ID | Q9BVM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Plasma membrane, Mitotic spindle,; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 203 aa / 23.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026224; Pfam: PF14913 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Plasma membrane, Mitotic spindle, Primary cilium | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deciphering cellular and molecular determinants of human DPCD protein in complex with RUVBL1/RUVBL2 AAA-ATPases.. *Journal of molecular biology*. PMID: 35901867
2. Root cap cell corpse clearance limits microbial colonization in Arabidopsis thaliana.. *eLife*. PMID: 39531016
3. DPCD is a regulator of R2TP in ciliogenesis initiation through Akt signaling.. *Cell reports*. PMID: 38306274
4. Repressive ZINC FINGER OF ARABIDOPSIS THALIANA proteins promote programmed cell death in the Arabidopsis columella root cap.. *Plant physiology*. PMID: 36852889
5. Plant proteases during developmental programmed cell death.. *Journal of experimental botany*. PMID: 30793182

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.2 |
| 高置信度残基 (pLDDT>90) 占比 | 75.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 88.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.2，有序区 88.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026224; Pfam: PF14913 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUVBL2 | 0.896 | 0.860 | — |
| RUVBL1 | 0.881 | 0.828 | — |
| WDR92 | 0.734 | 0.226 | — |
| STK36 | 0.613 | 0.000 | — |
| AK7 | 0.598 | 0.000 | — |
| TNFSF13 | 0.554 | 0.551 | — |
| POLL | 0.499 | 0.000 | — |
| RTTN | 0.499 | 0.000 | — |
| RPAP3 | 0.489 | 0.209 | — |
| SPAG6 | 0.485 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=89.2 + PDB: 无 | pLDDT=89.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Plasma membrane, Mitoti | 一致 |
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
1. DPCD — Protein DPCD，非常新颖，仅有少数基础研究。
2. 蛋白大小203 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166171-DPCD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPCD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166171-DPCD/subcellular

![](https://images.proteinatlas.org/36604/2146_C6_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/36604/2146_C6_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/36604/2177_G5_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/36604/2177_G5_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/36604/2244_B3_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/36604/2244_B3_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BVM2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
