---
type: protein-evaluation
gene: "CNOT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNOT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNOT2 |
| 蛋白名称 | CCR4-NOT transcription complex subunit 2 |
| 蛋白大小 | 540 aa / 59.7 kDa |
| UniProt ID | Q9NZN8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 540 aa / 59.7 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=59.1; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 71 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Targeting the CNOT2/VEGF pathway by Cornin attenuates angiogenesis and invasion in cervical cancer cells.. *Sci Rep*. PMID: 42045595
2. HIV Infection as an Independent Factor Accelerating Epigenetic Ageing in Men Treated with Integrase Inhibitors: A Case-Control Study.. *Viruses*. PMID: 41754541
3. CNOT2 /c-Myc/STAT3 signaling is critically involved in glycolysis mediated apoptosis of benzyl isothiocyanate in hepatocellular carcinoma.. *Sci Rep*. PMID: 41629418
4. Human Pumilio proteins use fuzzy multivalent hydrophobic interactions to recruit the CCR4-NOT deadenylase complex to repress mRNAs.. *bioRxiv*. PMID: 41446148
5. Study on the mechanism of LNC004268 regulating sheep myoblast proliferation and differentiation through hnRNPK-CNOT2 Axis.. *Int J Biol Macromol*. PMID: 40774498

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 54.8% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.1），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT10 | 0.000 | 0.000 | — |
| CNOT1 | 0.000 | 0.000 | — |
| CNOT11 | 0.000 | 0.000 | — |
| CNOT6 | 0.000 | 0.000 | — |
| CNOT3 | 0.000 | 0.000 | — |
| CNOT8 | 0.000 | 0.000 | — |
| CNOT9 | 0.000 | 0.000 | — |
| CNOT7 | 0.000 | 0.000 | — |
| CNOT4 | 0.000 | 0.000 | — |
| CNOT6L | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75175 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NZN8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15532 | psi-mi:"MI:0034"(display technology) | pubmed:- |
| uniprotkb:A0A0J1I0X6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NZN8-4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96C12 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q9H019 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q9HBH7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q13098-7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q15911-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.1 + PDB: 无 | pLDDT=59.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CNOT2 -- CCR4-NOT transcription complex subunit 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小540 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZN8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111596-CNOT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNOT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZN8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
