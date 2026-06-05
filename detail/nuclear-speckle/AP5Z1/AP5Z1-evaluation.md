---
type: protein-evaluation
gene: "AP5Z1"
date: 2026-06-01
tags: [protein-scout, nuclear-speckle, evaluation]
status: scored
---

## AP5Z1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AP5Z1 / KIAA0415, SPG48 |
| 蛋白全名 | AP-5 complex subunit zeta-1 |
| 蛋白大小 | 807 aa / 88.6 kDa |
| UniProt ID | O43299 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | HPA Supported: Nuclear speckles (main) + Nucleoplasm (additional); GO: nuclear speck IDA:HPA + nucleoplasm IDA:HPA + nucleus IDA:UniProtKB |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 807 aa, 88.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=18, broad=24 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 84.9; PDB 无 |

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/AP5Z1/AP5Z1-PAE.png]]
![[AP5Z1-PAE.png]]
| 调控结构域 | 5/10 | ×2 | 10.0 | AP-5 adaptor complex zeta subunit; 5 InterPro, 3 Pfam novel domains |
| PPI 网络 | 7/10 | ×3 | 21.0 | STRING 强 AP-5 complex 网络; IntAct NUP93/SPG11/MDFI/IRF2; NUP93 核孔连接 |
| **加权总分** | | | **131/180**** | |
| 互证加分 | | | +1.0 | UniProt/GO 多源 nuclear speck + nucleus 互证; DNA repair 功能注释; NUP93 核孔互作 |
| **归一化总分 (÷1.83)** | | | **71.6/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nuclear speckles (main), Nucleoplasm (additional) | Supported (HPA IF) |
| UniProt | Cytoplasm (ECO:0000269); Nucleus (ECO:0000269) | Experimental |
| GO-CC | cytoplasm IDA:UniProtKB; late endosome NAS; lysosome IEA; nuclear speck IDA:HPA; nucleoplasm IDA:HPA; nucleus IDA:UniProtKB | Experimental (IDA) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**核定位综合判断**: GO-CC 有 nuclear speck IDA:HPA 和 nucleoplasm IDA:HPA，UniProt 实验级（ECO:0000269）注释支持 Nucleus。HPA Supported 级别的 nuclear speck 主定位提供了明确的亚核结构指向，较之前的通用 "nucleus" 注释更精确。UniProt 双定位注释为实验级别，支持核散斑分类。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-O43299-F1 |
| 平均 pLDDT | 84.9 |
| pLDDT >90 | 54.6% |
| pLDDT 70-90 | 31.1% |
| pLDDT 50-70 | 9.4% |
| pLDDT <50 | 4.8% |
| PDB | 无 |
| InterPro | IPR028222, IPR055450, IPR011989, IPR056856, IPR056857 |
| Pfam | PF14764, PF25153, PF25154 |


#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 18 |
| PubMed broad | 24 |
| 别名 | KIAA0415, SPG48（未用于 scoring） |

关键文献包括 AP5Z1 在肝细胞癌中的作用 (PMID:40394639, PI3K/Akt/mTOR pathway)、遗传性黄斑营养不良 (PMID:40081374, AP-5 complex)、遗传性痉挛性截瘫 SPG48 (PMID:39059408, 25333062)。研究量中等偏低，蛋白在疾病背景下有一定关注度，但在核功能和 DNA repair 方面的独立研究较少。

#### 3.4 PPI 网络
| Partner | Source | Evidence/Method | Score/Experiments | PMID/Note | Relevance |
|---|---|---|---|---|---|
| AP5B1 | STRING | database 0.9 + textmining 0.98 | 0.998 | AP-5 beta1 subunit | AP-5 adaptor complex |
| AP5S1 | STRING + IntAct | database 0.9 + textmining 0.972; anti tag co-IP | 0.997 | PMID:33961781 | AP-5 sigma1 subunit |
| SPG11 | STRING + IntAct + UniProt | exp 0.435 + textmining 0.994; anti tag co-IP; UniProt exp 5 | 0.996 | PMID:33961781 | Spatacsin (SPG11 gene) |
| ZFYVE26 | STRING + UniProt | textmining 0.992; UniProt exp 5 | 0.992 | - | FYVE domain; SPG15 gene |
| AP5M1 | STRING | database 0.9 + textmining 0.741 | 0.973 | - | AP-5 mu1 subunit |
| AP4S1 | STRING | database 0.9 | 0.966 | - | AP-4 sigma1 subunit |
| AP4B1 | STRING | database 0.9 | 0.964 | - | AP-4 beta1 subunit |
| AP4E1 | STRING | database 0.9 | 0.962 | - | AP-4 epsilon1 subunit |
| NUP93 | IntAct + UniProt | two-hybrid array; UniProt exp 3 | - | PMID:32296183 | 核孔蛋白; 核质运输链接 |
| MDFI | IntAct | two-hybrid pooling | - | PMID:16189514 | MyoD family inhibitor |
| IRF2 | IntAct | anti tag co-IP | - | PMID:21903422 | 转录因子 |
| BUB1B | IntAct | pull down | - | PMID:32707033 | 有丝分裂检查点 |
| GPR182 | IntAct | anti tag co-IP | - | PMID:33961781 | GPCR |
| CXCR4 | IntAct | anti tag co-IP | - | PMID:33961781 | 趋化因子受体 |
| BAG2 | IntAct | anti tag co-IP | - | PMID:33961781 | BAG family chaperone |

**PPI 分析**: STRING 强支持 AP-5 adaptor complex 核心网络（AP5B1, AP5S1, SPG11, ZFYVE26, AP5M1），以及与 AP-4 adaptor complex 的交叉关联。IntAct 记录 NUP93（核孔蛋白，two-hybrid array）互作，提示可能与核孔复合体/核质运输有关联，为其 nuclear speck 定位提供可能的核输入机制线索。SPG11 和 ZFYVE26 均为遗传性痉挛性截瘫相关蛋白，在疾病网络中有重要意义。

### 4. 总体评价
AP5Z1 经 HPA 重新评估后确认为核散斑蛋白（HPA Supported: Nuclear speckles (main) + Nucleoplasm (additional)）。GO-CC 在 nuclear speck 和 nucleoplasm 均有 IDA 级别证据，UniProt 实验级注释支持 Nucleus。其主要功能背景为 AP-5 adaptor complex/endosomal transport，但 UniProt 功能注释提及可能参与 homologous recombination DNA DSB repair (PMID:20613862)，NUP93 核孔互作也提示核内功能。保留为中等置信度 nuclear-speckle 候选。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43299
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43299
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AP5Z1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000242802-AP5Z1
- HPA Subcellular: https://www.proteinatlas.org/ENSG00000242802-AP5Z1/subcellular
![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/AP5Z1/IF_images/AP5Z1_IF_35693.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/AP5Z1/AP5Z1-PAE.png]]

HPA IF 图像已本地嵌入。





![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/AP5Z1/AP5Z1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000242802-AP5Z1/subcellular

![](https://images.proteinatlas.org/35693/605_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/35693/605_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/35693/606_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/35693/606_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/35693/608_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/35693/608_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
