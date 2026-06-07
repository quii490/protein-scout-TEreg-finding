---
type: protein-evaluation
gene: "KANSL3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KANSL3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KANSL3 |
| 蛋白大小 | 904 aa |
| UniProt ID | Q9P2N6 (KAT8 regulatory NSL complex subunit 3) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL3/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL3/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus(ECO:0000269); Mitochondrion(ECO:0000269); Spindle pole(ECO:0000269) |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 904 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 14 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 60.12, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR046879(KANL3/Tex30 alpha/beta hydrolase-like); IPR056519(KANSL3 helical domai |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **142/183** |  |
| **归一化总分** |  |  | **77.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000269); Mitochondrion(ECO:0000269); Spindle pole(ECO:0000269) | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。



**结论**: KANSL3 Nucleus(ECO:0000269); Mitochondrion(ECO:0000269); Spindle pole(ECO:0000269)。核定位评分 9/10。

#### 3.2 蛋白大小评估
904 aa。较大蛋白，表达纯化有一定挑战。**评分**: 8/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 14 |
| 搜索策略 | "KANSL3"[Title/Abstract] |

**评价**: PubMed 14 篇。极度新颖，几乎未被研究。**评分**: 10/10。

**关键文献**:
1. Zhang X et al. (2025). "TRAP1 inhibits KANSL3 acetylation to alleviate mitochondrial dysfunction by promoting mitophagy in cardiomyocytes under diabetic conditions". *Cell Commun Signal*. PMID: 41039555
2. Yedier-Bayram O et al. (2022). "EPIKOL, a chromatin-focused CRISPR/Cas9-based screening platform, to identify cancer-specific epigenetic vulnerabilities". *Cell Death Dis*. PMID: 35973998
3. Chander A & Mager J (2024). "Loss of KANSL3 leads to defective inner cell mass and early embryonic lethality". *Mol Reprod Dev*. PMID: 38769918
4. Karoutas A et al. (2019). "The NSL complex maintains nuclear architecture stability via lamin A/C acetylation". *Nat Cell Biol*. PMID: 31576060
5. Sheikh BN et al. (2020). "Neural metabolic imbalance induced by MOF dysfunction triggers pericyte activation and breakdown of vasculature". *Nat Cell Biol*. PMID: 32541879
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 60.12 |
| pLDDT < 50 (无序)  | 48.1% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL3/KANSL3-PAE.png]]

**评价**: AlphaFold 一般质量预测，pLDDT 60.12。**评分**: 6/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR046879(KANL3/Tex30 alpha/beta hydrolase-like); IPR056519(KANSL3 helical domain); IPR029058(Alpha/Beta hydrolase fold) |


**染色质调控潜力分析**: IPR046879(KANL3/Tex30 alpha/beta hydrolase-like); IPR056519(KANSL3 helical domain); IPR029058(Alpha/Beta hydrolase fold)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| ARC70 | psi-mi:"MI:0007"(anti tag coim | pubmed:15175163 | — | Yes |
| RPS27A | psi-mi:"MI:0398"(two hybrid po | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | — | — |
| Kat8 | psi-mi:"MI:0676"(tandem affini | imex:IM-11719|pubmed:20360068 | — | Yes |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coim | pubmed:20362541|imex:IM-16928 | — | Yes |
| PHF20 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | Yes |
| PLEC | psi-mi:"MI:0030"(cross-linking | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| MCRS1 | 0.999 | — | Yes |
| KANSL2 | 0.999 | — | — |
| PHF20 | 0.998 | — | Yes |
| KANSL1 | 0.995 | — | — |
| OGT | 0.991 | — | — |
| WDR5 | 0.987 | — | Yes |
| KAT8 | 0.984 | — | — |
| HCFC1 | 0.964 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

PPI 互证分析**:
- STRING top partner: MCRS1 (score: 0.999)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 60.12 | — |
| 结构域 | InterPro | IPR046879(KANL3/Tex30 alpha/beta hydrolase-like); IPR056519(KANSL3 helical domai | — |
| 定位 | UniProt | Nucleus(ECO:0000269); Mitochondrion(ECO:0000269); Spindle pole(ECO:0000269) | — |
| PPI | STRING + IntAct | MCRS1 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 极度新颖: PubMed 14 篇
2. 一般质量 AlphaFold 结构: pLDDT 60.12

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 KANSL3 的核定位
- [ ] 在 TEreg 相关细胞系中检测 KANSL3 表达水平
- [ ] 通过 co-IP/MS 鉴定 KANSL3 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2N6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KANSL3%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2N6
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9P2N6/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[KANSL3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KANSL3/KANSL3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2N6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR046879;IPR056519;IPR026555; |
| Pfam | PF20408;PF23154; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114982-KANSL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PHF20 | Intact, Biogrid | true |
| FOXK2 | Biogrid | false |
| HCFC1 | Biogrid | false |
| HCFC2 | Biogrid | false |
| KANSL1 | Biogrid | false |
| KANSL2 | Biogrid | false |
| KAT8 | Biogrid | false |
| MCRS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
