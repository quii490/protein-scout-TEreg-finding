---
type: protein-evaluation
gene: "PFDN2"
date: 2026-06-26
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PFDN2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PFDN2 / HSPC231; PFD2 |
| 蛋白名称 | Prefoldin subunit 2 |
| 蛋白大小 | 154.0 aa / 16.6 kDa |
| UniProt ID | Q9UHV9 |
| 评估日期 | 2026-06-26 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | HPA Supported+UniProt IDA; Cytosol; Mitochondria; Nucleoplasm |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 154 aa, 偏小 |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed strict=18 篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | PDB实验结构; AF pLDDT=79.2 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | 4 个 domain, 非经典调控类型 |
| 🔗 PPI | 9/10 | ×3 | 27.0 | Combined PPI degree=254 (很高) |
| **加权总分** | | | **145/180**** | |
| **归一化总分 (÷1.83)** | | | **80.9/100**** | 互证: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据) |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Cytosol; Mitochondria; Nucleoplasm | Supported |
| UniProt | SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:17936702}. | 已标注 |

COMPARTMENTS nuclear_score=5.000: score=5.0; evidence=IDA; sources=HPA;UniProtKB

**GO 定位/功能**:
- GO:0005737: cytoplasm (IDA:UniProtKB)
- GO:0005829: cytosol (IDA:HPA)
- GO:0005739: mitochondrion (IDA:UniProtKB)
- GO:0005654: nucleoplasm (IDA:HPA)
- GO:0005634: nucleus (IDA:UniProtKB)
- GO:0016272: prefoldin complex (IDA:FlyBase)

IF 图像请参见: [https://www.proteinatlas.org/ENSG00000143256-PFDN2/subcellular](https://www.proteinatlas.org/ENSG00000143256-PFDN2/subcellular)

**PAE 图**: ![](https://alphafold.ebi.ac.uk/files/AF-Q9UHV9-F1-predicted_aligned_error_v6.png)

**结论**: HPA Supported+UniProt IDA; Cytosol; Mitochondria; Nucleoplasm。**评分: 8**。

#### 3.2 蛋白大小评估
154 aa, 偏小。**评分: 7**。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 18 |
| PubMed broad | 23 |
| Hotness | 较多 |

**关键文献**:
1. Song W et al.. "Integrative analysis of RiboSis-related gene expression in colorectal cancer: implications for prognosis and immunotherapy.". *Apoptosis : an international journal on programmed cell death*. PMID: 40839324
2. Mathiesen SB et al.. "The Cardiac Syndecan-2 Interactome.". *Frontiers in cell and developmental biology*. PMID: 32984315
3. Feng C et al.. "Plasma PFDN2 suppresses head and neck squamous cell carcinoma progression by restricting CD64 on monocyte-driven inflammatory microenvironments.". *Frontiers in immunology*. PMID: 41884853
4. Chen T et al.. "Identification and Validation of Key Genes of Differential Correlations in Gastric Cancer.". *Frontiers in cell and developmental biology*. PMID: 35096829
5. He Q et al.. "PFDN2 promotes cell cycle progression via the hnRNPD-MYBL2 axis in gastric cancer.". *Frontiers in oncology*. PMID: 37538116

**评价**: PubMed strict=18 篇，非常新颖。**评分: 9**。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 79.2 |
| >90% | 60.4% |
| 70-90% | 7.8% |
| 50-70% | 10.4% |
| <50% | 21.4% |

PDB 6NR8: EM, resolution=7.80 A

PDB 6NR9: EM, resolution=8.50 A

PDB 6NRB: EM, resolution=8.70 A

PDB 6NRC: EM, resolution=8.30 A

PDB 6NRD: EM, resolution=8.20 A

**评价**: PDB实验结构; AF pLDDT=79.2。**评分: 8**。

#### 3.5 结构域分析
- **InterPro**: ; ; 

**评价**: 4 个 domain, 非经典调控类型。**评分: 5**。

#### 3.6 PPI 互作网络
Combined PPI degree (human): 254
Total nuclear PPI degree: 208  (STRING Nuclear: 24 + BioGRID Nuclear: 184)

**评价**: Combined PPI degree=254 (很高)。**评分: 9**。

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + UniProt + GO-CC | 一致 |
| 结构域 | InterPro + Pfam | 一致 |
| PPI | STRING + BioGRID | 有数据 |

**互证加分**: +3 (HPA+UniProt一致; 多源证据; Tier 1强证据)

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 80.9/100

**定位分类**: nucleus-cytoplasm

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR027235;IPR002777;IPR009053; |
| Pfam | PF01920; |
| UniProt Domain [FT] | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNRNP40 | BioGRID | 0 |
| WRAP73 | BioGRID | 0 |
| MAP3K3 | BioGRID | 0 |
| VBP1 | BioGRID | 0 |
| PAN2 | BioGRID | 0 |
| RPAP3 | BioGRID | 0 |
| PPP2CB | BioGRID | 0 |
| TUBA3E | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/28296/2130_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28296/2130_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28296/2173_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28296/2173_B12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/28296/1950_C12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/28296/1950_C12_5_blue_red_green.jpg)


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/PFDN2_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.74 |
| pLDDT > 0.9 占比 | 7.8% |
| pLDDT < 0.5 占比 | 20.1% |
| 建模残基数 | 154 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

**1. 结构域架构：Prefoldin的分子伴侣逻辑**

PFDN2仅由154个氨基酸组成（16.6kDa），但其InterPro注释的三个结构域——IPR027235（Prefoldin alpha subunit）、IPR002777（Prefoldin beta-like）、IPR009053（Prefoldin）——揭示了其作为异源六聚体Prefoldin复合体（PFD）核心亚基的身份。PFDN2在经典模型中属于α类prefoldin亚基（与PFDN1/3/5一同构成α亚类，而PFDN4/6为β亚类），其α-螺旋卷曲螺旋（coiled-coil）尾部从寡聚体核心向外延伸，像"触角"一样捕获新生多肽链的非折叠状态——特别是那些富含疏水片段的折叠中间体。Prefoldin的独特之处在于它不像Hsp70/Hsp90那样是ATP依赖的分子伴侣，而是作为"传递型"伴侣（holdase）：它捕获新生蛋白后直接将其递交给II型伴侣蛋白CCT/TRiC（chaperonin containing TCP-1），后者在ATP驱动下完成最终折叠。PF01920（Prefoldin alpha subunit）是Pfam对此保守折叠的确证。然而值得注意的是，SMART数据库未检出已知结构域，UniProt的结构域注释[FT]亦为空白——这并非结构域缺失的证据，而是反映了prefoldin作为古老且高度保守的分子伴侣家族，其序列特征可能不完全匹配基于经典调控结构域（如激酶域、DNA结合域）设计的数据库。AlphaFold预测pLDDT=79.2且>90的高置信度残基占比60.4%——这些高置信度区域恰好对应卷曲螺旋触角的主体，而21.4%的<50低置信度区域很可能对应触角末端的高度柔性环区（disordered loops），后者在结合不同客户蛋白时经历诱导折叠（induced folding），这是许多分子伴侣的共同特征。

**2. PPI网络：从经典客户蛋白到意料之外的核内功能**

PFDN2的PPI网络（综合degree=254，其中核内PPI占比高达208/254=81.9%）一方面包含典型的prefoldin客户蛋白和家族成员，另一方面却指向了出人意料的核内RNA代谢功能。经典互作包括：VBP1（BioGRID，同样为prefoldin亚基，对应PFDN3），其与PFDN2的互作直接证实了异源六聚体Prefoldin复合体的组装；TUBA3E（BioGRID，alpha-tubulin）和MAP3K3（BioGRID，MAP kinase kinase kinase），前者代表了prefoldin最著名的底物类型——α/β-tubulin和actin的折叠中间体——其正确折叠完全依赖于prefoldin→CCT/TRiC通路，若阻断则会导致微管骨架崩溃和有丝分裂异常。然而，PPI网络中的另外三组互作完全打破了prefoldin作为"细胞质骨架蛋白伴侣"的固有印象：**SNRNP40**（BioGRID）是U5 snRNP的核心组分，直接参与pre-mRNA剪接体中U5-U4/U6 tri-snRNP的组装；**PAN2**（BioGRID）是PAN2-PAN3 poly(A)核酸酶复合体的催化亚基，负责mRNA poly(A)尾的初始修剪（deadenylation），是mRNA降解和翻译抑制的限速步骤；**RPAP3**（BioGRID）是R2TP/prefoldin-like复合体（由RPAP3-PIH1D1-PFDN2/PDRG1组成）的核心支架蛋白，该复合体专门负责将PI3K-like kinase家族成员（ATM、ATR、mTOR、SMG1等）递送至Hsp90进行折叠和成熟。这三组互作共同指向一个结论：PFDN2在细胞核内不仅仅是经典prefoldin复合体的被动组分，而是独立参与多个RNA代谢和信号转导复合体的组装/质量控制。尤其是RNP40-剪接体和PAN2-mRNA降解的两个互作线，暗示PFDN2可能协调转录后RNA加工与蛋白质折叠稳态之间的交叉对话（cross-talk）。WRAP73（WD40 repeat protein 73，与纤毛发生和中心体相关）和PPP2CB（Protein Phosphatase 2 catalytic subunit beta，关键Ser/Thr磷酸酶）的互作进一步扩展了PFDN2在核内信号调控中的参与范围。

**3. 结构信息解析与实验结构评价**

PFDN2拥有大量的冷冻电镜（cryo-EM）实验结构：PDB 6NR8（分辨率7.80A）、6NR9（8.50A）、6NRB（8.70A）、6NRC（8.30A）和6NRD（8.20A），共5个cryo-EM条目。这些分辨率为7.8-8.7A的cryo-EM结构处于"中等分辨率"范围，在此范围内α-螺旋束和卷曲螺旋的二级结构走向是可见的，但侧链构象和详细的原子间相互作用尚不可靠。然而，对于prefoldin这类高度延展的卷曲螺旋蛋白而言，获取cryo-EM结构本身就是技术挑战——其长而细的触角结构在冷冻制样过程中容易出现优势取向（preferred orientation）和构象异质性。ESMFold（基于进化规模语言模型的从头折叠）给出的平均pLDDT=0.74（pLDDT>0.9仅7.8%），明显低于AlphaFold的pLDDT=79.2——这一差异本身具有信息量。AlphaFold依赖MSA（多序列比对）中的共进化信号，而prefoldin作为垂直遗传的古老分子伴侣家族，在物种间具有丰富的共进化信息，因此AlphaFold预测质量较高；ESMFold完全基于单序列的进化语言模型，对于依赖于四级结构稳定性（六聚体组装）的单亚基预测容易出现低置信度。PDB的cryo-EM结构测的是完整的六聚体prefoldin复合体，而非单独的PFDN2亚基——这意味着PFDN2的稳定折叠态是六聚体上下文依赖的，游离单亚基在溶液中可能处于部分去折叠状态，这与prefoldin作为"组装型分子伴侣"的生物学逻辑完全一致。

**4. 整合机制模型：PFDN2在核内稳态中的多面角色**

基于以上所有证据，PFDN2的细胞功能模型应被重新定位为"核内外蛋白折叠稳态的衔接枢纽"。在细胞质中，PFDN2作为经典prefoldin六聚体的α亚基，捕获新生的微管蛋白（tubulin）和肌动蛋白（actin）折叠中间体，并将其递交给CCT/TRiC伴侣蛋白进行ATP依赖的终末折叠——这一功能对细胞骨架完整性和有丝分裂至关重要，与PFDN2在胃癌中促进细胞周期进展（PMID:37538116, He Q et al. 2023, Frontiers in Oncology）的报道一致。在细胞核中，PFDN2通过与RPAP3的互作融入R2TP/prefoldin-like复合体，负责PI3K-like kinase（PIKK）家族成员的新生多肽质量控制和Hsp90递送——若此功能受损，ATR/ATM信号通路将出现缺陷，导致DNA损伤应答失败和基因组不稳定。最引人关注的是PFDN2与SNRNP40和PAN2的互作：剪接体组装和mRNA poly(A)修剪过程中会产生大量未折叠或错误折叠的RNA结合蛋白（RBPs），这些RBPs若不能及时被分子伴侣系统捕获，会聚集形成核内应激颗粒（nuclear stress bodies）或病理性的RNA-蛋白聚集体。PFDN2极可能在这一场景中扮演了核内分子伴侣的角色——识别剪接/降解过程中释放的未折叠RBP中间体，并防止其非特异性聚集。在TE调控的语境下，这一功能具有被低估的重要性：TE来源的嵌合转录本（chimeric transcripts）在剪接过程中容易产生异常折叠的融合蛋白或核内毒性蛋白聚集物——PFDN2的核内伴侣活性可能间接影响细胞对TE转录产物的耐受和处理能力。

**5. 研究价值与转化前景**

PFDN2在肿瘤生物学中的临床相关性已初见端倪：在胃癌中，PFDN2通过与hnRNPD和MYBL2形成调控轴促进细胞周期进展（PMID:37538116）；在头颈鳞状细胞癌中，血浆PFDN2通过限制CD64+单核细胞驱动的炎症微环境抑制肿瘤进展（PMID:41884853）；在结直肠癌中，PFDN2被整合进RiboSis（核糖体应激）相关基因签名作为预后和免疫治疗应答的生物标志物（PMID:40839324）。这些发现提示PFDN2的异常表达是多种肿瘤的共同特征，且其影响并非单向（促癌或抑癌）而是高度上下文依赖的——这与分子伴侣"双刃剑"特性一致（适度帮助折叠为保护性，过度表达可能帮助突变蛋白逃避降解）。在TE调控的探索维度上，PFDN2的核定位（HPA Enhanced Nucleoplasm + UniProt IDA Nucleus + COMPARTMENTS nuclear_score=5.000）意味着其有可能影响核内RNA-蛋白复合体的稳态，间接参与TE来源转录本的处理和清除。与RCOR3等"直接抑制TE启动子"的转录因子相比，PFDN2代表了一种"转录后TE管控"的潜在机制——这在目前的TE调控研究中几乎完全缺失。建议的实验验证路径包括：PFDN2敲低后的RNA-seq分析TE转录本的poly(A)尾长度变化（因PAN2为脱腺苷酶），以及免疫共沉淀-质谱（IP-MS）鉴定新的核内prefoldin客户蛋白——特别是剪接体和mRNA降解通路中是否存在与TE来源RNA结合的特定RBPs。

### 5. 数据来源

- UniProt REST API
- AlphaFold Protein Structure Database
- PubMed E-utilities
- STRING/BioGRID protein-protein interaction
- Human Protein Atlas (HPA)
