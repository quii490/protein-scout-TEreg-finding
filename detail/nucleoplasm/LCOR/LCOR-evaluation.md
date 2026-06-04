---
type: protein-evaluation
gene: "LCOR"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LCOR 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LCOR |
| 蛋白大小 | 433 aa |
| UniProt ID | Q96JN0 (Ligand-dependent corepressor) |
| 子定位分类 | nucleoplasm |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LCOR/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LCOR/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus(ECO:0000255, ECO:0000269) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 433 aa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed 83 篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT 55.31, v6 |
| 🧬 调控结构域 | 9/10 | ×2 | 18 | IPR007889(DNA-binding HTH Psq-type); IPR009057(Homeodomain-like superfamily) |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 | 见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **105/183** |  |
| **归一化总分** |  |  | **57.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000255, ECO:0000269) | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |


**结论**: LCOR Nucleus(ECO:0000255, ECO:0000269)。核定位评分 9/10。

#### 3.2 蛋白大小评估
433 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 83 |
| 搜索策略 | "LCOR"[Title/Abstract] |

**评价**: PubMed 83 篇。有一定研究，但 niche 空间充足。**评分**: 6/10。

**关键文献**:
1. Sugimura R et al. (2017). "Haematopoietic stem and progenitor cells from human pluripotent stem cells". *Nature*. PMID: 28514439
2. Pérez-Núñez I et al. (2022). "LCOR mediates interferon-independent tumor immunogenicity and responsiveness to immune-checkpoint blockade in triple-negative breast cancer". *Nat Cancer*. PMID: 35301507
3. Selinger M et al. (2022). "Integrative RNA profiling of TBEV-infected neurons and astrocytes reveals potential pathogenic effectors". *Comput Struct Biotechnol J*. PMID: 35685361
4. Palomeque JÁ et al. (2026). "Estrogen receptor signaling drives immune evasion and immunotherapy resistance in HR+ breast cancer". *J Clin Invest*. PMID: 41289011
5. Li W et al. (2025). "Identification of the LCOR-PLCL1 pathway that restrains lipid accumulation and tumor progression in clear cell renal cell carcinoma". *Int J Biol Sci*. PMID: 40083699
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 55.31 |
| pLDDT < 50 (无序)  | 52.7% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LCOR/LCOR-PAE.png]]

**评价**: AlphaFold 较低质量预测，pLDDT 55.31。**评分**: 5/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR007889(DNA-binding HTH Psq-type); IPR009057(Homeodomain-like superfamily) |


**染色质调控潜力分析**: IPR007889(DNA-binding HTH Psq-type); IPR009057(Homeodomain-like superfamily)。**评分**: 9/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| KMT1C | psi-mi:"MI:0398"(two hybrid po | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | — | Yes |
| CTBP2 | psi-mi:"MI:0397"(two hybrid ar | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 | — | — |
| RORB | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | — | — |
| TRAF1 | psi-mi:"MI:1356"(validated two | pubmed:32296183|imex:IM-25472 | — | — |
| CHET9 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | Yes |
| CTBP1 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| CTBP1 | 0.980 | — | Yes |
| MTF2 | 0.949 | — | — |
| PHF1 | 0.900 | — | Yes |
| EZH2 | 0.900 | — | — |
| CTBP2 | 0.869 | — | Yes |
| ESR1 | 0.866 | — | — |
| SUZ12 | 0.852 | — | — |
| PHF19 | 0.843 | — | Yes |

**
**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

PPI 互证分析**:
- STRING top partner: CTBP1 (score: 0.98)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 55.31 | — |
| 结构域 | InterPro | IPR007889(DNA-binding HTH Psq-type); IPR009057(Homeodomain-like superfamily) | — |
| 定位 | UniProt | Nucleus(ECO:0000255, ECO:0000269) | — |
| PPI | STRING + IntAct | CTBP1 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 较新颖: PubMed 83 篇
2. 较低质量 AlphaFold 结构: pLDDT 55.31

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 LCOR 的核定位
- [ ] 在 TEreg 相关细胞系中检测 LCOR 表达水平
- [ ] 通过 co-IP/MS 鉴定 LCOR 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JN0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LCOR%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JN0
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q96JN0/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[LCOR-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/LCOR/LCOR-PAE.png]]




