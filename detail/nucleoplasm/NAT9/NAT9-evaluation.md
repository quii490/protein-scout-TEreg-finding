---
type: protein-evaluation
gene: "NAT9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAT9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAT9 / EBS |
| 蛋白名称 | Alpha/beta-tubulin-N-acetyltransferase 9 |
| 蛋白大小 | 207 aa / 23.4 kDa |
| UniProt ID | Q9BTE0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 207 aa / 23.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR000182, IPR039135; Pfam: PF13302 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EBS |

**关键文献**:
1. Characterization, expression profile, polymorphism and association of porcine NAT9 gene.. *Molecular biology reports*. PMID: 21688147
2. N-Acetyltransferase 9 Inhibits Porcine Reproductive and Respiratory Syndrome Virus Proliferation by N-Terminal Acetylation of the Structural Protein GP5.. *Microbiology spectrum*. PMID: 36695606
3. The genetics of psoriasis, psoriatic arthritis and atopic dermatitis.. *Human molecular genetics*. PMID: 14996755
4. [Expression of MIER3 in colorectal cancer and bioinformatic analysis of MIER3- interacting proteins].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 28801283
5. Association of single-nucleotide polymorphisms in NAT9 and MAP3K3 genes with litter size traits in Berkshire pigs.. *Archives animal breeding*. PMID: 32175444

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 77.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 96.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR000182, IPR039135; Pfam: PF13302 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CARD14 | 0.807 | 0.000 | — |
| SLC9A3R1 | 0.770 | 0.000 | — |
| MUS81 | 0.765 | 0.000 | — |
| CRYL1 | 0.757 | 0.000 | — |
| ESCO1 | 0.745 | 0.000 | — |
| ESCO2 | 0.744 | 0.000 | — |
| POR | 0.727 | 0.000 | — |
| RPTOR | 0.713 | 0.000 | — |
| FAM20B | 0.699 | 0.000 | — |
| CD300LB | 0.636 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| msl-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mnat9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| babos | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| ENSP00000350467.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ERG28 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LUC7L2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NUDT18 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NAT9 — Alpha/beta-tubulin-N-acetyltransferase 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小207 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTE0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109065-NAT9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAT9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTE0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
