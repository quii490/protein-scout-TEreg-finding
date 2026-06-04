---
type: protein-evaluation
gene: "DNAJB12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJB12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB12 |
| 蛋白名称 | DnaJ homolog subfamily B member 12 |
| 蛋白大小 | 375 aa / 41.9 kDa |
| UniProt ID | Q9NXW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 41.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.3; PDB: 2CTP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001623, IPR018253, IPR051100, IPR015399, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mendelian randomization analysis to identify potential drug targets for osteoarthritis.. *PloS one*. PMID: 39932908
2. DNAJB12 and DNJB14 are non-redundant Hsp40 redox chaperones involved in endoplasmic reticulum protein reflux.. *Biochimica et biophysica acta. General subjects*. PMID: 37925033
3. DNAJB12 and Hsp70 triage arrested intermediates of N1303K-CFTR for endoplasmic reticulum-associated autophagy.. *Molecular biology of the cell*. PMID: 33534640
4. Cytosolic and endoplasmic reticulum chaperones inhibit wt-p53 to increase cancer cells' survival by refluxing ER-proteins to the cytosol.. *eLife*. PMID: 40202782
5. DNAJB12 and Hsp70 Mediate Triage of Misfolded Membrane Proteins for Proteasomal versus Lysosomal Degradation.. *Autophagy reports*. PMID: 36743458

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.3 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 23.2% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 2CTP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.3，有序区 69.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR018253, IPR051100, IPR015399, IPR036869; Pfam: PF00226, PF09320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.972 | 0.800 | — |
| HSPA2 | 0.901 | 0.802 | — |
| HSPA9 | 0.855 | 0.666 | — |
| EXOC3 | 0.822 | 0.051 | — |
| HSPA5 | 0.809 | 0.495 | — |
| HSPA1L | 0.801 | 0.481 | — |
| SGTA | 0.781 | 0.217 | — |
| HSPH1 | 0.772 | 0.142 | — |
| HSPA1B | 0.767 | 0.447 | — |
| RNF5 | 0.727 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| MME | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17342744 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.3 + PDB: 2CTP | pLDDT=76.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / Nuclear membrane, Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJB12 — DnaJ homolog subfamily B member 12，非常新颖，仅有少数基础研究。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148719-DNAJB12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
