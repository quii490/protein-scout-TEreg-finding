---
type: protein-evaluation
gene: "SMAD6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMAD6 — REJECTED (研究热度过高 (PubMed strict=470，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMAD6 / MADH6 |
| 蛋白名称 | SMAD family member 6 |
| 蛋白大小 | 496 aa / 53.5 kDa |
| UniProt ID | O43541 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus, Primary ci; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 496 aa / 53.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=470 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus, Primary cilium, Basal body, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- heteromeric SMAD protein complex (GO:0071144)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 470 |
| PubMed broad count | 724 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MADH6 |

**关键文献**:
1. Lung endothelial cells regulate pulmonary fibrosis through FOXF1/R-Ras signaling.. *Nature communications*. PMID: 37137915
2. Lhx2 specifically expressed in HSCs promotes liver regeneration and inhibits liver fibrosis.. *Hepatology (Baltimore, Md.)*. PMID: 39693275
3. New Candidates for Autism/Intellectual Disability Identified by Whole-Exome Sequencing.. *International journal of molecular sciences*. PMID: 34948243
4. STAT3 Facilitates Super Enhancer Formation to Promote Fibroblast-To-Myofibroblast Differentiation by the Analysis of ATAC-Seq, RNA-Seq and ChIP-Seq.. *Journal of cellular and molecular medicine*. PMID: 40464702
5. SMAD6-deficiency in human genetic disorders.. *NPJ genomic medicine*. PMID: 36414630

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.6 |
| 高置信度残基 (pLDDT>90) 占比 | 44.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 56.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.6，有序区 56.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001132; Pfam: PF03165, PF03166 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMURF1 | 0.999 | 0.890 | — |
| SMURF2 | 0.998 | 0.772 | — |
| SMAD4 | 0.989 | 0.510 | — |
| SMAD1 | 0.985 | 0.748 | — |
| SMAD7 | 0.984 | 0.510 | — |
| TGFBR1 | 0.982 | 0.586 | — |
| SMAD2 | 0.972 | 0.328 | — |
| SMAD9 | 0.956 | 0.091 | — |
| SMAD5 | 0.953 | 0.328 | — |
| SMAD3 | 0.933 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RUNX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14420|pubmed:16299379 |
| STAMBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11483516|imex:IM-16878 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.6 + PDB: 无 | pLDDT=70.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus,  | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SMAD6 — SMAD family member 6，研究基础较多，新颖性有限。
2. 蛋白大小496 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 470 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 470 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43541
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137834-SMAD6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMAD6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43541
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
