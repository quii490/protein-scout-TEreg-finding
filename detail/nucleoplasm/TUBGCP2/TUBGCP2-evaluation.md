---
type: protein-evaluation
gene: "TUBGCP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TUBGCP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TUBGCP2 / GCP2 |
| 蛋白名称 | Gamma-tubulin complex component 2 |
| 蛋白大小 | 902 aa / 102.5 kDa |
| UniProt ID | Q9BSJ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome, Basal body; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 902 aa / 102.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.6; PDB: 6V6B, 6V6S, 6X0V, 7AS4, 7QJ0, 7QJ1, 7QJ2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007259, IPR040457, IPR042241, IPR041470; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasmic microtubule (GO:0005881)
- cytosol (GO:0005829)
- gamma-tubulin complex (GO:0000930)
- membrane (GO:0016020)
- microtubule organizing center (GO:0005815)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GCP2 |

**关键文献**:
1. A Zebrafish/Drosophila Dual System Model for Investigating Human Microcephaly.. *Cells*. PMID: 36078134
2. Somatic A-to-I RNA-edited RHOA isoform 2 specific-R176G mutation promotes tumor progression in lung adenocarcinoma.. *Molecular carcinogenesis*. PMID: 36453714
3. Thick Corpus Callosum: An Unusual Finding of TUBGCP2-Related Tubulinopathy.. *American journal of medical genetics. Part A*. PMID: 40448381
4. Bi-allelic Pathogenic Variants in TUBGCP2 Cause Microcephaly and Lissencephaly Spectrum Disorders.. *American journal of human genetics*. PMID: 31630790
5. Genetics and Expression Profile of the Tubulin Gene Superfamily in Breast Cancer Subtypes and Its Relation to Taxane Resistance.. *Cancers*. PMID: 30126203

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 28.6% |
| 置信残基 (pLDDT 70-90) 占比 | 38.1% |
| 中等置信 (pLDDT 50-70) 占比 | 19.5% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 66.7% |
| 可用 PDB 条目 | 6V6B, 6V6S, 6X0V, 7AS4, 7QJ0, 7QJ1, 7QJ2, 7QJ3, 7QJ4, 7QJ5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6V6B, 6V6S, 6X0V, 7AS4, 7QJ0, 7QJ1, 7QJ2, 7QJ3, 7QJ4, 7QJ5）+ AlphaFold极高置信度预测（pLDDT=75.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007259, IPR040457, IPR042241, IPR041470; Pfam: PF04130, PF17681 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TUBG1 | 0.999 | 0.995 | — |
| TUBGCP5 | 0.999 | 0.977 | — |
| TUBGCP4 | 0.999 | 0.979 | — |
| TUBGCP6 | 0.999 | 0.997 | — |
| TUBGCP3 | 0.999 | 0.997 | — |
| MZT1 | 0.998 | 0.985 | — |
| TUBG2 | 0.997 | 0.933 | — |
| MZT2A | 0.990 | 0.966 | — |
| MZT2B | 0.976 | 0.918 | — |
| CDK5RAP2 | 0.975 | 0.948 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| G5E859 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| Mzt2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Tubgcp6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBG1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 6V6B, 6V6S, 6X0V, 7AS4, 7QJ0,  | pLDDT=75.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TUBGCP2 — Gamma-tubulin complex component 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小902 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSJ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130640-TUBGCP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TUBGCP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSJ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
