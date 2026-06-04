---
type: protein-evaluation
gene: "PITPNA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PITPNA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PITPNA / PITPN |
| 蛋白名称 | Phosphatidylinositol transfer protein alpha isoform |
| 蛋白大小 | 270 aa / 31.8 kDa |
| UniProt ID | Q00169 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 270 aa / 31.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.4; PDB: 1UW5, 8PQO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001666, IPR055261, IPR023393; Pfam: PF02121 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PITPN |

**关键文献**:
1. Establishment of mouse line showing inducible priapism-like phenotypes.. *Reproductive medicine and biology*. PMID: 35765371
2. Restoration of PITPNA in Type 2 diabetic human islets reverses pancreatic beta-cell dysfunction.. *Nature communications*. PMID: 37460527
3. PITPNA-AS1 Inhibits Cell Proliferation and Migration in Ovarian Cancer by Regulating the MIR-223-3p/RHOB Axis.. *Revista de investigacion clinica; organo del Hospital de Enfermedades de la Nutricion*. PMID: 38753591
4. Repression of phosphatidylinositol transfer protein α ameliorates the pathology of Duchenne muscular dystrophy.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 28533404
5. LncRNA PITPNA-AS1/miR-223-3p/PTN axis regulates malignant progression and stemness in lung squamous cell carcinoma.. *Journal of clinical laboratory analysis*. PMID: 35588441

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.4 |
| 高置信度残基 (pLDDT>90) 占比 | 90.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 1UW5, 8PQO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1UW5, 8PQO）+ AlphaFold高质量预测（pLDDT=95.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001666, IPR055261, IPR023393; Pfam: PF02121 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PITPNM3 | 0.934 | 0.000 | — |
| YWHAE | 0.901 | 0.000 | — |
| PAFAH1B1 | 0.890 | 0.000 | — |
| SCARF1 | 0.858 | 0.000 | — |
| BHLHA9 | 0.834 | 0.000 | — |
| TRARG1 | 0.817 | 0.046 | — |
| CRK | 0.798 | 0.000 | — |
| TIMM22 | 0.768 | 0.000 | — |
| STAT4 | 0.750 | 0.000 | — |
| NTN1 | 0.700 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSDL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MORF4L2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MLKL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PMVK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| SIRT3 | psi-mi:"MI:0096"(pull down) | imex:IM-12078|pubmed:19343720 |
| GTF2F2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| S1PR4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.4 + PDB: 1UW5, 8PQO | pLDDT=95.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Vesicles | 一致 |
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
1. PITPNA — Phosphatidylinositol transfer protein alpha isoform，非常新颖，仅有少数基础研究。
2. 蛋白大小270 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q00169
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174238-PITPNA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PITPNA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q00169
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
