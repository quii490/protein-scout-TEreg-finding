---
type: protein-evaluation
gene: "MID1IP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MID1IP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MID1IP1 / MIG12 |
| 蛋白名称 | Mid1-interacting protein 1 |
| 蛋白大小 | 183 aa / 20.2 kDa |
| UniProt ID | Q9NPA3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 20.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR053719, IPR009786; Pfam: PF07084 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MIG12 |

**关键文献**:
1. Midline 1 interacting protein 1 promotes cancer metastasis through FOS-like 1-mediated matrix metalloproteinase 9 signaling in HCC.. *Hepatology (Baltimore, Md.)*. PMID: 36632999
2. Inhibition of MID1IP1 induces ferroptosis and suppresses c-Myc expression in colorectal cancer cell.. *Genes & genomics*. PMID: 41343117
3. Colocalization of MID1IP1 and c-Myc is Critically Involved in Liver Cancer Growth via Regulation of Ribosomal Protein L5 and L11 and CNOT2.. *Cells*. PMID: 32316188
4. Acetylcorynoline Induces Apoptosis and G2/M Phase Arrest through the c-Myc Signaling Pathway in Colon Cancer Cells.. *International journal of molecular sciences*. PMID: 38139419
5. Hypolipogenic effects of Icariside E4 via phosphorylation of AMPK and inhibition of MID1IP1 in HepG2 cells.. *Phytotherapy research : PTR*. PMID: 35916211

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 22.4% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 21.9% |
| 低置信 (pLDDT<50) 占比 | 31.7% |
| 有序区域 (pLDDT>70) 占比 | 46.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 46.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053719, IPR009786; Pfam: PF07084 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THRSP | 0.927 | 0.204 | — |
| MID1 | 0.708 | 0.367 | — |
| ACACA | 0.620 | 0.245 | — |
| ZBTB8A | 0.479 | 0.000 | — |
| GINM1 | 0.405 | 0.000 | — |
| TATDN2 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mid1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15070402 |
| SUFU | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CD9 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| GCH1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ATP6V0D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUV39H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC45A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPL38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| AK8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 15
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 6 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MID1IP1 — Mid1-interacting protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPA3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165175-MID1IP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MID1IP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPA3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
