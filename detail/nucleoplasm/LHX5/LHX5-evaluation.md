---
type: protein-evaluation
gene: "LHX5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LHX5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LHX5 |
| 蛋白大小 | 402 aa |
| UniProt ID | Q9H2C1 (LIM/homeobox protein Lhx5) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LHX5/IF_images/K-562_1.jpg|K-562]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LHX5/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | Nucleus(ECO:0000305) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 402 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 68 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 67.19, v6 |
| 🧬 调控结构域 | 9/10 | ×2 | 18 | IPR001356(Homeodomain); IPR001781(Zinc finger LIM-type); IPR017970(Homeobox cons |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **114/183** |  |
| **归一化总分** |  |  | **62.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000305) | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |


**结论**: LHX5 Nucleus(ECO:0000305)。核定位评分 8/10。

#### 3.2 蛋白大小评估
402 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 68 |
| 搜索策略 | "LHX5"[Title/Abstract] |

**评价**: PubMed 68 篇。有一定研究，但 niche 空间充足。**评分**: 6/10。

**关键文献**:
1. Rajabli F et al. (2025). "Multi-ancestry genome-wide meta-analysis of 56,241 individuals identifies known and novel cross-population and ancestry-specific associations as novel risk loci for Alzheimer's disease". *Genome Biol*. PMID: 40676597
2. Feng J et al. (2025). "Identification of chromatin remodeling-related gene signature to predict the prognosis in breast cancer". *Clin Exp Med*. PMID: 40317384
3. Sun L et al. (2015). "Conserved Noncoding Sequences Regulate lhx5 Expression in the Zebrafish Forebrain". *PLoS One*. PMID: 26147098
4. Miquelajáuregui A et al. (2010). "LIM-homeobox gene Lhx5 is required for normal development of Cajal-Retzius cells". *J Neurosci*. PMID: 20685998
5. Peng G & Westerfield M (2006). "Lhx5 promotes forebrain development and activates transcription of secreted Wnt antagonists". *Development*. PMID: 16854974
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 67.19 |
| pLDDT < 50 (无序)  | 43.3% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LHX5/LHX5-PAE.png]]

**评价**: AlphaFold 一般质量预测，pLDDT 67.19。**评分**: 6/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR001356(Homeodomain); IPR001781(Zinc finger LIM-type); IPR017970(Homeobox conserved site); IPR049618(Lhx1/5 LIM domain 1); IPR049619(Lhx1/5 LIM domain 2); IPR050453(LIM/homeobox TFs) |


**染色质调控潜力分析**: IPR001356(Homeodomain); IPR001781(Zinc finger LIM-type); IPR017970(Homeobox conserved site); IPR049618(Lhx1/5 LIM domain 1); IPR049619(Lhx1/5 LIM domain 2); IPR050453(LIM/homeobox TFs)。**评分**: 9/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| HTT | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | — |
| PRPF40A | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | — |
| PEX26 | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | — |
| LMO3 | psi-mi:"MI:0397"(two hybrid ar | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | Yes |
| UBQLN1 | psi-mi:"MI:0398"(two hybrid po | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| CCNK | 0.840 | — | — |
| BARHL1 | 0.666 | — | — |
| ZIC1 | 0.621 | — | — |
| DBX1 | 0.599 | — | — |
| LDB1 | 0.591 | — | — |
| PAX2 | 0.582 | — | — |
| LDB2 | 0.552 | — | — |
| FEZF1 | 0.551 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- GO: Nucleus

PPI 互证分析**:
- STRING top partner: CCNK (score: 0.84)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 67.19 | — |
| 结构域 | InterPro | IPR001356(Homeodomain); IPR001781(Zinc finger LIM-type); IPR017970(Homeobox cons | — |
| 定位 | UniProt | Nucleus(ECO:0000305) | — |
| PPI | STRING + IntAct | CCNK 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 较新颖: PubMed 68 篇
2. 一般质量 AlphaFold 结构: pLDDT 67.19

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 LHX5 的核定位
- [ ] 在 TEreg 相关细胞系中检测 LHX5 表达水平
- [ ] 通过 co-IP/MS 鉴定 LHX5 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2C1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LHX5%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2C1
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9H2C1/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[LHX5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LHX5/LHX5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H2C1 |
| SMART | SM00389;SM00132; |
| UniProt Domain [FT] | DOMAIN 3..61; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 62..125; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR001356;IPR017970;IPR009057;IPR049618;IPR049619;IPR050453;IPR001781; |
| Pfam | PF00046;PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000089116-LHX5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASP6 | Intact | false |
| CCK | Intact | false |
| COQ8A | Intact | false |
| FGFR3 | Intact | false |
| GRIN2C | Intact | false |
| GSN | Intact | false |
| HIP1 | Intact | false |
| HTT | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
