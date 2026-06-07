---
type: protein-evaluation
gene: "LRRC10B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC10B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC10B |
| 蛋白名称 | Leucine-rich repeat-containing protein 10B |
| 蛋白大小 | 292 aa / 32.7 kDa |
| UniProt ID | A6NIK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 32.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
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
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcriptome-wide association study and Mendelian randomization in pancreatic cancer identifies susceptibility genes and causal relationships with type 2 diabetes and venous thromboembolism.. *EBioMedicine*. PMID: 39002386
2. CREB Promotes Beta Cell Gene Expression by Targeting Its Coactivators to Tissue-Specific Enhancers.. *Molecular and cellular biology*. PMID: 31182641
3. Association of DNA Methylation in Blood Pressure-Related Genes With Ischemic Stroke Risk and Prognosis.. *Frontiers in cardiovascular medicine*. PMID: 35345488
4. Low expression lncRNA RPLP0P2 is associated with poor prognosis and decreased cell proliferation and adhesion ability in lung adenocarcinoma.. *Oncology reports*. PMID: 27460542
5. Identification and Validation of Signature Genes in Invasiveness-Associated Modules of Nonfunctioning Pituitary Adenomas.. *Biomedicines*. PMID: 41751383

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 67.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 79.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.5，有序区 79.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050216; Pfam: PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENST00000378075 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 1
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 无 | pLDDT=83.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 0 + 1 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC10B — Leucine-rich repeat-containing protein 10B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NIK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204950-LRRC10B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC10B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NIK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000204950-LRRC10B/subcellular

![](https://images.proteinatlas.org/47619/1370_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/47619/1370_F11_4_red_green.jpg)
![](https://images.proteinatlas.org/47619/1372_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/47619/1372_F11_4_red_green.jpg)
![](https://images.proteinatlas.org/47619/1413_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/47619/1413_E5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NIK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NIK2 |
| SMART | SM00364;SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR003591;IPR032675;IPR050216; |
| Pfam | PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204950-LRRC10B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
