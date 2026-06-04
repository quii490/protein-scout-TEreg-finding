---
type: protein-evaluation
gene: "ECPAS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ECPAS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ECPAS / ECM29, KIAA0368 |
| 蛋白名称 | Proteasome adapter and scaffold protein ECM29 |
| 蛋白大小 | 1845 aa / 204.3 kDa |
| UniProt ID | Q5VYK3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Endoplasmic reticulum; Endoplasmic reticulum-Golgi intermedi |
| 蛋白大小 | 5/10 | ×1 | 5 | 1845 aa / 204.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR055444, IPR024372, IPR055 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **145.5/180** | |
| **归一化总分** | | | **80.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Endoplasmic reticulum; Endoplasmic reticulum-Golgi intermediate compartment; Endosome; Cytoplasm, cy... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- early endosome (GO:0005769)
- endocytic vesicle (GO:0030139)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ECM29, KIAA0368 |

**关键文献**:
1. A novel endoplasmic reticulum adaptation is critical for the long-lived Caenorhabditis elegans rpn-10 proteasomal mutant.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 37355092
2. Proteasome-Associated Proteins, PA200 and ECPAS, Are Essential for Murine Spermatogenesis.. *Biomolecules*. PMID: 37189334
3. Whole-exome sequencing identifies ECPAS as a novel potentially pathogenic gene in multiple hereditary families with nonsyndromic orofacial cleft.. *Protein & cell*. PMID: 38695759
4. Combined proteomics and single cell RNA-sequencing analysis to identify biomarkers of disease diagnosis and disease exacerbation for systemic lupus erythematosus.. *Frontiers in immunology*. PMID: 36524113

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 39.4% |
| 置信残基 (pLDDT 70-90) 占比 | 47.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 4.5% |
| 有序区域 (pLDDT>70) 占比 | 87.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.7，有序区 87.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR055444, IPR024372, IPR055443; Pfam: PF23702, PF23731, PF13001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSMD14 | 0.976 | 0.930 | — |
| PSMD12 | 0.956 | 0.892 | — |
| PSMC3 | 0.947 | 0.893 | — |
| PSMD11 | 0.937 | 0.883 | — |
| PSMD8 | 0.936 | 0.847 | — |
| PSMD7 | 0.932 | 0.855 | — |
| PSMD4 | 0.930 | 0.734 | — |
| PSMC2 | 0.921 | 0.905 | — |
| PSMD3 | 0.912 | 0.810 | — |
| PSMC5 | 0.911 | 0.870 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| CLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| serA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2855532 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 5 / 15 = 33%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 33%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 无 | pLDDT=83.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Endoplasmic reticulum-Golgi / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ECPAS — Proteasome adapter and scaffold protein ECM29，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1845 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VYK3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136813-ECPAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ECPAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VYK3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
