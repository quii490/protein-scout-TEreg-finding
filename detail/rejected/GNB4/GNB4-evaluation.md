---
type: protein-evaluation
gene: "GNB4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNB4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB4 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit beta-4 |
| 蛋白大小 | 340 aa / 37.6 kDa |
| UniProt ID | Q9HAV0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 340 aa / 37.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=97.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- lysosomal membrane (GO:0005765)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Charcot-Marie-Tooth Hereditary Neuropathy Overview.. **. PMID: 20301532
2. Guanine nucleotide-binding protein subunit beta-4 promotes gastric cancer progression via activating Erk1/2.. *Acta biochimica et biophysica Sinica*. PMID: 32747927
3. Novel GNB4 Gene Variant and the Spectrum of GNB4 Variants in Patients With Charcot-Marie-Tooth Disease.. *Neurology. Genetics*. PMID: 41164122
4. Helicobacter pylori-induced aberrant demethylation and expression of GNB4 promotes gastric carcinogenesis via the Hippo-YAP1 pathway.. *BMC medicine*. PMID: 37016382
5. Prognostic and Immunological Value of GNB4 in Gastric Cancer by Analyzing TCGA Database.. *Disease markers*. PMID: 35756485

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 97.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=97.2，有序区 99.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF25391 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNG4 | 0.999 | 0.997 | — |
| GNG13 | 0.999 | 0.995 | — |
| GNGT1 | 0.999 | 0.995 | — |
| GNG11 | 0.999 | 0.995 | — |
| GNG5 | 0.999 | 0.995 | — |
| GNG2 | 0.999 | 0.997 | — |
| GNG10 | 0.999 | 0.995 | — |
| GNG7 | 0.999 | 0.995 | — |
| GNGT2 | 0.999 | 0.995 | — |
| GNG12 | 0.999 | 0.995 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| Tnf | psi-mi:"MI:0096"(pull down) | imex:IM-12051|pubmed:17623297 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| MTNR1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17215244|imex:IM-19124 |
| MTNR1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17215244|imex:IM-19124 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Haus4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Mau2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Trim69 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Haus1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 无 | pLDDT=97.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNB4 — Guanine nucleotide-binding protein subunit beta-4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAV0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114450-GNB4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAV0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
