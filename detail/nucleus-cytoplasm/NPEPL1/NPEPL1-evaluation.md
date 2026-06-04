---
type: protein-evaluation
gene: "NPEPL1"
date: 2026-06-01
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## NPEPL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NPEPL1 |
| 别名 | KIAA1974 |
| 蛋白全名 | Probable aminopeptidase NPEPL1 |
| 蛋白大小 | 523 aa / 55.9 kDa |
| UniProt ID | Q8NDH3 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | HPA Approved: Nucleoplasm (Main) + Cytosol (Additional); GO: nucleus HDA + cytoplasm IBA; 双源互证 |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 523 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=12, broad=15 |
| 三维结构 | 8/10 | ×3 | 24.0 | AlphaFold pLDDT 94.3; PDB 无 |

![[NPEPL1-PAE.png]]
| 调控结构域 | 6/10 | ×2 | 12.0 | Peptidase M17 domain; 氨基肽酶催化功能 |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING: STX16/ATRIP/DNPEP/PRPF19/NCOA5; IntAct 7 条; UniProt 5 条 |
| **加权总分** | | | **130/180**** | |
| 互证加分 | | | +1.0 | HPA Approved Nucleoplasm + GO nucleus HDA 双源互证核定位 |
| **归一化总分 (÷1.83)** | | | **71.0/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| HPA | Reliability (IF): Approved; Nucleoplasm (Main) + Cytosol (Additional) | Experimental (IF) |
| GO-CC | cytoplasm (IBA:GO_Central); nucleus (HDA:UniProtKB) | Experimental (HDA) |
| UniProt | Subcellular Location: 无 | 无注释 |

**HPA 定位**: HPA API 已查询（ENSG00000215440）。Reliability (IF) = Approved。Subcellular location = Nucleoplasm + Cytosol，Nucleoplasm 为 Main，Cytosol 为 Additional。HPA IF 实验确认 NPEPL1 主要定位于核质，附加胞质溶胶信号。IF display images: 无（HPA 仅返回 IHC/RNA 缩略图及 IF 60x60 缩略图，无 IF display 原图）。Approved 可靠性 + Nucleoplasm 注释即为经过验证的亚细胞定位结论。
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/NPEPL1/IF_images/NPEPL1_IF_17025.jpg]]

**多源互证**: HPA Approved Nucleoplasm (Main) + GO nucleus HDA 形成双源核定位互证。GO cytoplasm IBA + HPA Cytosol (Additional) 共同支持胞质定位。核-胞质双定位模式成立。UniProt Subcellular Location 为空（尚未收录定位），但 HPA Approved + GO HDA 的双源互证已满足分类要求。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q8NDH3-F1 |
| 平均 pLDDT | 94.3 |
| pLDDT >90 | 91.2% |
| pLDDT 70-90 | 4.2% |
| pLDDT 50-70 | 1.0% |
| pLDDT <50 | 3.6% |
| PDB | 无 |
| InterPro | IPR011356 (Peptidase M17), IPR041417, IPR000819 |
| Pfam | PF18295, PF00883 (Peptidase M17 family) |

AlphaFold pLDDT 94.3（mean），结构预测置信度极高（91.2% >90）。PAE image URL 存在 (AF-Q8NDH3-F1-predicted_aligned_error_v6.png)，未生成本地副本。Peptidase M17 结构域为氨基肽酶催化域。
![[NPEPL1-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 12 |
| PubMed broad | 15 |

文献涉及基因组/表观遗传关联分析：母体过敏与子代甲基化 (PMID:32902349)、肾透明细胞癌生物标志物 (PMID:37483037)、前列腺癌预后基因签名 (PMID:33671634)、阿尔茨海默症 GWAS (PMID:33372590)、吸烟相关炎症的遗传开关 (PMID:38116482)。研究量低 (strict=12)，独立功能研究空间充足。

#### 3.4 PPI 网络
| Partner | Source | Evidence/Method | Score/Experiments | PMID/Note | Relevance |
|---|---|---|---|---|---|
| STX16 | STRING | textmining | score 0.783 (TM 0.627) | syntaxin-16, Golgi trafficking | textmining driven |
| UQCRFS1 | STRING | database | score 0.683 (db 0.673) | mitochondrial complex III | database association |
| THYN1 | STRING | database | score 0.673 (db 0.673) | thymocyte nuclear protein | 核蛋白，database association |
| ATRIP | STRING | experimental | exp 0.48, score 0.524 | ATR-interacting protein | 实验验证（DNA damage response） |
| DNPEP | STRING | experimental+textmining | exp 0.109, score 0.514 | aspartyl aminopeptidase | 同功能家族 |
| MCMBP | STRING | experimental | exp 0.471, score 0.471 | MCM complex binding protein | 实验验证（核蛋白, DNA replication） |
| PRPF19 | STRING | textmining | score 0.464 | pre-mRNA processing factor 19 | 核蛋白（spliceosome） |
| NCOA5 | STRING | textmining | score 0.452 | nuclear receptor coactivator 5 | 核蛋白 |
| TFCP2 | UniProt+IntAct | two hybrid array | 3 experiments | PMID:25416956 | 转录因子（核蛋白） |
| MDFI | UniProt+IntAct | two hybrid array | 3 experiments | PMID:32296183 | MyoD family inhibitor |
| LAMP2 | UniProt+IntAct | two hybrid array | 3 experiments | PMID:32814053 (Cell Rep) | lysosomal membrane |
| HIP1 | UniProt+IntAct | two hybrid array | 3 experiments | PMID:32814053 (Cell Rep) | huntingtin interacting protein |
| CASP6 | UniProt+IntAct | two hybrid array | 3 experiments | PMID:32814053 (Cell Rep) | caspase-6 |
| TFRC | IntAct | cross-linking | PMID:30021884 | transferrin receptor | 实验验证 |

PPI 网络中含多个核定位伙伴：THYN1 (database), ATRIP (DNA damage response, exp validated), MCMBP (DNA replication, exp validated), PRPF19 (spliceosome), NCOA5 (nuclear receptor), TFCP2 (transcription factor)。核互作方向一致但实验验证有限。

### 4. 总体评价
NPEPL1 是基于 HPA Approved Nucleoplasm + GO nucleus HDA 双源互证重新分类的核-胞质蛋白。此前因仅 GO HDA 单源核证据被拒绝，现 HPA 提供独立的 Approved 实验级核定位确认。蛋白功能为推测的氨基肽酶（Peptidase M17 family），结构预测优秀（pLDDT 94.3）。PPI 网络含多个核功能伙伴（ATRIP, MCMBP, PRPF19, TFCP2），与核定位一致。研究新颖性高（strict=12）。推荐为中等优先级 nucleus-cytoplasm 候选。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDH3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPEPL1
- HPA: https://www.proteinatlas.org/ENSG00000215440-NPEPL1

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/NPEPL1/NPEPL1-PAE.png]]

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/NPEPL1/NPEPL1-PAE.png]]


