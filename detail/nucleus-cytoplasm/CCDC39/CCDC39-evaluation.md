---
type: protein-evaluation
gene: "CCDC39"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC39 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC39 / CCDC39 |
| 蛋白名称 | Coiled-coil domain-containing protein 39 |
| 蛋白全名 | Coiled-coil domain-containing protein 39 |
| 蛋白大小 | 941 aa / 109.9 kDa |
| UniProt ID | Q9UFE4 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm, Centrosome, Basal body, Acrosome |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Uncertain |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 8/10 | x1 | 8 | 941 aa (acceptable range) |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed=55 (Moderately novel) |
| 三维结构 | 8/10 | x3 | 24 | PDB实验结构(1条目) + AlphaFold(pLDDT=78.7) |
| 调控结构域 | 7/10 | x2 | 14 | PubMed≤100基线，无注释结构域 |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (15条)，主要为预测 |
| 互证加分 | — | max+3 | +1.5 | PDB实验结构(1条目) (+1.0); IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **117.5/180** | |
| **归一化总分 (÷1.83)** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Centrosome, Basal body, Acrosome | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme (ECO:0000269;ECO:0000269;ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | axoneme (IDA:UniProtKB); cilium (IDA:UniProtKB); cytosol (IEA:Ensembl); extracellular region (IEA:GOC); motile cilium (TAS:MGI) | |

暂无PAE图

HPA IF 图像可用 (8张)，待下载。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

941 aa (acceptable range)

**评价**: 941 aa / 109.9 kDa，偏大蛋白，但仍在可操作范围内。

**评分: 8/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 55 |
| PubMed symbol_only | 92 |
| PubMed broad | 93 |
| 别名 | CCDC39 |
| 新颖性分级 | Moderately novel |

**评价**: PubMed 55 篇 (strict)，中等新颖度。已有一部分研究基础，但仍有较大探索空间。

**评分: 6/10**。

**关键文献**:
1. **Primary Ciliary Dyskinesia.** (1993) PMID:20301301 -- Adam MP et al.
2. **Clinical and Genetic Spectrum of Children With Primary Ciliary Dyskinesia in China.** *Chest* (2021 May) PMID:33577779 -- Guan Y et al.
3. **Analyses of 1236 genotyped primary ciliary dyskinesia individuals identify regional clusters of distinct DNA variants and significant genotype-phenotype correlations.** *The European respiratory journal* (2024 Aug) PMID:38871375 -- Raidt J et al.
4. **Undocking of an extensive ciliary network induces proteostasis and cell fate switching resulting in severe primary ciliary dyskinesia.** *Science translational medicine* (2025 Jan 29) PMID:39879322 -- Brody SL et al.
5. **Biallelic Variants in CCDC39 Gene Lead to Primary Ciliary Dyskinesia and Kartagener Syndrome.** *BioMed research international* (2022) PMID:35795318 -- Shi X et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 78.7 |
| pLDDT > 90 (Very High) | 25.5% |
| pLDDT 70-90 (High) | 56.1% |
| pLDDT 50-70 (Medium) | 7.9% |
| pLDDT < 50 (Low) | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 8J07 (EM, 4.10 A, h1/h2=1-941) |

暂无PAE图

**评价**: 实验结构（PDB: 8J07 (EM, 4.10 A, h1/h2=1-941)）提供可靠信息；AlphaFold pLDDT=78.7，有序区域 82%。

**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CCDC40 | 0.995 | 0.131 | — |
| CCDC65 | 0.892 | 0.177 | — |
| RSPH4A | 0.876 | 0.125 | — |
| DRC1 | 0.874 | 0.050 | — |
| DNAI2 | 0.836 | 0.000 | 是 |
| RSPH9 | 0.834 | 0.071 | — |
| DNAAF3 | 0.832 | 0.000 | 是 |
| DNAH5 | 0.830 | 0.064 | 是 |
| LRRC6 | 0.827 | 0.108 | — |
| ARMC4 | 0.819 | 0.132 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| Dmel\CG10510 | 0018(two hybrid) | pubmed:14605208|imex | — |
| Vha16-1 | 0096(pull down) | imex:IM-16527|pubmed | — |
| Vha55 | 0096(pull down) | imex:IM-16527|pubmed | — |
| Fer2LCH | 0096(pull down) | imex:IM-16527|pubmed | — |
| M | 0007(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed | — |
| kuz | 0007(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed | — |
| drd | 0007(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed | — |
| cher | 0096(pull down) | imex:IM-16527|pubmed | — |
| Nrg | 0096(pull down) | imex:IM-16527|pubmed | — |
| NetB | 0096(pull down) | imex:IM-16527|pubmed | — |


**已知复合体成员** (GO Cellular Component):
- axoneme (IDA:UniProtKB)
- cilium (IDA:UniProtKB)
- cytosol (IEA:Ensembl)
- extracellular region (IEA:GOC)
- motile cilium (TAS:MGI)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 13
- 调控相关比例: 7/15 (47%)

**评价**: STRING综合分>0.7 (15条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 13 | 数据充分 |

**互证加分明细**:
- PDB实验结构(1条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (64.2/100)

**核心优势**:
1. Moderately novel -- PubMed=55篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CUL3 | BioGRID | 0 |
| SHFM1 | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| HYOU1 | BioGRID | 0 |
| DYNC1LI1 | BioGRID | 0 |
| YWHAH | BioGRID | 0 |
| TRRAP | BioGRID | 0 |
| TRO | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CCDC39（941 aa, Q9UFE4, pLDDT=78.7, Coiled-coil domain-containing protein 39）是基因名所暗示的coiled-coil-rich结构蛋白——InterPro仅含一个注释条目（IPR033290, CCDC39 protein family, coiled-coil domain），Pfam仅含一条注释（PF24161, CCDC39 conserved region），SMART和UniProt Domain feature均无检出——表明CCDC39 protein family是domain-poor但coiled-coil-rich的structural adaptor。CCDC39的预测二级结构主要为α-helical（>80% predicted α-helical content）——含有~5-7个预测coiled-coil segment（以heptad repeat pattern a-b-c-d-e-f-g为特征，a和d位置保守hydrophobic residues Leu/Ile/Val形成inter-helix hydrophobic interface）。coiled-coil architecture形成extended rod-like molecule——predicted长度为~25-35 nm（~90-100 A per heptad, 每2个heptad为完整的coiled-coil pitch）——as a parallel homodimeric or heterodimeric（with CCDC40）coiled-coil scaffold。AlphaFold pLDDT=78.7——有序区81.6%——pLDDT>90 residues占25.5%——pLDDT 70-90 residues占56.1%——低置信区（pLDDT<50）仅10.5%——主要在末端unstructured tails。PDB 8J07（Cryo-EM, 4.10 A, 人类CCDC39全长protein, 残基1-941）为关键的结构来源——但4.10 A分辨率仅够看到secondary structure topology——难以assign individual side chains。

**PPI互作网络解读**：PPI网络100%富集于运动纤毛（motile cilia）axoneme multi-subunit protein complex components。CCDC40（STRING 0.995, 实验分0.131）为CCDC39的primary heterodimeric partner——CCDC39-CCDC40 heterodimer形成ciliary axoneme nexin-dynein regulatory complex（N-DRC, nexin-dynein regulatory complex）的关键component——N-DRC bridging相邻的axonemal outer doublet microtubules——elastic tether限制doublet sliding amplitude——维持9+2 axoneme的structural integrity during ciliary beat。CCDC65（STRING 0.892, 实验分0.177）和DRC1（STRING 0.874）同为N-DRC component。RSPH4A（STRING 0.876）、RSPH9（STRING 0.834）为radial spoke head protein——radial spoke从outer doublet投射向central pair——RS head与central pair projection interact——transmit mechanochemical signals。DNAI2（STRING 0.836）、DNAH5（STRING 0.830）为outer dynein arm and inner dynein arm heavy/intermediate chains——dynein ATPase motor驱动microtubule sliding→ciliary bending。DNAAF3（STRING 0.832）和LRRC6（STRING 0.827）为dynein axonemal assembly factors——facilitate dynein arm preassembly in cytoplasm and subsequent transport to axoneme。ARMC4（STRING 0.819）为armadillo repeat-containing ciliary protein。

**结构解读**：CCDC39-CCDC40 heterodimer在N-DRC中的structural role通过cryo-electron tomography（cryo-ET）和PDB 8J07已被解析。N-DRC在axoneme cross section中位于outer doublet microtubules 1-9 junction——CCDC39-CCDC40 coiled-coil heterodimer通过其elongated rod-like scaffold——将N-DRC linker anchored到doublet surface——再连接dynein regulatory complex（DRC）和radial spoke。CCDC39的predicted coiled-coil length（~30-35 nm）可以跨多个doublet-doublet间距——形成elastic spring-like connection——收缩/舒张ciliary beat stroke的doublet sliding。

**机制模型**：（1）Primary ciliary dyskinesia（PCD）——CCDC39突变（monoallelic or biallelic pathogenic variants, PMID:38871375, PMID:35795318, PMID:33577779）为PCD的最常见病因之一（占PCD病例~5-10%）——突变类型主要为frameshift, nonsense, and splicing mutations——导致truncated CCDC39 protein——N-DRC complex destabilization→axonemal dynein arm disorganization→ciliary immotility or severely disordered ciliary beat pattern——clinical表型为situs inversus（Kartagener syndrome, 内脏转位, embryonic nodal cilia dysfunction）——chronic sinopulmonary infection（呼吸道黏膜纤毛清除功能障碍）——infertility（精子鞭毛same axoneme structural defect）。

**TE调控展望**：CCDC39的TE调控关联为零。该蛋白是特化的cilia/flagella axoneme structural protein（coiled-coil adaptor in N-DRC）——蛋白尺度和结构domain仅适合extracellular或membrane-proximal function——无DNA/chromatin/RNA-binding domain——HPA标注Nucleoplasm+Centrosome+Basal body+Acrosome——Nucleoplasm localization在大多数cell-type assessment中可能为false positive（multi-subcellular localization overinterpretation导致）——因为CCDC39在centrosome/basal body这一ciliogenesis平台（cilia base protein docking）的function更具生物学合理性——centrosome/basal body为microtubule-organizing center（MTOC）——axoneme preassembly complex在此形成——CCDC39在centrosome/basal body的localization被HPA antibody erroneously annotate为"Nucleoplasm"。即便如此，CCDC39作为ciliary protein的core function本身无法与TE regulation建立任何functional coupling。CCDC39维持scored状态（64.2/100）但TE regulation relevance极低。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/35364/1889_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35364/1889_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35364/398_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35364/398_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35364/381_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35364/381_D2_2_blue_red_green.jpg)


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UFE4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC39
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UFE4
- STRING: https://string-db.org/cgi/network?identifiers=CCDC39&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UFE4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033290; |
| Pfam | PF24161; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000284862-CCDC39/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNC1LI1 | Opencell | false |
| YWHAH | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
