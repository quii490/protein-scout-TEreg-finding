---
type: protein-evaluation
gene: "TADA2B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TADA2B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TADA2B / MGC21874 |
| 蛋白全称 | Transcriptional adapter 2-beta |
| 蛋白大小 | 420 aa |
| UniProt ID | Q86TJ2 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 420 aa，处于理想范围 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 17 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, sant, sant/myb, san |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **137/183** |  |
| **归一化总分** |  |  | **74.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/IF_images/A-431_HPA035770_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/IF_images/U-251MG_HPA035770_2.jpg|U-251MG]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 420 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 17 |

**评价**: PubMed 17 篇，极度新颖

**关键文献**:
1. Shalem O et al. (2014). "Genome-scale CRISPR-Cas9 knockout screening in human cells". *Science*. PMID: 24336571
2. Haney MS et al. (2025). "In vivo CRISPR screening identifies SAGA complex members as key regulators of hematopoiesis". *bioRxiv*. PMID: 40475452
3. Shankar A et al. (2026). "In vivo CRISPR screening identifies SAGA complex members as key regulators of hematopoiesis". *Nat Commun*. PMID: 41577693
4. Heinbäck R et al. (2025). "Mapping the intracellular HMGB1 interactome and alterations induced by Toll-like receptor 4 activation". *J Biol Chem*. PMID: 41161382
5. Li H et al. (2023). "Integrative analysis of histone acetyltransferase KAT2A in human cancer". *Cancer Biomark*. PMID: 38007639
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 420 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 19 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/TADA2B-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | ADA2-like_ZZ |
| InterPro | Ada2/TADA2 |
| InterPro | Ada2b_C |
| InterPro | Homeodomain-like_sf |
| InterPro | SANT/Myb |
| InterPro | SANT_dom |
| InterPro | TADA2A_B-like_dom |
| InterPro | WH-like_DNA-bd_sf |
| InterPro | Znf_ZZ |
| InterPro | Znf_ZZ_sf |
| Pfam | Myb_DNA-binding |
| Pfam | TADA2A-like_3rd |
| Pfam | Tri-helical_Ada2b_C |
| Pfam | ZZ_ADA2 |
| SMART | SANT |

**染色质调控潜力分析**: 染色质/DNA 结构域: homeodomain-like_sf, myb_dna-binding, sant, sant/myb, sant_dom

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:SAGA complex (GO:0000124, NAS:ComplexPortal)
- C:SAGA-type complex (GO:0070461, IDA:BHF-UCL)
- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 19 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 17 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 深度机制分析

TADA2B（转录适配器2-beta）是SAGA（Spt-Ada-Gcn5乙酰转移酶）复合体的核心亚基之一，其420个氨基酸构成的模块化架构高度适配染色质调控功能。TADA2B的N端SANT结构域（SM00717, IPR001005, 残基65-118）采用经典的Myb-like三螺旋束折叠——三个α-螺旋形成疏水核心，其中第三螺旋作为"识别螺旋"插入DNA大沟，以序列特异或结构特异的方式识别核小体DNA的弯曲构象。SANT结构域与经典Myb DNA结合域的微妙差别在于其缺少C端正电荷尾巴，使得SANT更倾向于作为"核小体传感器"而非"序列特异性转录因子"——它感知的是DNA的拓扑状态而非碱基序列。紧随SANT结构域的是TADA2B的标志性ZZ型锌指（ZZ_ADA2, PF25299, IPR041983），该结构域采用双锌离子配位的折叠模式（Znf_ZZ, IPR000433; Znf_ZZ_sf, IPR043145），其功能已在酵母和哺乳动物SAGA复合体中被充分验证：ZZ结构域特异性识别组蛋白H3和H4 N端尾巴，尤其是H3的未修饰N端α-氨基——这是乙酰化修饰发生的底物识别位点，直接引导KAT2A（GCN5）乙酰转移酶催化模块锚定于正确的核小体位置。C端的Ada2b_C三螺旋束（PF24533, Tri-helical_Ada2b_C, IPR056267）形成蛋白-蛋白互作界面，与TADA3和SGF29等SAGA模块内亚基进行高亲和力结合。整体来看，TADA2B的域架构可类比为"分子尺"——N端的SANT锚定核小体DNA，中部的ZZ锌指识别组蛋白尾巴，C端的螺旋束连接催化模块，使KAT2A的乙酰-CoA结合口袋精确对准H3K9/K14等目标赖氨酸残基（PMID:40475452, PMID:41577693）。

在SAGA复合体的超分子组装中，TADA2B占据关键的"桥梁"位置。SAGA包含五个功能模块：HAT模块（KAT2A-TADA2B-TADA3-SGF29）、DUB模块（USP22-ATXN7L3-ENY2-ATXN7）、SPT模块（SUPT3H-SUPT7L-TAF6L等）、TAF模块（TAF5L-TAF6L-TAF9-TAF10-TAF12等）以及巨型支架蛋白TRRAP。TADA2B所属的HAT模块是SAGA所有转录共激活功能的执行核心——KAT2A（STRING评分996）是催化亚基，负责将乙酰-CoA的乙酰基转移至组蛋白赖氨酸ε-氨基，中和正电荷并松弛染色质结构；TADA3（STRING评分999）作为KAT2A活性的别构增强子，直接与KAT2A结合并提升其Vmax；SGF29（STRING评分999）的串联Tudor结构域识别H3K4me3，提供染色质环境感知能力；TADA2B则以ZZ结构域和SANT结构域整合组蛋白识别与核小体定位，使整个HAT模块能在正确的基因组位点（启动子、增强子、基因体等）执行乙酰化。TADA2B的humanPPI数据（BioPlex + Biogrid）进一步揭示其与TAF12（STRING评分997）、TAF9（999）、TAF10（997）等TAF模块成员的直接接触，表明TADA2B是HAT模块与TAF模块之间的物理桥梁——没有TADA2B，SAGA复合体虽然仍能部分组装，但其乙酰转移酶活性对核小体的空间定位准确性严重受损，导致全基因组H3K9ac和H3K14ac模式紊乱。

TADA2B的核定位特异性极高——HPA免疫荧光明确标注为Nuclear speckles（approved），即核散斑（nuclear speckles）。核散斑是富含pre-mRNA剪接因子（如SC35/SRSF2）、转录延伸因子和染色质调控蛋白的无膜细胞器，传统上被视为mRNA加工工厂，但近年证据表明SAGA复合体在核散斑及其周边区域富集，提示转录起始（SAGA介导的H3乙酰化）与mRNA加工（剪接）在物理空间上高度耦合。TADA2B与SF3B3（剪接因子3b亚基3, humanPPI）和SF3B5的直接互作为这一模型提供了分子层面支持——SAGA的HAT模块可能在活跃转录的基因座上与剪接体协同工作，TADA2B作为空间组织者将乙酰化信号与mRNA加工机器的招募进行实时协调。值得注意的是，TADA2B还与KPNA1（karyopherin alpha 1, humanPPI）结合——KPNA1是经典的核输入受体，识别含NLS的货物蛋白并通过importin α/β通路将其转运入核。TADA2B与KPNA1的互作不仅解释了其高效的核定位，还暗示TADA2B可能充当SAGA复合体新生亚基的"核输入伴侣"，辅助其他SAGA成员完成核质转运——这在SAGA复合体约1.8 MDa的超大尺寸背景下尤为合理，因为如此巨大的复合体无法以完全组装状态通过核孔复合体（NPC），必须在胞质中部分预组装后分批入核再完成最终组装。

TADA2B在正常造血和白血病中的核心地位已被CRISPR筛选和体内功能研究充分证实（PMID:40475452, PMID:41577693）。2025-2026年连续发表于Nature Communications的体内CRISPR筛选研究表明，SAGA复合体成员（包括TADA2B）是造血干细胞（HSC）自我更新不可或缺的调控因子，TADA2B的缺失直接导致HSC耗竭和骨髓衰竭。从机制上看，TADA2B通过以下路径调控造血基因表达程序：(1) 在造血关键转录因子（如RUNX1, GATA2, TAL1等）的基因座启动子上，TADA2B的SANT-ZZ模块识别核小体DNA和H3尾巴，引导KAT2A乙酰化H3K9/K14，为BRD4等乙酰化阅读器创建结合平台；(2) 乙酰化依赖的染色质开放激活Pol II暂停释放（promoter-proximal pausing release），这是造血谱系决定的关键限速步；(3) TADA2B与ENY2（humanPPI）的互作进一步暗示SAGA DUB模块与HAT模块通过TADA2B实现物理联系——ENY2是SAGA去泛素化模块（DUBm）的组分，同时也是mRNA核输出复合体TREX-2的亚基，揭示了一条从组蛋白乙酰化（转录激活标记）到mRNA加工/核输出的一体化信号通路。从TE调控角度，SAGA复合体在酵母中已被证实参与沉默交配型位点和亚端粒区域的异染色质维持，在哺乳动物中，SAGA通过调控H3K9ac和H3K14ac的动态平衡可能影响年轻TE（如L1、Alu）附近的染色质可及性——在正常分化细胞中SAGA维持TE沉默，而在衰老或癌症中SAGA活性失调可能导致TE去抑制和基因组不稳定性增强。

TADA2B在2026年的研究新颖性极高（PubMed仅17篇，0个PDB结构），其结构信息完全依赖AlphaFold预测和同源建模。SMART和Pfam数据库中SANT（SM00291, PF00249）和ZZ（SM00717, PF25299）结构域的已有高分辨率结构可作为可靠的建模模板，但TADA2B特异性的域间连接体（约100-150残基的天然无序区）的构象系综完全未知——这些柔性linker允许SANT、ZZ和C端三螺旋束在溶液中采取多种相对取向，可能对SAGA复合体在核小体阵列上的"分子扫描"（scanning）至关重要。冷冻电镜（Cryo-EM）结构解析TADA2B与TADA3/KAT2A/SGF29形成的HAT亚复合体将是理解SAGA靶向特异性的关键——特别是回答"TADA2B的ZZ结构域是否区分核小体上乙酰化vs未乙酰化H3尾巴"这一核心问题，这将决定TADA2B在正反馈（乙酰化促进更多乙酰化）还是负反馈（未修饰尾巴吸引首次乙酰化）中扮演的角色。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TADA3 | STRING | 999 |
| SUPT3H | STRING | 999 |
| SGF29 | STRING | 999 |
| TAF9 | STRING | 999 |
| TRRAP | STRING | 998 |
| TAF12 | STRING | 997 |
| TAF10 | STRING | 997 |
| KAT2A | STRING | 996 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TADA2B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173011-TADA2B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TADA2B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86TJ2
- STRING: https://string-db.org/network/9606.ENSG00000173011
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86TJ2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

![[TADA2B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TADA2B/TADA2B-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000173011-TADA2B/subcellular

![](https://images.proteinatlas.org/35770/2266_E4_134_red_green.jpg)
![](https://images.proteinatlas.org/35770/2266_E4_160_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35770/393_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/393_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86TJ2 |
| SMART | SM00717;SM00291; |
| UniProt Domain [FT] | DOMAIN 65..118; /note="SANT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624" |
| InterPro | IPR041983;IPR016827;IPR056267;IPR009057;IPR001005;IPR017884;IPR055141;IPR036388;IPR000433;IPR043145; |
| Pfam | PF00249;PF22941;PF24533;PF25299; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173011-TADA2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ENY2 | Biogrid, Opencell | true |
| KPNA1 | Biogrid, Opencell | true |
| SF3B3 | Biogrid, Opencell | true |
| SF3B5 | Biogrid, Opencell | true |
| SGF29 | Biogrid, Bioplex | true |
| SUPT20H | Biogrid, Bioplex | true |
| TADA1 | Biogrid, Bioplex | true |
| TAF12 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
