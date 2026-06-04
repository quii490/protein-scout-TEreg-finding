---
type: protein-evaluation
gene: "POR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## POR — REJECTED (研究热度过高 (PubMed strict=942，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POR / CYPOR |
| 蛋白名称 | NADPH--cytochrome P450 reductase |
| 蛋白大小 | 677 aa / 76.7 kDa |
| UniProt ID | P16435 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 677 aa / 76.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=942 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.0; PDB: 1B1C, 3FJO, 3QE2, 3QFC, 3QFR, 3QFS, 3QFT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- intracellular membrane-bounded organelle (GO:0043231)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 942 |
| PubMed broad count | 56891 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CYPOR |

**关键文献**:
1. Pharmacogenomics of human P450 oxidoreductase.. *Frontiers in pharmacology*. PMID: 24847272
2. Identification of functional circuitry between retrosplenial and postrhinal cortices during fear conditioning.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 22933791
3. Genetics of congenital adrenal hyperplasia.. *Best practice & research. Clinical endocrinology & metabolism*. PMID: 19500762
4. Steroid 17-hydroxylase and 17,20-lyase deficiencies, genetic and pharmacologic.. *The Journal of steroid biochemistry and molecular biology*. PMID: 26862015
5. Is Cell-Free DNA Testing in Hepatocellular Carcinoma Ready for Prime Time?. *International journal of molecular sciences*. PMID: 37762533

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 80.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 91.8% |
| 可用 PDB 条目 | 1B1C, 3FJO, 3QE2, 3QFC, 3QFR, 3QFS, 3QFT, 5EMN, 5FA6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1B1C, 3FJO, 3QE2, 3QFC, 3QFR, 3QFS, 3QFT, 5EMN, 5FA6）+ AlphaFold极高置信度预测（pLDDT=91.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001709; Pfam: PF00667, PF00258, PF00175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYB5A | 0.997 | 0.099 | — |
| CYB5B | 0.997 | 0.099 | — |
| CYP3A4 | 0.992 | 0.294 | — |
| HMOX1 | 0.965 | 0.797 | — |
| CYP51A1 | 0.960 | 0.087 | — |
| CYP3A5 | 0.953 | 0.045 | — |
| CYP4F3 | 0.951 | 0.045 | — |
| CYP3A7 | 0.945 | 0.045 | — |
| PPIG | 0.944 | 0.071 | — |
| CYP4F2 | 0.940 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pla2g4a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Dmel\CG33523 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| XRCC6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Cyp4p2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| pip | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| STAT1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| zntC | psi-mi:"MI:0018"(two hybrid) | pubmed:18000013 |
| CYP2C2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-17497|pubmed:21081644 |
| PGRMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17497|pubmed:21081644 |
| wg | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 1B1C, 3FJO, 3QE2, 3QFC, 3QFR,  | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Vesicles; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. POR — NADPH--cytochrome P450 reductase，研究基础较多，新颖性有限。
2. 蛋白大小677 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 942 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 942 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16435
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127948-POR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16435
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
