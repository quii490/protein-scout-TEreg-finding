---
type: protein-evaluation
gene: "CSRP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSRP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSRP2 / LMO5, SMLIM |
| 蛋白名称 | Cysteine and glycine-rich protein 2 |
| 蛋白大小 | 193 aa / 21.0 kDa |
| UniProt ID | Q16527 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 193 aa / 21.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- focal adhesion (GO:0005925)
- nucleus (GO:0005634)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 87 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LMO5, SMLIM |

**关键文献**:
1. CSRP2 promotes the glioblastoma mesenchymal phenotype via p130Cas-mediated NF-κB and MAPK pathways.. *Journal of experimental & clinical cancer research : CR*. PMID: 40764945
2. CSRP2 promotes cell stemness in head and neck squamous cell carcinoma.. *Head & neck*. PMID: 37466293
3. Targeting immunosuppressive macrophages by CSRP2-regulated CCL28 signaling sensitizes hepatocellular carcinoma to lenvatinib.. *Journal for immunotherapy of cancer*. PMID: 41043855
4. [Role and mechanism of cysteine and glycine-rich protein 2 in the malignant progression of neuroblastoma].. *Beijing da xue xue bao. Yi xue ban = Journal of Peking University. Health sciences*. PMID: 38864136
5. Cloning, structural analysis, and chromosomal localization of the human CSRP2 gene encoding the LIM domain protein CRP2.. *Genomics*. PMID: 9286703

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 60.6% |
| 中等置信 (pLDDT 50-70) 占比 | 31.6% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 60.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.6，有序区 60.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PIAS1 | 0.633 | 0.230 | — |
| SPARC | 0.596 | 0.000 | — |
| SRF | 0.570 | 0.000 | — |
| TAGLN | 0.500 | 0.000 | — |
| LMO1 | 0.500 | 0.000 | — |
| GATA5 | 0.445 | 0.000 | — |
| FLNA | 0.442 | 0.047 | — |
| RNF168 | 0.426 | 0.000 | — |
| MED14 | 0.426 | 0.000 | — |
| RPS27L | 0.424 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| VMP1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| ARHGAP11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| COG6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STK4 | psi-mi:"MI:0018"(two hybrid) | pubmed:23386615|imex:IM-23209 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.6 + PDB: 无 | pLDDT=70.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CSRP2 — Cysteine and glycine-rich protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小193 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16527
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175183-CSRP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSRP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16527
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSRP2/CSRP2-PAE.png]]
