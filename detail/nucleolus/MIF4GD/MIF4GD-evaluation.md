---
type: protein-evaluation
gene: "MIF4GD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIF4GD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MIF4GD / SLIP1 |
| 蛋白名称 | MIF4G domain-containing protein |
| 蛋白大小 | 222 aa / 25.4 kDa |
| UniProt ID | A9UHW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Golgi apparatus, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 222 aa / 25.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016024, IPR003890, IPR051367; Pfam: PF02854 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Golgi apparatus, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- histone mRNA stem-loop binding complex (GO:0062073)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SLIP1 |

**关键文献**:
1. Novel interactors and a role for supervillin in early cytokinesis.. *Cytoskeleton (Hoboken, N.J.)*. PMID: 20309963
2. INT6 interacts with MIF4GD/SLIP1 and is necessary for efficient histone mRNA translation.. *RNA (New York, N.Y.)*. PMID: 22532700
3. MIF4G domain containing protein regulates cell cycle and hepatic carcinogenesis by antagonizing CDK2-dependent p27 stability.. *Oncogene*. PMID: 24336329
4. Replication stress-induced alternative mRNA splicing alters properties of the histone RNA-binding protein HBP/SLBP: a key factor in the control of histone gene expression.. *Bioscience reports*. PMID: 23941746

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 82.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.8，有序区 92.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR003890, IPR051367; Pfam: PF02854 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLBP | 0.999 | 0.895 | — |
| DDX19A | 0.932 | 0.929 | — |
| DDX19B-2 | 0.903 | 0.901 | — |
| CTIF | 0.875 | 0.847 | — |
| EIF4G1 | 0.825 | 0.000 | — |
| EIF3G | 0.692 | 0.502 | — |
| DDX19B | 0.650 | 0.643 | — |
| SLC25A19 | 0.604 | 0.000 | — |
| PABPC1 | 0.559 | 0.000 | — |
| EIF4E | 0.550 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000484245.1 | psi-mi:"MI:0071"(molecular sieving) | pubmed:23286197|imex:IM-26490 |
| DDX19A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HGS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| HDAC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| PPARG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SLBP | psi-mi:"MI:0872"(atomic force microscopy) | pubmed:23286197|imex:IM-26490 |
| DDX19B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AQP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTIF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 无 | pLDDT=91.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli; 额外: Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MIF4GD — MIF4G domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小222 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A9UHW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125457-MIF4GD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIF4GD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A9UHW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000125457-MIF4GD/subcellular

![](https://images.proteinatlas.org/51222/704_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/51222/704_E10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A9UHW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A9UHW6 |
| SMART | SM00543; |
| UniProt Domain [FT] | DOMAIN 3..205; /note="MIF4G" |
| InterPro | IPR016024;IPR003890;IPR051367; |
| Pfam | PF02854; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125457-MIF4GD/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX19A | Intact, Biogrid, Bioplex | true |
| DDX19B | Intact, Biogrid, Bioplex | true |
| HDAC4 | Intact, Biogrid | true |
| SLBP | Intact, Biogrid | true |
| CTIF | Biogrid | false |
| EIF3G | Intact | false |
| ERI1 | Intact | false |
| HGS | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
