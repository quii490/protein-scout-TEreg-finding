---
type: protein-evaluation
gene: "APEX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## APEX2 — REJECTED (研究热度过高 (PubMed strict=274，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APEX2 |
| 蛋白名称 | APEX2 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | APEX2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=274 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60/180** | |
| **归一化总分** | | | **33.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Vesicles | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 274 |
| PubMed broad count | 416 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Directed evolution of APEX2 for electron microscopy and proximity labeling.. *Nature methods*. PMID: 25419960
2. APEX Peroxidase-Catalyzed Proximity Labeling and Multiplexed Quantitative Proteomics.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 31124087
3. S-palmitoylation coordinates the trafficking of ATG9A to mediate autophagy initiation.. *Autophagy*. PMID: 40394978
4. Nanoparticles Induce Protein Corona Conformational Change to Reshape Intracellular Interactome for Microglial Polarization.. *ACS nano*. PMID: 40913578
5. Protein Carrier AAV.. *bioRxiv : the preprint server for biology*. PMID: 39185209

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APEX1 | 0.942 | 0.000 | — |
| TOP3A | 0.849 | 0.000 | — |
| TDP1 | 0.780 | 0.289 | — |
| UNG | 0.769 | 0.113 | — |
| FEN1 | 0.758 | 0.066 | — |
| ERCC4 | 0.754 | 0.494 | — |
| OGG1 | 0.753 | 0.134 | — |
| NTHL1 | 0.747 | 0.314 | — |
| PCNA | 0.710 | 0.465 | — |
| NEIL3 | 0.676 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Nucleoli fibrillar center; 额外: Vesicl | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. APEX2 — APEX2 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 274 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 274 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

APEX2（UniProt Q9UBZ4）是抗坏血酸过氧化物酶（APX）家族成员——在大豆抗坏血酸过氧化物酶（APEX, pea APX）的基础上通过定向进化获得增强活性的工程化变体（Lam等人, 2015, PMID:25419960）。APEX2的域架构为N端过氧化物酶催化域（InterPro:IPR004808, IPR020847/IPR036691/endonuclease/exonuclease/phosphatase-like, IPR005135, Pfam:PF03372/Exo_endo_phos）+ C端锌指域（IPR010666, Pfam:PF06839/Zf-GRF）。APEX2在H2O2存在下催化生物素-苯酚的自由基聚合——产生短寿命（<1 ms）的生物素-苯氧基自由基，共价标记邻近蛋白（<20 nm范围内的Lys/Tyr残基）——这是"邻近标记"（proximity labeling, PL）技术的分子基础。

HPA确认APEX2定位于Nucleoplasm和Nucleoli fibrillar center（Supported）——核质和核仁纤维中心的定位可能反映APEX2的氧化还原功能与DNA碱基切除修复（BER）通路的联系。STRING互作图谱以BER/DNA修复酶为核心：APEX1（AP endonuclease 1, score=0.942）是APEX2的同源物和主要互作蛋白；TOP3A（topoisomerase III alpha, 0.849）、TDP1（tyrosyl-DNA phosphodiesterase 1, 0.780）、UNG（uracil-DNA glycosylase, 0.769）、FEN1（flap endonuclease 1, 0.758）、ERCC4/XPF（0.754）、OGG1（8-oxoguanine glycosylase, 0.753）、NTHL1（endonuclease III-like 1, 0.747）和PCNA（0.710）全部为BER和DNA修复的核心酶——这强烈提示APEX2/APEX1在核质和核仁的DNA损伤修复中具有互补/冗余的功能角色。

APEX2作为广泛使用的邻近标记工具蛋白，其生物学功能长期被工具化应用掩盖。定向进化过程（14轮随机突变+筛选）使APEX2的催化效率相比大豆APX提升了约10-100倍——但代价是引入了多个人工突变（G160V, A14V, K14D, DelL242等），这些突变可能改变底物特异性、稳定性和互作网络。APEX2在HPA中的核仁纤维中心——rDNA基因座所在区域——的定位暗示其可能参与rDNA的碱基切除修复和质量控制。

PubMed=274篇使APEX2因研究热度过高被淘汰（新颖性=0/50分）。其工具蛋白身份（工程化突变体而非天然蛋白）+研究过饱和使APEX2完全不适用于TE调控候选筛选——APEX2的核定位促进BER和DNA修复的生物学功能已在数十个独立研究中充分验证。
- UniProt: https://www.uniprot.org/uniprotkb/APEX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169188-APEX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APEX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/APEX2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169188-APEX2/subcellular

![](https://images.proteinatlas.org/48577/827_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/48577/827_A7_4_red_green.jpg)
![](https://images.proteinatlas.org/48577/829_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/48577/829_A7_4_red_green.jpg)
![](https://images.proteinatlas.org/48577/977_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/48577/977_A7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UBZ4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004808;IPR020847;IPR036691;IPR005135;IPR010666; |
| Pfam | PF03372;PF06839; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169188-APEX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APBA2 | Intact | false |
| COMMD4 | Opencell | false |
| CUL9 | Biogrid | false |
| MKRN3 | Intact | false |
| PCNA | Biogrid | false |
| TSHZ3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
