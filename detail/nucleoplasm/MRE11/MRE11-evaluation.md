---
type: protein-evaluation
gene: "MRE11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MRE11 — REJECTED (研究热度过高 (PubMed strict=1361，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MRE11 / HNGS1, MRE11A |
| 蛋白名称 | Double-strand break repair protein MRE11 |
| 蛋白大小 | 708 aa / 80.6 kDa |
| UniProt ID | P49959 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 708 aa / 80.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1361 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.4; PDB: 3T1I, 7ZQY, 8BAH, 8K00 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004843, IPR029052, IPR003701, IPR038487, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome; Chromosome, telomere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BRCA1-C complex (GO:0070533)
- chromosomal region (GO:0098687)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Mre11 complex (GO:0030870)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1361 |
| PubMed broad count | 2526 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HNGS1, MRE11A |

**关键文献**:
1. Metabolic regulation of homologous recombination repair by MRE11 lactylation.. *Cell*. PMID: 38128537
2. RNF126-Mediated MRE11 Ubiquitination Activates the DNA Damage Response and Confers Resistance of Triple-Negative Breast Cancer to Radiotherapy.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 36563124
3. MRE11 UFMylation promotes ATM activation.. *Nucleic acids research*. PMID: 30783677
4. NSUN2-mediated R-loop stabilization as a key driver of bladder cancer progression and cisplatin sensitivity.. *Cancer letters*. PMID: 39732321
5. Saikosaponin D Mitigates Radioresistance in Triple-Negative Breast Cancer by Inducing MRE11 De-Lactylation via HIF1α/HDAC5 Pathway.. *Theranostics*. PMID: 40963916

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 47.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 67.5% |
| 可用 PDB 条目 | 3T1I, 7ZQY, 8BAH, 8K00 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3T1I, 7ZQY, 8BAH, 8K00）+ AlphaFold高质量预测（pLDDT=75.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004843, IPR029052, IPR003701, IPR038487, IPR007281; Pfam: PF00149, PF04152 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATM | 0.999 | 0.907 | — |
| BRCA1 | 0.999 | 0.994 | — |
| BARD1 | 0.999 | 0.994 | — |
| RAD50 | 0.999 | 0.998 | — |
| NBN | 0.999 | 0.999 | — |
| BRIP1 | 0.998 | 0.994 | — |
| RBBP8 | 0.997 | 0.855 | — |
| XRCC6 | 0.987 | 0.899 | — |
| EXO1 | 0.985 | 0.878 | — |
| FEN1 | 0.984 | 0.878 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BtbVII | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Msp300 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Usp32 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| danr | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| oc | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Dmel\CG14322 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Ehbp1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| BicDR | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| tou | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| alphaSnap | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 3T1I, 7ZQY, 8BAH, 8K00 | pLDDT=75.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, telomere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MRE11 — Double-strand break repair protein MRE11，研究基础较多，新颖性有限。
2. 蛋白大小708 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1361 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1361 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49959
- Protein Atlas: https://www.proteinatlas.org/ENSG00000020922-MRE11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MRE11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49959
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
