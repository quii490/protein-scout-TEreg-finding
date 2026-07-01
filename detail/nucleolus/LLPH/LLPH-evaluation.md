---
type: protein-evaluation
gene: "LLPH"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LLPH 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LLPH |
| 蛋白名称 | Protein LLP homolog |
| 蛋白大小 | 129 aa |
| UniProt ID | Q9BRT6 (Protein LLP homolog) |
| 子定位分类 | nucleolus |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/LLPH/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/LLPH/IF_images/RT-4_1.jpg|RT-4]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 10/10 | ×4 | 40 | Nucleus, nucleolus(ECO:0000250); Chromosome(ECO:0000269) |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 129 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 16 篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT 74.44, v6 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | IPR018784(LLP homolog-like) |
| 🔗 PPI 网络 | 5/10 | ×3 | 15 |见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 多源数据互证 |
| **原始总分** |  |  | **149/183** |  |
| **归一化总分** |  |  | **81.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus, nucleolus(ECO:0000250); Chromosome(ECO:0000269) | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。



**结论**: LLPH Nucleus, nucleolus(ECO:0000250); Chromosome(ECO:0000269)。核定位评分 10/10。

#### 3.2 蛋白大小评估
129 aa。蛋白偏小。**评分**: 8/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 16 |
| 搜索策略 | "LLPH"[Title/Abstract] |


**已知复合体成员** (GO Cellular Component):
- （暂无数据：通过 GO 数据库查询该蛋白所属的已知复合体）
**关键文献**:
1. Susanto et al. (2024). "RAPIDASH: Tag-free enrichment of ribosome-associated proteins reveals composition dynamics in embryonic tissue, cancer cells, and macrophages.". *Mol Cell*. PMID: 39260367
2. Zong et al. (2023). "Extracellular vesicles long RNA profiling identifies abundant mRNA, circRNA and lncRNA in human bile as potential biomarkers for cancer diagnosis.". *Carcinogenesis*. PMID: 37696683
3. Susanto et al. (2023). "RAPIDASH: A tag-free enrichment of ribosome-associated proteins reveals compositional dynamics in embryonic tissues and stimulated macrophages.". *bioRxiv*. PMID: 38106052
4. Durán et al. (2024). "Evaluation of aldosterone to direct renin ratio, low renin and related Phenotypes in Afro-Colombian patients with apparent treatment resistant hypertension.". *Sci Rep*. PMID: 39103362
5. Zeng et al. (2023). "Multi-omics data reveals novel impacts of human papillomavirus integration on the epigenomic and transcriptomic signatures of cervical tumorigenesis.". *J Med Virol*. PMID: 37212325
**评价**: PubMed 16 篇。极度新颖，几乎未被研究。**评分**: 10/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 74.44 |
| pLDDT < 50 (无序)  | 20.2% |
| AlphaFold 版本 | v6 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/LLPH/LLPH-PAE.png]]

**评价**: AlphaFold 中等质量预测，pLDDT 74.44。**评分**: 7/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR018784(LLP homolog-like) |


**染色质调控潜力分析**: IPR018784(LLP homolog-like)。**评分**: 7/10。

#### 3.6 PPI 网络
**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| LYAR | psi-mi:"MI:0006"(anti bait coi | pubmed:17353931 | — | — |
| psi-mi:ssrna_uc(display_short) | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 | — | — |
| Ctcf | psi-mi:"MI:0676"(tandem affini | imex:IM-11719|pubmed:20360068 | — | Yes |
| SRPK3 | psi-mi:"MI:0676"(tandem affini | pubmed:23602568|imex:IM-17935 | — | — |
| RPS6 | psi-mi:"MI:1314"(proximity-dep | pubmed:29568061|imex:IM-26301 | — | — |
| psi-mi:polg_zikvk(display_long | psi-mi:"MI:0007"(anti tag coim | pubmed:30177828|imex:IM-26452 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| RPL30 | 0.894 | — | — |
| ZNF593 | 0.890 | — | — |
| RSL24D1 | 0.868 | — | — |
| NMD3 | 0.861 | — | — |
| GNL2 | 0.860 | — | — |
| EIF6 | 0.849 | — | — |
| RPL36AL | 0.849 | — | — |
| RPL7A | 0.847 | — | — |

**PPI 互证分析**:
- STRING top partner: RPL30 (score: 0.894)
- IntAct interactions: 15 total
- **PPI 评分**: 5/10
##### PPI 数据源补充核查（自动审计）

**IntAct/BioGrid 实验互作核查**:
| Partner | 方法 | PMID |
|---------|------|------|
| — | two hybrid pooling approach | 16189514 |
| — | anti bait coimmunoprecipitation | 17353931 |
| — | pull down | 23902751 |
| — | tandem affinity purification | 20360068 |
| — | tandem affinity purification | 23602568 |
| — | proximity-dependent biotin identification | 29568061 |
| — | anti tag coimmunoprecipitation | 30177828 |
| — | tandem affinity purification | 31527615 |
| — | pull down | 30833792 |
| — | tandem affinity purification | 31527615 |

**STRING 预测/整合互作核查**:
| Partner | Score |
|---------|-------|
| RPL30 | 0.894 |
| ZNF593 | 0.890 |
| RSL24D1 | 0.868 |
| NMD3 | 0.861 |
| GNL2 | 0.860 |
| EIF6 | 0.849 |
| RPL36AL | 0.849 |
| RPL7A | 0.847 |
| GTPBP4 | 0.845 |
| RPL14 | 0.843 |

**GO-CC 复合体/定位核查**:
- GO:0005694: chromosome (IDA:UniProtKB)
- GO:0005730: nucleolus (IDA:HPA)

**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold v6 | pLDDT 74.44 | — |
| 结构域 | InterPro | IPR018784(LLP homolog-like) | — |
| 定位 | UniProt | Nucleus, nucleolus(ECO:0000250); Chromosome(ECO:0000269) | — |
| PPI | STRING + IntAct | RPL30 等 | — |

**互证加分明细**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 极度新颖: PubMed 16 篇
2. 中等质量 AlphaFold 结构: pLDDT 74.44

**风险/不确定性**:
1. 核定位需 HPA/IF 实验验证
2. 染色质/TE 调控功能缺乏直接实验证据

**下一步建议**:
- [ ] 使用 HPA/IF 确认 LLPH 的核定位
- [ ] 在 TEreg 相关细胞系中检测 LLPH 表达水平
- [ ] 通过 co-IP/MS 鉴定 LLPH 的染色质调控相关互作伙伴

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPL30 | STRING | 894 |
| ZNF593 | STRING | 890 |
| RSL24D1 | STRING | 868 |
| NMD3 | STRING | 861 |
| GNL2 | STRING | 860 |
| EIF6 | STRING | 849 |
| EIF3A | STRING | 849 |
| RPL36AL | STRING | 849 |


### HPA IF 图像

![](https://images.proteinatlas.org/48920/749_C10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48920/749_C10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48920/1392_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48920/1392_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48920/735_C10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48920/735_C10_3_blue_red_green.jpg)


### 深度机制分析

LLPH（Protein LLP homolog, 129 aa, UniProt Q9BRT6）是LLP同源蛋白——LLP（lupus La protein）最初在系统性红斑狼疮（SLE）中被鉴定为自身抗原。LLPH是极小蛋白（129 aa），域架构为单拷贝LLP同源域（IPR018784/LLP homolog-like, Pfam:PF10169/DUF2376）。AlphaFold v6 pLDDT=74.4和ESMFold从头折叠验证（平均pLDDT=0.62）确认LLPH以中等置信度折叠，约20%残基处于无序状态。129 aa的尺寸允许被动扩散通过核孔复合物——符合核仁富集蛋白的典型特征。

UniProt将LLPH定位于Nucleus, nucleolus（ECO:0000250, 序列同源推断）和Chromosome（ECO:0000269, 实验证据——直接来自GO注释: GO:0005694, IDA:HPA）——这是关键的实验线索：LLPH在染色体上有直接定位的实验证据（IDA=inferred from direct assay），暗示其可能在有丝分裂染色体上执行支架功能。GO-CC中chromosome（GO:0005694, IDA:UniProtKB）和nucleolus（GO:0005730, IDA:HPA）的双重注释提示LLPH在间期定位于核仁、在有丝分裂期重新分配至浓缩染色体——这类动态重新定位模式常见于核仁蛋白（如nucleophosmin/NPM1, nucleolin/C23）。

STRING互作图谱以核糖体生物发生因子为主导：RPL30、ZNF593、RSL24D1、NMD3、GNL2、EIF6——所有伙伴的功能指向60S核糖体大亚基的组装和核仁-细胞质转运。GNL2（nucleostemin）是三磷酸鸟苷酶，定位于核仁并参与pre-rRNA加工和核糖体组装。DDX21（humanPPI: Biogrid/Opencell, AF3结构可用）是RNA解旋酶——该互作最为关键，因为DDX21直接参与核仁rRNA转录、处理和修饰，且在先天免疫中感知胞质dsRNA。KRR1（Kri1同源物, Bioplex）是90S前核糖体/SSU processome组分。

IntAct实验互作中LYAR（Ly-1 antibody reactive clone, PMID:17353931）是锌指蛋白，在pre-rRNA切割和细胞生长调控中发挥作用。Ctcf（CCCTC结合因子, PMID:20360068）的互作最为突出——CTCF是绝缘子结合蛋白，通过与cohesin协同形成染色质环域（TADs），直接影响TE（尤其是内源性逆转录病毒）与邻近基因的物理隔绝。若LLPH-CTCF互作在核仁/核质中真实存在，LLPH可能参与CTCF介导的染色质环锚定和绝缘子功能——而CTCF结合位点的DNA甲基化丧失是TE激活的早期标志。RPS6（40S核糖体蛋白S6）的邻近标记数据（BioID, PMID:29568061）确认LLPH在核仁前核糖体颗粒中的物理邻近定位。

LLPH极度新颖（PubMed=16篇, 50/50分），染色体定位+核仁富集+DDX21/CTCF互作的组合构成有吸引力的TE调控探索靶标——特别是核仁作为rDNA转录+TE抑制区室的双重身份。但实验数据全部为高通量方法（Y2H, TAP, BioID）产生——无低通量功能验证。实验优先级：LLPH-ChIP-seq（检测占据的基因组位点——关注rDNA和重复序列）；LLPH-CTCF的co-IP验证；LLPH敲除后rDNA表观基因组和CTCF ChIP-seq的变化。归一化得分81.4/100归因于核定位满分（10/10）+新颖性满分（10/10），但蛋白尺寸极小（8/10）和结构/PPI的中等水平限制了其作为全面TE调控因子的潜力。

| 指标 | 数值 |
|---|---|
| 平均 pLDDT | 0.62 |
| >0.9 | 0.0% |
| <0.5 | 20.9% |
| 残基数 | 129 |

ESMFold 从头折叠验证。PDB: `detail/_esm_structures/LLPH_esmfold.pdb`

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRT6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LLPH%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRT6
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9BRT6/
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

![[LLPH-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/LLPH/LLPH-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BRT6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018784; |
| Pfam | PF10169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139233-LLPH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX21 | Biogrid, Opencell | true |
| RPS16 | Biogrid, Opencell | true |
| AGR2 | Biogrid | false |
| ILF3 | Opencell | false |
| IPO5 | Opencell | false |
| KRR1 | Bioplex | false |
| PSPC1 | Opencell | false |
| RPL11 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
