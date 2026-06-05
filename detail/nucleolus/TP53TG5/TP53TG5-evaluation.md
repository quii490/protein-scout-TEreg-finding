---
type: protein-evaluation
gene: "TP53TG5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TP53TG5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TP53TG5 / C20orf10 |
| 蛋白名称 | TP53-target gene 5 protein |
| 蛋白大小 | 290 aa / 34.0 kDa |
| UniProt ID | Q9Y2B4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Nucleoli rim; 额外: Mitotic chromosome; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 34.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029290; Pfam: PF15331 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Mitotic chromosome | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf10 |

**关键文献**:
1. Isolation and characterization of a novel TP53-inducible gene, TP53TG5, which suppresses growth and shows cell cycle-dependent transition of expression.. *Genes, chromosomes & cancer*. PMID: 10719363
2. Clinical genomics expands the morbid genome of intellectual disability and offers a high diagnostic yield.. *Molecular psychiatry*. PMID: 27431290
3. Apoptosis-related gene expression can predict the response of ovarian cancer cell lines to treatment with recombinant human TRAIL alone or combined with cisplatin.. *Clinics (Sao Paulo, Brazil)*. PMID: 32187278

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.5 |
| 高置信度残基 (pLDDT>90) 占比 | 8.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 22.1% |
| 低置信 (pLDDT<50) 占比 | 62.1% |
| 有序区域 (pLDDT>70) 占比 | 15.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.5），有序残基占 15.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029290; Pfam: PF15331 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSME3IP1 | 0.538 | 0.538 | — |
| SYS1 | 0.510 | 0.000 | — |
| TP53I11 | 0.491 | 0.000 | — |
| WFDC6 | 0.453 | 0.000 | — |
| C16orf90 | 0.447 | 0.000 | — |
| MADD | 0.441 | 0.000 | — |
| AEBP1 | 0.433 | 0.000 | — |
| TP53I13 | 0.432 | 0.000 | — |
| FNTA | 0.420 | 0.420 | — |
| TP53RK | 0.414 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FNTB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSME3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSME3IP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GRN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| NEFL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| FNTA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSP90AA4P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 8
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 8 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.5 + PDB: 无 | pLDDT=50.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli, Nucleoli rim; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 11 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TP53TG5 — TP53-target gene 5 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2B4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124251-TP53TG5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TP53TG5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2B4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000124251-TP53TG5/subcellular

![](https://images.proteinatlas.org/58510/1928_D5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/58510/1928_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58510/1955_A2_17_cr5dc042df71bb5_blue_red_green.jpg)
![](https://images.proteinatlas.org/58510/1955_A2_27_cr5dc042df725a2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58510/1977_B11_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/58510/1977_B11_63_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2B4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
