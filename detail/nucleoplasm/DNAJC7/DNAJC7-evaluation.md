---
type: protein-evaluation
gene: "DNAJC7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC7 |
| 蛋白名称 | DnaJ homolog subfamily C member 7 |
| 蛋白大小 | 497 aa / 56.8 kDa |
| UniProt ID | A0A6I8PU73 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC7/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC7/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 497 aa / 56.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 58 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The USP19-DnaJC7 Axis Stabilizes p53 in Cisplatin-Treated Epithelial Ovarian Cancer.. *Cells*. PMID: 42193933
2. Large-scale exome analyses reveal new rare variant contributions in amyotrophic lateral sclerosis.. *Nat Genet*. PMID: 41917433
3. The Hsp40 cochaperone DNAJC7 regulates polyglutamine aggregation and exhibits context-dependent effects on polyglycine aggregation.. *J Biol Chem*. PMID: 41708002
4. Holding but not folding: How a single charge flip uncouples the DNAJC7-Hsp70 relay in amyotrophic lateral sclerosis.. *FEBS J*. PMID: 41728998
5. The ALS-associated E425K mutation uncouples DNAJC7 from the Hsp70 chaperone cycle.. *FEBS J*. PMID: 41531269

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 73.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 8.2% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC7/DNAJC7-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 86.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA4 | 0.000 | 0.000 | — |
| HSP90AA1 | 0.000 | 0.000 | — |
| HSPA8 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSP90AB1 | 0.000 | 0.000 | — |
| TOMM34 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| BAG2 | 0.000 | 0.000 | — |
| BAG5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q99615 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:Q9NRI5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9BUB5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:K7EIH8 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DNAJC7 — DnaJ homolog subfamily C member 7，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小497 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A6I8PU73
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168259-DNAJC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A6I8PU73
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DNAJC7/DNAJC7-PAE.png]]




