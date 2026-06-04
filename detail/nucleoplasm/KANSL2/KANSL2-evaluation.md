---
type: protein-evaluation
gene: "KANSL2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KANSL2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KANSL2 |
| 蛋白大小 | 492 aa |
| UniProt ID | Q9H9L4 (KAT8 regulatory NSL complex subunit 2) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus(ECO:0000269); Mitochondrion(ECO:0000250) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 492 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 65.81, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR025927(KANL2-like zinc-finger domain); IPR026316(KAT8 regulatory NSL complex |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **144/183** |  |
| **归一化总分** |  |  | **78.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000269); Mitochondrion(ECO:0000250) | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。



**结论**: KANSL2 Nucleus(ECO:0000269); Mitochondrion(ECO:0000250)。核定位评分 9/10。

#### 3.2 蛋白大小评估
492 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 15 |
| 搜索策略 | "KANSL2"[Title/Abstract] |

**评价**: PubMed 15 篇。极度新颖，几乎未被研究。**评分**: 10/10。

**关键文献**:
1. Georgieva AM et al. (2025). "Regulation of NSL by TAF4A is critical for genome stability and quiescence of muscle stem cells". *Nat Commun*. PMID: 41028714
2. Jiang K et al. (2025). "The histone modifier KANSL2 is an actionable biomarker in multiple myeloma". *Mol Cancer Ther*. PMID: 41294048
3. Li Z et al. (2023). "Comprehensive synergy mapping links a BAF- and NSL-containing "supercomplex" to the transcriptional silencing of HIV-1". *Cell Rep*. PMID: 37682714
4. Ferreyra Solari NE et al. (2016). "The NSL Chromatin-Modifying Complex Subunit KANSL2 Regulates Cancer Stem-like Properties in Glioblastoma That Contribute to Tumorigenesis". *Cancer Res*. PMID: 27406830
5. Karoutas A et al. (2019). "The NSL complex maintains nuclear architecture stability via lamin A/C acetylation". *Nat Cell Biol*. PMID: 31576060
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 65.81 |
| pLDDT < 50 (无序)  | 33.1% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL2/KANSL2-PAE.png]]

**评价**: AlphaFold 一般质量预测，pLDDT 65.81。**评分**: 6/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR025927(KANL2-like zinc-finger domain); IPR026316(KAT8 regulatory NSL complex subunit 2) |


**染色质调控潜力分析**: IPR025927(KANL2-like zinc-finger domain); IPR026316(KAT8 regulatory NSL complex subunit 2)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| Kat8 | psi-mi:"MI:0676"(tandem affini | imex:IM-11719|pubmed:20360068 | — | Yes |
| NECAB1 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| PHF20 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | Yes |
| TNIK | psi-mi:"MI:0399"(two hybrid fr | pubmed:31413325|imex:IM-26801 | — | — |
| CEP63 | psi-mi:"MI:0399"(two hybrid fr | pubmed:31413325|imex:IM-26801 | — | — |
| CDC5L | psi-mi:"MI:0399"(two hybrid fr | pubmed:31413325|imex:IM-26801 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| WDR5 | 0.999 | — | Yes |
| KANSL3 | 0.999 | — | — |
| KANSL1 | 0.999 | — | — |
| MCRS1 | 0.999 | — | Yes |
| PHF20 | 0.998 | — | Yes |
| OGT | 0.978 | — | — |
| KAT8 | 0.967 | — | — |
| HCFC1 | 0.954 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- GO: Mitochondrion, Nucleus

PPI 互证分析**:
- STRING top partner: WDR5 (score: 0.999)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 65.81 | — |
| 结构域 | InterPro | IPR025927(KANL2-like zinc-finger domain); IPR026316(KAT8 regulatory NSL complex  | — |
| 定位 | UniProt | Nucleus(ECO:0000269); Mitochondrion(ECO:0000250) | — |
| PPI | STRING + IntAct | WDR5 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 极度新颖: PubMed 15 篇
2. 一般质量 AlphaFold 结构: pLDDT 65.81

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 KANSL2 的核定位
- [ ] 在 TEreg 相关细胞系中检测 KANSL2 表达水平
- [ ] 通过 co-IP/MS 鉴定 KANSL2 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9L4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KANSL2%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9L4
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9H9L4/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[KANSL2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL2/KANSL2-PAE.png]]


