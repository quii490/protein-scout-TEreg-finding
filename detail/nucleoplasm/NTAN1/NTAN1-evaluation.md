---
type: protein-evaluation
gene: "NTAN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NTAN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NTAN1 |
| 蛋白名称 | Protein N-terminal asparagine amidohydrolase |
| 蛋白大小 | 310 aa / 34.7 kDa |
| UniProt ID | Q96AB6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 310 aa / 34.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.6; PDB: 6A0E, 6A0F, 6A0H, 6A0I |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026750; Pfam: PF14736 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Ntan1 gene is expressed in perineural glia and neurons of adult Drosophila.. *Scientific reports*. PMID: 36042338
2. Structural Analyses on the Deamidation of N-Terminal Asn in the Human N-Degron Pathway.. *Biomolecules*. PMID: 31968674
3. The magnetism responsive gene Ntan1 in mouse brain.. *Neurochemistry international*. PMID: 16600435
4. Molecular karyotyping and gene expression analysis in childhood cancer patients.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 32577795
5. Behavioral characterization of mice lacking the ubiquitin ligase UBR1 of the N-end rule pathway.. *Genes, brain, and behavior*. PMID: 12882367

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 94.2% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 97.1% |
| 可用 PDB 条目 | 6A0E, 6A0F, 6A0H, 6A0I |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6A0E, 6A0F, 6A0H, 6A0I）+ AlphaFold高质量预测（pLDDT=95.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026750; Pfam: PF14736 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SELL | 0.995 | 0.000 | — |
| CHST4 | 0.962 | 0.000 | — |
| CHST2 | 0.913 | 0.000 | — |
| MADCAM1 | 0.859 | 0.000 | — |
| CCR7 | 0.790 | 0.000 | — |
| WDYHV1 | 0.776 | 0.230 | — |
| UBR2 | 0.731 | 0.292 | — |
| PDXDC1 | 0.724 | 0.000 | — |
| ATE1 | 0.716 | 0.292 | — |
| CCL21 | 0.709 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E2f2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| CycG | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Akt | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| RhoGAP68F | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| CycA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| CycJ | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Pld3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Cdc14 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| pie | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Mps1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 6A0E, 6A0F, 6A0H, 6A0I | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Golgi apparatus | 一致 |
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
1. NTAN1 — Protein N-terminal asparagine amidohydrolase，非常新颖，仅有少数基础研究。
2. 蛋白大小310 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AB6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157045-NTAN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NTAN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AB6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157045-NTAN1/subcellular

![](https://images.proteinatlas.org/51418/791_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/51418/791_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/51418/794_F10_3_red_green.jpg)
![](https://images.proteinatlas.org/51418/794_F10_4_red_green.jpg)
![](https://images.proteinatlas.org/51418/798_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/51418/798_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AB6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AB6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026750; |
| Pfam | PF14736; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157045-NTAN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATE1 | Biogrid | false |
| RIPK1 | Intact, Bioplex | false |
| UBR2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
