---
type: protein-evaluation
gene: "PLEKHA5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHA5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHA5 / KIAA1686, PEPP2 |
| 蛋白名称 | Pleckstrin homology domain-containing family A member 5 |
| 蛋白大小 | 1116 aa / 127.5 kDa |
| UniProt ID | Q9HAU0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1116 aa / 127.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.1; PDB: 2DKP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR040392, IPR057971, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1686, PEPP2 |

**关键文献**:
1. Genome-Wide Association Study in Acute Tubulointerstitial Nephritis.. *Journal of the American Society of Nephrology : JASN*. PMID: 36749126
2. A phosphorylation-controlled switch confers cell cycle-dependent protein relocalization.. *Nature cell biology*. PMID: 39209962
3. Proximity Labeling Reveals Spatial Regulation of the Anaphase-Promoting Complex/Cyclosome by a Microtubule Adaptor.. *ACS chemical biology*. PMID: 35952650
4. PLEKHA5 regulates tumor growth in metastatic melanoma.. *Cancer*. PMID: 31769872
5. Identification and characterization of splicing variants of PLEKHA5 (Plekha5) during brain development.. *Gene*. PMID: 22037487

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.1 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 62.5% |
| 有序区域 (pLDDT>70) 占比 | 31.3% |
| 可用 PDB 条目 | 2DKP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.1），有序残基占 31.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR040392, IPR057971, IPR001202; Pfam: PF00169, PF25541, PF00397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDZD11 | 0.777 | 0.599 | — |
| PLEK2 | 0.578 | 0.000 | — |
| PLEK | 0.571 | 0.000 | — |
| ACTR10 | 0.555 | 0.088 | — |
| PLEKHA4 | 0.531 | 0.292 | — |
| MPHOSPH8 | 0.520 | 0.082 | — |
| NUDT4 | 0.503 | 0.000 | — |
| AEBP2 | 0.483 | 0.071 | — |
| FRMD4B | 0.461 | 0.094 | — |
| SLC15A5 | 0.455 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000299275.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| RBFOX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ATN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ATXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| MAX | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| ARHGEF9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| CEP350 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| CEP250 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| tmp_locus_29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.1 + PDB: 2DKP | pLDDT=55.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEKHA5 — Pleckstrin homology domain-containing family A member 5，非常新颖，仅有少数基础研究。
2. 蛋白大小1116 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAU0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000052126-PLEKHA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAU0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
