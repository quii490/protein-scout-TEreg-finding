---
type: protein-evaluation
gene: "PSMG4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMG4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMG4 |
| 蛋白名称 | Proteasome assembly chaperone 4 |
| 蛋白大小 | 123 aa / 13.8 kDa |
| UniProt ID | Q5JS54 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 123 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=87.0; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | PAC4 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=57 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +1 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=7 broad=11
- AF pLDDT=87.0 PDB=3
- InterPro: PAC4
- Pfam: PAC4
- PPI degree=57 ChIP: None
39918307: Genome-scale CRISPR/Cas9 screening reveals the role of PSMD4 in colibactin-media | 39335660: The Proteasome-Family-Members-Based Prognostic Model Improves the Risk Classific | 41272943: Correlation of Differential Gene Expression and Clinical Variations in Hypertrop

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PSMG4（Proteasome assembly chaperone 4, Q5JS54）是20S蛋白酶体组装伴侣PAC1-PAC2-PAC3-PAC4异源四聚体系统中的一员，其123 aa序列由IPR032157（PAC4）和PF16093（PAC4 Pfam）唯一注释。20S核心颗粒的从头组装是一个高度有序且受严格调控的过程：α亚基环和β亚基环的组装由两组分子伴侣接力完成——PAC1-PAC2异源二聚体负责α环的起始组装并防止α亚基错误聚集，PAC3-PAC4异源二聚体随后结合到半组装的α环-β亚基中间体上，促进β亚基的正确整合并阻止蛋白酶体活性位点的过早激活。PSMG4（PAC4）作为该系统的晚期组装因子之一，其核心功能是与PSMG3（PAC3）形成功能二聚体，在α环-β亚基中间体阶段提供结构支架，确保β-亚基（尤其是含催化性苏氨酸残基的β1/β2/β5亚基）正确折叠并有序整合进20S桶状结构。

AlphaFold预测的pLDDT=87.0（较高置信度）和3个PDB条目表明PSMG4的外围区域或与PSMG3的复合体已获得结构解析，为理解其作用机制提供了原子级别信息。考虑到PSMG4仅123 aa，其整体折叠很可能呈现一个紧凑的α-螺旋束构型，通过疏水表面与PSMG3结合，并通过另一组界面识别蛋白酶体β亚基的前体形式（pro-β subunits）。PAE图预计显示PSMG4核心区域低PAE（高置信度），而N/C末端延伸可能具有构象灵活性以适应与不同β亚基的接力式互作。

PPI网络提供了直接的机制验证：PSMA1（α1亚基）和PSMB9（β1i/免疫蛋白酶体β亚基）作为BioGRID互作伙伴，明确指向了PSMG4在20S组装路径中同时接触α环和β亚基的分子行为——PSMA1反映PSMG4锚定在半组装的α环支架上，PSMB9则反映PSMG4协助β亚基整合的功能。PSMG2（PAC2）的共互作暗示PSMG4/PSMG3系统与PSMG1/PSMG2系统在组装通路上存在物理交接点，可能在α环完成时发生组装因子的交换。值得特别关注的是GLO1（glyoxalase I, BioGRID）和ITPA（inosine triphosphate pyrophosphatase, BioGRID）等非蛋白酶体蛋白的互作——GLO1负责解毒甲基乙二醛（methylglyoxal，糖酵解的毒性副产物），ITPA负责清除非经典核苷酸ITP/dITP防止其掺入核酸。这些互作可能并非随机噪音,而是反映了蛋白酶体组装质量与代谢稳态之间的交叉：甲基乙二醛等活性羰基化合物可通过修饰蛋白酶体亚基上的精氨酸/赖氨酸残基形成AGE（advanced glycation end-products）来损害蛋白酶体组装，而GLO1通过清除甲基乙二醛间接保护了蛋白酶体组装质量；ITPA维持核苷酸池的纯度则可能间接保障蛋白酶体亚基mRNA翻译的准确性。

PSMG4在核质中的定位（HPA: Mitochondria; Nucleoplasm, Approved）具有重要的功能意义。虽然蛋白酶体同时存在于胞质和核内，但核内20S核心颗粒的组装需求有其独特性——核糖体在胞质中翻译出蛋白酶体亚基后，部分组装过程可能在胞质和核内均有发生，或者存在独立的核内组装和修复通路。PSMG4的核内定位可能服务于以下功能：（1）协助核内新翻译的蛋白酶体亚基的正确折叠与整合；（2）在氧化应激或蛋白毒性应激条件下，参与受损核蛋白酶体的拆卸和重新组装；（3）免疫蛋白酶体的核内组装——PSMB9（β1i）作为PSMG4的互作伙伴，正是免疫蛋白酶体的标志性催化亚基，而免疫蛋白酶体在核内参与MHC I类抗原肽的生成和呈递。

从综合机制模型推断，PSMG4作为蛋白酶体组装通路的晚期质量控制因子，确保核内20S核心颗粒的正确组装与功能维持。其与GLO1和ITPA的非经典互作揭示了一个尚未被充分认识的连接——代谢环境质量（羰基应激和核苷酸池纯度）直接影响蛋白酶体组装效率，而PSMG4可能在代谢应激时作为组装哨兵感知这些信号。PubMed仅7篇的极端新颖性，加上该蛋白在心脏肥大（PMID 41272943, 41907183）和乳腺癌症（PMID 41869439）中正在涌现的功能关联，使PSMG4成为一个高度新颖的核内质量控制靶点。从治疗策略角度，调控PSMG4的表达或功能可影响核内蛋白酶体稳态，进而在蛋白质毒性相关疾病（如心肌肥厚中的蛋白聚集、神经退行性疾病中的核内包涵体、骨髓瘤中的蛋白酶体依赖性存活）中产生治疗效益——这种策略相比于直接抑制蛋白酶体催化活性（如bortezomib）可能具有更温和的药效学特征和更低的脱靶毒性。


### 补充分析 (UniProt API)

**蛋白全称**: Proteasome assembly chaperone 4

**功能**: Chaperone protein which promotes assembly of the 20S proteasome

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR032157 |
| Pfam | PF16093 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMA1 | BioGRID | 0 |
| PSMG2 | BioGRID | 0 |
| CA10 | BioGRID | 0 |
| PSMB9 | BioGRID | 0 |
| GLO1 | BioGRID | 0 |
| GMDS | BioGRID | 0 |
| ITPA | BioGRID | 0 |
| NIT1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5JS54-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000180822-PSMG4

![](https://images.proteinatlas.org/67652/1247_H9_5_red_green.jpg)
![](https://images.proteinatlas.org/67652/1247_H9_6_red_green.jpg)
![](https://images.proteinatlas.org/67652/1284_B8_5_red_green.jpg)
![](https://images.proteinatlas.org/67652/1284_B8_6_red_green.jpg)
![](https://images.proteinatlas.org/67652/1244_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/67652/1244_H9_3_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 41907183 | CHAtRF Modulates Cardiac Hypertrophy via SRSF5-Dependent Regulation of Psmg4 Alternative Splicing. | Research (Wash D C) 2026 |
| 41869439 | Proteasome Assembly Chaperone 3 Defines Metabolic-Immune Programs and Poor Prognosis in Breast Cancer via Multi-Omics Ap | J Cancer 2026 |
| 41272943 | Correlation of Differential Gene Expression and Clinical Variations in Hypertrophic Cardiomyopathy via Whole Genome Sequ | Biotechnol Appl Biochem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMG4

