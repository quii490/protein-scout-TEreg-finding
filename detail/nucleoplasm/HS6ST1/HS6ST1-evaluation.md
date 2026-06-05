---
type: protein-evaluation
gene: "HS6ST1"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## HS6ST1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | HS6ST1 / HS6ST |
| 蛋白全名 | Heparan-sulfate 6-O-sulfotransferase 1 |
| 蛋白大小 | 411 aa / 48.2 kDa |
| UniProt ID | O60243 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | HPA: Nucleoplasm Approved; UniProt: Membrane (ECO:0000305); GO: Golgi membrane/plasma membrane |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 411 aa, 48.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=54, broad=100 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 86.6; pLDDT >90 70.3%; 无 PDB |

![[HS6ST1-PAE.png]]
| 调控结构域 | 6/10 | ×2 | 12.0 | Sulfotransferase domain (PF03567); 硫酸乙酰肝素修饰酶 |
| PPI 网络 | 6/10 | ×3 | 18.0 | STRING HS2ST1 strongest (0.996); IntAct 多 coIP partner |
| **加权总分** | | | **108/180**** | |
| 互证加分 | | | +1.0 | HPA Approved; STRING HS biosynthesis pathway strong |
| **归一化总分 (÷1.83)** | | | **59.0/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Membrane (ECO:0000305) | Predicted |
| GO-CC | Golgi membrane (TAS:Reactome); plasma membrane (TAS:ProtInc) | Predicted |
| Protein Atlas (IF) | Nucleoplasm (Approved) | Approved |

**HPA IF 状态**: IF available (Approved reliability) — HPA 给出 Nucleoplasm Approved 定位。UniProt 和 GO-CC 均支持高尔基体膜和质膜定位，与典型的 sulfotransferase 分泌途径一致。HPA 的核质定位与 UniProt 膜定位存在矛盾，可能反映 HS6ST1 在核内合成硫酸乙酰肝素或细胞周期依赖的亚细胞分布变化。Kallmann syndrome 相关基因，神经发育中关键。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-O60243-F1 |
| 平均 pLDDT | 86.6 |
| pLDDT >90 | 70.3% |
| pLDDT 70-90 | 12.9% |
| pLDDT 50-70 | 7.5% |
| pLDDT <50 | 9.2% |
| PDB | 无 |
| InterPro | IPR010635, IPR027417, IPR005331 |
| Pfam | PF03567 (Sulfotransferase_3) |

**AlphaFold PAE 状态**: PAE 已下载，见上图。结构整体置信度良好（pLDDT 86.6），仅 <10% 残基置信度低于 50，折叠可信。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 54 |
| PubMed broad | 100 |
| 别名 | HS6ST（未用于 scoring） |

关键文献涉及 Kallmann syndrome/低促性腺激素性性腺功能减退症（PMID:23643382, PMID:20301509），Hs6st1 与 Fgfr1 在发育中的交叉通路（PMID:35899427），以及 Hs6st1/Hs2st 调控 Erk 信号促进胼胝体发育（PMID:24501377）。研究集中在发育神经生物学和硫酸乙酰肝素信号调控。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| HS2ST1 | STRING | 0.996 (exp 0.091) | Heparan sulfate biosynthesis |
| GLCE | STRING | 0.873 (exp 0.125) | Heparan sulfate epimerase |
| NDST1 | STRING | 0.755 (textmining) | Heparan sulfate N-deacetylase/sulfotransferase |
| HS3ST1 | STRING | 0.754 (textmining) | Heparan sulfate 3-O-sulfotransferase |
| PROKR2 | STRING | 0.724 (textmining) | Kallmann syndrome gene |
| ANOS1 | STRING | 0.732 (textmining) | Kallmann syndrome gene |
| NRG1 | IntAct | anti tag coIP (PMID:28514442) | Neuregulin, neural signaling |
| FBXO2 | IntAct | anti tag coIP (PMID:33961781) | Ubiquitin ligase |
| KRT31 | IntAct | validated Y2H (PMID:32296183) | Keratin |
| B3GNT3 | IntAct | anti tag coIP (PMID:28514442) | Glycosyltransferase |

STRING 网络以 textmining 为主集中于硫酸乙酰肝素生物合成途径（HS2ST1, GLCE, NDST1, NDST2 等）。IntAct 记录到 NRG1、FBXO2 等共免疫沉淀。无 UniProt 实验互作记录。PPI 指向糖胺聚糖代谢而非核功能网络。

### 4. 总体评价
HS6ST1 是一个定位信息存在内部矛盾的案例：HPA Approved Nucleoplasm vs UniProt/Golgi membrane。作为硫酸乙酰肝素修饰酶，其经典定位应为高尔基体，但 HPA 核质信号值得进一步验证。蛋白结构好（pLDDT 86.6）、研究量适中（PM=54）、Kallmann syndrome 相关使其有生物学意义。建议作为低优先级核质候选保留，重点验证 HPA 核定位信号的可靠性。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60243
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60243
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HS6ST1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136720-HS6ST1

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HS6ST1/IF_images/A-431_1.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HS6ST1/IF_images/U-251MG_1.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HS6ST1/HS6ST1-PAE.png]]

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HS6ST1/HS6ST1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60243-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
