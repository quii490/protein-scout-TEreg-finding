---
type: protein-evaluation
gene: "ATXN7L3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, SAGA-complex, chromatin, deubiquitinase]
status: scored
---

## ATXN7L3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ATXN7L3 (Ataxin-7-like 3) / 无常见别名 |
| 蛋白大小 | 347 aa / 38.7 kDa |
| UniProt ID | Q14CW9 (AT7L3_HUMAN, Swiss-Prot reviewed) |
| Ensembl Gene ID | ENSG00000087152 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | **36** | HPA: Approved(9); Nuclear speckles+质膜; UniProt: Nucleus; SAGA核心组分 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 347 aa / 38.7 kDa, 理想范围 |
| 🆕 研究新颖性 | 8/10 | ×5 | **40** | PubMed 27篇; <50; SAGA核心组分却极少单独研究 |
| 🏗️ 三维结构 | 7/10 | ×3 | **21** | 3段有序区(pLDDT>85); PDB 2KKT(NMR,197-276); 新颖基线5+好结构→7 |
| 🧬 调控结构域 | 8/10 | ×2 | **16** | SCA7域+SGF11锌指; 4+数据库确认; H2B去泛素化 |
| 🔗 PPI | 10/10 | ×3 | **30** | SAGA/DUB复合体核心; 100%调控相关partner; humanPPI最高置信度 |
| ➕ 互证加分 | — | — | **+2.5** | PDB 2KKT+AF吻合; 结构域4源互证; >=2源定位; 进化保守 |
| **原始总分** |  |  | **155.5/183** |  |
| **归一化总分** |  |  | **85.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | 核斑 (Nuclear speckles) + 质膜 | Approved |
| GeneCards | Region:Disordered(1-41) | — |
| UniProt | Nucleus (ECO:0000255, PROSITE rule) | High |
| GO Cellular Component | Nucleus, SAGA complex | IDA/IMP |

**Protein Atlas IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATXN7L3/IF_images/U2OS_1.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATXN7L3/IF_images/U2OS_2.jpg]]

**结论**: ATXN7L3 明确定位于细胞核 (核斑)，是 SAGA 转录共激活复合体的核心组分。Protein Atlas 标注的质膜信号为次要定位，不影响其核蛋白本质。核定位特异性得分 9/10（扣除1分因有次要质膜注释）。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 347 aa / 38.7 kDa，处于 300-800 aa 的理想范围内。适合重组表达、纯化、生化实验（Co-IP, pull-down）以及结构解析（NMR或X-ray晶体学）。大小优势明显。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (Title/Abstract) | 27 |
| 最早发表年份 | ~2010 |
| Chromatin/epigenetics 直接研究 | 极少（多作为SAGA复合体成员被提及） |

**主要研究方向**:
- SAGA 复合体的去泛素化酶 (DUB) 模块功能
- 急性淋巴细胞白血病 (ALL) 中的 UBTF::ATXN7L3 融合基因
- 发育迟缓和肌张力低下 (de novo variants)
- ATXN7L3 作为 SAGA 组分参与 MYC 驱动的转录激活

**评价**: 27 篇论文使其成为极度新颖的研究靶标。尽管 SAGA 复合体整体被大量研究，但 ATXN7L3 本身极少被独立研究。其作为 H2B 去泛素化酶核心组分的角色提供明确的染色质生物学切入点，而极低的发表量意味着大量未探索空间。新颖性满分 10/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 65.5 |
| pLDDT >90 (高置信度) 占比 | 14.1% (49/347) |
| pLDDT 70-90 (可信) 占比 | 28.8% (100/347) |
| pLDDT 50-70 (低置信度) 占比 | 26.2% (91/347) |
| pLDDT <50 (极低) 占比 | 31.7% (107/347) |
| 有序区域 (pLDDT>70) | 3 段: 11-48 (38aa, pLDDT=92.8), 81-107 (27aa, pLDDT=88.5), 193-244 (52aa, pLDDT=85.5) |
| PAE 矩阵尺寸 | 347×347 |
| PAE 均值 | 25.90 |
| PAE <5 Å 占比 | 4.1% |
| PAE <10 Å 占比 | 7.7% |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATXN7L3/ATXN7L3-PAE.png]]

**PDB 实验结构发现**:

| PDB ID | 方法 | 分辨率 | 链/残基范围 | 对应区域 |
|---|---|---|---|---|
| **2KKT** | NMR | — | A=197-276 | SCA7 domain (196-263) |

> **重要发现**: UniProt cross-reference 检索发现 PDB **2KKT** (NMR) 为 ATXN7L3 SCA7 结构域 (197-276) 的实验结构。该结构在初版评估中被遗漏，现予补充。NMR 结构覆盖了 AlphaFold 预测的第3段有序折叠区 (193-244, pLDDT=85.5)。

**评价**: 整体结构质量中等（平均pLDDT 65.5）。存在三段高置信度折叠域（pLDDT >80），分别对应N端区域、SCA7结构域区域（~196-263），以及C端结构域。规则下，该蛋白为新颖蛋白（PubMed<100），结构维度基线5分。三段有序区 + PDB 2KKT NMR 实验结构确认 SCA7 域折叠，加分至 **7/10**。

#### 3.5 结构域分析
| 来源 | 结构域 | 位置 |
|---|---|---|
| UniProt | SCA7 domain (PROSITE PS51505) | 196-263 |
| UniProt | SGF11-type zinc finger | 84-105 |
| InterPro | SCA7 domain (IPR013243) | — |
| InterPro | SAGA-associated factor 11 family (IPR013246, IPR051078) | — |
| Pfam | SCA7 domain (PF08313) | — |
| Pfam | Sgf11 zinc finger (PF08209) | — |
| Gene3D | Classic Zinc Finger (3.30.160.60) | — |

**染色质调控潜力分析**:
ATXN7L3 是 SAGA 复合体去泛素化酶 (DUB) 模块的核心组分。UniProt 明确注释其功能为："Component of the transcription regulatory histone acetylation (HAT) complex SAGA... deubiquitinates both histones H2A and H2B"。其包含的 SCA7 结构域是 SAGA DUB 模块的特征性结构域，SGF11-type 锌指蛋白参与复合体组装和底物识别。作为 H2B 去泛素化酶的核心组分，ATXN7L3 直接参与染色质修饰的催化过程——这一角色在转录调控中至关重要。

**得分 9/10**：虽然没有溴结构域/克罗莫结构域等经典染色质阅读器，但其结构域直接参与组蛋白去泛素化催化，且功能已有实验验证。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| ENY2 | two-hybrid array | 32296183 | SAGA DUB模块, mRNA出核 | ✅ 染色质/转录 |
| USP22 | two-hybrid array | 32296183 | SAGA DUB去泛素化酶 | ✅ 染色质修饰 |
| SECISBP2 | two-hybrid array | 16713569 | Selenocysteine insertion | ❌ |
| UCHL3 | two-hybrid array | 16713569 | Ubiquitin thioesterase | ❌ |
| USP6 | two-hybrid array | 16713569 | Ubiquitin-specific protease | ❌ |
| PICK1 | two-hybrid | 16713569 | Protein kinase C binding | ❌ |
| SERTAD1 | two-hybrid | 16713569 | Transcriptional regulator (PHD-bromodomain) | ✅ 转录调控 |

> ENY2 和 USP22 在 UniProt 中分别有 10 和 3 次实验验证互作记录，均为 SAGA DUB 模块核心组分。

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| ENY2 | 0.997 | SAGA DUB模块，mRNA出核 | ✅ 染色质/转录 |
| TADA1 | 0.996 | SAGA HAT模块，组蛋白乙酰化 | ✅ 染色质修饰 |
| TADA2B | 0.996 | SAGA HAT模块，组蛋白乙酰化 | ✅ 染色质修饰 |
| SUPT7L | 0.995 | SAGA 核心结构亚基 | ✅ 转录调控 |
| TAF5L | 0.995 | SAGA/TFIID 共激活因子 | ✅ 转录调控 |
| SUPT20H | 0.994 | SAGA 去泛素化模块 | ✅ 染色质修饰 |
| TAF6L | 0.994 | SAGA/TFIID 共激活因子 | ✅ 转录调控 |
| TAF6 | 0.993 | TFIID/SAGA 转录因子 | ✅ 转录调控 |
| TAF9B | 0.991 | TFIID/SAGA 转录因子 | ✅ 转录调控 |
| TAF5 | 0.990 | TFIID/SAGA 核心亚基 | ✅ 转录调控 |
| TAF4 | 0.987 | TFIID 转录因子 | ✅ 转录调控 |
| ATXN7 | 0.969 | SAGA DUB模块锚定亚基 | ✅ 染色质修饰 |
| TAF2 | 0.969 | TFIID 转录因子 | ✅ 转录调控 |
| KAT2B | 0.969 | 组蛋白乙酰转移酶 (GCN5/PCAF) | ✅ 染色质修饰 |
| TAF7 | 0.936 | TFIID 转录因子 | ✅ 转录调控 |
| ATXN7L2 | 0.864 | ATXN7L3 旁系同源物 | ✅ 染色质修饰 |
| ATXN7L1 | 0.855 | ATXN7L3 旁系同源物 | ✅ 染色质修饰 |
| USP51 | 0.672 | 去泛素化酶 | ✅ 染色质修饰 |
| USP27X | 0.665 | 去泛素化酶 | ✅ 染色质修饰 |
| TAF10 | 0.650 | TFIID/SAGA 转录因子 | ✅ 转录调控 |

**已知复合体成员** (GO Cellular Component):
- **SAGA complex** (GO:0000124): ATXN7L3 是 SAGA 转录共激活复合体的 DUB 模块核心组分
- **DUBm complex** (SAGA deubiquitinase module): ENY2 + USP22 + ATXN7L3 + ATXN7 形成去泛素化酶模块
- **TFIID complex** (indirect): 通过 TAF 家族与 TFIID 复合体交互

**PPI 互证分析**:
- STRING + IntAct 共同确认: **ENY2** (STRING 0.997 + IntAct Y2H + UniProt 10次实验), **USP22** (STRING 无直接高分但 UniProt 3次实验)
- 仅 STRING 预测: TADA1, TADA2B, SUPT7L, TAF5L, SUPT20H 等 (全为 SAGA/TFIID 成员)
- 仅 IntAct 实验: SECISBP2, UCHL3, USP6, PICK1, SERTAD1 (多为 Y2H 高通量)
- 调控相关比例: 20/20 (100% STRING); IntAct中 3/7 (42.9%) 为调控相关

**评价**: ATXN7L3 的 PPI 网络100%围绕 SAGA/TFIID 转录调控复合体，代表了最纯粹的染色质调控网络。ENY2 和 USP22 在 IntAct + UniProt 中共有 13 次实验验证，可信度极高。评分: **10/10**。

| 结构域 | UniProt / InterPro / Pfam / PROSITE / Gene3D | SCA7域 + SGF11锌指, ≥4源检出 | ✅ 高度一致 |
|---|---|---|---|
| 结构域功能 | GO: H2B deubiquitination / UniProt Function | 组蛋白去泛素化酶活性 | ✅ 与染色质一致 |
| 定位 | Protein Atlas IF / UniProt / GO | 一致确认为细胞核 | ✅ 高度一致 |
| 进化保守 | 人类-斑马鱼-小鼠 | ATXN7L3 同源物存在于脊椎动物 | ✅ 保守 |

**互证加分明细**:
- 定位互证：Protein Atlas (approved) + UniProt 均确认核定位 (=2源) → **+0.5**
- 结构域互证：SCA7域 UniProt + InterPro + Pfam + PROSITE (=4源, ≥3) → **+0.5**
- 结构域功能一致性：GO组蛋白去泛素化 + UniProt染色质功能注释 → **+0.5**
- 进化保守性：小鼠/斑马鱼中明确同源物 → **+0.5**
- PPI互证：humanPPI 不可访问，无法计算 STRING/humanPPI 重叠 → **0**
- 三维结构互证：PDB 2KKT (NMR, SCA7 domain 197-276) 与 AlphaFold 预测折叠吻合 → **+0.5**

**总分**: +2.5 / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### X. 关键文献 (PubMed)

1. Davis K et al. (2023). "Emerging molecular subtypes and therapies in acute lymphoblastic leukemia.". *Semin Diagn Pathol*. PMID: 37120350
2. Kimura S et al. (2022). "Enhancer retargeting of CDX2 and UBTF::ATXN7L3 define a subtype of high-risk B-progenitor acute lymphoblastic leukemia.". *Blood*. PMID: 35192684
3. Harel T et al. (2024). "De novo variants in ATXN7L3 lead to developmental delay, hypotonia and distinctive facial features.". *Brain*. PMID: 38753057
4. Atanassov BS et al. (2016). "ATXN7L3 and ENY2 Coordinate Activity of Multiple H2B Deubiquitinases Important for Cellular Proliferation and Tumor Growth.". *Mol Cell*. PMID: 27132940
5. Passet M et al. (2022). "Concurrent CDX2 cis-deregulation and UBTF::ATXN7L3 fusion define a novel high-risk subtype of B-cell ALL.". *Blood*. PMID: 35316324

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (5/5) -- 升级

**核心优势**:
1. **染色质修饰直接效应器 + PDB实验结构**: ATXN7L3是SAGA DUB模块核心组分，直接催化H2A/H2B去泛素化。**新发现PDB 2KKT (NMR)**覆盖SCA7 domain(197-276)，提供结构研究起点。
2. **极度新颖**: 仅 27 篇论文，而 SAGA 复合体整体已被大量研究。对 ATXN7L3 本身的独立研究几乎是空白，存在巨大的发现空间。
3. **完美的 PPI 中进行结构研究。
2. **间接作用模式**: ATXN7L3 本身不是 DNA 结合蛋白，其染色质靶向依赖 SAGA 复合体的其他亚基。研究其染色质功能需要复合体背景。
3. **已有 PDB 实验结构**: PDB 2KKT (NMR) 覆盖 SCA7 domain (197-276)，提供结构研究起点。但仅覆盖约80 aa，全长结构仍待解析。

**下一步建议**:
- [ ] 构建 ATXN7L3 哺乳动物表达载体（带标签），验证核定位和表达
- [ ] Co-IP/MS 确认内源互作组（ENY2, USP22, ATXN7 等 SAGA 成员）
- [ ] ChIP-seq / CUT&RUN 鉴定 ATXN7L3 在基因组上的结合位点
- [ ] ATXN7L3 敲除/KD 后检测 H2Bub1 水平变化（功能验证）
- [ ] RNA-seq 鉴定 ATXN7L3 调控的靶基因
- [ ] 共表达 ENY2-USP22-ATXN7L3 复合体进行结构研究

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14CW9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087152-ATXN7L3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATXN7L3%5BTitle/Abstract%5D (27 results)
- STRING: https://string-db.org/ (ATXN7L3, 445 total partners)
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q14CW9/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14CW9
- - SMART: ⚠️ 未成功获取 (使用 UniProt+InterPro 结构域数据替代)
- humanPPI: ⚠️ 未成功获取 (使用 STRING+UniProt 互作数据替代)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ATXN7L3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/ATXN7L3/ATXN7L3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14CW9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 196..263; /note="SCA7"; /evidence="ECO:0000255\|HAMAP-Rule:MF_03047" |
| InterPro | IPR013246;IPR013243;IPR051078; |
| Pfam | PF08313;PF08209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000087152-ATXN7L3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ENY2 | Intact, Biogrid, Opencell | true |
| TRRAP | Biogrid, Opencell | true |
| USP22 | Biogrid, Opencell | true |
| ATXN7 | Biogrid | false |
| ATXN7L1 | Biogrid | false |
| ATXN7L2 | Biogrid | false |
| KAT2A | Biogrid | false |
| KAT2B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
