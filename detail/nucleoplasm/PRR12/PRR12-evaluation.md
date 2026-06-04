---
type: protein-evaluation
gene: "PRR12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR12 / KIAA1205 |
| 蛋白名称 | Proline-rich protein 12 |
| 蛋白大小 | 2036 aa / 211.0 kDa |
| UniProt ID | Q9ULL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Postsynaptic density; Synapse, synaptosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2036 aa / 211.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052466, IPR025451; Pfam: PF13926 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Postsynaptic density; Synapse, synaptosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- neuron projection (GO:0043005)
- nucleus (GO:0005634)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1205 |

**关键文献**:
1. Haploinsufficiency of PRR12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 33824499
2. Co-essentiality analysis identifies PRR12 as a cohesin interacting protein and contributor to genomic integrity.. *Developmental cell*. PMID: 39742660
3. Dominant variants in PRR12 result in unilateral or bilateral complex microphthalmia.. *Clinical genetics*. PMID: 33314030
4. RAD21 inhibited transcription of tumor suppressor MIR4697HG and led to glioma tumorigenesis.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 31884342
5. Splicing and frameshift variants in QSER1 may be involved in developmental phenotypes.. *HGG advances*. PMID: 41139957

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.8 |
| 高置信度残基 (pLDDT>90) 占比 | 9.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 83.1% |
| 有序区域 (pLDDT>70) 占比 | 13.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.8），有序残基占 13.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052466, IPR025451; Pfam: PF13926 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCAF1 | 0.802 | 0.000 | — |
| ZNF865 | 0.711 | 0.045 | — |
| PRRG2 | 0.704 | 0.000 | — |
| PRR16 | 0.540 | 0.000 | — |
| ZNF316 | 0.510 | 0.045 | — |
| CTAGE8 | 0.510 | 0.000 | — |
| PAGR1 | 0.487 | 0.000 | — |
| LMNTD2 | 0.444 | 0.000 | — |
| FIZ1 | 0.442 | 0.045 | — |
| TP53BP1 | 0.439 | 0.439 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PUM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| rpoD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FASN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| NCBP2 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| Ncstn | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Mad2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.8 + PDB: 无 | pLDDT=42.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Postsynaptic density; Synapse, synaptosom / Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRR12 — Proline-rich protein 12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2036 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=42.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126464-PRR12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
