---
type: protein-evaluation
gene: "P2RX6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## P2RX6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | P2RX6 / P2RXL1, P2X6 |
| 蛋白名称 | P2X purinoceptor 6 |
| 蛋白大小 | 441 aa / 48.8 kDa |
| UniProt ID | O15547 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cell membrane; Endoplasmic reticulum; Nucleus; Nucleus inner |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 48.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003049, IPR027309, IPR001429, IPR059116, IPR053 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Cell membrane; Endoplasmic reticulum; Nucleus; Nucleus inner membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- dendritic spine (GO:0043197)
- endoplasmic reticulum membrane (GO:0005789)
- glutamatergic synapse (GO:0098978)
- neuronal cell body (GO:0043025)
- nuclear inner membrane (GO:0005637)
- parallel fiber to Purkinje cell synapse (GO:0098688)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: P2RXL1, P2X6 |

**关键文献**:
1. Next Generation Sequencing and Electromyography Reveal the Involvement of the P2RX6 Gene in Myopathy.. *Current issues in molecular biology*. PMID: 38392191
2. [An epigenetic clock model for assessing the human biological age of healthy aging].. *Zhonghua yi xue za zhi*. PMID: 35012300
3. Subcutaneous adipose tissue alteration in aging process associated with thyroid hormone signaling.. *BMC medical genomics*. PMID: 37626392
4. Detection of Selection Signatures in Anqing Six-End-White Pigs Based on Resequencing Data.. *Genes*. PMID: 36553577
5. The m(6)A-suppressed P2RX6 activation promotes renal cancer cells migration and invasion through ATP-induced Ca(2+) influx modulating ERK1/2 phosphorylation and MMP9 signaling pathway.. *Journal of experimental & clinical cancer research : CR*. PMID: 31159832

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 56.5% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 12.0% |
| 有序区域 (pLDDT>70) 占比 | 82.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.9，有序区 82.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003049, IPR027309, IPR001429, IPR059116, IPR053792; Pfam: PF00864 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| P2RX1 | 0.995 | 0.000 | — |
| P2RX3 | 0.993 | 0.000 | — |
| P2RX4 | 0.993 | 0.000 | — |
| P2RX2 | 0.982 | 0.095 | — |
| P2RX5 | 0.971 | 0.000 | — |
| P2RX7 | 0.949 | 0.000 | — |
| GRIN2C | 0.923 | 0.000 | — |
| GRIN2D | 0.915 | 0.000 | — |
| GRIN1 | 0.912 | 0.000 | — |
| GRIN2A | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| DNAJB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BAG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SULT2B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLK10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| F2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 无 | pLDDT=82.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Endoplasmic reticulum; Nucleus; Nuc / Nucleoli, Cytosol | 一致 |
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
1. P2RX6 — P2X purinoceptor 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15547
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099957-P2RX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=P2RX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15547
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
