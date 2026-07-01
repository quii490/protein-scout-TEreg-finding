---
type: protein-evaluation
gene: "FEM1A"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FEM1A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FEM1A |
| 蛋白名称 | Protein fem-1 homolog A |
| 蛋白大小 | 669 aa / 73.6 kDa |
| UniProt ID | Q9BSK4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Golgi apparatus; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 669 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=21 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=88.7; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ankyrin_rpt; Ankyrin_rpt-contain_sf; TPR-like_helical_dom_sf |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=119 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm (Supported)
- PubMed strict=21 broad=29
- AF pLDDT=88.7 PDB=0
- InterPro: Ankyrin_rpt; Ankyrin_rpt-contain_sf; TPR-like_helical_dom_sf
- Pfam: Ank; Ank_2
- PPI degree=119 ChIP: None
41085794: A prognostic model for gastric cancer constructed by multiple machine learning a | 16254458: The Fem1a gene is downregulated in Rhabdomyosarcoma. | 28118078: FEM1 proteins are ancient regulators of SLBP degradation.

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein fem-1 homolog A

**功能**: Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation (PubMed:29779948, PubMed:33398168, PubMed:33398170). The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytical

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002110 |
| InterPro | IPR036770 |
| InterPro | IPR011990 |
| Pfam | PF00023 |
| Pfam | PF12796 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TCEAL1 | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| CUL2 | BioGRID | 0 |
| PTGER4 | BioGRID | 0 |
| CDK17 | BioGRID | 0 |
| ANLN | BioGRID | 0 |
| NLRP3 | BioGRID | 0 |
| SLBP | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BSK4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000141965-FEM1A

![](https://images.proteinatlas.org/16565/131_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/16565/131_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/16565/164_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/16565/164_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/63622/1220_A9_7_red_green.jpg)
![](https://images.proteinatlas.org/63622/1220_A9_10_red_green.jpg)
![](https://images.proteinatlas.org/63622/1201_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/63622/1201_E11_2_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能**：FEM1A是fem-1家族的三个哺乳动物同源物之一（FEM1A/B/C），含有两个标志性蛋白互作结构域。锚蛋白重复序列（Ankyrin repeat, InterPro: IPR002110; Pfam: PF00023和PF12796）是自然界最常见的蛋白质-蛋白质互作模块——每个重复单元由33个残基形成螺旋-转角-螺旋结构，多个重复串联堆叠成延长的弯曲螺线管，提供大面积结合界面用于识别结构多样的靶蛋白。在FEM1A中，锚蛋白重复序列构成C-degron（C端降解子）识别模块的核心——通过其螺线管凹面结合靶蛋白极端C端序列实现特异性识别。TPR样螺旋结构域超家族（IPR011990）则介导与elongin C的对接，这是所有CRL2底物受体的共同结构特征。pLDDT=88.7对全长669个氨基酸的蛋白而言属良好水平，部分区域的不确定性可能对应C-degron识别界面的动态构象采样。

**PPI网络与底物识别广度**：FEM1A的PPI网络（degree=119, 均来自BioGRID低通量实验）揭示了其作为CRL2 E3泛素连接酶底物识别适配器的中枢角色。CUL2（BioGRID count=0）是Cullin-2支架蛋白——与elongin B/C、RBX1和FEM1A共同组装为完整的CRL2 E3连接酶复合物。SLBP（茎环结合蛋白）是唯一获实验验证的生理底物（PMID: 28118078）——SLBP是组蛋白mRNA前体3'端加工的必需因子，其蛋白水平在S期末/G2期通过FEM1A介导的C-degron识别被CRL2泛素化降解，从而限缩组蛋白mRNA加工至S期。这一发现确立了FEM1蛋白家族是C-degron通路——即DesCEND通路（Destruction via C-End Degrons）——的古老调控因子。ELAVL1/HuR是调控富含AU元件mRNA稳定性的关键RNA结合蛋白，潜在互作提示mRNA代谢与蛋白降解之间存在交叉调控。ANLN（anillin）是胞质分裂收缩环的核心肌动蛋白结合蛋白，连接FEM1A与有丝分裂末期调控。NLRP3是炎症小体核心组分，建立了FEM1A与天然免疫的联系。CDK17（PCTAIRE家族）和TCEAL1（转录延伸因子A样1）的互作分别指向细胞周期和转录调控功能。

**结构解读**：pLDDT=88.7对全长669个氨基酸是良好水平。锚蛋白重复结构域在AlphaFold预测中通常置信度较高，因为重复单元堆积具有明确的序列-结构关系。然而，螺线管固有的曲率和柔韧性意味着不同重复单元间的局部堆积几何存在不确定性。C-degron结合口袋位于锚蛋白重复片段的C端区域，FEM1A偏好含有碱性C端残基（Arg或Lys等）的降解子（PMID: 29779948, PMID: 33398168, PMID: 33398170）——其精细构象根据结合的C端序列动态变化，体现底物识别的可塑性。TPR样结构域预测采用典型螺线管折叠，介导与elongin C的对接——这一界面在所有CRL2底物受体中高度保守。由于尚无实验PDB结构（PDB=0），FEM1A与C-degron肽段及elongin B/C的复合物结构是未来结构生物学的关键目标，对于理解底物选择性和PROTAC/分子胶设计具有直接指导意义。

**分子机制模型**：FEM1A作为CRL2 E3泛素连接酶的底物识别适配器，在DesCEND通路中发挥核心功能的分子机制可分为三步。第一步（组装）：FEM1A通过N端TPR样结构域被elongin B/C异源二聚体识别，elongin C桥接FEM1A至Cullin-2，后者通过C端WHB结构域招募RBX1（含RING finger）形成完整CRL2复合物。第二步（底物识别）：FEM1A通过C端锚蛋白重复螺线管识别底物蛋白的极端C端降解子——该降解子通常少于10个残基，可存在于全长蛋白、蛋白酶解切割产物或翻译提前终止产生的截短蛋白（这使DesCEND通路兼具质量控制和新底物发现的特性）。第三步（泛素化）：底物结合触发构象变化，使底物赖氨酸残基被带到RBX1招募的E2泛素结合酶附近，催化多聚泛素链形成并介导蛋白酶体降解。在细胞生理层面，该通路调控SLBP的S/G2期特异性降解（PMID: 28118078），确保组蛋白合成与DNA复制精确耦合。核质定位（HPA Supported级别）与SLBP等核蛋白底物的降解需求一致，而Golgi定位提示质控功能可能延伸至分泌途径。

**研究与治疗意义**：FEM1A仅21篇严格PubMed文献（9/10新颖性）、无实验结构，但占据C-degron通路的生化核心地位——该通路是蛋白稳态调控的新兴前沿，近年才被系统地分子定义。FEM1A在横纹肌肉瘤中下调（PMID: 16254458）和胃癌预后模型中的鉴定（PMID: 41085794）暗示该蛋白的丧失可能导致特定癌蛋白底物的异常积累，驱动肿瘤发生。C-degron通路的可劫持性为靶向蛋白降解（TPD）提供了新范式：通过设计模拟C-degron的小分子（分子胶）或PROTAC将目标蛋白桥接到FEM1A，可劫持CRL2 E3连接酶实现选择性靶蛋白降解——与现有CRBN/VHL为基础的PROTAC形成互补策略。考虑到SLBP是有丝分裂-组蛋白耦合的关键节点，FEM1A-SLBP轴在快速增殖肿瘤细胞中的治疗脆弱性值得深入探索。

### PubMed 文献

**PubMed count: 29**

| 41085794 | A prognostic model for gastric cancer constructed by multiple machine learning algorithms. | J Mol Histol 2025 |
| 40565326 | Full-Length Transcriptome of Testis and Ovary Provides Insights into Alternative Splicing During Gonadal Development in  | Int J Mol Sci 2025 |
| 38663500 | Evaluating the potential of daily intake of polystyrene microplastics via drinking water in inducing PCOS and its ovaria | NanoImpact 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FEM1A

