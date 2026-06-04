---
type: protein-evaluation
gene: "MPHOSPH9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MPHOSPH9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MPHOSPH9 / MPP9 |
| 蛋白名称 | M-phase phosphoprotein 9 |
| 蛋白大小 | 1183 aa / 133.0 kDa |
| UniProt ID | Q99550 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm, Golgi apparatus, ; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1183 aa / 133.0 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026636 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm, Golgi apparatus, Centrosome, Basal body | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; G... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MPP9 |

**关键文献**:
1. Unveiling the genetic overlap and causal links between gastroesophageal reflux disease and asthma.. *International journal of surgery (London, England)*. PMID: 40932390
2. RNA-seq reveals a novel porcine lncRNA MPHOSPH9-OT1 induces CXCL8/IL-8 expression in ETEC infected IPEC-J2 cells.. *Frontiers in cellular and infection microbiology*. PMID: 36093177
3. Array-based gene expression, CGH and tissue data defines a 12q24 gain in neuroblastic tumors with prognostic implication.. *BMC cancer*. PMID: 20444257
4. Multiplexed CRISPR gene editing in primary human islet cells with Cas9 ribonucleoprotein.. *bioRxiv : the preprint server for biology*. PMID: 37745551
5. Multiplexed CRISPR gene editing in primary human islet cells with Cas9 ribonucleoprotein.. *iScience*. PMID: 38205242

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 22.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 63.7% |
| 有序区域 (pLDDT>70) 占比 | 30.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 30.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026636 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCNB1 | 0.817 | 0.094 | — |
| RAD51 | 0.786 | 0.638 | — |
| CEP97 | 0.663 | 0.089 | — |
| CCDC14 | 0.636 | 0.595 | — |
| FANCM | 0.603 | 0.333 | — |
| FBH1 | 0.600 | 0.471 | — |
| BLM | 0.596 | 0.401 | — |
| CEP83 | 0.589 | 0.099 | — |
| RAD52 | 0.559 | 0.402 | — |
| DMC1 | 0.555 | 0.447 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0G2RM98 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| nfo | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000475489.1 | psi-mi:"MI:0018"(two hybrid) | pubmed:24136289|doi:10.1039/C3 |
| KATNB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26929214|imex:IM-26156 |
| IKBKG | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TMCO1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PIH1D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24656813|imex:IM-23101 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Plasma membrane, Cytosol; 额外: Nucleoplasm, Golgi a | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. MPHOSPH9 — M-phase phosphoprotein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99550
- Protein Atlas: https://www.proteinatlas.org/ENSG00000051825-MPHOSPH9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPHOSPH9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99550
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:55:50
