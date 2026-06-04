---
type: protein-evaluation
gene: "DOC2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOC2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOC2A |
| 蛋白名称 | Double C2-like domain-containing protein alpha |
| 蛋白大小 | 400 aa / 44.0 kDa |
| UniProt ID | Q14183 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cell Junctions; 额外: Nucleoplasm, Nucleoli; UniProt: Lysosome; Cytoplasmic vesicle, secretory vesicle, synaptic v |
| 蛋白大小 | 10/10 | ×1 | 10 | 400 aa / 44.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=78.0; PDB: 4MJJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR014638, IPR043566, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | Lysosome; Cytoplasmic vesicle, secretory vesicle, synaptic vesicle membrane; Synapse, synaptosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extrinsic component of synaptic vesicle membrane (GO:0098850)
- glutamatergic synapse (GO:0098978)
- lysosome (GO:0005764)
- neuron projection (GO:0043005)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. doc2a and doc2b contribute to locomotor and social behaviors by down-regulating npas4b in zebrafish.. *BMC biology*. PMID: 40597089
2. Disease-linked mutations in Munc18-1 deplete synaptic Doc2.. *Brain : a journal of neurology*. PMID: 38242640
3. The 16p11.2 homologs fam57ba and doc2a generate certain brain and body phenotypes.. *Human molecular genetics*. PMID: 28934389
4. Increased expression of DOC2A in human and rat temporal lobe epilepsy.. *Epilepsy research*. PMID: 30844661
5. Down-Regulation of Double C2 Domain Alpha Promotes the Formation of Hyperplastic Nerve Fibers in Aganglionic Segments of Hirschsprung's Disease.. *International journal of molecular sciences*. PMID: 36142117

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 58.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 21.0% |
| 有序区域 (pLDDT>70) 占比 | 67.4% |
| 可用 PDB 条目 | 4MJJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=78.0，有序区 67.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR014638, IPR043566, IPR047022; Pfam: PF00168 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UNC13B | 0.920 | 0.510 | — |
| SCGN | 0.846 | 0.609 | — |
| SNAP25 | 0.772 | 0.050 | — |
| RPH3AL | 0.758 | 0.000 | — |
| UNC13A | 0.740 | 0.000 | — |
| UBASH3B | 0.705 | 0.692 | — |
| HIRIP3 | 0.700 | 0.000 | — |
| SEZ6L2 | 0.695 | 0.000 | — |
| ASPHD1 | 0.684 | 0.000 | — |
| RAB27A | 0.681 | 0.155 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DOC2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCTD21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTC21B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBASH3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VDAC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SCGN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SETMAR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR137B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAP1GDS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| TRNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 4MJJ | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome; Cytoplasmic vesicle, secretory vesicle,  / Cell Junctions; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DOC2A — Double C2-like domain-containing protein alpha，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小400 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14183
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149927-DOC2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOC2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14183
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
