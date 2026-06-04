---
type: protein-evaluation
gene: "GNB5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNB5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB5 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit beta-5 |
| 蛋白大小 | 395 aa / 43.6 kDa |
| UniProt ID | O14775 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Centrosome, Rods & Rings; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 43.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.0; PDB: 7EWP, 7EWR, 8SG8, 8SG9, 8SGC, 8SGL, 8SH9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Centrosome, Rods & Rings | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell tip (GO:0051286)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- GTPase activator complex (GO:1902773)
- heterotrimeric G-protein complex (GO:0005834)
- nucleus (GO:0005634)
- parallel fiber to Purkinje cell synapse (GO:0098688)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 161 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GNB5-Related Neurodevelopmental Disorder.. **. PMID: 34436834
2. Gnb5 is a negative regulator of the BACE1-mediated Aβ generation and ameliorates cognitive deficits in a mouse model of Alzheimer's disease.. *PLoS biology*. PMID: 40587559
3. Gene mutations in comorbidity of epilepsy and arrhythmia.. *Journal of neurology*. PMID: 36376730
4. Inhibition of G-protein signalling in cardiac dysfunction of intellectual developmental disorder with cardiac arrhythmia (IDDCA) syndrome.. *Journal of medical genetics*. PMID: 33172956
5. The epileptology of GNB5 encephalopathy.. *Epilepsia*. PMID: 31631344

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 96.7% |
| 可用 PDB 条目 | 7EWP, 7EWR, 8SG8, 8SG9, 8SGC, 8SGL, 8SH9, 8SHA, 8SHD, 8SHE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7EWP, 7EWR, 8SG8, 8SG9, 8SGC, 8SGL, 8SH9, 8SHA, 8SHD, 8SHE）+ AlphaFold极高置信度预测（pLDDT=94.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF25391 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RGS11 | 0.999 | 0.725 | — |
| GNG7 | 0.999 | 0.995 | — |
| GNG2 | 0.999 | 0.996 | — |
| RGS9BP | 0.999 | 0.000 | — |
| RGS6 | 0.999 | 0.788 | — |
| RGS7 | 0.999 | 0.999 | — |
| RGS9 | 0.999 | 0.908 | — |
| GNG4 | 0.999 | 0.996 | — |
| PDCL | 0.998 | 0.994 | — |
| GNG5 | 0.998 | 0.995 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| OLFM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PSD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MVD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF3J | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NR6A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| E2F2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PSMD4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RPA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Mtap | psi-mi:"MI:0397"(two hybrid array) | pubmed:16603075|imex:IM-19959 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.0 + PDB: 7EWP, 7EWR, 8SG8, 8SG9, 8SGC,  | pLDDT=94.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nuclear speckles; 额外: Centrosome, Rods & Rings | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GNB5 — Guanine nucleotide-binding protein subunit beta-5，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14775
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069966-GNB5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14775
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
