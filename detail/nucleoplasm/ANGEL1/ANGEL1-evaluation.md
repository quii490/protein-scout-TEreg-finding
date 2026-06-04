---
type: protein-evaluation
gene: "ANGEL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANGEL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANGEL1 / KIAA0759 |
| 蛋白名称 | RNA 2',3'-cyclic phosphatase ANGEL1 |
| 蛋白大小 | 670 aa / 75.3 kDa |
| UniProt ID | Q9UNK9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Mitochondrion outer membrane; Golgi apparatus; Endoplasmic r |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 670 aa / 75.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050410, IPR036691, IPR005135; Pfam: PF03372 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Mitochondrion outer membrane; Golgi apparatus; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- mitochondrial outer membrane (GO:0005741)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0759 |

**关键文献**:
1. Explore the role of long noncoding RNAs and mRNAs in intracranial atherosclerotic stenosis: From the perspective of neutrophils.. *Brain circulation*. PMID: 38284107
2. Efficient heterologous expression of cellobiose 2-epimerase gene in Escherichia coli under the control of T7 lac promoter without addition of IPTG and lactose.. *Protein expression and purification*. PMID: 39074650
3. Tracking a refined eIF4E-binding motif reveals Angel1 as a new partner of eIF4E.. *Nucleic acids research*. PMID: 23814182
4. BRD9 recognizes lactate-induced H3K18 lactylation to drive oncogenic chromatin remodeling in hepatocellular carcinoma.. *Cell death and differentiation*. PMID: 41792243

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 31.2% |
| 有序区域 (pLDDT>70) 占比 | 57.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 中等质量（pLDDT=70.0，有序区 57.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050410, IPR036691, IPR005135; Pfam: PF03372 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VASH1 | 0.850 | 0.000 | — |
| POMT2 | 0.754 | 0.000 | — |
| EIF4E | 0.732 | 0.612 | — |
| TGFB3 | 0.589 | 0.000 | — |
| TMEM43 | 0.552 | 0.000 | — |
| DDX19A | 0.521 | 0.000 | — |
| RNF187 | 0.495 | 0.000 | — |
| CNOT8 | 0.490 | 0.000 | — |
| EIF4ENIF1 | 0.489 | 0.254 | — |
| GEMIN5 | 0.482 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MICU1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PB2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| APOBEC3D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HTR2C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IQCN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF414 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EIF4E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.0 + PDB: 无 | pLDDT=70.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion outer membrane; Golgi apparatus; End / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ANGEL1 — RNA 2',3'-cyclic phosphatase ANGEL1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小670 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNK9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013523-ANGEL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANGEL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNK9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:51:13
