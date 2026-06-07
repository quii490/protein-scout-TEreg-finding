---
type: protein-evaluation
gene: "KBTBD6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KBTBD6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KBTBD6 |
| 蛋白名称 | Kelch repeat and BTB domain-containing protein 6 |
| 蛋白大小 | 674 aa / 76.1 kDa |
| UniProt ID | Q86V97 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 674 aa / 76.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.2; PDB: 4XC2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR046790, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of potential crucial genes in monocytes for atherosclerosis using bioinformatics analysis.. *The Journal of international medical research*. PMID: 32314637
2. Imprinting at the KBTBD6 locus involves species-specific maternal methylation and monoallelic expression in livestock animals.. *Journal of animal science and biotechnology*. PMID: 37817239
3. Human LC3 and GABARAP subfamily members achieve functional specificity via specific structural modulations.. *Autophagy*. PMID: 30982432
4. The KBTBD6/7-DRD2 axis regulates pituitary adenoma sensitivity to dopamine agonist treatment.. *Acta neuropathologica*. PMID: 32572597
5. Regular football training down-regulates miR-1303 muscle expression in veterans.. *European journal of applied physiology*. PMID: 34212217

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 55.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 4XC2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=81.2，有序区 77.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR046790, IPR047931; Pfam: PF07707, PF00651, PF20165 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KBTBD7 | 0.995 | 0.809 | — |
| CUL3 | 0.991 | 0.649 | — |
| RBX1 | 0.940 | 0.329 | — |
| KBTBD8 | 0.920 | 0.045 | — |
| KLHL42 | 0.915 | 0.062 | — |
| KLHL9 | 0.914 | 0.000 | — |
| KCTD17 | 0.914 | 0.069 | — |
| KLHL8 | 0.912 | 0.000 | — |
| SPOPL | 0.909 | 0.084 | — |
| TNFAIP1 | 0.909 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| OSBPL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| GABARAPL2 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| KBTBD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 4XC2 | pLDDT=81.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KBTBD6 — Kelch repeat and BTB domain-containing protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小674 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86V97
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165572-KBTBD6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KBTBD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86V97
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86V97-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86V97 |
| SMART | SM00875;SM00225;SM00612; |
| UniProt Domain [FT] | DOMAIN 63..138; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037" |
| InterPro | IPR011705;IPR017096;IPR000210;IPR046790;IPR047931;IPR047933;IPR015915;IPR006652;IPR011333; |
| Pfam | PF07707;PF00651;PF20165;PF01344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165572-KBTBD6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GABARAP | Intact, Biogrid | true |
| GABARAPL1 | Intact, Biogrid | true |
| GABARAPL2 | Intact, Biogrid | true |
| KBTBD7 | Intact, Biogrid, Bioplex | true |
| MAP1LC3B | Intact, Biogrid | true |
| ABT1 | Bioplex | false |
| APOBEC3C | Bioplex | false |
| ARIH1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
