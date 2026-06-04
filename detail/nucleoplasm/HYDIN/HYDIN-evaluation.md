---
type: protein-evaluation
gene: "HYDIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HYDIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HYDIN / HYDIN1, KIAA1864 |
| 蛋白名称 | Hydrocephalus-inducing protein homolog |
| 蛋白大小 | 5121 aa / 575.9 kDa |
| UniProt ID | Q4G0P3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytokinetic bridge, Primary cilium, Cytosol, Equatorial segm; UniProt: Cell projection, cilium; Cytoplasm, cytoskeleton, cilium axo |
| 蛋白大小 | 0/10 | ×1 | 0 | 5121 aa / 575.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.5; PDB: 2E6J, 2YS4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033305, IPR033768, IPR053879, IPR013783, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytokinetic bridge, Primary cilium, Cytosol, Equatorial segment; 额外: Nucleoplasm, Mitotic spindle | Approved |
| UniProt | Cell projection, cilium; Cytoplasm, cytoskeleton, cilium axoneme; Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axonemal central apparatus (GO:1990716)
- axonemal central pair projection (GO:1990718)
- axoneme (GO:0005930)
- cilium (GO:0005929)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 115 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HYDIN1, KIAA1864 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. Hydin as the Candidate Master Sex Determination Gene in Channel Catfish (Ictalurus punctatus) and Its Epigenetic Regulation.. *Marine biotechnology (New York, N.Y.)*. PMID: 39579181
3. Characterization of pathogenic genetic variants in Russian patients with primary ciliary dyskinesia using gene panel sequencing and transcript analysis.. *Orphanet journal of rare diseases*. PMID: 39180133
4. SPEF2- and HYDIN-Mutant Cilia Lack the Central Pair-associated Protein SPEF2, Aiding Primary Ciliary Dyskinesia Diagnostics.. *American journal of respiratory cell and molecular biology*. PMID: 31545650
5. HYDIN mutation status as a potential predictor of immune checkpoint inhibitor efficacy in melanoma.. *Aging*. PMID: 37595251

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.5 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 2E6J, 2YS4 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2E6J, 2YS4）+ AlphaFold高质量预测（pLDDT=84.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033305, IPR033768, IPR053879, IPR013783, IPR027417; Pfam: PF17213, PF22544 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPRIN2 | 0.914 | 0.000 | — |
| SRGAP2 | 0.883 | 0.091 | — |
| SRGAP3 | 0.875 | 0.091 | — |
| NBPF1 | 0.861 | 0.000 | — |
| DRD5 | 0.833 | 0.049 | — |
| NPEPPS | 0.829 | 0.045 | — |
| UGT2B17 | 0.827 | 0.045 | — |
| RSPH4A | 0.802 | 0.045 | — |
| GTF2I | 0.797 | 0.000 | — |
| CCDC40 | 0.776 | 0.107 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PEF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.5 + PDB: 2E6J, 2YS4 | pLDDT=84.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm, cytoskeleton,  / Cytokinetic bridge, Primary cilium, Cytosol, Equat | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. HYDIN — Hydrocephalus-inducing protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小5121 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4G0P3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157423-HYDIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HYDIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4G0P3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
