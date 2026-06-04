---
type: protein-evaluation
gene: "LEMD2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LEMD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LEMD2 |
| 蛋白大小 | 503 aa |
| UniProt ID | Q8NC56 (LEM domain-containing protein 2) |
| 子定位分类 | nuclear-envelope |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/LEMD2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/LEMD2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus inner membrane(ECO:0000269); Nuclear envelope; Spindle(ECO:0000269) |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 503 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 46 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 60.0, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR003887(LEM domain); IPR018996(Man1/Src1-like C-terminal); IPR041885(MAN1 wing |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 |见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus inner membrane(ECO:0000269); Nuclear envelope; Spindle(ECO:0000269) | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。



**结论**: LEMD2 Nucleus inner membrane(ECO:0000269); Nuclear envelope; Spindle(ECO:0000269)。核定位评分 9/10。

#### 3.2 蛋白大小评估
503 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 46 |
| 搜索策略 | "LEMD2"[Title/Abstract] |

**关键文献**:
1. Di et al. (2024). "Micronuclear collapse from oxidative damage.". *Science*. PMID: 39208110
2. Chen et al. (2023). "Mechanistic Insights of the LEMD2 p.L13R Mutation and Its Role in Cardiomyopathy.". *Circ Res*. PMID: 36656972
3. Timmer et al. (2025). "LRRC59 cooperates with nuclear transporters to restrain the nuclear envelope repair machinery and safeguard genome integrity.". *Nat Commun*. PMID: 41387506
4. Vargas et al. (2023). "The Role of the LEMD2 p.L13R Mutation in Dilated Cardiomyopathy.". *Circ Res*. PMID: 36656966
5. He et al. (2022). "Collective analysis of the expression and prognosis for LEM-domain proteins in prostate cancer.". *World J Surg Oncol*. PMID: 35650630
**评价**: PubMed 46 篇。非常新颖，少数基础研究。**评分**: 8/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 60.0 |
| pLDDT < 50 (无序)  | 50.0% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/LEMD2/LEMD2-PAE.png]]

**评价**: AlphaFold 一般质量预测，pLDDT 60.0。**评分**: 6/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR003887(LEM domain); IPR018996(Man1/Src1-like C-terminal); IPR041885(MAN1 winged-helix); IPR052277(Inner Nuclear Membrane ESCRT-Associated Protein) |


**染色质调控潜力分析**: IPR003887(LEM domain); IPR018996(Man1/Src1-like C-terminal); IPR041885(MAN1 winged-helix); IPR052277(Inner Nuclear Membrane ESCRT-Associated Protein)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| CHRNB3 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| SGSM3 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| LMNA | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 | — | — |
| IRF2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 | — | — |
| SH2D3C | psi-mi:"MI:0007"(anti tag coim | pubmed:31980649|imex:IM-26434 | — | — |
| SSBP3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 | — | Yes |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| CHMP7 | 0.996 | — | Yes |
| IST1 | 0.901 | — | — |
| BANF1 | 0.901 | — | Yes |
| EMD | 0.900 | — | — |
| BANF2 | 0.848 | — | Yes |
| ANKLE2 | 0.839 | — | — |
| LMNA | 0.834 | — | — |
| FZR1 | 0.792 | — | — |

**
**已知复合体成员** (GO Cellular Component):
- （待补充：通过 GO 数据库查询该蛋白所属的已知复合体）
PPI 互证分析**:
- STRING top partner: CHMP7 (score: 0.996)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10


#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 60.0 | — |
| 结构域 | InterPro | IPR003887(LEM domain); IPR018996(Man1/Src1-like C-terminal); IPR041885(MAN1 wing | — |
| 定位 | UniProt | Nucleus inner membrane(ECO:0000269); Nuclear envelope; Spindle(ECO:0000269) | — |
| PPI | STRING + IntAct | CHMP7 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 较新颖: PubMed 46 篇
2. 一般质量 AlphaFold 结构: pLDDT 60.0

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 LEMD2 的核定位
- [ ] 在 TEreg 相关细胞系中检测 LEMD2 表达水平
- [ ] 通过 co-IP/MS 鉴定 LEMD2 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NC56
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LEMD2%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NC56
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q8NC56/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[LEMD2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/LEMD2/LEMD2-PAE.png]]


