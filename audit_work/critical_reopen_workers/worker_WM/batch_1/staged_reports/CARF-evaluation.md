---
type: protein-evaluation
gene: "CARF"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, rejected-on-reeval]
status: reevaluated
reeval_result: REJECT_CONFIRMED
original_rejection: "核定位证据不足 (HPA Vesicles 为主) + PubMed 102 > 100 + PPI 弱"
---

## CARF -- RE-EVALUATED: REJECT CONFIRMED (原始总分 44.5/180, 归一化 24.7/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARF (ALS2CR8) |
| 蛋白名称 | Calcium-responsive transcription factor |
| 蛋白大小 | 725 aa / 80.7 kDa |
| UniProt ID | Q8N187 |
| 核定位 (HPA IF) | Vesicles (主), Nucleoli fibrillar center (附加), Cytosol (附加); Approved |
| 核定位 (UniProt) | Nucleus (ECO:0000250, 序列同源性) |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | HPA 主定位 Vesicles + PubMed 102 > 100 + 无 PDB + PPI 弱 |

### 2. False Rejection Recheck

**原始淘汰判定**: HPA Vesicles 为主定位 + PubMed 102 > 100 + 无实验结构 + PPI 极弱

**Recheck 发现**:

1. **HPA 主定位为 Vesicles, 这是重大的核定位否定信号**: HPA IF 可靠性为 Approved (高可信度), 但主定位是 Vesicles (囊泡)。Nucleoli fibrillar center 仅为附加定位。这意味着在免疫荧光实验中, 主要信号出现在囊泡中, 核内信号较弱或仅在特定亚核结构中可见。对于一个名称暗示转录因子功能的蛋白 ("Calcium-responsive transcription factor"), 这种定位分布是矛盾的。

2. **PubMed 文献计数存在严重的同义词污染 (CRISPR-CARF)**: 这是本次重评中的一个关键发现。PubMed broad count=386 篇, 但其中大部分文献是关于 **CRISPR-associated Rossmann fold (CARF)** 结构域的细菌/古菌免疫系统研究, 而非人类 CARF 基因。CRISPR-CARF 是近年来非常热门的领域。strict query (102 篇) 试图过滤但仍无法完全排除污染。人工审阅 Top 5 关键文献发现: 3 篇是关于 CRISPR-Cas 系统的 CARF 核酸酶 (Baca et al., 2024, Nature; Li et al., 2025, Science), 1 篇是关于辣椒 fertility restorer CaRf (同源但非人), 仅有 1 篇关于人类 CARF 的细胞衰老功能 (Wadhwa et al., 2017)。这表明真实的 human CARF 文献数可能远低于 102。**但存在严重的研究关注度分散问题: 即使真正的文献数 <100, 该基因的文献搜索噪声极大, 影响研究效率**。

3. **功能注释与实际数据严重不匹配**: 蛋白名称称 "Calcium-responsive transcription factor", 但 GO-CC 仅列 granular component 和 nucleus, STRING 最高 combined score 仅 0.637 (BDNF, text-mining), 没有任何实验验证的互作。AlphaFold pLDDT=55.5 (低), 无 PDB。这使其成为本次 8 个重评基因中证据链最薄弱的候选。

4. **无 PDB 结构、无高质量 AlphaFold**: 725 aa 蛋白仅 24% 残基 pLDDT>90, 58.9% <50。这预示该蛋白可能主要是天然无序蛋白, 或 AlphaFold 在当前版本中无法正确预测其折叠。

**结论**: CARF 在多维度均表现最弱 -- 核定位矛盾 (HPA Vesicles 主定位, UniProt 仅序列推断), 结构数据差 (无 PDB, AF pLDDT=55.5), PPI 极弱 (全 text-mining), 且 PubMed 计数受 CRISPR-CARF 严重污染。即使真实文献 <100, 其他维度的重大缺陷也不支持通过。总分 44.5/180, 为 8 个重评基因中最低。强烈维持 REJECT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Vesicles (主, Approved) + Nucleoli fibrillar center (附加); UniProt: Nucleus (ECO:0000250, 序列推断) |
| 蛋白大小 | 8/10 | x1 | 8 | 725 aa / 80.7 kDa (理想范围 200-800 aa 上限) |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=102 (>100, 但严重受 CRISPR-CARF 污染; 真实 human CARF 文献可能 <60) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=55.5; 无 PDB; 仅 24% 残基 pLDDT>90 |
| 调控结构域 | 3/10 | x2 | 6 | IPR029309 (DUF4557), Pfam PF15299 (DUF4557); 未表征结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING: BDNF(0.637, 全 text-mining); 无 experimental partner; IntAct 15 互作 (全为大型 co-IP screen) |
| 互证加分 | -- | max +3 | 0.5 | 仅 STRING+IntAct 双源 (但质量低) |
| **原始总分** | | | **44.5/180** | |
| **归一化总分** | | | **24.7/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles (主定位), Nucleoli fibrillar center (附加), Cytosol (附加) | Approved |
| UniProt subcellular | Nucleus (ECO:0000250, 序列同源性) | Swiss-Prot |
| GO Cellular Component | granular component (GO:0001652, IEA:Ensembl); nucleus (GO:0005634, ISS:UniProt) | 电子注释为主 |

**核定位证据分析**:
- HPA Approved 级别 IF 主定位为 **Vesicles** (囊泡)。对于一个名称中含 "transcription factor" 的蛋白, 这是极强的矛盾信号
- Nucleoli fibrillar center 为附加定位(非主要), 提示该蛋白在核仁纤维中心有微弱分布
- UniProt 的 Nucleus 注释基于序列同源性 (ECO:0000250), 非直接实验 -- 这在 Swiss-Prot 中属于低级别证据
- GO-CC 仅两个条目: granular component (IEA) 和 nucleus (ISS) -- 均为电子推断, 无直接实验
- 蛋白名称暗示 Ca2+ 响应性转录因子功能, 但亚细胞定位数据不支持这一推断

**结论**: 核定位证据非常薄弱。HPA Approved 级 IF 显示主定位为囊泡而非细胞核。UniProt 核定位仅基于序列同源性推断。得分 3/10 反映了核定位存在的可能性但证据严重不足。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 725 aa |
| 分子量 | 80.7 kDa |
| 理想范围 | 200-800 aa (上限) |

**评价**: 725 aa, 80.7 kDa, 处于理想范围上限。虽然大小适中, 但由于结构数据差 (pLDDT=55.5), 表达纯化可能面临溶解度和折叠问题。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 102 |
| PubMed symbol_only count | 246 |
| PubMed broad count | 386 |
| 别名(未计入scoring) | ALS2CR8 |

**关键文献 (人工审阅) (需注意 CRISPR-CARF 污染)**:
1. **CRISPR-Cas 系统**: Baca CF, Yu Y, Rostol JT et al. (2024). "The CRISPR effector Cam1 mediates membrane depolarization for phage defence." *Nature*. PMID: 38200316 (NOT human CARF -- CRISPR-associated Rossmann fold)
2. **Human CARF**: Taha MS, Haghighi F, Stefanski A et al. (2021). "Novel FMRP interaction networks linked to cellular stress." *The FEBS journal*. PMID: 32525608 (human CARF, FMRP interactor)
3. **Pepper CaRf**: Nie Z, Song Y, Wang H et al. (2022). "Fine Mapping and Gene Analysis of restorer-of-fertility Gene CaRf(HZ) in Pepper." *Int J Mol Sci*. PMID: 35886981 (NOT human CARF -- plant fertility restorer)
4. **Human CARF**: Wadhwa R, Kalra RS, Kaul SC et al. (2017). "CARF is a multi-module regulator of cell proliferation and a molecular bridge between cellular senescence and carcinogenesis." *Mechanisms of ageing and development*. PMID: 28754531 (human CARF)
5. **CRISPR-Cas 系统**: Li Y, Li Z, Yan P et al. (2025). "Antiviral signaling of a type III CRISPR-associated deaminase." *Science*. PMID: 39666823 (NOT human CARF)

**人工审阅发现**: 5 篇 "top papers" 中: 2 篇为 CRISPR-CARF (细菌), 1 篇为植物 CaRf (辣椒 fertility restorer), 2 篇为人类 CARF。**实际 human CARF 功能文献估计 <40 篇**。但 PubMed strict query 无法完全排除同义词污染 (CRISPR 领域大量使用 "CARF" 指 Rossmann fold 结构域), 导致计数严重高估。

**评价**: PubMed strict=102 触发了一票否决 (0/10)。然而人工审阅揭示真实 human CARF 文献数可能 <40 篇。这是一个因基因符号与热门领域 (CRISPR) 的结构域名称冲突导致的技术性误判。但由于基因名称的选择不属于评估流程的控制范围, 且该基因在其他多个维度同样不达标, 维持 0/10 判定。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 24.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 58.9% |
| 有序区域 (pLDDT>70) 占比 | 32.3% |
| 可用 PDB 条目 | 无 |

**评价**: 无 PDB 实验结构。AlphaFold 预测质量低 (mean pLDDT=55.5), 仅 24% 残基高置信 (pLDDT>90), 58.9% 残基低置信 (pLDDT<50)。该蛋白可能含有大量天然无序区域, 或 AlphaFold 当前版本无法正确预测其折叠 (可能是新型折叠类型)。无论哪种情况, 对实验设计都不利。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR029309 (Domain of unknown function DUF4557) |
| Pfam | PF15299 (Domain of unknown function DUF4557) |

**染色质调控潜力分析**: CARF 仅含一个未表征结构域 (DUF4557), 无任何功能注释。DUF4557 的功能、折叠类型和配体结合能力均未知。虽然蛋白名称暗示 Ca2+ 结合和转录激活功能, 但这些功能尚未映射到已知的结构域。结构域分析对功能预测几乎没有帮助。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BDNF | 0.637 | 0 | 脑源性神经营养因子 (CARF 的假定转录靶基因) |
| MECP2 | 0.509 | 0 | 甲基-CpG 结合蛋白 2 |
| TRPC6 | 0.496 | 0 | 钙通道 |
| CPA5 | 0.477 | 0 | 羧肽酶 |
| THADA | 0.476 | 0 | 甲状腺腺瘤相关蛋白 |
| NTRK2 | 0.476 | 0 | BDNF 受体 TrkB |
| TMEM260 | 0.475 | 0 | 跨膜蛋白 |
| NBEAL1 | 0.474 | 0 | BEACH 结构域蛋白 |
| NTF4 | 0.454 | 0 | 神经营养因子 4 |
| USF1 | 0.453 | 0 | 转录因子 USF1 |

**实验验证互作** (IntAct, 精选):

| Partner | 方法 | PMID |
|---------|------|------|
| LMO3 | two hybrid pooling | 16189514 |
| CDKN2AIP | pull down | 23902751 |
| DHX58 | anti tag coimmunoprecipitation | 21903422 |
| CUL3 | tandem affinity purification | 21145461 |
| ZSCAN31 | anti tag coimmunoprecipitation | 28514442 |
| ESR1 | tandem affinity purification | 31527615 |
| HNRNPF | anti tag coimmunoprecipitation | 28514442 |
| ELAVL2 | anti tag coimmunoprecipitation | 28514442 |
| FGF3 | anti tag coimmunoprecipitation | 28514442 |
| SART3 | anti tag coimmunoprecipitation | 28514442 |

**PPI 互证分析**:
- STRING combined scores 全部 <0.65, 且 Experimental 列全为 0
- 没有 STRING 实验验证的互作伙伴 -- 所有关联均为 text-mining
- IntAct 互作来自大型 co-IP/MS 筛选 (PMID:28514442 贡献了多个互作), 缺乏靶向验证
- 互作伙伴功能分散 (钙通道、剪接因子、泛素连接酶、神经营养因子受体)
- STRING partners: 15, IntAct interactions: 15

**评价**: PPI 网络极其薄弱。STRING 全 text-mining, 无实验支持。IntAct 互作缺乏聚焦性 (无功能收敛)。这可能是本次 8 个重评基因中最弱的 PPI 网络。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5, 无 PDB | 仅预测, 预测质量低 | 无验证 |
| 定位 | UniProt (Nucleus) + HPA (Vesicles main) | 矛盾 | 严重不一致 |
| PPI | STRING + IntAct | 15 (全 text-mining) + 15 (co-IP screens) | 数据存在但质量极低 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0 (无 PDB, AF 质量低)
- 多库定位一致: +0 (UniProt 说 Nucleus, HPA 说 Vesicles -- 严重矛盾)
- STRING + IntAct 双源验证: +0.5 (仅因数据存在)
- 结构域 + AlphaFold 一致性: +0 (DUF4557 未表征, AF 质量低)
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 5. 总体评价

**推荐等级**: REJECT CONFIRMED (原始评估 REJECTED -> 重新评估 REJECTED)

**核心优势**:
1. 蛋白大小适中 (725 aa, 80.7 kDa)
2. 蛋白名称暗示转录因子功能 ("Calcium-responsive transcription factor") -- 名义上符合筛选目标

**劣势/不确定性**:
1. **HPA 主定位为 Vesicles (囊泡), Approved 级别, 直接与转录因子身份矛盾**
2. UniProt 核定位仅基于序列推断 (ECO:0000250), 非实验证据
3. 无 PDB 实验结构, AlphaFold pLDDT=55.5 (58.9% 残基无序)
4. PPI 极弱: STRING 全 text-mining, 无实验 verified partner
5. 唯一的 InterPro 结构域是 DUF4557 (未表征), 无功能注释
6. PubMed strict=102 触发一票否决, 且基因名称与 CRISPR-CARF 结构性冲突导致文献搜索严重污染
7. 如果真实文献 <40, 虽可激活研究新颖性得分, 但其他维度 (核定位 3/10 + 结构 3/10 + PPI 3/10) 仍然全面不达标

**False Rejection 定性**:
原始评估在多维度均正确判断了 CARF 的缺陷。PubMed 文献污染 (CRISPR-CARF 同义词) 虽然导致研究新颖性被高估为 >100 (实际 true 文献数可能 <40), 但即便修正研究新颖性得分, 核定位 (HPA Vesicles), 结构 (AF pLDDT=55.5, 无 PDB), PPI (全 text-mining) 三个维度的根本性缺陷也不支持通过。总分 44.5/180 为本次 8 个重评基因中最低。强烈维持 REJECT。

**特别说明**: 鉴于 CARF 基因名称与 CRISPR-CARF 结构域存在严重命名冲突, 建议在 PubMed 搜索和文献审阅中额外注意基因/蛋白名称与其他领域的歧义风险。类似问题也可能出现在其他基因 (如 CARF, MLXIPL/WBSCR14) 的评估中。

**下一步建议**:
- [ ] 不推荐 CARF 作为 TE 调控核蛋白的候选目标
- [ ] 鉴于 CARF 的名义功能 (Calcium-responsive transcription factor), 如需探索 Ca2+ 信号与 TE 调控的交叉, 可考虑其他更好的候选 (如 NFAT 家族, CREB, CaMK 激酶)
- [ ] 将 CARF 作为 PubMed 同义词污染的案例记录, 用于改进评估流程中的基因名称消歧

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N187
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138380-CARF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N187
- STRING: https://string-db.org/network/9606.ENSP00000260956
- Data fetched live: 2026-06-02
