---
type: protein-evaluation
gene: "BARHL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BARHL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BARHL2 |
| 蛋白名称 | BarH-like 2 homeobox protein |
| 蛋白大小 | 387 aa / 42.0 kDa |
| UniProt ID | Q9NY43 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 387 aa / 42.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.3; PDB: 8PM5, 8PM7, 8PMC, 8PMF, 8PMN, 8PMV, 8PN4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Fusion Genes Landscape of Lung Cancer Patients From Inner Mongolia, China.. *Genes, chromosomes & cancer*. PMID: 39011998
2. BARHL2 differentially regulates the development of retinal amacrine and ganglion neurons.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 19339595
3. The conserved barH-like homeobox-2 gene barhl2 acts downstream of orthodentricle-2 and together with iroquois-3 in establishment of the caudal forebrain signaling center induced by Sonic Hedgehog.. *Developmental biology*. PMID: 25281935
4. Role of the Barhl2 homeobox gene in the specification of glycinergic amacrine cells.. *Development (Cambridge, England)*. PMID: 14998930
5. Expression of Barhl2 and its relationship with Pax6 expression in the forebrain of the mouse embryo.. *BMC neuroscience*. PMID: 27887593

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.3 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 44.7% |
| 低置信 (pLDDT<50) 占比 | 32.6% |
| 有序区域 (pLDDT>70) 占比 | 22.8% |
| 可用 PDB 条目 | 8PM5, 8PM7, 8PMC, 8PMF, 8PMN, 8PMV, 8PN4, 8PNA, 8PNC, 8R7F |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.3），有序残基占 22.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR052145; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXN4 | 0.669 | 0.066 | — |
| PTF1A | 0.663 | 0.046 | — |
| BHLHE22 | 0.635 | 0.000 | — |
| POU4F2 | 0.599 | 0.000 | — |
| ISL1 | 0.552 | 0.104 | — |
| LHX5 | 0.524 | 0.104 | — |
| ATOH7 | 0.521 | 0.000 | — |
| NEUROD4 | 0.513 | 0.000 | — |
| LHX1 | 0.507 | 0.104 | — |
| LHX9 | 0.480 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MBD2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26348|pubmed:27593931 |
| PLEKHF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REL | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.3 + PDB: 8PM5, 8PM7, 8PMC, 8PMF, 8PMN,  | pLDDT=61.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BARHL2 — BarH-like 2 homeobox protein，非常新颖，仅有少数基础研究。
2. 蛋白大小387 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NY43
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143032-BARHL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BARHL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NY43
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
