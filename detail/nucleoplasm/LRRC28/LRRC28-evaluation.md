---
type: protein-evaluation
gene: "LRRC28"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC28 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC28 |
| 蛋白名称 | Leucine-rich repeat-containing protein 28 |
| 蛋白大小 | 367 aa / 41.9 kDa |
| UniProt ID | Q86X40 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 367 aa / 41.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050216, IPR055 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Mitochondria | Approved |
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
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Injury-induced immune responses in Hydra.. *Seminars in immunology*. PMID: 25086685
2. Expression of circular RNAs in the vascular dementia rats.. *Neuroscience letters*. PMID: 32534097
3. miR-218 contributes to drug resistance in multiple myeloma via targeting LRRC28.. *Journal of cellular biochemistry*. PMID: 33417267
4. Identification of differential expression of genes in hepatocellular carcinoma by suppression subtractive hybridization combined cDNA microarray.. *Oncology reports*. PMID: 17786358
5. Novel genomic markers and genes related to reproduction in prolific Chios dairy sheep: a genome-wide association study.. *Animal : an international journal of animal bioscience*. PMID: 36801549

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 92.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.2，有序区 92.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050216, IPR055414; Pfam: PF23598, PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NYX | 0.603 | 0.000 | — |
| ADGRL2 | 0.514 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| ADGRL1 | 0.514 | 0.514 | — |
| PRELP | 0.509 | 0.000 | — |
| FAM217B | 0.505 | 0.000 | — |
| LUM | 0.496 | 0.000 | — |
| AP5B1 | 0.485 | 0.045 | — |
| ASB8 | 0.481 | 0.093 | — |
| KERA | 0.479 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=90.2 + PDB: 无 | pLDDT=90.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Golgi apparatus, Mitochondria | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. LRRC28 — Leucine-rich repeat-containing protein 28，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小367 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86X40
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168904-LRRC28/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC28
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X40
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000168904-LRRC28/subcellular

![](https://images.proteinatlas.org/39378/1042_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/39378/1042_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/39378/1128_H10_4_red_green.jpg)
![](https://images.proteinatlas.org/39378/1128_H10_5_red_green.jpg)
![](https://images.proteinatlas.org/39378/421_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/39378/421_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86X40-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86X40 |
| SMART | SM00364;SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR003591;IPR032675;IPR050216;IPR055414; |
| Pfam | PF23598;PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168904-LRRC28/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL5 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
