---
type: protein-evaluation
gene: "CFL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CFL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CFL2 |
| 蛋白名称 | Cofilin-2 |
| 蛋白大小 | 166 aa / 18.7 kDa |
| UniProt ID | Q9Y281 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus matrix; Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 166 aa / 18.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.5; PDB: 7M0G, 7U8K |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002108, IPR029006, IPR017904; Pfam: PF00241 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus matrix; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- I band (GO:0031674)
- nuclear matrix (GO:0016363)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 126 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of susceptibility loci for Takayasu arteritis through a large multi-ancestral genome-wide association study.. *American journal of human genetics*. PMID: 33308445
2. Intra-tumor heterogeneity-resistant gene signature predicts prognosis and immune infiltration in breast cancer.. *Frontiers in immunology*. PMID: 41080607
3. SP1-activated CFL2 promotes high glucose-induced retinal pigment epithelial cell injury and involves the AMPK/mTOR pathway.. *Journal of diabetes investigation*. PMID: 40857037
4. CFL2 is an essential mediator for myogenic differentiation in C2C12 myoblasts.. *Biochemical and biophysical research communications*. PMID: 33187645
5. Role of MiR-325-3p in the Regulation of CFL2 and Myogenic Differentiation of C2C12 Myoblasts.. *Cells*. PMID: 34685705

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 49.4% |
| 置信残基 (pLDDT 70-90) 占比 | 47.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 7M0G, 7U8K |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7M0G, 7U8K）+ AlphaFold高质量预测（pLDDT=88.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002108, IPR029006, IPR017904; Pfam: PF00241 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LIMK1 | 0.998 | 0.130 | — |
| WASL | 0.997 | 0.091 | — |
| ACTB | 0.996 | 0.876 | — |
| ACTG1 | 0.996 | 0.854 | — |
| CTTN | 0.996 | 0.221 | — |
| SSH1 | 0.995 | 0.128 | — |
| HCLS1 | 0.995 | 0.071 | — |
| WDR1 | 0.993 | 0.576 | — |
| LIMK2 | 0.990 | 0.130 | — |
| SSH3 | 0.989 | 0.128 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-10201319 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ENSP00000500002.1 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |
| ENSP00000500532.1 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| ACTG1 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| ACTB | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MAB21L2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MOV10 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 7M0G, 7U8K | pLDDT=88.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix; Cytoplasm, cytoskeleton / Plasma membrane; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CFL2 — Cofilin-2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小166 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y281
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165410-CFL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CFL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y281
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
