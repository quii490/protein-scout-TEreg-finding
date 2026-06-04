---
type: protein-evaluation
gene: "TTI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTI1 / KIAA0406, SMG10 |
| 蛋白名称 | TELO2-interacting protein 1 homolog |
| 蛋白大小 | 1089 aa / 122.1 kDa |
| UniProt ID | O43156 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1089 aa / 122.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.3; PDB: 7F4U, 7OLE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR052587, IPR057567, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- TORC1 complex (GO:0031931)
- TORC2 complex (GO:0031932)
- TTT Hsp90 cochaperone complex (GO:0110078)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0406, SMG10 |

**关键文献**:
1. Structure of the Human TELO2-TTI1-TTI2 Complex.. *Journal of molecular biology*. PMID: 34838521
2. Bi-allelic TTI1 variants cause an autosomal-recessive neurodevelopmental disorder with microcephaly.. *American journal of human genetics*. PMID: 36724785
3. TTT (Tel2-Tti1-Tti2) Complex, the Co-Chaperone of PIKKs and a Potential Target for Cancer Chemotherapy.. *International journal of molecular sciences*. PMID: 37175973
4. A susceptibility gene signature for ERBB2-driven mammary tumour development and metastasis in collaborative cross mice.. *EBioMedicine*. PMID: 39067134
5. Hippocalcin-Like 1 blunts liver lipid metabolism to suppress tumorigenesis via directly targeting RUVBL1-mTOR signaling.. *Theranostics*. PMID: 36438486

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 43.6% |
| 置信残基 (pLDDT 70-90) 占比 | 39.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 83.0% |
| 可用 PDB 条目 | 7F4U, 7OLE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7F4U, 7OLE）+ AlphaFold高质量预测（pLDDT=81.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR052587, IPR057567, IPR057566; Pfam: PF24176, PF24181, PF24173 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRR5 | 0.999 | 0.000 | — |
| MLST8 | 0.999 | 0.099 | — |
| RICTOR | 0.999 | 0.326 | — |
| MTOR | 0.999 | 0.994 | — |
| TELO2 | 0.999 | 0.995 | — |
| TTI2 | 0.999 | 0.965 | — |
| RPTOR | 0.999 | 0.326 | — |
| MAPKAP1 | 0.997 | 0.000 | — |
| DEPTOR | 0.995 | 0.052 | — |
| AKT1S1 | 0.993 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TTI2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SDO1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ASA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| TEL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSZ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 7F4U, 7OLE | pLDDT=81.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Vesicles; 额外: Nucleoplasm | 一致 |
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
1. TTI1 — TELO2-interacting protein 1 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小1089 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43156
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101407-TTI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43156
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
