---
type: protein-evaluation
gene: "LRWD1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRWD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LRWD1 |
| 蛋白大小 | 647 aa |
| UniProt ID | Q9UFC0 (Leucine-rich repeat and WD repeat-containing protein 1) |
| 子定位分类 | chromatin |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/LRWD1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/LRWD1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36 | Nucleus(ECO:0000269); Centromere; Telomere; Centrosome; Kinetochore |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 647 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 32 篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT 83.44, v6 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | IPR001611(Leucine-rich repeat); IPR001680(WD40 repeat); IPR003591(LRR typical su |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 |见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **142/183** |  |
| **归一化总分** |  |  | **77.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus(ECO:0000269); Centromere; Telomere; Centrosome; Kinetochore | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。



**结论**: LRWD1 Nucleus(ECO:0000269); Centromere; Telomere; Centrosome; Kinetochore。核定位评分 9/10。

#### 3.2 蛋白大小评估
647 aa。适合生化实验和结构解析。**评分**: 10/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 32 |
| 搜索策略 | "LRWD1"[Title/Abstract] |


**已知复合体成员** (GO Cellular Component):
- （待补充：通过 GO 数据库查询该蛋白所属的已知复合体）
**关键文献**:
1. Samare-Najaf et al. (2023). "The constructive and destructive impact of autophagy on both genders' reproducibility, a comprehensive review.". *Autophagy*. PMID: 37505071
2. Kang et al. (2022). "Lrwd1 impacts cell proliferation and the silencing of repetitive DNA elements.". *Genesis*. PMID: 35451548
3. Chan et al. (2012). "Leucine-rich repeat and WD repeat-containing protein 1 is recruited to pericentric heterochromatin by trimethylated lysine 9 of histone H3 and maintains heterochromatin silencing.". *J Biol Chem*. PMID: 22427655
4. Luo et al. (2025). "Germline-specific deletion of testis-highly expressed Lrwd1 reveals nonessential roles in male fertility.". *Theriogenology*. PMID: 40203731
5. Teng et al. (2010). "Expression of lrwd1 in mouse testis and its centrosomal localization.". *Int J Androl*. PMID: 20180869
**评价**: PubMed 32 篇。非常新颖，少数基础研究。**评分**: 8/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 83.44 |
| pLDDT < 50 (无序)  | 9.9% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/LRWD1/LRWD1-PAE.png]]

**评价**: AlphaFold 高质量预测，pLDDT 83.44。**评分**: 8/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR001611(Leucine-rich repeat); IPR001680(WD40 repeat); IPR003591(LRR typical subtype); IPR019775(WD40 repeat conserved site); IPR052489(LRWD1 family) |


**染色质调控潜力分析**: IPR001611(Leucine-rich repeat); IPR001680(WD40 repeat); IPR003591(LRR typical subtype); IPR019775(WD40 repeat conserved site); IPR052489(LRWD1 family)。**评分**: 8/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| H3FA | psi-mi:"MI:1314"(proximity-dep | pubmed:29568061|imex:IM-26301 | — | Yes |
| ESR1 | psi-mi:"MI:0676"(tandem affini | pubmed:31527615|imex:IM-26954 | — | Yes |
| MAPK13 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008|pubmed:31585087|imex:IM-27423 | — | — |
| ORC6 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| DNAJC7 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | Yes |
| STN1 | psi-mi:"MI:0007"(anti tag coim | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| ORC3 | 0.995 | — | Yes |
| ORC5 | 0.994 | — | Yes |
| ORC2 | 0.993 | — | Yes |
| ORC4 | 0.987 | — | Yes |
| ORC1 | 0.974 | — | Yes |
| ORC6 | 0.964 | — | Yes |
| REPIN1 | 0.746 | — | — |
| CDT1 | 0.734 | — | — |

**PPI 互证分析**:
- STRING top partner: ORC3 (score: 0.995)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | tandem affinity purification | 20360068 |
| — | proximity-dependent biotin identification | 29568061 |
| — | tandem affinity purification | 31527615 |
| — | tandem affinity purification | 31527615 |
| — | pull down | 31585087 |
| — | anti tag coimmunoprecipitation | 28514442 |
| — | anti tag coimmunoprecipitation | 28514442 |
| — | anti tag coimmunoprecipitation | 28514442 |
| — | anti tag coimmunoprecipitation | 28514442 |
| — | anti tag coimmunoprecipitation | 28514442 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| ORC3 | 0.995 |
| ORC5 | 0.994 |
| ORC2 | 0.993 |
| ORC4 | 0.987 |
| ORC1 | 0.974 |
| ORC6 | 0.964 |
| REPIN1 | 0.746 |
| CDT1 | 0.734 |
| OBI1 | 0.679 |
| TICRR | 0.619 |

**GO-CC 复合体/定位核查**:
- GO:0005813: centrosome (IEA:UniProtKB-SubCell)
- GO:0000781: chromosome, telomeric region (IDA:GO_Central)
- GO:0000776: kinetochore (IDA:UniProtKB)
- GO:0005664: nuclear origin of replication recognition complex (IDA:UniProtKB)
- GO:0005730: nucleolus (IDA:HPA)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)
- GO:0005721: pericentric heterochromatin (IDA:UniProtKB)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 83.44 | — |
| 结构域 | InterPro | IPR001611(Leucine-rich repeat); IPR001680(WD40 repeat); IPR003591(LRR typical su | — |
| 定位 | UniProt | Nucleus(ECO:0000269); Centromere; Telomere; Centrosome; Kinetochore | — |
| PPI | STRING + IntAct | ORC3 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 较新颖: PubMed 32 篇
2. 高质量 AlphaFold 结构: pLDDT 83.44

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 LRWD1 的核定位
- [ ] 在 TEreg 相关细胞系中检测 LRWD1 表达水平
- [ ] 通过 co-IP/MS 鉴定 LRWD1 的染色质调控相关互作伙伴

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UFC0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRWD1%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UFC0
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9UFC0/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

![[LRWD1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/LRWD1/LRWD1-PAE.png]]


