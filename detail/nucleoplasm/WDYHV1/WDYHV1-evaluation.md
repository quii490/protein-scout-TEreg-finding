---
type: protein-evaluation
gene: "WDYHV1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## WDYHV1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | WDYHV1 |
| 蛋白名称 | Protein N-terminal glutamine amidohydrolase |
| 蛋白大小 | 205 aa / 23.7 kDa |
| UniProt ID | Q96HA8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 205 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=94.3; PDB=15 |
| 调控结构域 | 4/10 | ×2 | 8.0 | N_Gln_amidohydro_ab_roll_sf; NTAQ1; Prot_N_Gln_amidohydro_ab_roll |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=429 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=2 broad=3
- AF pLDDT=94.3 PDB=15
- InterPro: N_Gln_amidohydro_ab_roll_sf; NTAQ1; Prot_N_Gln_amidohydro_ab_roll
- Pfam: Nt_Gln_amidase
- PPI degree=429 ChIP: None
29351916: Pathways Impacted by Genomic Alterations in Pulmonary Carcinoid Tumors. | 32782434: Evaluation of the upregulation and surface expression of hypoxanthine guanine ph

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein N-terminal glutamine amidohydrolase

**功能**: Mediates the side-chain deamidation of N-terminal glutamine residues to glutamate, an important step in N-end rule pathway of protein degradation. Conversion of the resulting N-terminal glutamine to glutamate renders the protein susceptible to arginylation, polyubiquitination and degradation as specified by the N-end rule. Does not act on substrates with internal or C-terminal glutamine and does not act on non-glutamine residues in any position. Does not deaminate acetylated N-terminal glutamine

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037132 |
| InterPro | IPR039733 |
| InterPro | IPR023128 |
| Pfam | PF09764 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBR2 | STRING | 790 |
| ATE1 | STRING | 728 |
| XIAP | BioGRID | 1 |
| JUP | BioGRID | 1 |
| CBFA2T2 | BioGRID | 1 |
| TRIP13 | BioGRID | 1 |
| PCBD1 | BioGRID | 1 |
| RBBP8 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96HA8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000156795

![](https://images.proteinatlas.org/24823/231_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/231_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/24823/230_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/230_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/24823/232_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/24823/232_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/53680/965_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/53680/965_G12_2_red_green.jpg)

### 深度机制分析

WDYHV1（亦称为NTAQ1）编码N端谷氨酰胺酰胺水解酶，是**N端法则（N-end rule）蛋白降解途径的限速启动酶**。其核心催化结构域为PF09764（Nt_Gln_amidase），隶属于IPR037132超家族（N_Gln_amidohydro_ab_roll_sf），该折叠采用α/β滚轮状拓扑结构，活性位点特异性识别底物蛋白的N端谷氨酰胺残基。AlphaFold预测的整体pLDDT高达94.3，提示该205残基蛋白几乎完全有序折叠，15个PDB条目进一步验证了其结构的高度可信度。IPR039733（NTAQ1）注释明确将其归类为N端谷氨酰胺特异性酰胺水解酶，与作用于天冬酰胺的NTAN1形成正交底物选择性——仅催化N端Gln→Glu的脱酰胺转化，对内部或C端Gln以及乙酰化N端Gln完全无活性，这一严格的化学选择性奠定了其在蛋白质质量控制体系中的独特地位。

PPI网络分析揭示了一条完整的分层降解信号传导轴。STRING评分最高的两个互作伙伴——UBR2（790分）和ATE1（728分）——恰好分别代表N端法则的下游执行步骤：ATE1（精氨酰tRNA转移酶）将WDYHV1生成的N端Glu进一步修饰为N端Arg，而UBR2（E3泛素连接酶，含UBR-box识别N端降解子）识别N端Arg后催化底物多聚泛素化并靶向26S蛋白酶体降解。这一WDYHV1→ATE1→UBR2的线性信号传递链在生化逻辑上构成了一个近乎不可逆的分子计时器：一旦N端Gln被脱酰胺，底物蛋白的命运即被锁定，后续的精氨酰化和泛素化仅是无法回头的执行步骤。BioGRID鉴定到的XIAP（X连锁凋亡抑制因子）和RBBP8（CtIP，DNA双链断裂末端切除核酸酶）互作暗示该降解通路可能参与调控凋亡阈值设定与DNA损伤应答中的蛋白质稳态——这两个过程均依赖精确的蛋白质半衰期控制。

从结构生物学角度审视，pLDDT=94.3和15个PDB实验结构使WDYHV1成为当前数据集中结构表征最为充分的蛋白之一。高分辨率结构应能清晰展示催化三联体的精确几何排布以及底物结合口袋对N端Gln侧链酰胺基团的静电识别机制。值得特别注意的是，该蛋白仅205个残基却记录有429个PPI伙伴，这一异常高的degree/残基比值（约2.1 partners/residue）强烈提示其并非通过传统的蛋白质-蛋白质相互作用界面识别底物，而是主要通过酶活性位点短暂接触大量不同底物的N端——这是典型的"酶-底物"而非"支架蛋白"互作模式，高PPI degree在此反映的是底物广谱性而非稳定复合体形成。

综合机制模型：WDYHV1作为N端法则的"看门人"，在胞质和核质中对新生蛋白质或经蛋白酶体/caspase加工后暴露N端Gln的蛋白片段进行脱酰胺标记。该标记启动一个条件性降解程序——底物必须同时满足"暴露N端Gln"和"被脱酰胺"两个条件才会进入ATE1→UBR2→蛋白酶体通路。研究发现仅有3篇PubMed文献，且其中两篇（32782434、29351916）分别涉及急性淋巴细胞白血病HPRT表达和肺类癌基因组改变，无一篇为WDYHV1的直接功能研究，表明该蛋白的功能机制在人类疾病背景下近乎完全未被探索。其极低文献量与高置信度结构数据之间的显著反差，使其成为冷冻电镜结构-功能研究与化学生物学探针开发的理想靶标。靶向WDYHV1活性位点的小分子抑制剂理论上可选择性稳定特定N端Gln蛋白底物，为调控N端法则依赖的蛋白质质量控制提供全新的药理学切入点，尤其是在依赖特定短寿蛋白降解的细胞周期调控和凋亡通路中具有潜在治疗价值。

### PubMed 文献

**PubMed count: 3**

| 32782434 | Evaluation of the upregulation and surface expression of hypoxanthine guanine phosphoribosyltransferase in acute lymphob | Cancer Cell Int 2020 |
| 29351916 | Pathways Impacted by Genomic Alterations in Pulmonary Carcinoid Tumors. | Clin Cancer Res 2018 |
| 28600779 | The landscape of genetic diseases in Saudi Arabia based on the first 1000 diagnostic panels and exomes. | Hum Genet 2017 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/WDYHV1

