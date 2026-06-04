---
type: protein-evaluation
gene: "KCTD13"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD13 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCTD13 |
| 蛋白大小 | 329 aa |
| UniProt ID | Q8WZ19 (BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 1) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KCTD13/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KCTD13/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus(ECO:0000269) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 329 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 37 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT 78.75, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR000210(BTB/POZ domain); IPR003131(K+ channel tetramerisation BTB); IPR045068( |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000269) | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |


**结论**: KCTD13 Nucleus(ECO:0000269)。核定位评分 9/10。

#### 3.2 蛋白大小评估
329 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 37 |
| 搜索策略 | "KCTD13"[Title/Abstract] |

**评价**: PubMed 37 篇。非常新颖，少数基础研究。**评分**: 8/10。

**关键文献**:
1. Gu J et al. (2023). "KCTD13-mediated ubiquitination and degradation of GluN1 regulates excitatory synaptic transmission and seizure susceptibility". *Cell Death Differ*. PMID: 37142655
2. Taniue K et al. (2024). "The MTR4/hnRNPK complex surveils aberrant polyadenylated RNAs with multiple exons". *Nat Commun*. PMID: 39419981
3. Cheng J et al. (2024). "KCTD10 regulates brain development by destabilizing brain disorder-associated protein KCTD13". *Proc Natl Acad Sci U S A*. PMID: 38489388
4. Teng X et al. (2019). "KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders". *CNS Neurosci Ther*. PMID: 31197948
5. Escamilla CO et al. (2017). "Kctd13 deletion reduces synaptic transmission via increased RhoA". *Nature*. PMID: 29088697
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 78.75 |
| pLDDT < 50 (无序)  | 21.3% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KCTD13/KCTD13-PAE.png]]

**评价**: AlphaFold 中等质量预测，pLDDT 78.75。**评分**: 7/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR000210(BTB/POZ domain); IPR003131(K+ channel tetramerisation BTB); IPR045068(BTB/POZ adapter CUL3-RhoA) |


**染色质调控潜力分析**: IPR000210(BTB/POZ domain); IPR003131(K+ channel tetramerisation BTB); IPR045068(BTB/POZ adapter CUL3-RhoA)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| KAT7 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | Yes |
| NUDT18 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | — |
| VTA1 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | — |
| ZMYND19 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | Yes |
| LNX1 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | — |
| ARMC7 | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| CUL3 | 0.996 | — | Yes |
| UBXN7 | 0.995 | — | — |
| FAF1 | 0.994 | — | — |
| TNFAIP1 | 0.989 | — | — |
| KCTD10 | 0.979 | — | — |
| KCTD17 | 0.934 | — | — |
| KLHL22 | 0.920 | — | — |
| KLHL20 | 0.919 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- GO: Nucleus

PPI 互证分析**:
- STRING top partner: CUL3 (score: 0.996)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 78.75 | — |
| 结构域 | InterPro | IPR000210(BTB/POZ domain); IPR003131(K+ channel tetramerisation BTB); IPR045068( | — |
| 定位 | UniProt | Nucleus(ECO:0000269) | — |
| PPI | STRING + IntAct | CUL3 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 较新颖: PubMed 37 篇
2. 中等质量 AlphaFold 结构: pLDDT 78.75

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 KCTD13 的核定位
- [ ] 在 TEreg 相关细胞系中检测 KCTD13 表达水平
- [ ] 通过 co-IP/MS 鉴定 KCTD13 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WZ19
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD13%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WZ19
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q8WZ19/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[KCTD13-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/KCTD13/KCTD13-PAE.png]]




