---
type: protein-evaluation
gene: "AKIP1"
date: 2026-06-04
tags: [protein-scout, rescored, rescued-to-scored, critical-false-rejection]
status: rescored-to-scored
previous_status: scored
previous_rejection_reason: nuclear_score ≤ 3
rescue_reason: "HPA Nucleoplasm(Supported)+UniProt Nucleus(IDA×2)+GO-CC nucleoplasm(IDA:HPA); Function=RELA nuclear localization enhancer; nuclear_score=3 was an error despite PubMed 61 and low AF quality"
revised_nuclear_score: 6
---

## AKIP1 核蛋白评估报告 -- CRITICAL FALSE REJECTION RE-EVALUATION

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKIP1 / BCA3 / C11orf17 |
| 蛋白大小 | 210 aa / 23.1 kDa |
| UniProt ID | Q9NQ31 |
| 蛋白全名 | A-kinase-interacting protein 1 |
| HPA IF 主定位 | Nucleoplasm |
| HPA Reliability | Supported |
| 原评估状态 | REJECTED (nuclear_score=3) |
| 重新评估日期 | 2026-06-04 |
| 重新评估结果 | **RESCUED TO SCORED** |
| 注意 | 此基因其他维度(Pubmed热度, AF质量)仍有局限，但核定位证据本身已达到scored标准 |

### 2. 评分总览（修订后）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **6/10** | ×4 | 24 | HPA Nucleoplasm(Supported); UniProt Nucleus(IDA×2); GO-CC nucleoplasm(IDA:HPA); Function RELA nuclear transporter |
| 蛋白大小 | 5/10 | ×1 | 5 | 210aa/23.1kDa，极小蛋白 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=61 (41-60→6) |
| 三维结构 | 4/10 | ×3 | 12 | pLDDT=68.2, pct<50=31.0%，高比例无序 |
| 调控结构域 | 4/10 | ×2 | 8 | IPR033214 (AKIP1 family)，adaptor蛋白 |
| PPI网络 | 6/10 | ×3 | 18 | PRKACA(实验0.51), RELA(实验0.51); NF-kB+核转运功能 |
| **加权总分** | | | **97/180** | |
| **归一化总分 (÷1.8)** | | | **53.9/100** | |

### 3. False rejection recheck -- CRITICAL

**为何本次重新评估被列为CRITICAL:**

AKIP1代表了"功能本身即核定位调控"的特殊类型——其已知功能是增强NF-kB亚基RELA的**核定位和核保留**。这意味着AKIP1蛋白必须定位于细胞核才能执行其核心功能(促进RELA的核定位和磷酸化)。尽管PubMed研究热度中等(61篇)且AlphaFold结构质量低(pLDDT 68.2)，但这些与核定位是独立维度——核定位评分不应因其他维度低而被压低。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Nucleus: ECO:0000269 ×2 (IDA, 两次独立实验验证)
   - 单一核定位，无胞质注释
   - 与其他有一定非核信号的基因不同，AKIP1的UniProt定位是纯核的

2. **GO-CC (harvest packet)**:
   - GO:0005654 nucleoplasm: IDA:HPA (实验)
   - 单一GO-CC条目，且为核定位

3. **HPA Subcellular (harvest packet)**:
   - Main location: Nucleoplasm
   - Reliability: Supported
   - 单一核定位，无附加定位

4. **功能证据 -- 本身是核定位调控因子**:
   - UniProt function: "Enhances NF-kappa-B transcriptional activity by **regulating the nuclear localization** of the NF-kappa-B subunit RELA and promoting the phosphorylation of RELA by PRKACA"
   - 此蛋白的功能是促进另一个蛋白(RELA)的核定位——该功能预设其自身核定位
   - 与RELA(0.757, exp=0.51 STRING)和PRKACA(0.896, exp=0.51)的实验互作在本功能框架内

**为何原核定位评分=3是错误的:**

AKIP1拥有:
- UniProt Nucleus IDA (两次独立实验, ECO:0000269 ×2)
- GO-CC nucleoplasm IDA:HPA
- HPA Nucleoplasm主定位 (Supported)
- **零胞质/膜GO-CC或UniProt注释**
- 功能本身即为核定位调控

在纯核定位蛋白中，score=3是极大的低估。正确的核定位评分应≥6/10。

**修订后核定位评分: 6/10**
- HPA Nucleoplasm (Supported): 核蛋白确认
- UniProt Nucleus (IDA ×2): 双实验验证
- GO-CC nucleoplasm (IDA:HPA): 实验验证
- 纯核定位，无胞质信号
- 扣分项: HPA reliability为Supported而非Approved; 蛋白小且无序，可能难以特异性定位
- 功能预设核定位(RELA nuclear import enhancer): 加分

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | Nucleoplasm (main) | Supported | IF实验 |
| UniProt | Nucleus | IDA (×2) | ECO:0000269 |
| GO-CC | nucleoplasm | IDA:HPA | 实验验证 |

AKIP1是少数在三大数据库(HPA/UniProt/GO-CC)均为纯核定位的蛋白。HPA仅报告Nucleoplasm(main)，无additional location。UniProt双IDA证据。GO-CC仅含nucleoplasm(IDA:HPA)。其功能——促进RELA核定位和磷酸化——本身就要求AKIP1在核内执行功能。值得注意的是，RELA正是通过AKIP1被保留在核内并磷酸化以激活NF-kB靶基因转录——这一功能的分子机制要求AKIP1-RELA-PRKACA形成核内三元复合物。**修订评分: 6/10**。

#### 4.2 蛋白大小评估

210 aa / 23.1 kDa。极端小的adaptor蛋白，近于ANAPC13(74aa)和AKIRIN1(192aa)之间。仅含IPR033214家族分类，无Pfam功能域。小蛋白实验操作便利。**评分: 5/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 61 |
| PubMed symbol_only | 64 |
| 别名 | BCA3, C11orf17 |
| 主要方向 | NF-kB信号、心肌重塑、胶质母细胞瘤、宫颈癌转移 |

PubMed 61篇(strict)，中等研究热度。AKIP1在NF-kB信号通路(特别是RELA亚基的调控)中有系统研究，但在TE/转座子调控领域完全未被探索。NF-kB信号与内源性逆转录病毒(ERV)激活和炎症反应有已知交叉——LTR启动子驱动的ERV转录可激活cGAS-STING通路，而NF-kB是该通路的下游效应器。AKIP1作为NF-kB核定位的正调控因子，可能参与ERV激活的NF-kB响应。**评分: 6/10** (41-60篇)。

**关键文献**:
1. Gao N et al. (2008). "AKIP1 enhances NF-kappaB-dependent gene expression by promoting the nuclear retention and phosphorylation of p65." *J Biol Chem*. PMID: 18178962 -- 核心功能
2. Nijholt KT et al. (2023). "AKIP1 promotes cardiomyocyte elongation and physiological cardiac remodelling." *Sci Rep*. PMID: 36899057
3. Wan S et al. (2023). "AKIP1 accelerates glioblastoma progression through stabilizing EGFR expression." *Oncogene*. PMID: 37596322
4. Yulia A et al. (2021). "PKA and AKIP1 interact to mediate cAMP-driven COX-2 expression." *PLoS One*. PMID: 34166397
5. Zhang X et al. (2020). "AKIP1 promotes EMT and metastasis via PI3K/Akt/IKKβ pathway in cervical cancer." *Cell Biochem Funct*. PMID: 32401379

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.2 |
| pLDDT > 90 (Very High) | 26.2% |
| pLDDT 70-90 (High) | 21.4% |
| pLDDT 50-70 (Medium) | 21.4% |
| pLDDT < 50 (Low) | 31.0% |
| 有序区域 (pLDDT>70) | 47.6% |
| 实验结构 (PDB) | 无 |

AlphaFold低质量预测，31%残基无序。作为adaptor蛋白，高比例无序区域(IDR)可能具有功能性——无序区域常在多蛋白互作中提供柔性结合界面。类似CREB binding protein和p53的N端无序区通过诱导折叠(indued folding)与不同伴侣结合。但无PDB实验结构限制了结构生物学应用。**评分: 4/10**。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR033214 (A-kinase-interacting protein 1 family) |
| Pfam | 无 |

无已知功能域。作为PKA(PKRACA)和NF-kB(RELA)之间的桥接adaptor，AKIP1通过蛋白-蛋白互作将cAMP信号传导至NF-kB转录激活。**与TE调控的潜在关联**: NF-kB通路在ERV去抑制和炎症中起核心作用——ERV的LTR启动子在衰老和癌症中被去甲基化后，可通过cGAS-STING-TBK1-IKK-NF-kB轴驱动炎症基因表达。AKIP1作为RELA核保留的正调控因子，可能在该通路中放大NF-kB对ERV激活的响应，从而影响TE驱动的炎症。**评分: 4/10**。

#### 4.6 PPI 网络

| Partner | Combined Score | Experimental | 功能 |
|---------|---------------|--------------|------|
| PRKACA | 0.896 | 0.51 | PKA催化亚基(cAMP信号) |
| PRKACB | 0.796 | 0 | PKA催化亚基β |
| RELA | 0.757 | 0.51 | NF-kB p65亚基(转录因子) |
| SIRT1 | 0.585 | 0.292 | 去乙酰化酶(老化/代谢) |

**IntAct实验互作**: PRKACA(Y2H, PMID:15630084), FHL2(Y2H array), RNF2(co-IP, PMID:26496610), CNOT2(co-IP), LNX1(holdup assay, direct interaction, PMID:36115835), NOS1(holdup assay, direct interaction), POC1B(co-IP, PMID:33961781), TNFRSF1B(co-IP)

PPI以PRKACA(0.51实验)和RELA(0.51实验)为核心，直接关联cAMP-PKA-NF-kB信号轴。LNX1(ligand of numb-protein X1, E3泛素连接酶)的直接互作(holdup assay)尤其有趣——LNX1通过泛素化调控NOTCH和NUMB信号，可能在核内通过降解AKIP1调控NF-kB活性。**评分: 6/10** (因PRKACA+RELA双实验确认且生物学功能明确)。

### 5. Rescue Decision

**决策: RESCUED TO SCORED**

**核定位评分修正**: 从3/10 → 6/10。修正依据:
1. HPA Nucleoplasm (Supported) 纯核定位
2. UniProt Nucleus (IDA ×2) 双实验验证
3. GO-CC nucleoplasm (IDA:HPA) 单一纯核GO-CC
4. 零胞质/膜注释，纯核定位蛋白
5. 功能本身为核定位调控 (RELA nuclear retention enhancer)

**修正后加权总分**: 97/180 (53.9/100)。总分相对较低(主要因为PubMed热度+低AF质量)，但这反映了各维度独立评分的原则——核定位评分应在其自身维度公正评估。

**AKIP1应进入scored蛋白列表，但需注意其局限性**: 蛋白小(210aa)、高度无序(31% pLDDT<50)、PubMed热度中等(61篇)。其核心吸引力在于: (1) 纯核定位; (2) NF-kB信号通路的直接核调控因子; (3) NF-kB-ERV激活的潜在交叉点。在scored列表中，可根据实验优先级综合考虑。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ31
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKIP1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000166452-AKIP1
- STRING: https://string-db.org/network/9606.ENSP00000362598
- IntAct: https://www.ebi.ac.uk/intact/interactors/id:Q9NQ31
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/AKIP1.json (2026-06-03)

HPA IF图像可在线获取(Supported, Nucleoplasm, 多细胞系)，未下载本地。PAE未生成本地。

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ31-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQ31 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033214; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166452-AKIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| POC1A | Biogrid, Bioplex | true |
| PRKACA | Intact, Biogrid | true |
| FGFR3 | Intact | false |
| FHL2 | Intact | false |
| GSN | Intact | false |
| POC1B | Bioplex | false |
| RELA | Biogrid | false |
| SENP8 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
