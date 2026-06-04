---
type: protein-evaluation
gene: "GRK3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GRK3 — REJECTED (研究热度过高 (PubMed strict=228，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRK3 / ADRBK2, BARK2 |
| 蛋白名称 | G protein-coupled receptor kinase 3 |
| 蛋白大小 | 688 aa / 79.7 kDa |
| UniProt ID | P35626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Postsynapse; Presynapse |
| 蛋白大小 | 10/10 | ×1 | 10 | 688 aa / 79.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=228 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000961, IPR000239, IPR011009, IPR011993, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | Postsynapse; Presynapse | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)
- postsynapse (GO:0098794)
- presynapse (GO:0098793)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 228 |
| PubMed broad count | 324 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ADRBK2, BARK2 |

**关键文献**:
1. G Protein-Coupled Receptor Kinase 3 Exacerbates Diabetic Heart Injuries Through Direct Phosphorylation of Cannabinoid Receptor 2 in Humans and Mice.. *Circulation*. PMID: 40772312
2. Cell-based and isoform-selective G protein-coupled receptor kinase assays for comprehensive inhibitor evaluation.. *Communications biology*. PMID: 41545717
3. Signal profiles and spatial regulation of β-arrestin recruitment through Gβ(5) and GRK3 at the μ-opioid receptor.. *European journal of pharmacology*. PMID: 39579957
4. GRK3 as a Prognosis Biomarker in Gastric Cancer.. *Journal of Cancer*. PMID: 35281865
5. GRK3 is a poor prognosticator and serves as a therapeutic target in advanced gastric adenocarcinoma.. *Journal of experimental & clinical cancer research : CR*. PMID: 35996148

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 3.3% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.4，有序区 90.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR000239, IPR011009, IPR011993, IPR001849; Pfam: PF00169, PF00069, PF00615 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARRB2 | 0.965 | 0.046 | — |
| GRK2 | 0.961 | 0.620 | — |
| OPRM1 | 0.936 | 0.097 | — |
| SMO | 0.935 | 0.247 | — |
| ARRB1 | 0.933 | 0.052 | — |
| CSNK1E | 0.923 | 0.000 | — |
| CSNK1G2 | 0.902 | 0.000 | — |
| CSNK1A1L | 0.902 | 0.000 | — |
| CSNK1G3 | 0.902 | 0.000 | — |
| CSNK1D | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| groEL | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| Opn4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-20979|pubmed:22159583 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| GRK2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28706196|doi:10.1038/s4 |
| ENST00000324198 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.4 + PDB: 无 | pLDDT=89.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynapse; Presynapse / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

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
1. GRK3 — G protein-coupled receptor kinase 3，研究基础较多，新颖性有限。
2. 蛋白大小688 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 228 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 228 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100077-GRK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
