---
type: protein-evaluation
gene: "DCK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCK — REJECTED (研究热度过高 (PubMed strict=324，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCK |
| 蛋白名称 | Deoxycytidine kinase |
| 蛋白大小 | 260 aa / 30.5 kDa |
| UniProt ID | P27707 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 260 aa / 30.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=324 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.4; PDB: 1P5Z, 1P60, 1P61, 1P62, 2A2Z, 2A30, 2A7Q |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002624, IPR050566, IPR031314, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 324 |
| PubMed broad count | 1121 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The role of alternative splicing in cancer: From oncogenesis to drug resistance.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 33070093
2. HSP90 regulates dCK stability and inhibits ionizing radiation-induced ferroptosis in cervical cancer cells.. *Cell death discovery*. PMID: 40263268
3. Cladribine modifies functional properties of microglia.. *Clinical and experimental immunology*. PMID: 32492189
4. DNA polymerases in precise and predictable CRISPR/Cas9-mediated chromosomal rearrangements.. *BMC biology*. PMID: 38066536
5. DCK is an Unfavorable Prognostic Biomarker and Correlated With Immune Infiltrates in Liver Cancer.. *Technology in cancer research & treatment*. PMID: 32588770

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 71.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 6.5% |
| 有序区域 (pLDDT>70) 占比 | 87.3% |
| 可用 PDB 条目 | 1P5Z, 1P60, 1P61, 1P62, 2A2Z, 2A30, 2A7Q, 2NO0, 2NO1, 2NO6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1P5Z, 1P60, 1P61, 1P62, 2A2Z, 2A30, 2A7Q, 2NO0, 2NO1, 2NO6）+ AlphaFold极高置信度预测（pLDDT=88.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002624, IPR050566, IPR031314, IPR027417; Pfam: PF01712 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDA | 0.996 | 0.000 | — |
| DCTD | 0.985 | 0.000 | — |
| NT5C2 | 0.967 | 0.000 | — |
| CMPK2 | 0.956 | 0.000 | — |
| PNP | 0.951 | 0.000 | — |
| ADA | 0.950 | 0.000 | — |
| AMPD2 | 0.950 | 0.000 | — |
| APRT | 0.950 | 0.000 | — |
| AMPD1 | 0.948 | 0.000 | — |
| NT5C | 0.948 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sti | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cpn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sgg | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| Rtnl1 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| Fas2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| PAPLA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| dally | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| dock | psi-mi:"MI:0018"(two hybrid) | pubmed:8663600 |
| Ptp61F | psi-mi:"MI:0096"(pull down) | pubmed:8663600 |
| robo1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14527437 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 1P5Z, 1P60, 1P61, 1P62, 2A2Z,  | pLDDT=88.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DCK — Deoxycytidine kinase，研究基础较多，新颖性有限。
2. 蛋白大小260 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 324 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 324 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

DCK（Deoxycytidine kinase, 260 aa, 30.5 kDa, UniProt P27707）属于脱氧核苷激酶家族（dNK），InterPro注释涵盖Deoxynucleoside kinase domain（IPR002624）、dNK超家族（IPR050566）和P-loop NTPase折叠（IPR027417, IPR031314），Pfam归属为dNK（PF01712），SMART未检出条目。AlphaFold v6 pLDDT=88.4（高置信残基71.9%, 有序区87.3%）预测高质量全原子结构，且已有10个PDB实验结构支持（1P5Z, 1P60, 1P61, 1P62, 2A2Z, 2A30, 2A7Q, 2NO0, 2NO1, 2NO6），提供了无配体状态、底物类似物结合态和产物结合态的多种构象。DCK采用典型的5股平行β-sheet夹层α-螺旋的Rossmann折叠——P-loop（GXXXXGKT/S磷酸结合环）位于β1-α1连接处，催化关键Asp/Glu残基位于loop区域，共同构成核苷/NTP结合和磷酸转移的活性中心。HPA确认Nucleoplasm定位（Supported），UniProt和GO-CC均支持细胞核分布（nucleoplasm GO:0005654, nucleus GO:0005634）。

PPI互作网络以核苷酸代谢酶为核心。STRING高分伙伴包括CDA/胞苷脱氨酶（combined score=0.996）、DCTD/dCMP脱氨酶（0.985）、NT5C2/5'-核苷酸酶（0.967）、CMPK2/UMP-CMP激酶（0.956）、PNP/嘌呤核苷磷酸化酶（0.951）和ADA/腺苷脱氨酶（0.950）——形成一个完整的核苷酸补救合成和分解互作网络。这种酶-酶共进化关联反映了核苷酸代谢酶在系统中通过底物通道（substrate channeling）进行代谢物高效传递的进化策略。IntAct互作包括ANKRD13A（Bioplex, 泛素化调控蛋白）、CDK1（Biogrid, 细胞周期依赖性激酶）、DGUOK（Intact/Bioplex, 脱氧鸟苷激酶——DCK的线粒体同系物），提示DCK的功能关联超越了单纯的核苷酸代谢。

DCK的生化机制是核苷酸补救合成途径的限速步骤：催化dCyd（脱氧胞苷）+ ATP/NTP → dCMP（脱氧胞苷酸）+ ADP/NDP的磷酸转移反应。该反应为DNA复制和修复提供dNTP前体，特别是在非分裂细胞中——此时核糖核苷酸还原酶（RNR）的从头合成途径被下调，补救合成成为dNTP的主要来源。DCK同时可以磷酸化多种核苷类似物前药（如吉西他滨dFdC、阿糖胞苷ara-C、克拉屈滨CdA），使其活化为细胞毒性代谢物，因此DCK是多种抗癌和抗病毒化疗药物的关键代谢激活酶。

核定位（HPA Nucleoplasm supported）提示DCK在核内直接为DNA聚合酶（Pol δ, Pol ε）提供局部dNTP供应——这被称为"dNTP的核内合成假说"。该模型预言DCK在DNA复制叉和损伤位点附近局部富集以提供按需的dCTP前体供应。然而DCK本身不含任何DNA/RNA结合域（无ZnF、HMG、AT-hook等）、染色质结合域（无chromo、bromo、PHD、SANT等）或转录调控域，且PPI网络中无转录因子、染色质重塑因子或组蛋白修饰酶的直接互作。这意味着DCK对基因表达——包括TE表达——的影响完全通过其核苷酸代谢产物（dCTP/dNTP池）的间接效应实现：dNTP池失调可影响复制叉稳定性→基因组不稳定性→应激性TE去抑制。但DCK作为TE直接调控因子的证据不足，且PubMed 324篇的研究热度过高（>100，REJECTED），不符合本筛选的新颖性标准。

DCK的结构-功能映射极为清晰——PDB 1P60（dCK-dCyd-ADP三元复合物）精确揭示了底物识别模式（Gln97和Arg128与胞嘧啶碱基的H键网络）+磷酸供体ATP/ADP结合（P-loop, Mg2+配位Asp133/Glu53）→催化反应。这一高度结构解析的酶提供了基于结构药物设计的模板——但在TE调控领域，DCK的间接性和非特异性使其不适合作为靶向的TE调控工具蛋白。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P27707
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156136-DCK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P27707
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000156136-DCK/subcellular

![](https://images.proteinatlas.org/59609/1082_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/59609/1082_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/59609/1103_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/59609/1103_F1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P27707-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P27707 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002624;IPR050566;IPR031314;IPR027417; |
| Pfam | PF01712; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156136-DCK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANKRD13A | Bioplex | false |
| CDK1 | Biogrid | false |
| DGUOK | Intact, Bioplex | false |
| GPR182 | Bioplex | false |
| GPR45 | Bioplex | false |
| GZMH | Bioplex | false |
| IRF2BPL | Bioplex | false |
| ISX | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
