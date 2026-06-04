---
type: protein-evaluation
gene: "KLHDC4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHDC4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KLHDC4 |
| 蛋白大小 | 520 aa |
| UniProt ID | Q8TBB5 (Kelch domain-containing protein 4) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KLHDC4/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KLHDC4/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus(ECO:0000255) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 520 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 10 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT 80.38, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR015915(Kelch-type beta-propeller); IPR052588(Kelch domain-containing protein) |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **146/183** |  |
| **归一化总分** |  |  | **79.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000255) | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |


**结论**: KLHDC4 Nucleus(ECO:0000255)。核定位评分 8/10。

#### 3.2 蛋白大小评估
520 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 10 |
| 搜索策略 | "KLHDC4"[Title/Abstract] |

**评价**: PubMed 10 篇。极度新颖，几乎未被研究。**评分**: 10/10。

**关键文献**:
1. Kim JP et al. (2026). "Genetic architecture of plasma pTau217 and related biomarkers in Alzheimer's disease via genome-wide association studies". *Alzheimers Dement*. PMID: 41804841
2. Xu Y et al. (2024). "Genetic variation mining of the Chinese mitten crab (Eriocheir sinensis) based on transcriptome data from public databases". *Brief Funct Genomics*. PMID: 38984674
3. Chen T et al. (2020). "Systematic analysis of survival-associated alternative splicing signatures in clear cell renal cell carcinoma". *J Cell Biochem*. PMID: 31886566
4. Pyun H et al. (2024). "Functional Annotation and Gene Set Analysis of Gastric Cancer Risk Loci in a Korean Population". *Cancer Res Treat*. PMID: 37340842
5. Lian YF et al. (2016). "Upregulation of KLHDC4 Predicts a Poor Prognosis in Human Nasopharyngeal Carcinoma". *PLoS One*. PMID: 27030985
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 80.38 |
| pLDDT < 50 (无序)  | 20.8% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KLHDC4/KLHDC4-PAE.png]]

**评价**: AlphaFold 高质量预测，pLDDT 80.38。**评分**: 8/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR015915(Kelch-type beta-propeller); IPR052588(Kelch domain-containing protein) |


**染色质调控潜力分析**: IPR015915(Kelch-type beta-propeller); IPR052588(Kelch domain-containing protein)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| CROT | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| CEP76 | psi-mi:"MI:0397"(two hybrid ar | imex:IM-23318|pubmed:25416956 | — | — |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 | — | — |
| AHR | psi-mi:"MI:0007"(anti tag coim | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 | — | — |
| PRPF40A | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | — |
| RAN | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | Yes |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| CROT | 0.623 | — | — |
| ARMC6 | 0.539 | — | — |
| UTP6 | 0.538 | — | — |
| CEBPZ | 0.519 | — | — |
| ZCCHC14 | 0.468 | — | — |
| SHCBP1 | 0.457 | — | — |
| ARMC7 | 0.451 | — | — |
| PRDM15 | 0.450 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

PPI 互证分析**:
- STRING top partner: CROT (score: 0.623)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 80.38 | — |
| 结构域 | InterPro | IPR015915(Kelch-type beta-propeller); IPR052588(Kelch domain-containing protein) | — |
| 定位 | UniProt | Nucleus(ECO:0000255) | — |
| PPI | STRING + IntAct | CROT 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 极度新颖: PubMed 10 篇
2. 高质量 AlphaFold 结构: pLDDT 80.38

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 KLHDC4 的核定位
- [ ] 在 TEreg 相关细胞系中检测 KLHDC4 表达水平
- [ ] 通过 co-IP/MS 鉴定 KLHDC4 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBB5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHDC4%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBB5
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q8TBB5/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[KLHDC4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KLHDC4/KLHDC4-PAE.png]]




