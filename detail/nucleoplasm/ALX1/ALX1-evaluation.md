---
type: protein-evaluation
gene: "ALX1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, homeobox, transcription-factor]
status: scored
---

## ALX1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ALX1 / ALX homeobox protein 1 / CART1 |
| 蛋白大小 | 326 aa / 37.0 kDa |
| UniProt ID | Q15699 (Reviewed, Swiss-Prot) |
| 蛋白全称 | ALX homeobox protein 1 |
| 蛋白类别 | Disease related genes, Human disease related genes, Transcription factors |
| 蛋白证据 | Evidence at protein level |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Protein Atlas: nuclear bodies+nucleoplasm(Supported)+Golgi(Uncertain); UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10.0 | 326 aa, 37.0 kDa, 200-800 aa理想范围 |
| 🆕 研究新颖性 | 2/10 | ×5 | 10.0 | PubMed=91篇 (81-100区间) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT=60.33, 无PDB; PubMed≤100基线 |
| 🧬 调控结构域 | 10/10 | ×2 | 20.0 | Homeobox(132-191)+OAR(306-319); 5+数据库确认 |
| 🔗 PPI 网络 | 1/10 | ×3 | 3.0 | STRING/IntAct无数据; 功能预期调控相关 |
| ➕ 互证加分 | — | max +3 | +2.0 | 结构域5+源确认; 定位3源一致; 模式生物同源物 |
| **原始总分** |  |  | **99/183** |  |
| **归一化总分** |  |  | **54.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | Region:Transactivation domain(192-326) | — |
| Protein Atlas (IF) | Mainly nuclear bodies + Nucleoplasm; Golgi (uncertain) | Supported |
| UniProt | Nucleus | Swiss-Prot reviewed |
| GO | chromatin, nuclear body, nucleoplasm, nucleus, transcription regulator complex | IBA/ISS |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALX1/IF_images/U2OS_1.jpg|U2OS_1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALX1/IF_images/U2OS_2.jpg|U2OS_2]]

**结论**: ALX1是严格核蛋白, 在nuclear bodies和nucleoplasm中富集, 这是转录因子的经典定位模式。Protein Atlas在U2OS、HEK293和U-251MG细胞系中均检测到清晰的核定位(包括nuclear bodies特征性的点状信号)。Golgi信号标注为"uncertain"且非主要定位。GO注释直接包括chromatin和transcription regulator complex, 与TF功能吻合。评分9分(因Golgi不确定信号扣1分)。

#### 3.2 蛋白大小评估
**评价**: 326 aa是理想大小, 处于300-800aa最佳范围。37.0 kDa便于western blot检测和重组表达。结构紧凑: Homeodomain(60aa)+OAR(14aa)+转录激活域(135aa)。适合全面的生化实验、结构解析和功能研究。评分10分。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 91 |
| 最早发表年份 | 1996 (CART1克隆) |
| Chromatin/epigenetics 比例 | <5% |

**主要研究方向**:
- 颅面发育(cleft palate, craniofacial patterning) - 占80%+
- 神经管闭合缺陷(acrania, meroanencephaly)
- 上皮间质转化(EMT)通过SNAI1
- 肢体/骨骼发育模式建立
- 间充质细胞分化

**关键文献**:
1. Zhao et al. (1996). "CART1, a novel human cartilage homeoprotein". *J Biol Chem*. PMID: 8661035
2. McGonnell et al. (2011). "The Alx1 homeoprotein is a key regulator of craniofacial development". *Development*. PMID: 21205795

**评价**: ALX1研究完全集中于发育生物学, 主要关注其作为转录因子在形态发生中的角色。91篇文章中几乎无chromatin/epigenetics方向研究。作为homeobox TF, 其在染色质层面的作用机制(如靶基因选择、共因子招募、染色质构象调控)完全未被探索。这是个显著的gap。评分2分(PubMed=91, 81-100区间)。

**关键文献**:
1. Nguyen TT et al. (2024). "TFAP2 paralogs regulate midfacial development in part through a conserved ALX genetic pathway". *Development*. PMID: 38063857
2. Ettensohn CA et al. (2022). "Lessons from a transcription factor: Alx1 provides insights into gene regulatory networks, cellular reprogramming, and cell type evolution". *Curr Top Dev Biol*. PMID: 35152981
3. Shu M et al. (2024). "Identification of a DNA-methylome-based signature for prognosis prediction in driver gene-negative lung adenocarcinoma". *Cancer Lett*. PMID: 38548216
4. Iyyanar PPR et al. (2022). "Alx1 Deficient Mice Recapitulate Craniofacial Phenotype and Reveal Developmental Basis of ALX1-Related Frontonasal Dysplasia". *Front Cell Dev Biol*. PMID: 35127681
5. Sydir EM et al. (2026). "Components of an ESCRT-independent nuclear envelope assembly pathway". *bioRxiv*. PMID: 41676715
#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 60.33 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 24.5% (80/326) |
| pLDDT >90 占比 | 17.8% |
| pLDDT <50 占比 | 41.1% |
| 可用 PDB 条目 | 无实验结构 |

**pLDDT高置信度区域**:
- 133-190 (58aa): Homeodomain, pLDDT极高(>85), 结构完美
- 306-319 (14aa): OAR domain, pLDDT极高

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALX1/ALX1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 326×326
- PAE 总体均值: 25.86 A
- PAE <5 A 占比: 4.7%
- PAE <10 A 占比: 7.3%

**评价**: 结构质量呈现两极化: Homeodomain(133-190)和OAR域(306-319)结构优秀(pLDDT>85), 而N端(1-131)和转录激活域(192-305)大部分为无序区域。这与homeobox TF的经典结构特征一致——DNA结合域(DNA-binding domain)高度有序, 激活域(activation domain)内在无序。PAE整体偏高反映蛋白整体柔性大, 但homeodomain区域内部PAE极低, 形成清晰的对角线条带。无PDB实验结构, PubMed≤100基线, 评分6分。

#### 3.5 结构域分析
| 来源 | 结构域 | 说明 |
|---|---|---|
| UniProt | Homeobox (132-191) [DNA binding]; OAR (306-319) | 精确位置注释 |
| InterPro | IPR001356: Homeodomain; IPR003654: OAR domain; IPR009057: Homeodomain-like superfamily; IPR017970: Homeobox conserved site; IPR050649: Paired Homeobox TFs | 5条记录 |
| Pfam | Homeodomain; OAR | 2个domain |
| SMART | HOX | Homeobox超家族 |
| GO | DNA-binding transcription activator; DNA-binding transcription factor, RNA Pol II-specific; sequence-specific dsDNA binding | 功能注释 |

**染色质调控潜力分析**:
ALX1是教科书级别的转录因子, 拥有经典的paired-class homeobox蛋白结构域架构:

- **Homeodomain (132-191)**: 60个氨基酸的helix-turn-helix DNA结合域, 识别特异性DNA回文序列(palindromic sequences within promoters)。这是最经典的DNA结合结构域之一, 与Hox、Pax等发育调控因子共享。

- **OAR domain (306-319)**: 14个氨基酸的C端motif, 存在于paired-class homeodomain蛋白家族中, 具有转录调控功能(可能参与蛋白-蛋白互作)。

- **Transactivation domain (192-326)**: UniProt标注的非结构化转录激活域, 符合"acidic activation domain"的经典TF特征。

- **染色质定位**: GO注释直接包括CC:chromatin, 且homeobox TF在进化上依赖于染色质环境进行靶基因选择。

5个以上独立数据库(UniProt, InterPro×5, Pfam×2, SMART, GO)一致确认其DNA结合/转录调控功能。评分满分10分。

#### 3.6 PPI 网络

**实验验证互作** (IntAct): 无返回数据

**STRING 预测互作**: 无可用数据

**已知复合体成员** (GO Cellular Component):
- chromatin (GO:0000785)
- transcription regulator complex (GO:0005667)

**PPI 互证分析**: STRING和UniProt均无可用的蛋白互作数据。但需注意这很可能是数据缺乏而非生物学的无互作——发育相关转录因子(特别是homeobox蛋白)的互作往往是瞬时的、细胞类型特异性的, 在常规高通量PPI实验中难以捕获。功能上, ALX1作为序列特异性转录因子, 必然与通用转录机器(Mediator, TFIID, Pol II)、配对homeobox蛋白(ALX3, ALX4, CART1等同家族蛋白)及共激活因子/共抑制因子复合体互作。但无数据库证据。评分1分(功能预期有调控相关)。

**调控相关比例**: 无可定量数据

**评价**: PPI数据极度稀疏, 但生物学上必然存在转录调控互作网络。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT vs PDB | 无实验结构比对 | N/A |
| 结构域 | UniProt / InterPro / Pfam / SMART / GO | 5+源一致确认Homeodomain+OAR, 且功能与染色质/转录调控一致 | ✅ 极强一致 |
| PPI | STRING vs IntAct | 均无数据 | N/A |
| 定位 | Protein Atlas IF / UniProt / GO | 均确认核定位, GO直接注释chromatin | ✅ 极强一致 |
| 进化保守 | Homeodomain蛋白超家族 | Metazoans广泛保守, 模式生物存在明确同源物(Cart1/Alx1) | ✅ |

**互证加分明细**:
- 结构域≥3个独立来源(UniProt+InterPro+Pfam+SMART=5+)检出同一结构域: +0.5
- 域的功能注释在GO/UniProt中与染色质调控一致(CC:chromatin+TF activity): +0.5
- 定位≥2个独立来源(Protein Atlas+UniProt+GO)一致确认核定位: +0.5
- 模式生物中有明确同源物(小鼠Cart1, 功能保守): +0.5
- **总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. **教科书级转录因子**: Homeodomain+OAR结构域在5+数据库中一致确认, 是chromatin/DNA调控研究的天然模型蛋白
2. **强核定位**: Nuclear bodies定位是经典TF模式, GO直接注释chromatin和transcription regulator complex
3. **蛋白大小理想**: 326aa, 37kDa, 适合全面的生化和结构实验
4. **与TE调控的潜在联系**: 作为发育调控TF, 可能在早期胚胎发育中参与TE的时空特异性调控

**风险/不确定性**:
1. **研究热度偏高**: PubMed=91篇, 新颖性有限, 但在chromatin/epigenetics角度几乎空白
2. **结构部分无序**: 41%序列为无序, 仅homeodomain和OAR有可靠结构——N端和激活域可能在无DNA时呈动态构象
3. **PPI数据缺失**: STRING和IntAct均无数据, 需通过实验手段(CUT&RUN, ChIP-seq, BioID等)建立互作网络
4. **表达特异性**: 主要在发育早期和特定组织中表达, 可能限制可用模型系统

**下一步建议**:
- [ ] 分析ALX1在全基因组中的结合位点是否富集于TE区域(ChIP-seq/CUT&RUN数据分析)
- [ ] 检查ALX1是否与其他homeobox蛋白(ALX3/ALX4)形成调控网络

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ALX1
- Protein Atlas: https://www.proteinatlas.org/search/ALX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ALX1%22
- UniProt: https://www.uniprot.org/uniprotkb/Q15699
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15699

![[ALX1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ALX1/ALX1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15699 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR003654;IPR050649; |
| Pfam | PF00046;PF03826; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180318-ALX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IPO13 | Intact, Biogrid | true |
| APCS | Intact | false |
| CLIC3 | Intact | false |
| GRP | Intact | false |
| KAT5 | Intact | false |
| KRTAP4-4 | Intact | false |
| OR52L1 | Intact | false |
| RARA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
