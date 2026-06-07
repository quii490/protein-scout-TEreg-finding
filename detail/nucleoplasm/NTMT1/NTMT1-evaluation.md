---
type: protein-evaluation
gene: "NTMT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NTMT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NTMT1 / C9orf32, METTL11A, NRMT, NRMT1 |
| 蛋白名称 | N-terminal Xaa-Pro-Lys N-methyltransferase 1 |
| 蛋白大小 | 223 aa / 25.4 kDa |
| UniProt ID | Q9BV86 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 223 aa / 25.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.5; PDB: 2EX4, 5CVD, 5CVE, 5E1B, 5E1D, 5E1M, 5E1O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008576, IPR029063; Pfam: PF05891 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf32, METTL11A, NRMT, NRMT1 |

**关键文献**:
1. Spinal-Specific Super Enhancer in Neuropathic Pain.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 37802656
2. Venglustat Inhibits Protein N-Terminal Methyltransferase 1 in a Substrate-Competitive Manner.. *Journal of medicinal chemistry*. PMID: 36074125
3. Kinetic mechanism of protein N-terminal methyltransferase 1.. *The Journal of biological chemistry*. PMID: 25771539
4. Discovering the N-Terminal Methylome by Repurposing of Proteomic Datasets.. *Journal of proteome research*. PMID: 34382793
5. The comprehensive analysis of the prognostic and functional role of N-terminal methyltransferases 1 in pan-cancer.. *PeerJ*. PMID: 37901469

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.5 |
| 高置信度残基 (pLDDT>90) 占比 | 97.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 2EX4, 5CVD, 5CVE, 5E1B, 5E1D, 5E1M, 5E1O, 5E2A, 5E2B, 6DTN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EX4, 5CVD, 5CVE, 5E1B, 5E1D, 5E1M, 5E1O, 5E2A, 5E2B, 6DTN）+ AlphaFold极高置信度预测（pLDDT=97.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008576, IPR029063; Pfam: PF05891 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCC1 | 0.928 | 0.426 | — |
| KLHL31 | 0.883 | 0.000 | — |
| RPL23A | 0.811 | 0.000 | — |
| DRG1 | 0.686 | 0.613 | — |
| RANBP1 | 0.661 | 0.000 | — |
| RABIF | 0.652 | 0.000 | — |
| DDB2 | 0.644 | 0.292 | — |
| METTL17 | 0.624 | 0.000 | — |
| EEF1AKMT2 | 0.620 | 0.000 | — |
| PRMT6 | 0.600 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| DRG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| RBMX | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PRKCE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| DIS3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| VAMP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLYR1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DENR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.5 + PDB: 2EX4, 5CVD, 5CVE, 5E1B, 5E1D,  | pLDDT=97.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NTMT1 — N-terminal Xaa-Pro-Lys N-methyltransferase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小223 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BV86
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148335-NTMT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NTMT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BV86
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000148335-NTMT1/subcellular

![](https://images.proteinatlas.org/20092/234_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/20092/234_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/20092/235_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/20092/235_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/20092/535_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/20092/535_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BV86-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BV86 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008576;IPR029063; |
| Pfam | PF05891; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148335-NTMT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DRG1 | Biogrid, Opencell | true |
| PPP1R16B | Bioplex | false |
| RCC1 | Intact | false |
| SMYD3 | Bioplex | false |
| VCY | Bioplex | false |
| VCY1B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
