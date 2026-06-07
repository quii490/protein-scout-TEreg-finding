---
type: protein-evaluation
gene: "TSPYL2"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## TSPYL2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TSPYL2 / CDA1, DENTT, TSPX, SE20-4, HRIHFB2216, CTCL, CINAP |
| 蛋白全名 | Testis-specific Y-encoded-like protein 2 |
| 蛋白大小 | 693 aa / 79.4 kDa |
| UniProt ID | Q9H2G4 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | Nucleus (ECO:0000269, 2x) + Cytoplasm (ECO:0000250); GO nucleoplasm TAS, nucleolus IDA, chromatin IBA |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 693 aa, 79.4 kDa, 处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=38, symbol_only=45, broad=64 |
| 三维结构 | 6/10 | ×3 | 18.0 | 0 PDB; AF pLDDT=57.3, 56.9% <50 |
| 调控结构域 | 7/10 | ×2 | 14.0 | 3 domains (2 InterPro + 1 Pfam): NAP family (nucleosome assembly) |
| PPI 网络 | 5/10 | ×3 | 15.0 | IntAct 15 + STRING 15 + UniProt 33; chromatin, nucleosome, histone |
| **加权总分** | | | **113/180**** | |
| 互证加分 | | | +0.5 | 多库结构域一致(+0.5) |
| **归一化总分 (÷1.83)** | | | **61.7/100**** | |


### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269, 2x); Cytoplasm (ECO:0000250) | 核:实验证据; 质:by similarity |
| GO-CC | chromatin IBA; cytoplasm IEA; nucleolus IDA; nucleoplasm TAS; nucleus IDA | 实验+预测 |
| Protein Atlas (IF) | HPA 有 IHC/RNA 数据但 IF 未获取 | 未确认 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — Nucleus 定位有强实验证据 (2 x ECO:0000269 + IDA)。Nucleolus (IDA) 和 nucleoplasm (TAS) 定位进一步确认核内分布。Chromatin IBA 暗示染色质关联。

**结论**: 核定位置信度高。Nucleolus + Nucleoplasm 双核内定位。Chromatin binding (IBA) 进一步支持核功能。Cytoplasm 定位为 by similarity。

#### 3.2 结构与结构域

| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9H2G4-F1 (v6) |
| 平均 pLDDT | 57.3 |
| pLDDT >90 / 70-90 / 50-70 / <50 | 17.6% / 11.7% / 13.9% / 56.9% |
| PDB | 0 |

| 来源 | 结构域 |
|---|---|
| InterPro | IPR037231 (NAP-like_sf), IPR002164 (NAP_family) |
| Pfam | PF00956 (NAP) |

**评价**: NAP (Nucleosome Assembly Protein) 家族成员。NAP domain 是经典的 histone chaperone domain，参与 nucleosome assembly/disassembly。虽然 AF pLDDT 均值仅 57.3 (大量无序区域)，但 NAP domain 本身是已知折叠。无序区域可能参与蛋白互作调控。无实验结构(PBD=0)。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 38 |
| PubMed symbol_only | 45 |
| PubMed broad | 64 |

**关键文献**:
1. Cardano M et al. (2023). "Sex specific regulation of TSPY-Like 2 in the DNA damage response of cancer cells." *Cell Death Dis*. PMID: 36918555
2. Bonenti E et al. (2026). "TSPY-like 2, Beyond the Histone Chaperone Role." *Biomolecules*. PMID: 41897314
3. Sui M et al. (2024). "The role of Testis-Specific Protein Y-encoded-Like 2 in kidney injury." *iScience*. PMID: 38665207
4. Tan H et al. (2024). "TSPYL1 as a Critical Regulator of TGF-beta Signaling through Repression of TGFBR1 and TSPYL2." *Adv Sci*. PMID: 38588050
5. Li Y et al. (2024). "Testis-Specific Protein, Y-Encoded-Like 2 Activates JAK2/STAT3 Pathway in Hypothalamic Paraventricular Nucleus to Sustain Hypertension." *Am J Hypertens*. PMID: 38782571

**评价**: DNA damage response、TGF-beta signaling、histone chaperone 功能。2026年有"Beyond the Histone Chaperone Role"综述。新颖性中等偏上(38 strict)。

#### 3.4 PPI 网络

**UniProt 实验互作** (精选):

| Partner | Experiments | Relevance |
|---|---|---|
| ABT1 | 5 | Basal transcription activator |
| CSNK2A1 | 5 | Casein kinase 2, chromatin |
| MCRS1 | 5 | Nucleosome remodeling |
| NOP53 | 5 | Nucleolar, ribosome |
| ZNF687 | 4 | Zinc finger |
| AEBP2 | 3 | PRC2 component, chromatin |
| HMGXB4 | 3 | HMG-box, chromatin |
| INO80B | 3 | INO80 chromatin remodeler |
| KMT5B | 3 | Histone methyltransferase (H4K20) |
| PHF19 | 3 | PRC2 reader, chromatin |
| RBM15 | 3 | RNA binding, chromatin |
| SNIP1 | 3 | Transcription regulation |

**STRING 预测互作** (score >0.4):

| Partner | Score | Experimental | Relevance |
|---|---|---|---|
| TSPYL1 | 0.786 | 0.737 | TSPYL family, TGF-beta |
| ZMYND8 | 0.783 | 0.748 | Chromatin reader, DNA damage |
| TBR1 | 0.768 | 0.292 | CASK/TBR1 complex, neuronal |
| KDM5C | 0.715 | 0.482 | Histone demethylase, chromatin |
| XBP1 | 0.754 | 0 | Transcription factor |
| CASK | 0.574 | 0.292 | Scaffold, neuronal |

**已知复合体**: Chromatin (GO:0000785, IBA); Chromatin binding (GO:0003682, IBA); Nucleosome assembly (GO:0006334, IEA). CASK/TBR1/TSPYL2 transcriptional complex.

**评价**: PPI 网络强烈指向 chromatin/nucleosome regulation。关键互作包括: INO80B (chromatin remodeler), KMT5B (H4K20 methyltransferase), PHF19/AEBP2 (PRC2), ZMYND8 (chromatin reader/DDR), KDM5C (histone demethylase), MCRS1 (nucleosome remodeling)。UniProt 记录 33 个互作伙伴。

#### 3.5 多库互证

| 维度 | 来源 | 结果 | 一致性 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 0 PDB, AF only | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | NAP family (3 domains) | 多库一致 |
| PPI 网络 | STRING + IntAct + UniProt | Chromatin/nucleosome | 多源一致 |
| 核定位 | HPA/UniProt/GO | Nucleus + Nucleolus + Chromatin | 强一致 |

**互证加分明细**: 多库结构域一致(+0.5), 总计 +0.5

### 4. 总体评价

TSPYL2 是极具吸引力的候选蛋白。NAP (Nucleosome Assembly Protein) 家族成员，具有 histone chaperone 功能。核定位证据强(Nucleus + Nucleolus + Nucleoplasm)，chromatin binding (IBA)。PPI 网络极其丰富: INO80B (chromatin remodeler)、KMT5B (H4K20me)、PHF19/AEBP2 (PRC2)、KDM5C (H3K4me3 demethylase)、ZMYND8 (chromatin reader/DNA damage)。CASK/TBR1/TSPYL2 转录调控复合体已在神经元中定义。DNA damage response 和 TGF-beta signaling 中的功能已被报道。缺点是无实验结构，AF pLDDT 偏低。

**推荐**: 高优先级。NAP/histone chaperone + chromatin PPI 网络强大 + CASK/TBR1 转录复合体 + DNA damage response。虽然 AF 结构质量欠佳，但功能证据和 PPI 网络充分弥补。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9H2G4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2G4
- PDB: None
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPYL2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184205-TSPYL2 (HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。)

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。核定位基于 UniProt + GO-CC。



#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| TSPYL1 | STRING | 0.786 |
| ZMYND8 | STRING | 0.783 |
| ZNF687 | STRING | 0.774 |
| TBR1 | STRING | 0.768 |
| XBP1 | STRING | 0.754 |
| APTX | IntAct | psi-mi:"MI:0018"(two hybrid) |
| COIL | IntAct | psi-mi:"MI:0018"(two hybrid) |
| GFI1B | IntAct | psi-mi:"MI:0018"(two hybrid) |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H2G4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H2G4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037231;IPR002164; |
| Pfam | PF00956; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184205-TSPYL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABT1 | Intact, Biogrid | true |
| CSNK2A1 | Intact, Biogrid | true |
| NOP53 | Intact, Biogrid | true |
| ZFP91 | Intact, Biogrid | true |
| ZNF687 | Intact, Biogrid | true |
| CASK | Biogrid | false |
| CCNB1 | Biogrid | false |
| CEP19 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
